#!/usr/bin/env python3
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
#
# SPDX-License-Identifier: Apache-2.0
"""Unit tests for validate_dpp_export.py."""

import json
import tempfile
from pathlib import Path

import pytest

from validate_dpp_export import load_json_file, validate_json_against_schema


class TestLoadJsonFile:
    """Tests for load_json_file function."""

    def test_load_valid_json(self) -> None:
        """Test loading a valid JSON file."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            test_data = {"key": "value", "number": 42}
            json.dump(test_data, f)
            temp_path = Path(f.name)
        
        try:
            result = load_json_file(temp_path)
            assert result == test_data
        finally:
            temp_path.unlink()

    def test_load_json_with_unicode(self) -> None:
        """Test loading JSON with unicode characters."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False, encoding='utf-8') as f:
            test_data = {"aircraft": "AMPEL360 Q100", "fuel": "H₂", "temp": "−253°C"}
            json.dump(test_data, f, ensure_ascii=False)
            temp_path = Path(f.name)
        
        try:
            result = load_json_file(temp_path)
            assert result == test_data
        finally:
            temp_path.unlink()

    def test_load_invalid_json_exits(self) -> None:
        """Test that invalid JSON causes system exit."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            f.write("{invalid json")
            temp_path = Path(f.name)
        
        try:
            with pytest.raises(SystemExit):
                load_json_file(temp_path)
        finally:
            temp_path.unlink()

    def test_load_nonexistent_file_exits(self) -> None:
        """Test that missing file causes system exit."""
        nonexistent_path = Path("/nonexistent/path/file.json")
        
        with pytest.raises(SystemExit):
            load_json_file(nonexistent_path)


class TestValidateJsonAgainstSchema:
    """Tests for validate_json_against_schema function."""

    def test_valid_data_passes(self) -> None:
        """Test that valid data passes validation."""
        schema = {
            "$schema": "http://json-schema.org/draft-07/schema#",
            "type": "object",
            "required": ["name"],
            "properties": {
                "name": {"type": "string"}
            }
        }
        data = {"name": "test"}
        
        is_valid, errors = validate_json_against_schema(data, schema, "test.json", "test.schema.json")
        
        assert is_valid is True
        assert errors == []

    def test_invalid_data_fails(self) -> None:
        """Test that invalid data fails validation."""
        schema = {
            "$schema": "http://json-schema.org/draft-07/schema#",
            "type": "object",
            "required": ["name"],
            "properties": {
                "name": {"type": "string"}
            }
        }
        data = {"name": 123}  # Wrong type
        
        is_valid, errors = validate_json_against_schema(data, schema, "test.json", "test.schema.json")
        
        assert is_valid is False
        assert len(errors) > 0
        assert "name" in errors[0].lower()

    def test_missing_required_field(self) -> None:
        """Test that missing required field is detected."""
        schema = {
            "$schema": "http://json-schema.org/draft-07/schema#",
            "type": "object",
            "required": ["name", "value"],
            "properties": {
                "name": {"type": "string"},
                "value": {"type": "number"}
            }
        }
        data = {"name": "test"}  # Missing 'value'
        
        is_valid, errors = validate_json_against_schema(data, schema, "test.json", "test.schema.json")
        
        assert is_valid is False
        assert len(errors) > 0

    def test_invalid_schema_detected(self) -> None:
        """Test that invalid schema structure is detected."""
        # Schema with structural error (invalid property type)
        invalid_schema = {
            "$schema": "http://json-schema.org/draft-07/schema#",
            "type": "object",
            "properties": "invalid"  # Should be an object, not a string
        }
        data = {"name": "test"}
        
        is_valid, errors = validate_json_against_schema(data, invalid_schema, "test.json", "bad.schema.json")
        
        assert is_valid is False
        assert len(errors) > 0
        assert "schema" in errors[0].lower()

    def test_nested_validation_error(self) -> None:
        """Test that nested validation errors include path."""
        schema = {
            "$schema": "http://json-schema.org/draft-07/schema#",
            "type": "object",
            "properties": {
                "nested": {
                    "type": "object",
                    "properties": {
                        "value": {"type": "string"}
                    }
                }
            }
        }
        data = {"nested": {"value": 123}}  # Wrong type in nested field
        
        is_valid, errors = validate_json_against_schema(data, schema, "test.json", "test.schema.json")
        
        assert is_valid is False
        assert len(errors) > 0
        # Check that error message includes path
        assert "nested" in errors[0]


class TestDppExportSchemas:
    """Integration tests for DPP Export schemas."""

    def test_manifest_schema_structure(self) -> None:
        """Test that manifest schema has required structure."""
        schema_path = Path(__file__).parent.parent / "schemas" / "dpp_export" / "v0.1" / "manifest.schema.json"
        
        if not schema_path.exists():
            pytest.skip("Manifest schema not found")
        
        schema = json.loads(schema_path.read_text())
        
        assert schema["$schema"] == "http://json-schema.org/draft-07/schema#"
        assert "export_id" in schema["required"]
        assert "files" in schema["required"]
        assert schema["properties"]["files"]["uniqueItems"] is True

    def test_baseline_schema_structure(self) -> None:
        """Test that baseline schema has required structure."""
        schema_path = Path(__file__).parent.parent / "schemas" / "dpp_export" / "v0.1" / "baseline.schema.json"
        
        if not schema_path.exists():
            pytest.skip("Baseline schema not found")
        
        schema = json.loads(schema_path.read_text())
        
        assert schema["$schema"] == "http://json-schema.org/draft-07/schema#"
        assert "baseline_id" in schema["required"]
        assert "components" in schema["required"]

    def test_effectivity_schema_anyof_constraint(self) -> None:
        """Test that effectivity schema has anyOf constraint for exclusions."""
        schema_path = Path(__file__).parent.parent / "schemas" / "dpp_export" / "v0.1" / "effectivity.schema.json"
        
        if not schema_path.exists():
            pytest.skip("Effectivity schema not found")
        
        schema = json.loads(schema_path.read_text())
        
        # Navigate to exclusions property
        rules_items = schema["properties"]["rules"]["items"]
        exclusions = rules_items["properties"]["exclusions"]
        
        # Check anyOf constraint exists
        assert "anyOf" in exclusions
        assert len(exclusions["anyOf"]) >= 2

    def test_software_bom_schema_filename_pattern(self) -> None:
        """Test that software BOM schema enforces basename-only filenames."""
        schema_path = Path(__file__).parent.parent / "schemas" / "dpp_export" / "v0.1" / "software_bom.schema.json"
        
        if not schema_path.exists():
            pytest.skip("Software BOM schema not found")
        
        schema = json.loads(schema_path.read_text())
        
        # Check binary_files filename pattern
        binary_files = schema["properties"]["software_components"]["items"]["properties"]["binary_files"]
        filename_prop = binary_files["items"]["properties"]["filename"]
        
        assert "pattern" in filename_prop
        # Pattern should prevent path separators
        assert "[^/\\\\]" in filename_prop["pattern"] or "^[^/\\\\]+$" in filename_prop["pattern"]


class TestHardeningConstraints:
    """Tests for schema hardening constraints."""

    def test_manifest_rejects_absolute_paths(self) -> None:
        """Test that manifest schema rejects absolute paths."""
        schema_path = Path(__file__).parent.parent / "schemas" / "dpp_export" / "v0.1" / "manifest.schema.json"
        
        if not schema_path.exists():
            pytest.skip("Manifest schema not found")
        
        schema = json.loads(schema_path.read_text())
        
        # Valid data with absolute path
        data = {
            "export_id": "TEST",
            "export_version": "0.1",
            "created_at": "2025-12-12T10:00:00Z",
            "aircraft_model": "TEST",
            "baseline_id": "TEST",
            "files": [
                {
                    "path": "/absolute/path.json",
                    "type": "baseline",
                    "checksum": "a" * 64
                }
            ]
        }
        
        is_valid, errors = validate_json_against_schema(data, schema, "test.json", "manifest.schema.json")
        
        assert is_valid is False
        assert any("path" in error.lower() for error in errors)

    def test_manifest_rejects_duplicate_files(self) -> None:
        """Test that manifest schema rejects duplicate files."""
        schema_path = Path(__file__).parent.parent / "schemas" / "dpp_export" / "v0.1" / "manifest.schema.json"
        
        if not schema_path.exists():
            pytest.skip("Manifest schema not found")
        
        schema = json.loads(schema_path.read_text())
        
        # Data with duplicate files
        data = {
            "export_id": "TEST",
            "export_version": "0.1",
            "created_at": "2025-12-12T10:00:00Z",
            "aircraft_model": "TEST",
            "baseline_id": "TEST",
            "files": [
                {
                    "path": "test.json",
                    "type": "baseline",
                    "checksum": "a" * 64
                },
                {
                    "path": "test.json",
                    "type": "baseline",
                    "checksum": "a" * 64
                }
            ]
        }
        
        is_valid, errors = validate_json_against_schema(data, schema, "test.json", "manifest.schema.json")
        
        assert is_valid is False

    def test_effectivity_exclusions_require_identifier(self) -> None:
        """Test that effectivity exclusions require at least msn or tail_number."""
        schema_path = Path(__file__).parent.parent / "schemas" / "dpp_export" / "v0.1" / "effectivity.schema.json"
        
        if not schema_path.exists():
            pytest.skip("Effectivity schema not found")
        
        schema = json.loads(schema_path.read_text())
        
        # Data with exclusion but no msn or tail_number
        data = {
            "effectivity_id": "TEST",
            "baseline_id": "TEST",
            "rules": [
                {
                    "rule_id": "R1",
                    "component_id": "C1",
                    "applicability": {},
                    "exclusions": {
                        "reason": "Test exclusion"
                    }
                }
            ]
        }
        
        is_valid, errors = validate_json_against_schema(data, schema, "test.json", "effectivity.schema.json")
        
        assert is_valid is False


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
