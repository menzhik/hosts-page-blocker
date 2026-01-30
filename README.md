# hosts-page-blocker

[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![CI](https://github.com/menzhik/hosts-page-blocker/workflows/Ruff%20Check/badge.svg)](https://github.com/menzhik/hosts-page-blocker/actions)

Block distracting websites at the OS level via `/etc/hosts`.

Harder to bypass than browser extensions (requires OS-level file editing)

**Target use-case:** Block distracting websites (e.g. social media, news, messaging) during focused work hours.

## Prerequisites

- Python 3.6 or newer (stdlib only, no dependencies)
- Admin/root privileges (required to modify hosts file)
- Linux, macOS, or Windows

## Usage

1. Clone the repo:

```sh
git clone https://github.com/menzhik/hosts-page-blocker.git
cd hosts-page-blocker
```

2. Run with admin/root privileges:

```sh
# Linux/macOS
sudo python3 main.py

# Windows (run terminal as Administrator)
python main.py
```

3. Enter URLs to block:

```sh
Number of pages: 1
Enter URL: example.com
```

**Re-running the script is safe** — it replaces the old block instead of appending duplicates.

## How it works

The tool adds entries to your system's hosts file between markers:

```
# hosts-page-blocker BEGIN
0.0.0.0        example.com
::1            example.com
0.0.0.0        www.example.com
::1            www.example.com
# hosts-page-blocker END
```

Examples use placeholder domains (`example.com`). Replace them locally with the domains you want to block.

## Development

For contributors (optional, not required for users):

```sh
# Install uv (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install dev dependencies
uv sync

# Run linter
uv run ruff check
```

## License

MIT License — see [LICENSE](LICENSE)
