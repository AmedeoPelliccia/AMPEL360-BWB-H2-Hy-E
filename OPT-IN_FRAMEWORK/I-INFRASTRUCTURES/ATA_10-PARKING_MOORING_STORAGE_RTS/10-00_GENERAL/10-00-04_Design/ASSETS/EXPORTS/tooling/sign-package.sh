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
# sign-package.sh
#
# Sign packages with GPG and generate detached signatures.
#
# Usage:
#   bash tooling/sign-package.sh Q100-ATA10_EXPORT_20251201_v1.tar.gz
#   bash tooling/sign-package.sh packages/full-release/Q100-10-800_H2System_20251201_v1.tar.gz --key-id ABCD1234
#
# Options:
#   --key-id <KEY>  : GPG key ID to use for signing (default: auto-select)
#   --output-dir <DIR> : Directory for signature file (default: same as package)
#   --help          : Show this help message
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
KEY_ID=""
OUTPUT_DIR=""

# Help function
show_help() {
    grep '^#' "$0" | grep -v '#!/usr/bin/env' | sed 's/^# //' | sed 's/^#//'
}

# Parse arguments
PACKAGE_FILE=""
while [[ $# -gt 0 ]]; do
    case $1 in
        --key-id)
            KEY_ID="$2"
            shift 2
            ;;
        --output-dir)
            OUTPUT_DIR="$2"
            shift 2
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

# Set output directory
if [[ -z "$OUTPUT_DIR" ]]; then
    OUTPUT_DIR=$(dirname "$PACKAGE_FILE")
fi

# Check for GPG
if ! command -v gpg &> /dev/null; then
    echo -e "${RED}Error: gpg command not found${NC}" >&2
    echo "Install GPG (GnuPG) to sign packages"
    exit 1
fi

echo -e "${GREEN}=== AMPEL360 Package Signer ===${NC}"
echo "Package: $(basename "$PACKAGE_FILE")"
# Portable file size calculation
FILE_SIZE=$(wc -c < "$PACKAGE_FILE" | tr -d ' ')
echo "Size:    ${FILE_SIZE} bytes"
echo ""

# Check GPG keys
if [[ -z "$KEY_ID" ]]; then
    echo "Available GPG keys:"
    gpg --list-secret-keys --keyid-format LONG 2>/dev/null || {
        echo -e "${RED}Error: No GPG keys found${NC}" >&2
        echo ""
        echo "To create a GPG key:"
        echo "  gpg --full-generate-key"
        echo ""
        echo "Follow the prompts to generate a key pair."
        exit 1
    }
    echo ""
    
    # Try to auto-select key
    KEY_ID=$(gpg --list-secret-keys --keyid-format LONG 2>/dev/null | grep -A 1 "^sec" | grep -oE '[A-F0-9]{16}' | head -1)
    
    if [[ -z "$KEY_ID" ]]; then
        echo -e "${RED}Error: Could not auto-select GPG key${NC}" >&2
        echo "Specify key with --key-id option"
        exit 1
    fi
    
    echo -e "${YELLOW}Auto-selected key: ${KEY_ID}${NC}"
else
    # Verify key exists
    if ! gpg --list-secret-keys "$KEY_ID" &>/dev/null; then
        echo -e "${RED}Error: GPG key not found: ${KEY_ID}${NC}" >&2
        exit 1
    fi
fi

echo ""
echo -e "${GREEN}Signing package with key ${KEY_ID}...${NC}"

# Create signature
SIG_FILE="${OUTPUT_DIR}/$(basename "$PACKAGE_FILE").sig"

# Sign with detached signature
if gpg --detach-sign --armor --default-key "$KEY_ID" --output "$SIG_FILE" "$PACKAGE_FILE"; then
    echo -e "${GREEN}  ✓ Signature created: $(basename "$SIG_FILE")${NC}"
else
    echo -e "${RED}  ✗ Signing failed${NC}" >&2
    exit 1
fi

# Verify signature immediately
echo ""
echo -e "${GREEN}Verifying signature...${NC}"
if gpg --verify "$SIG_FILE" "$PACKAGE_FILE" 2>&1 | grep -q "Good signature"; then
    echo -e "${GREEN}  ✓ Signature valid${NC}"
else
    echo -e "${RED}  ✗ Signature verification failed${NC}" >&2
    exit 1
fi

# Get signature info
echo ""
echo -e "${GREEN}Signature Information:${NC}"
gpg --verify "$SIG_FILE" "$PACKAGE_FILE" 2>&1 | grep -E "(Good signature|using|key ID)" || true

echo ""
echo -e "${GREEN}=== Signing Complete ===${NC}"
echo "Package:   $(basename "$PACKAGE_FILE")"
echo "Signature: $(basename "$SIG_FILE")"
echo "Key ID:    ${KEY_ID}"
echo ""
echo "To verify this signature:"
echo "  gpg --verify $(basename "$SIG_FILE") $(basename "$PACKAGE_FILE")"
echo ""
echo "To export public key for distribution:"
echo "  gpg --armor --export ${KEY_ID} > signatures/public-keys/release-key-${KEY_ID}.asc"
echo ""
