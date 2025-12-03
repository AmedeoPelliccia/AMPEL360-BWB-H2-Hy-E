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
"""Unit tests for sidebar_sync.py."""

import tempfile
from pathlib import Path
from typing import Set

import pytest

from sidebar_sync import (
    END_MARKER,
    START_MARKER,
    extract_links_from_text,
    extract_manual_links_from_sidebar,
    find_markdown_files,
    update_sidebar_content,
)


class TestExtractLinksFromText:
    """Tests for extract_links_from_text function."""

    def test_single_link(self) -> None:
        """Test extraction of a single link."""
        text = "See [[Home]] for more info."
        result = extract_links_from_text(text)
        assert result == {"Home"}

    def test_multiple_links(self) -> None:
        """Test extraction of multiple links."""
        text = "Check [[Home]], [[Getting_Started]], and [[FAQ]]."
        result = extract_links_from_text(text)
        assert result == {"Home", "Getting_Started", "FAQ"}

    def test_no_links(self) -> None:
        """Test text with no links returns empty set."""
        text = "This is plain text with no wiki links."
        result = extract_links_from_text(text)
        assert result == set()

    def test_empty_text(self) -> None:
        """Test empty text returns empty set."""
        result = extract_links_from_text("")
        assert result == set()

    def test_link_with_spaces(self) -> None:
        """Test links with spaces are trimmed."""
        text = "See [[ Home ]] and [[  Getting Started  ]]."
        result = extract_links_from_text(text)
        assert result == {"Home", "Getting Started"}

    def test_nested_brackets_ignored(self) -> None:
        """Test that nested brackets don't match."""
        text = "Invalid [[link [with] nested]] brackets."
        result = extract_links_from_text(text)
        # The regex won't match because of nested brackets
        assert result == set()

    def test_multiline_text(self) -> None:
        """Test extraction from multiline text."""
        text = """
        # Page Title
        
        See [[Home]] for details.
        
        Also check:
        - [[Page_One]]
        - [[Page_Two]]
        """
        result = extract_links_from_text(text)
        assert result == {"Home", "Page_One", "Page_Two"}

    def test_duplicate_links(self) -> None:
        """Test that duplicates are deduplicated."""
        text = "[[Home]] is linked here and [[Home]] is linked again."
        result = extract_links_from_text(text)
        assert result == {"Home"}


class TestExtractManualLinksFromSidebar:
    """Tests for extract_manual_links_from_sidebar function."""

    def test_sidebar_without_auto_block(self) -> None:
        """Test sidebar without auto-generated block."""
        sidebar = """
        # Sidebar
        - [[Home]]
        - [[Getting_Started]]
        """
        result = extract_manual_links_from_sidebar(sidebar)
        assert result == {"Home", "Getting_Started"}

    def test_sidebar_with_auto_block(self) -> None:
        """Test that auto-generated block links are excluded."""
        sidebar = f"""
        # Sidebar
        - [[Home]]
        - [[Manual_Page]]
        
        {START_MARKER}
        - [[Auto_Page_1]]
        - [[Auto_Page_2]]
        {END_MARKER}
        """
        result = extract_manual_links_from_sidebar(sidebar)
        assert result == {"Home", "Manual_Page"}
        assert "Auto_Page_1" not in result
        assert "Auto_Page_2" not in result

    def test_sidebar_with_content_after_auto_block(self) -> None:
        """Test sidebar with content after auto-generated block."""
        sidebar = f"""
        # Sidebar
        - [[Before]]
        
        {START_MARKER}
        - [[Auto_Page]]
        {END_MARKER}
        
        - [[After]]
        """
        result = extract_manual_links_from_sidebar(sidebar)
        assert result == {"Before", "After"}
        assert "Auto_Page" not in result


class TestUpdateSidebarContent:
    """Tests for update_sidebar_content function."""

    def test_add_missing_links_no_existing_block(self) -> None:
        """Test adding missing links when no auto block exists."""
        sidebar = "# Sidebar\n- [[Home]]"
        missing: Set[str] = {"New_Page", "Another_Page"}
        
        result = update_sidebar_content(sidebar, missing)
        
        assert START_MARKER in result
        assert END_MARKER in result
        assert "[[Another_Page]]" in result
        assert "[[New_Page]]" in result
        assert "[[Home]]" in result

    def test_update_existing_block(self) -> None:
        """Test updating an existing auto block."""
        sidebar = f"""# Sidebar
- [[Home]]

{START_MARKER}
- [[Old_Page]]
{END_MARKER}
"""
        missing: Set[str] = {"New_Page"}
        
        result = update_sidebar_content(sidebar, missing)
        
        assert "[[New_Page]]" in result
        assert "[[Old_Page]]" not in result
        assert "[[Home]]" in result

    def test_empty_missing_links(self) -> None:
        """Test when there are no missing links."""
        sidebar = "# Sidebar\n- [[Home]]"
        missing: Set[str] = set()
        
        result = update_sidebar_content(sidebar, missing)
        
        assert START_MARKER in result
        assert END_MARKER in result
        assert "No internal links pending" in result

    def test_idempotency(self) -> None:
        """Test that running twice produces the same result."""
        sidebar = "# Sidebar\n- [[Home]]"
        missing: Set[str] = {"Page_A", "Page_B"}
        
        result1 = update_sidebar_content(sidebar, missing)
        result2 = update_sidebar_content(result1, missing)
        
        # Second run should keep same missing links
        # (since they're still not in manual section)
        assert result1 == result2

    def test_links_sorted_alphabetically(self) -> None:
        """Test that missing links are sorted alphabetically."""
        sidebar = "# Sidebar\n- [[Home]]"
        missing: Set[str] = {"Zebra", "Alpha", "Middle"}
        
        result = update_sidebar_content(sidebar, missing)
        
        # Find positions of each link in result
        alpha_pos = result.find("[[Alpha]]")
        middle_pos = result.find("[[Middle]]")
        zebra_pos = result.find("[[Zebra]]")
        
        assert alpha_pos < middle_pos < zebra_pos


class TestFindMarkdownFiles:
    """Tests for find_markdown_files function."""

    def test_find_files_in_directory(self) -> None:
        """Test finding markdown files in a directory."""
        with tempfile.TemporaryDirectory() as tmpdir:
            base = Path(tmpdir)
            
            # Create test files
            (base / "page1.md").write_text("# Page 1")
            (base / "page2.md").write_text("# Page 2")
            (base / "other.txt").write_text("Not markdown")
            
            result = find_markdown_files(base)
            
            assert len(result) == 2
            names = {f.name for f in result}
            assert names == {"page1.md", "page2.md"}

    def test_excludes_sidebar_and_footer(self) -> None:
        """Test that _Sidebar.md and _Footer.md are excluded."""
        with tempfile.TemporaryDirectory() as tmpdir:
            base = Path(tmpdir)
            
            (base / "page.md").write_text("# Page")
            (base / "_Sidebar.md").write_text("# Sidebar")
            (base / "_Footer.md").write_text("# Footer")
            
            result = find_markdown_files(base)
            
            assert len(result) == 1
            assert result[0].name == "page.md"

    def test_excludes_git_and_github_dirs(self) -> None:
        """Test that .git and .github directories are excluded."""
        with tempfile.TemporaryDirectory() as tmpdir:
            base = Path(tmpdir)
            
            (base / "page.md").write_text("# Page")
            
            git_dir = base / ".git"
            git_dir.mkdir()
            (git_dir / "config.md").write_text("# Git config")
            
            github_dir = base / ".github"
            github_dir.mkdir()
            (github_dir / "workflow.md").write_text("# Workflow")
            
            result = find_markdown_files(base)
            
            assert len(result) == 1
            assert result[0].name == "page.md"

    def test_finds_files_in_subdirectories(self) -> None:
        """Test finding files in nested directories."""
        with tempfile.TemporaryDirectory() as tmpdir:
            base = Path(tmpdir)
            
            (base / "root.md").write_text("# Root")
            
            subdir = base / "subdir"
            subdir.mkdir()
            (subdir / "nested.md").write_text("# Nested")
            
            result = find_markdown_files(base)
            
            assert len(result) == 2
            names = {f.name for f in result}
            assert names == {"root.md", "nested.md"}


class TestIntegration:
    """Integration tests for the sidebar sync workflow."""

    def test_full_workflow(self) -> None:
        """Test a complete sync workflow."""
        with tempfile.TemporaryDirectory() as tmpdir:
            base = Path(tmpdir)
            
            # Create markdown files with links
            (base / "page1.md").write_text("See [[Home]] and [[New_Feature]].")
            (base / "page2.md").write_text("Check [[FAQ]] and [[Home]].")
            
            # Create initial sidebar
            sidebar_path = base / "_Sidebar.md"
            sidebar_path.write_text("# Sidebar\n- [[Home]]\n")
            
            # Find files and extract links
            md_files = find_markdown_files(base)
            all_links = set()
            for f in md_files:
                all_links |= extract_links_from_text(f.read_text())
            
            # Get sidebar links
            sidebar_text = sidebar_path.read_text()
            sidebar_links = extract_manual_links_from_sidebar(sidebar_text)
            
            # Calculate missing
            missing = all_links - sidebar_links
            
            # Update sidebar
            updated = update_sidebar_content(sidebar_text, missing)
            
            assert "[[New_Feature]]" in updated
            assert "[[FAQ]]" in updated
            assert "[[Home]]" in updated  # Original still present


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
