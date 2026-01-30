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
# verify-package.sh
#
# Verify package signatures and checksums.
#
# Usage:
#   bash tooling/verify-package.sh Q100-ATA10_EXPORT_20251201_v1.tar.gz
#   bash tooling/verify-package.sh packages/full-release/Q100-10-800_H2System_20251201_v1.tar.gz
#
# Options:
#   --skip-signature : Skip GPG signature verification
#   --skip-checksum  : Skip SHA256 checksum verification
#   --help           : Show this help message
###############################################################################

set -euo pipefail

# Color output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
EXPORTS_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"

# Default values
SKIP_SIGNATURE=false
SKIP_CHECKSUM=false

# Help function
show_help() {
    grep '^#' "$0" | grep -v '#!/usr/bin/env' | sed 's/^# //' | sed 's/^#//'
}

# Parse arguments
PACKAGE_FILE=""
while [[ $# -gt 0 ]]; do
    case $1 in
        --skip-signature)
            SKIP_SIGNATURE=true
            shift
            ;;
        --skip-checksum)
            SKIP_CHECKSUM=true
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
            else
                echo -e "${RED}Error: Multiple package files specified${NC}" >&2
                exit 1
            fi
            ;;
    esac
done

# Validate package file
if [[ -z "$PACKAGE_FILE" ]]; then
    echo -e "${RED}Error: Package file required${NC}" >&2
    show_help
    exit 1
fi

# Resolve package path
if [[ ! -f "$PACKAGE_FILE" ]]; then
    # Try relative to exports directory
    ALT_PATH="${EXPORTS_DIR}/${PACKAGE_FILE}"
    if [[ -f "$ALT_PATH" ]]; then
        PACKAGE_FILE="$ALT_PATH"
    else
        echo -e "${RED}Error: Package file not found: $PACKAGE_FILE${NC}" >&2
        exit 1
    fi
fi

PACKAGE_FILE=$(realpath "$PACKAGE_FILE")
PACKAGE_DIR=$(dirname "$PACKAGE_FILE")
PACKAGE_NAME=$(basename "$PACKAGE_FILE")

echo -e "${GREEN}=== AMPEL360 Package Verifier ===${NC}"
echo "Package: ${PACKAGE_NAME}"
# Portable file size calculation
FILE_SIZE=$(wc -c < "$PACKAGE_FILE" | tr -d ' ')
echo "Size:    ${FILE_SIZE} bytes"
echo ""

# Track verification results
CHECKS_PASSED=0
CHECKS_FAILED=0
CHECKS_SKIPPED=0

# Checksum verification
if [[ "$SKIP_CHECKSUM" == false ]]; then
    echo -e "${GREEN}Step 1: Verifying SHA256 checksum...${NC}"
    
    CHECKSUM_FILE="${PACKAGE_FILE}.sha256"
    
    if [[ ! -f "$CHECKSUM_FILE" ]]; then
        echo -e "${YELLOW}  ⚠ Checksum file not found: $(basename "$CHECKSUM_FILE")${NC}"
        echo -e "${YELLOW}  Skipping checksum verification${NC}"
        ((CHECKS_SKIPPED++))
    else
        # Read expected checksum
        EXPECTED_CHECKSUM=$(cat "$CHECKSUM_FILE" | awk '{print $1}')
        
        # Calculate actual checksum
        echo "  Calculating SHA256..."
        ACTUAL_CHECKSUM=$(sha256sum "$PACKAGE_FILE" | awk '{print $1}')
        
        # Compare
        if [[ "$EXPECTED_CHECKSUM" == "$ACTUAL_CHECKSUM" ]]; then
            echo -e "${GREEN}  ✓ Checksum valid${NC}"
            echo "    Expected: ${EXPECTED_CHECKSUM}"
            echo "    Actual:   ${ACTUAL_CHECKSUM}"
            ((CHECKS_PASSED++))
        else
            echo -e "${RED}  ✗ Checksum mismatch${NC}" >&2
            echo "    Expected: ${EXPECTED_CHECKSUM}"
            echo "    Actual:   ${ACTUAL_CHECKSUM}"
            ((CHECKS_FAILED++))
        fi
    fi
else
    echo -e "${YELLOW}Step 1: Checksum verification skipped${NC}"
    ((CHECKS_SKIPPED++))
fi

echo ""

# Signature verification
if [[ "$SKIP_SIGNATURE" == false ]]; then
    echo -e "${GREEN}Step 2: Verifying GPG signature...${NC}"
    
    # Check for GPG
    if ! command -v gpg &> /dev/null; then
        echo -e "${YELLOW}  ⚠ gpg command not found${NC}"
        echo -e "${YELLOW}  Skipping signature verification${NC}"
        ((CHECKS_SKIPPED++))
    else
        # Look for signature file
        SIG_FILE="${PACKAGE_FILE}.sig"
        
        if [[ ! -f "$SIG_FILE" ]]; then
            echo -e "${YELLOW}  ⚠ Signature file not found: $(basename "$SIG_FILE")${NC}"
            echo -e "${YELLOW}  Skipping signature verification${NC}"
            ((CHECKS_SKIPPED++))
        else
            # Create secure temporary file
            GPG_LOG=$(mktemp)
            trap "rm -f ${GPG_LOG}" EXIT
            
            # Verify signature
            if gpg --verify "$SIG_FILE" "$PACKAGE_FILE" 2>&1 | tee "${GPG_LOG}" | grep -q "Good signature"; then
                echo -e "${GREEN}  ✓ Signature valid${NC}"
                
                # Extract signer info
                KEY_ID=$(grep "using" "${GPG_LOG}" | grep -oE '[A-F0-9]{16}' | head -1 || echo "unknown")
                SIGNER=$(grep "Good signature" "${GPG_LOG}" | sed 's/.*from "//' | sed 's/".*//' || echo "unknown")
                
                echo "    Signed by: ${SIGNER}"
                echo "    Key ID:    ${KEY_ID}"
                ((CHECKS_PASSED++))
            else
                echo -e "${RED}  ✗ Signature verification failed${NC}" >&2
                cat "${GPG_LOG}" >&2
                ((CHECKS_FAILED++))
            fi
            
            rm -f "${GPG_LOG}"
        fi
    fi
else
    echo -e "${YELLOW}Step 2: Signature verification skipped${NC}"
    ((CHECKS_SKIPPED++))
fi

echo ""

# Additional checks
echo -e "${GREEN}Step 3: Additional checks...${NC}"

# Check file is not empty
if [[ ! -s "$PACKAGE_FILE" ]]; then
    echo -e "${RED}  ✗ Package file is empty${NC}" >&2
    ((CHECKS_FAILED++))
else
    echo -e "${GREEN}  ✓ Package file is not empty${NC}"
    ((CHECKS_PASSED++))
fi

# Check file extension
VALID_EXTS=("tar.gz" "zip" "tar" "7z")
FILE_EXT="${PACKAGE_NAME##*.}"
if [[ "$PACKAGE_NAME" == *.tar.gz ]]; then
    FILE_EXT="tar.gz"
fi

VALID_EXT=false
for ext in "${VALID_EXTS[@]}"; do
    if [[ "$FILE_EXT" == "$ext" ]]; then
        VALID_EXT=true
        break
    fi
done

if [[ "$VALID_EXT" == true ]]; then
    echo -e "${GREEN}  ✓ Valid file extension: .${FILE_EXT}${NC}"
    ((CHECKS_PASSED++))
else
    echo -e "${YELLOW}  ⚠ Non-standard file extension: .${FILE_EXT}${NC}"
    echo "    Expected one of: ${VALID_EXTS[*]}"
    ((CHECKS_SKIPPED++))
fi

# Check archive integrity (if tar/zip)
if [[ "$FILE_EXT" == "tar.gz" ]] || [[ "$FILE_EXT" == "tar" ]]; then
    echo "  Checking tar archive integrity..."
    if tar -tzf "$PACKAGE_FILE" > /dev/null 2>&1; then
        echo -e "${GREEN}  ✓ Archive integrity OK${NC}"
        ((CHECKS_PASSED++))
    else
        echo -e "${RED}  ✗ Archive is corrupted${NC}" >&2
        ((CHECKS_FAILED++))
    fi
elif [[ "$FILE_EXT" == "zip" ]]; then
    if command -v unzip &> /dev/null; then
        echo "  Checking zip archive integrity..."
        if unzip -t "$PACKAGE_FILE" > /dev/null 2>&1; then
            echo -e "${GREEN}  ✓ Archive integrity OK${NC}"
            ((CHECKS_PASSED++))
        else
            echo -e "${RED}  ✗ Archive is corrupted${NC}" >&2
            ((CHECKS_FAILED++))
        fi
    else
        echo -e "${YELLOW}  ⚠ unzip not available, skipping integrity check${NC}"
        ((CHECKS_SKIPPED++))
    fi
fi

echo ""

# Summary
echo -e "${GREEN}=== Verification Summary ===${NC}"
echo "Package: ${PACKAGE_NAME}"
echo ""
echo "Results:"
echo -e "  ${GREEN}Passed:  ${CHECKS_PASSED}${NC}"
echo -e "  ${RED}Failed:  ${CHECKS_FAILED}${NC}"
echo -e "  ${YELLOW}Skipped: ${CHECKS_SKIPPED}${NC}"
echo ""

if [[ $CHECKS_FAILED -eq 0 ]]; then
    echo -e "${GREEN}✓ All verification checks passed${NC}"
    exit 0
else
    echo -e "${RED}✗ Verification failed with ${CHECKS_FAILED} error(s)${NC}" >&2
    exit 1
fi
