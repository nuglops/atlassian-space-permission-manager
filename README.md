# Atlassian Space Permission Manager

A lightweight Python tool to automate and manage Confluence space permissions for groups using the Atlassian REST API.

## Features
- Assigns `read` and `write` permissions to Confluence groups on a given space.
- Supports dry-run mode to preview changes.
- Easily extendable to batch process multiple spaces or permissions.

## Prerequisites

- Python 3.7+
- Atlassian Cloud account
- Confluence API token

## Installation

```bash
git clone https://github.com/yourusername/atlassian-space-permission-manager.git
cd atlassian-space-permission-manager
pip install -r requirements.txt
```

## Configuration

Update `config.example.json` and rename it to `config.json`.

```json
{
  "url": "https://your-domain.atlassian.net/wiki",
  "username": "your-email@example.com",
  "api_token": "your-api-token"
}
```

## Usage

```bash
python manage_group_space_permissions.py SPACE_KEY GROUP_NAME
```

With dry-run (no changes applied):

```bash
python manage_group_space_permissions.py SPACE_KEY GROUP_NAME --dry-run
```

## License

MIT © Jeff Silver
