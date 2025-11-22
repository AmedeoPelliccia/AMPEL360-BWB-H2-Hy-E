#!/bin/bash
# Setup script for AMPEL360 Q100 Git hooks

echo "🔧 Setting up AMPEL360 Q100 Git hooks..."

# Get the repository root
REPO_ROOT=$(git rev-parse --show-toplevel 2>/dev/null)

if [ -z "$REPO_ROOT" ]; then
    echo "❌ Error: Not in a git repository"
    exit 1
fi

# Check if hooks directory exists
HOOKS_SOURCE="$REPO_ROOT/.github/hooks"
HOOKS_TARGET="$REPO_ROOT/.git/hooks"

if [ ! -d "$HOOKS_SOURCE" ]; then
    echo "❌ Error: Hooks source directory not found: $HOOKS_SOURCE"
    exit 1
fi

# Copy or symlink hooks
echo "📋 Installing hooks..."

if [ -f "$HOOKS_SOURCE/pre-commit" ]; then
    # Create symlink (preferred) or copy
    if ln -sf "../../.github/hooks/pre-commit" "$HOOKS_TARGET/pre-commit" 2>/dev/null; then
        echo "  ✅ pre-commit hook symlinked"
    else
        cp "$HOOKS_SOURCE/pre-commit" "$HOOKS_TARGET/pre-commit"
        chmod +x "$HOOKS_TARGET/pre-commit"
        echo "  ✅ pre-commit hook copied"
    fi
else
    echo "  ⚠️  pre-commit hook not found"
fi

echo ""
echo "✅ Git hooks setup complete!"
echo ""
echo "The following validations will run on every commit:"
echo "  • Q100 model code in drawing filenames"
echo "  • Forbidden file extension checks"
echo "  • Strategic mission scope validation"
echo ""
echo "To bypass hooks (not recommended):"
echo "  git commit --no-verify"
