#!/usr/bin/env bash
# Copyright 2025 AMPEL360 Project Contributors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

###############################################################################
# upload-to-artifactory.sh
#
# Upload packages to Artifactory or S3.
# Path: releases/ATA10/<version>/
#
# Usage:
#   bash ci/ci-scripts/upload-to-artifactory.sh Q100-ATA10_EXPORT_20251201_v1.tar.gz releases/ATA10/v1.0.0/
#   bash ci/ci-scripts/upload-to-artifactory.sh <PACKAGE> <TARGET_PATH>
#
# Environment Variables:
#   ARTIFACTORY_URL      : Base URL of Artifactory (e.g., https://artifactory.company.com)
#   ARTIFACTORY_USER     : Username for authentication
#   ARTIFACTORY_API_KEY  : API key for authentication
#   ARTIFACTORY_REPO     : Repository name (default: ampel360-releases)
#
# Or for S3:
#   AWS_S3_BUCKET        : S3 bucket name
#   AWS_REGION           : AWS region (default: us-east-1)
#   AWS_ACCESS_KEY_ID    : AWS access key
#   AWS_SECRET_ACCESS_KEY: AWS secret key
#
# Options:
#   --backend <TYPE>     : Upload backend (artifactory or s3, default: artifactory)
#   --dry-run            : Show what would be uploaded without actually uploading
#   --help               : Show this help message
###############################################################################

set -euo pipefail

# Color output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Default values
BACKEND="${UPLOAD_BACKEND:-artifactory}"
DRY_RUN=false
ARTIFACTORY_REPO="${ARTIFACTORY_REPO:-ampel360-releases}"
AWS_REGION="${AWS_REGION:-us-east-1}"

# Help function
show_help() {
    grep '^#' "$0" | grep -v '#!/usr/bin/env' | sed 's/^# //' | sed 's/^#//'
}

# Parse arguments
PACKAGE_FILE=""
TARGET_PATH=""
while [[ $# -gt 0 ]]; do
    case $1 in
        --backend)
            BACKEND="$2"
            shift 2
            ;;
        --dry-run)
            DRY_RUN=true
            shift
            ;;
        --help)
            show_help
            exit 0
            ;;
        -*)
            echo -e "${RED}Error: Unknown option $1${NC}" >&2
            show_help
            exit 1
            ;;
        *)
            if [[ -z "$PACKAGE_FILE" ]]; then
                PACKAGE_FILE="$1"
                shift
            elif [[ -z "$TARGET_PATH" ]]; then
                TARGET_PATH="$1"
                shift
            else
                echo -e "${RED}Error: Too many arguments${NC}" >&2
                show_help
                exit 1
            fi
            ;;
    esac
done

# Validate arguments
if [[ -z "$PACKAGE_FILE" ]] || [[ -z "$TARGET_PATH" ]]; then
    echo -e "${RED}Error: Package file and target path are required${NC}" >&2
    show_help
    exit 1
fi

# Check package file exists
if [[ ! -f "$PACKAGE_FILE" ]]; then
    echo -e "${RED}Error: Package file not found: $PACKAGE_FILE${NC}" >&2
    exit 1
fi

PACKAGE_FILE=$(realpath "$PACKAGE_FILE")
PACKAGE_NAME=$(basename "$PACKAGE_FILE")

echo -e "${GREEN}=== AMPEL360 Package Uploader ===${NC}"
echo "Backend:      ${BACKEND}"
echo "Package:      ${PACKAGE_NAME}"
echo "Target Path:  ${TARGET_PATH}"
echo "Dry Run:      ${DRY_RUN}"
echo ""

# Upload to Artifactory
upload_artifactory() {
    echo -e "${GREEN}Uploading to Artifactory...${NC}"
    
    # Check required variables
    if [[ -z "${ARTIFACTORY_URL:-}" ]]; then
        echo -e "${RED}Error: ARTIFACTORY_URL not set${NC}" >&2
        exit 1
    fi
    
    if [[ -z "${ARTIFACTORY_USER:-}" ]] || [[ -z "${ARTIFACTORY_API_KEY:-}" ]]; then
        echo -e "${RED}Error: ARTIFACTORY_USER and ARTIFACTORY_API_KEY must be set${NC}" >&2
        exit 1
    fi
    
    # Build upload URL
    UPLOAD_URL="${ARTIFACTORY_URL}/${ARTIFACTORY_REPO}/${TARGET_PATH}${PACKAGE_NAME}"
    
    echo "Upload URL: ${UPLOAD_URL}"
    
    if [[ "$DRY_RUN" == true ]]; then
        echo -e "${YELLOW}[DRY RUN] Would upload to: ${UPLOAD_URL}${NC}"
        return 0
    fi
    
    # Upload with curl
    HTTP_CODE=$(curl -s -o /tmp/artifactory-response.txt -w "%{http_code}" \
        -u "${ARTIFACTORY_USER}:${ARTIFACTORY_API_KEY}" \
        -T "${PACKAGE_FILE}" \
        "${UPLOAD_URL}")
    
    if [[ $HTTP_CODE -ge 200 ]] && [[ $HTTP_CODE -lt 300 ]]; then
        echo -e "${GREEN}  ✓ Upload successful (HTTP ${HTTP_CODE})${NC}"
        
        # Upload checksum if exists
        CHECKSUM_FILE="${PACKAGE_FILE}.sha256"
        if [[ -f "$CHECKSUM_FILE" ]]; then
            echo "  Uploading checksum..."
            curl -s -u "${ARTIFACTORY_USER}:${ARTIFACTORY_API_KEY}" \
                -T "${CHECKSUM_FILE}" \
                "${UPLOAD_URL}.sha256" > /dev/null
            echo -e "${GREEN}  ✓ Checksum uploaded${NC}"
        fi
        
        # Upload signature if exists
        SIG_FILE="${PACKAGE_FILE}.sig"
        if [[ -f "$SIG_FILE" ]]; then
            echo "  Uploading signature..."
            curl -s -u "${ARTIFACTORY_USER}:${ARTIFACTORY_API_KEY}" \
                -T "${SIG_FILE}" \
                "${UPLOAD_URL}.sig" > /dev/null
            echo -e "${GREEN}  ✓ Signature uploaded${NC}"
        fi
        
        return 0
    else
        echo -e "${RED}  ✗ Upload failed (HTTP ${HTTP_CODE})${NC}" >&2
        cat /tmp/artifactory-response.txt >&2
        return 1
    fi
}

# Upload to S3
upload_s3() {
    echo -e "${GREEN}Uploading to S3...${NC}"
    
    # Check required variables
    if [[ -z "${AWS_S3_BUCKET:-}" ]]; then
        echo -e "${RED}Error: AWS_S3_BUCKET not set${NC}" >&2
        exit 1
    fi
    
    # Check for AWS CLI
    if ! command -v aws &> /dev/null; then
        echo -e "${RED}Error: aws CLI not found${NC}" >&2
        echo "Install with: pip install awscli"
        exit 1
    fi
    
    # Build S3 path
    S3_PATH="s3://${AWS_S3_BUCKET}/${TARGET_PATH}${PACKAGE_NAME}"
    
    echo "S3 Path: ${S3_PATH}"
    
    if [[ "$DRY_RUN" == true ]]; then
        echo -e "${YELLOW}[DRY RUN] Would upload to: ${S3_PATH}${NC}"
        return 0
    fi
    
    # Upload with AWS CLI
    if aws s3 cp "${PACKAGE_FILE}" "${S3_PATH}" --region "${AWS_REGION}"; then
        echo -e "${GREEN}  ✓ Upload successful${NC}"
        
        # Upload checksum if exists
        CHECKSUM_FILE="${PACKAGE_FILE}.sha256"
        if [[ -f "$CHECKSUM_FILE" ]]; then
            echo "  Uploading checksum..."
            aws s3 cp "${CHECKSUM_FILE}" "${S3_PATH}.sha256" --region "${AWS_REGION}"
            echo -e "${GREEN}  ✓ Checksum uploaded${NC}"
        fi
        
        # Upload signature if exists
        SIG_FILE="${PACKAGE_FILE}.sig"
        if [[ -f "$SIG_FILE" ]]; then
            echo "  Uploading signature..."
            aws s3 cp "${SIG_FILE}" "${S3_PATH}.sig" --region "${AWS_REGION}"
            echo -e "${GREEN}  ✓ Signature uploaded${NC}"
        fi
        
        return 0
    else
        echo -e "${RED}  ✗ Upload failed${NC}" >&2
        return 1
    fi
}

# Execute upload based on backend
case "$BACKEND" in
    artifactory)
        upload_artifactory
        ;;
    s3)
        upload_s3
        ;;
    *)
        echo -e "${RED}Error: Unknown backend: ${BACKEND}${NC}" >&2
        echo "Supported backends: artifactory, s3"
        exit 1
        ;;
esac

echo ""
echo -e "${GREEN}=== Upload Complete ===${NC}"
echo "Package: ${PACKAGE_NAME}"
echo "Target:  ${TARGET_PATH}"
echo ""
