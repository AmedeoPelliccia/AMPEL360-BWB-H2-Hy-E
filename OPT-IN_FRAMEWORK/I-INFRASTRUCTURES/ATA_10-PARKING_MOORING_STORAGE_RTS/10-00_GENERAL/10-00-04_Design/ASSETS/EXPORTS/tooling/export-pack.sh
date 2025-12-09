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
# export-pack.sh
#
# Build release packages for ATA Chapter 10 design exports.
# Validates contents, generates checksums, and creates standardized packages.
#
# Usage:
#   bash tooling/export-pack.sh --series 10-800 --date 20251201 --version v1
#   bash tooling/export-pack.sh --series 10-00 --date 20251215 --version v2.1 --model Q100
#
# Options:
#   --series <ATA-SERIES>  : ATA series to package (e.g., 10-800, 10-00)
#   --date <YYYYMMDD>      : Date stamp for package filename
#   --version <VERSION>    : Version tag (e.g., v1, v2.1)
#   --model <MODEL>        : Aircraft model (default: Q100)
#   --package-type <TYPE>  : Package type (default: full-release)
#   --output-dir <DIR>     : Output directory (default: packages/full-release)
#   --help                 : Show this help message
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
REPO_ROOT="$(cd "${EXPORTS_DIR}/../../../../../../.." && pwd)"

# Default values
MODEL="Q100"
ATA_CHAPTER="10"
SERIES=""
DATE=""
VERSION=""
PACKAGE_TYPE="full-release"
OUTPUT_DIR="${EXPORTS_DIR}/packages/full-release"

# Help function
show_help() {
    grep '^#' "$0" | grep -v '#!/usr/bin/env' | sed 's/^# //' | sed 's/^#//'
}

# Parse arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --series)
            SERIES="$2"
            shift 2
            ;;
        --date)
            DATE="$2"
            shift 2
            ;;
        --version)
            VERSION="$2"
            shift 2
            ;;
        --model)
            MODEL="$2"
            shift 2
            ;;
        --package-type)
            PACKAGE_TYPE="$2"
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
        *)
            echo -e "${RED}Error: Unknown option $1${NC}" >&2
            show_help
            exit 1
            ;;
    esac
done

# Validate required arguments
if [[ -z "$SERIES" ]] || [[ -z "$DATE" ]] || [[ -z "$VERSION" ]]; then
    echo -e "${RED}Error: --series, --date, and --version are required${NC}" >&2
    show_help
    exit 1
fi

# Validate date format
if ! [[ "$DATE" =~ ^[0-9]{8}$ ]]; then
    echo -e "${RED}Error: Date must be in YYYYMMDD format${NC}" >&2
    exit 1
fi

# Validate series format
if ! [[ "$SERIES" =~ ^[0-9]{2}-[0-9]{2,3}$ ]]; then
    echo -e "${YELLOW}Warning: Series format may be non-standard (expected: XX-YYY)${NC}" >&2
fi

echo -e "${GREEN}=== AMPEL360 Export Packager ===${NC}"
echo "Model:        ${MODEL}"
echo "ATA Chapter:  ${ATA_CHAPTER}"
echo "Series:       ${SERIES}"
echo "Date:         ${DATE}"
echo "Version:      ${VERSION}"
echo "Package Type: ${PACKAGE_TYPE}"
echo "Output Dir:   ${OUTPUT_DIR}"
echo ""

# Create temporary working directory
TEMP_DIR=$(mktemp -d)
trap "rm -rf ${TEMP_DIR}" EXIT

PACKAGE_NAME="${MODEL}-${SERIES}_${PACKAGE_TYPE}_${DATE}_${VERSION}"
WORK_DIR="${TEMP_DIR}/${PACKAGE_NAME}"
mkdir -p "${WORK_DIR}"

echo -e "${GREEN}Step 1: Collecting assets...${NC}"

# Define source directories based on series
DESIGN_DIR="${REPO_ROOT}/OPT-IN_FRAMEWORK/I-INFRASTRUCTURES/ATA_${ATA_CHAPTER}-PARKING_MOORING_STORAGE_RTS/${SERIES}_*/10-00-04_Design"
ASSETS_DIR="${REPO_ROOT}/OPT-IN_FRAMEWORK/I-INFRASTRUCTURES/ATA_${ATA_CHAPTER}-PARKING_MOORING_STORAGE_RTS/10-00_GENERAL/10-00-04_Design/ASSETS"

# Collect files based on package type
case "${PACKAGE_TYPE}" in
    "drawings")
        echo "  - Collecting drawings for series ${SERIES}..."
        find "${ASSETS_DIR}/DRAWINGS" -type f -name "${SERIES}-*.svg" -o -name "${SERIES}-*.pdf" 2>/dev/null | \
            while read -r file; do
                cp -v "$file" "${WORK_DIR}/" || true
            done
        ;;
    "assemblies")
        echo "  - Collecting assemblies for series ${SERIES}..."
        find "${ASSETS_DIR}/ASSEMBLIES" -type f -name "ASM-${SERIES}-*.yaml" -o -name "ASM-${SERIES}-*.json" 2>/dev/null | \
            while read -r file; do
                cp -v "$file" "${WORK_DIR}/" || true
            done
        ;;
    "3d-models")
        echo "  - Collecting 3D models for series ${SERIES}..."
        find "${ASSETS_DIR}/MODELS" -type f -name "${SERIES}-*.step" -o -name "${SERIES}-*.stp" -o -name "${SERIES}-*.iges" 2>/dev/null | \
            while read -r file; do
                cp -v "$file" "${WORK_DIR}/" || true
            done
        ;;
    "boms")
        echo "  - Collecting BOMs for series ${SERIES}..."
        find "${ASSETS_DIR}" -type f -name "${SERIES}-*BOM*.csv" -o -name "${SERIES}-*bom*.csv" 2>/dev/null | \
            while read -r file; do
                cp -v "$file" "${WORK_DIR}/" || true
            done
        ;;
    "specs")
        echo "  - Collecting specifications for series ${SERIES}..."
        find "${DESIGN_DIR}" -type f -name "${SERIES}-*.md" -o -name "${SERIES}-*.pdf" 2>/dev/null | \
            while read -r file; do
                cp -v "$file" "${WORK_DIR}/" || true
            done
        ;;
    "full-release")
        echo "  - Collecting all assets for series ${SERIES}..."
        # Copy all relevant files
        find "${ASSETS_DIR}" -type f \( -name "${SERIES}-*" -o -name "ASM-${SERIES}-*" \) 2>/dev/null | \
            while read -r file; do
                cp -v "$file" "${WORK_DIR}/" || true
            done
        ;;
    *)
        echo -e "${RED}Error: Unknown package type: ${PACKAGE_TYPE}${NC}" >&2
        exit 1
        ;;
esac

FILE_COUNT=$(find "${WORK_DIR}" -type f | wc -l)
echo -e "${GREEN}  ✓ Collected ${FILE_COUNT} files${NC}"

if [[ ${FILE_COUNT} -eq 0 ]]; then
    echo -e "${YELLOW}Warning: No files found for series ${SERIES}${NC}"
    echo -e "${YELLOW}Package will be empty. Continuing anyway...${NC}"
fi

echo ""
echo -e "${GREEN}Step 2: Creating package metadata...${NC}"

# Generate package metadata
cat > "${WORK_DIR}/package-metadata.json" <<EOF
{
  "package_id": "PKG-${SERIES}-${DATE}",
  "package_type": "${PACKAGE_TYPE}",
  "ata_series": "${SERIES}",
  "model": "${MODEL}",
  "effectivity": "${MODEL} BWB-H2",
  "created_at": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
  "created_by": "${USER}@ampel360.aero",
  "version": "${VERSION}",
  "file_count": ${FILE_COUNT},
  "source_repo": "AMPEL360-BWB-H2-Hy-E"
}
EOF

echo -e "${GREEN}  ✓ Metadata created${NC}"

echo ""
echo -e "${GREEN}Step 3: Generating checksums...${NC}"

# Create checksums directory
mkdir -p "${WORK_DIR}/checksums"

# Generate per-file checksums
find "${WORK_DIR}" -type f -not -path "*/checksums/*" -not -name "package-metadata.json" | \
    while read -r file; do
        filename=$(basename "$file")
        sha256sum "$file" | awk '{print $1}' > "${WORK_DIR}/checksums/${filename}.sha256"
    done

CHECKSUM_COUNT=$(find "${WORK_DIR}/checksums" -type f | wc -l)
echo -e "${GREEN}  ✓ Generated ${CHECKSUM_COUNT} checksums${NC}"

echo ""
echo -e "${GREEN}Step 4: Creating package archive...${NC}"

# Create output directory
mkdir -p "${OUTPUT_DIR}"

# Create tarball
OUTPUT_FILE="${OUTPUT_DIR}/${PACKAGE_NAME}.tar.gz"
tar -czf "${OUTPUT_FILE}" -C "${TEMP_DIR}" "${PACKAGE_NAME}"

# Generate package-level checksum
sha256sum "${OUTPUT_FILE}" | awk '{print $1}' > "${OUTPUT_FILE}.sha256"

FILE_SIZE=$(stat -f%z "${OUTPUT_FILE}" 2>/dev/null || stat -c%s "${OUTPUT_FILE}")
echo -e "${GREEN}  ✓ Package created: ${OUTPUT_FILE}${NC}"
echo -e "${GREEN}  ✓ Size: ${FILE_SIZE} bytes${NC}"

# Create index file
cat > "${OUTPUT_DIR}/${PACKAGE_NAME}.index.json" <<EOF
{
  "package_name": "${PACKAGE_NAME}.tar.gz",
  "package_type": "${PACKAGE_TYPE}",
  "model": "${MODEL}",
  "ata_chapter": "${ATA_CHAPTER}",
  "series": "${SERIES}",
  "version": "${VERSION}",
  "date": "${DATE}",
  "file_count": ${FILE_COUNT},
  "size_bytes": ${FILE_SIZE},
  "sha256": "$(cat ${OUTPUT_FILE}.sha256)",
  "created_at": "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
}
EOF

echo ""
echo -e "${GREEN}=== Package Build Complete ===${NC}"
echo "Package:  ${OUTPUT_FILE}"
echo "Checksum: ${OUTPUT_FILE}.sha256"
echo "Index:    ${OUTPUT_DIR}/${PACKAGE_NAME}.index.json"
echo ""
echo "Next steps:"
echo "  1. Verify package: bash tooling/verify-package.sh ${PACKAGE_NAME}.tar.gz"
echo "  2. Sign package: bash tooling/sign-package.sh ${PACKAGE_NAME}.tar.gz"
echo "  3. Generate manifest: python tooling/generate-manifest.py --dir ${OUTPUT_DIR}"
echo ""
