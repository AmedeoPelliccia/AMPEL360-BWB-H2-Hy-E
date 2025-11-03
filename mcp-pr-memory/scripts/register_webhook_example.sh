#!/usr/bin/env bash
# Example: create webhook via GitHub CLI (gh) - requires gh auth
REPO="owner/repo"
URL="https://your-host.example.com/webhook"
SECRET="${GITHUB_SECRET}" # set locally before running
gh api repos/$REPO/hooks -f config='{"url":"'$URL'","content_type":"json","secret":"'$SECRET'"}' -f events='["pull_request","push"]' -f active=true
