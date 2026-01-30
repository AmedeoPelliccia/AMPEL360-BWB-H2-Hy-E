#!/usr/bin/env python3
# Copyright 2025 AMPEL360 Project Contributors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# SPDX-License-Identifier: Apache-2.0

"""
Test suite for Gate 0 metadata screening tool.

Tests metadata detection, validation, and coherence checking.
"""

import json
import pathlib
import sys
import tempfile
import unittest

# Add tools directory to path
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))

from genccc.gate0_metadata_screen import (
    detect_metadata,
    extract_yaml_frontmatter,
    has_yaml_frontmatter,
    check_parseability,
    check_required_keys,
    check_coherence,
    extract_axis_from_path,
    extract_ata_chapter_from_path,
    validate_version_format,
    validate_date_format,
)


class TestMetadataDetection(unittest.TestCase):
    """Test metadata detection functionality."""
    
    def test_yaml_frontmatter_detection(self):
        """Test YAML front-matter detection."""
        content_with_fm = """---
document_id: TEST-001
title: Test Document
---

# Content here
"""
        content_without_fm = """# Document Title

Some content without front-matter.
"""
        
        self.assertTrue(has_yaml_frontmatter(content_with_fm))
        self.assertFalse(has_yaml_frontmatter(content_without_fm))
    
    def test_yaml_frontmatter_extraction(self):
        """Test YAML front-matter extraction."""
        content = """---
document_id: TEST-001
title: Test Document
version: 1.0
---

# Content
"""
        metadata = extract_yaml_frontmatter(content)
        self.assertIsNotNone(metadata)
        self.assertEqual(metadata["document_id"], "TEST-001")
        self.assertEqual(metadata["title"], "Test Document")
        self.assertEqual(metadata["version"], 1.0)
    
    def test_inline_metadata_detection(self):
        """Test inline metadata detection."""
        content = """# Document Title

## Document Information

- **Document ID**: 95-10-01-01-001
- **Title**: Flight Ops Document
- **Version**: 1.0
- **Status**: Active
"""
        temp_file = pathlib.Path("test.md")
        detected, metadata = detect_metadata(temp_file, content)
        
        self.assertTrue(detected)
        self.assertIsNotNone(metadata)
        self.assertEqual(metadata["document_id"], "95-10-01-01-001")
        self.assertEqual(metadata["version"], "1.0")


class TestPathParsing(unittest.TestCase):
    """Test path-based information extraction."""
    
    def test_axis_extraction(self):
        """Test OPT-IN axis extraction from path."""
        test_cases = [
            ("OPT-IN_FRAMEWORK/N-NEURAL_NETWORKS_USERS_TRACEABILITY/ATA_95/file.md", "N"),
            ("OPT-IN_FRAMEWORK/I-INFRASTRUCTURES/ATA_02/file.md", "I"),
            ("OPT-IN_FRAMEWORK/O-ORGANIZATION/ATA_04/file.md", "O"),
            ("OPT-IN_FRAMEWORK/P-PROGRAM/ATA_06/file.md", "P"),
            ("OPT-IN_FRAMEWORK/T-TECHNOLOGY_AMEDEOPELLICCIA-ON_BOARD_SYSTEMS/file.md", "T"),
            ("some/other/path/file.md", None),
        ]
        
        for path_str, expected_axis in test_cases:
            path = pathlib.Path(path_str)
            axis = extract_axis_from_path(path)
            self.assertEqual(axis, expected_axis, f"Failed for path: {path_str}")
    
    def test_ata_chapter_extraction(self):
        """Test ATA chapter extraction from path."""
        test_cases = [
            ("OPT-IN_FRAMEWORK/N-NEURAL_NETWORKS/ATA_95-DIGITAL_PRODUCT_PASSPORT/file.md", "95"),
            ("OPT-IN_FRAMEWORK/I-INFRASTRUCTURES/ATA_02-OPERATIONS_INFORMATION/file.md", "02"),
            ("path/to/02-11-00_AIRCRAFT_DIMENSIONS/file.md", "02"),
            ("path/to/95-20_Subsystems/file.md", "95"),
            ("some/other/path/file.md", None),
        ]
        
        for path_str, expected_ata in test_cases:
            path = pathlib.Path(path_str)
            ata = extract_ata_chapter_from_path(path)
            self.assertEqual(ata, expected_ata, f"Failed for path: {path_str}")


class TestVersionAndDateValidation(unittest.TestCase):
    """Test version and date format validation."""
    
    def test_version_format_validation(self):
        """Test version format validation."""
        valid_versions = ["R01", "R99", "1.0", "2.1", "v1.0", "v1.0.0", "1.0.0"]
        invalid_versions = ["R1", "R001", "1", "vv1.0", "1.0.0.0"]
        
        for version in valid_versions:
            self.assertTrue(
                validate_version_format(version),
                f"Version {version} should be valid"
            )
        
        for version in invalid_versions:
            self.assertFalse(
                validate_version_format(version),
                f"Version {version} should be invalid"
            )
    
    def test_date_format_validation(self):
        """Test date format validation."""
        valid_dates = ["2025-12-13", "2025-01-01", "2025-12-31T10:30:00"]
        invalid_dates = ["2025-13-01", "25-12-13", "2025/12/13", "invalid"]
        
        for date in valid_dates:
            self.assertTrue(
                validate_date_format(date),
                f"Date {date} should be valid"
            )
        
        for date in invalid_dates:
            self.assertFalse(
                validate_date_format(date),
                f"Date {date} should be invalid"
            )


class TestCoherenceChecks(unittest.TestCase):
    """Test metadata coherence checking."""
    
    def test_axis_coherence(self):
        """Test axis coherence between path and metadata."""
        file_path = pathlib.Path("OPT-IN_FRAMEWORK/N-NEURAL_NETWORKS/ATA_95/file.md")
        
        # Matching axis
        metadata = {"optin_axis": "N"}
        issues = check_coherence(file_path, metadata)
        axis_issues = [i for i in issues if i.code == "AXIS_MISMATCH"]
        self.assertEqual(len(axis_issues), 0)
        
        # Mismatching axis
        metadata = {"optin_axis": "I"}
        issues = check_coherence(file_path, metadata)
        axis_issues = [i for i in issues if i.code == "AXIS_MISMATCH"]
        self.assertEqual(len(axis_issues), 1)
    
    def test_ata_chapter_coherence(self):
        """Test ATA chapter coherence between path and metadata."""
        file_path = pathlib.Path("OPT-IN_FRAMEWORK/N-NEURAL_NETWORKS/ATA_95-DPP/file.md")
        
        # Matching ATA chapter
        metadata = {"ata_chapter": "95"}
        issues = check_coherence(file_path, metadata)
        ata_issues = [i for i in issues if i.code == "ATA_CHAPTER_MISMATCH"]
        self.assertEqual(len(ata_issues), 0)
        
        # Mismatching ATA chapter
        metadata = {"ata_chapter": "02"}
        issues = check_coherence(file_path, metadata)
        ata_issues = [i for i in issues if i.code == "ATA_CHAPTER_MISMATCH"]
        self.assertEqual(len(ata_issues), 1)
    
    def test_version_format_coherence(self):
        """Test version format coherence."""
        file_path = pathlib.Path("test.md")
        
        # Valid version
        metadata = {"version": "1.0"}
        issues = check_coherence(file_path, metadata)
        version_issues = [i for i in issues if i.code == "INVALID_VERSION_FORMAT"]
        self.assertEqual(len(version_issues), 0)
        
        # Invalid version
        metadata = {"version": "invalid"}
        issues = check_coherence(file_path, metadata)
        version_issues = [i for i in issues if i.code == "INVALID_VERSION_FORMAT"]
        self.assertEqual(len(version_issues), 1)
    
    def test_date_format_coherence(self):
        """Test date format coherence."""
        file_path = pathlib.Path("test.md")
        
        # Valid date
        metadata = {"date": "2025-12-13"}
        issues = check_coherence(file_path, metadata)
        date_issues = [i for i in issues if i.code == "INVALID_DATE_FORMAT"]
        self.assertEqual(len(date_issues), 0)
        
        # Invalid date
        metadata = {"date": "invalid"}
        issues = check_coherence(file_path, metadata)
        date_issues = [i for i in issues if i.code == "INVALID_DATE_FORMAT"]
        self.assertEqual(len(date_issues), 1)


class TestRequiredKeys(unittest.TestCase):
    """Test required keys validation."""
    
    def test_all_required_keys_present(self):
        """Test when all required keys are present."""
        metadata = {
            "document_id": "TEST-001",
            "title": "Test Document",
            "version": "1.0",
            "status": "Active",
        }
        issues = check_required_keys(metadata)
        error_issues = [i for i in issues if i.severity == "ERROR"]
        self.assertEqual(len(error_issues), 0)
    
    def test_missing_required_keys(self):
        """Test when required keys are missing."""
        metadata = {
            "title": "Test Document",
        }
        issues = check_required_keys(metadata)
        error_issues = [i for i in issues if i.severity == "ERROR"]
        self.assertGreater(len(error_issues), 0)
        
        # Check that specific keys are flagged
        missing_keys = [i.field for i in error_issues]
        self.assertIn("document_id", missing_keys)
        self.assertIn("version", missing_keys)
        self.assertIn("status", missing_keys)


if __name__ == "__main__":
    unittest.main()
