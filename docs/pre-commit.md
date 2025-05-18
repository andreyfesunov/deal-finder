# pre-commit

## About

pre-commit is a framework for managing and maintaining Git hooks. It allows you to automatically run checks (e.g., linting, formatting, commit message validation) before committing code.

## Installation

1. Install pre-commit framework with your system package manager, for instance, Arch's pacman:

```bash
sudo pacman -S pre-commit
```

2. Install hooks:

```bash
pre-commit install
```

Also install the commit-msg hook:

```bash
pre-commit install --hook-type commit-msg
```

## Usage

Run hooks:

```bash
pre-commit run --all-files
```

## Rules

### commit-msg

This project uses the `commit-msg` hook from `pre-commit`, so all commit messages must follow these rules.

#### Commit Format

Commit messages should follow this pattern:

##### Allowed Types:
- **feat** — adding a new feature;
- **fix** — fixing a bug;
- **refactor** — refactoring code without changing logic;
- **docs** — updating documentation;
- **style** — formatting changes, no logic changes;
- **test** — adding or updating tests;
- **chore** — changes not affecting code (configs, build, etc.);
- **perf** — performance improvements.

##### Examples:
✅ **Correct:**
- `feat(auth): added OAuth2.0 support`
- `fix(notifications): fixed email sending issue`
- `docs(readme): updated installation guide`
- `refactor(core): optimized database queries`

❌ **Incorrect:**
- `fixed bug` (missing type)
- `fix: fixed a bug` (missing scope)
- `Added a new feature` (wrong format)

##### Commit Length
- The first line must not exceed **72 characters**.
- If additional details are needed, add a blank line and write a more detailed description.
