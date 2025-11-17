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

#!/bin/bash

echo "=== Verifying 95-20_Subsystems Structure ==="
echo ""

# Check main README
if [ -f "README.md" ]; then
    echo "✓ Main README.md exists"
else
    echo "✗ Main README.md missing"
    exit 1
fi

# Check core overview documents
for doc in "95-20-00-001_Subsystems_Overview.md" "95-20-00-002_Subsystems_Integration_Map.md" "95-20-00-003_Cross_ATA_Dependencies.csv"; do
    if [ -f "$doc" ]; then
        echo "✓ Core document: $doc"
    else
        echo "✗ Core document missing: $doc"
        exit 1
    fi
done

# Check 00_META folder and documents
if [ -d "00_META" ]; then
    echo "✓ 00_META folder exists"
    for doc in "95-20-00-004_Subsystems_Taxonomy.md" "95-20-00-005_Subsystems_Traceability_Matrix.csv" "95-20-00-006_Subsystem_Registry.json" "95-20-00-007_CAOS_Subsystems_Hooks.md"; do
        if [ -f "00_META/$doc" ]; then
            echo "✓ META document: $doc"
        else
            echo "✗ META document missing: $doc"
            exit 1
        fi
    done
else
    echo "✗ 00_META folder missing"
    exit 1
fi

# Check all subsystem folders
subsystems=("95-20-01_NN_Core_Platform" "95-20-02_NN_DPP_Blockchain" "95-20-21_NN_ECS" "95-20-27_NN_Flight_Controls" "95-20-28_NN_Fuel_System" "95-20-31_NN_Recording_Systems" "95-20-42_NN_IMA_Integration" "95-20-45_NN_Maintenance" "95-20-49_NN_APU" "95-20-53_NN_Structures" "95-20-57_NN_Wing_Systems" "95-20-70_NN_Propulsion" "95-20-80_NN_Energy_Systems")

for subsystem in "${subsystems[@]}"; do
    if [ -d "$subsystem" ]; then
        echo "✓ Subsystem folder: $subsystem"
        
        # Check README
        if [ -f "$subsystem/README.md" ]; then
            echo "  ✓ README.md exists"
        else
            echo "  ✗ README.md missing"
            exit 1
        fi
        
        # Check ASSETS folder
        if [ -d "$subsystem/ASSETS" ]; then
            echo "  ✓ ASSETS folder exists"
        else
            echo "  ✗ ASSETS folder missing"
            exit 1
        fi
    else
        echo "✗ Subsystem folder missing: $subsystem"
        exit 1
    fi
done

echo ""
echo "=== Structure Validation Complete ==="
echo "✓ All required components present"
echo ""
echo "Summary:"
echo "- 1 Main README"
echo "- 3 Core overview documents"
echo "- 4 META governance documents"
echo "- 13 Subsystem folders with README and ASSETS"
echo ""
echo "Total: 21 key documents + 13 subsystem structures"
echo ""
echo "Structure is COMPLETE and follows OPT-IN Framework conventions!"
