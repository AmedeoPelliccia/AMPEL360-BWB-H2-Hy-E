---
description: "GitHub Actions workflows for AMPEL360"
applyTo: ".github/workflows/**/*.yml"
---

## Workflow Guidelines

- Use `actions/checkout@v4` and latest stable `actions/setup-*` actions.
- Always define **least-privilege** `permissions:` at job level.
- Keep workflows:
  - Deterministic.
  - Fast enough for normal CI usage.
  - Clear in purpose (one concern per workflow where possible).
- Secrets:
  - Never hard-code secrets.
  - Always use `${{ secrets.* }}` and document required secrets in the repo docs.
- Naming:
  - Use descriptive `name:` and job IDs to clarify intent (e.g. `geometry-watchdog`, `doc-meta-enforcer`).
- For the `copilot-setup-steps` workflow:
  - Ensure the job is called exactly `copilot-setup-steps`.
  - Use only the minimal steps needed to install tools/dependencies for Copilot's environment.
