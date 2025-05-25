from atlassian import Confluence
import argparse
import logging
import json

# Load configuration from config.json
with open('config.json') as f:
    cfg = json.load(f)

CONFLUENCE_URL = cfg['url']
USERNAME = cfg['username']
API_TOKEN = cfg['api_token']

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def set_space_permissions(confluence, space_key, group_name, dry_run=False):
    permissions = [
        {"subjects": {"user": [], "group": [{"type": "group", "name": group_name}]},
         "operation": {"operation": "read", "targetType": "space"}},
        {"subjects": {"user": [], "group": [{"type": "group", "name": group_name}]},
         "operation": {"operation": "write", "targetType": "space"}}
    ]

    logger.info(f"{'DRY-RUN: ' if dry_run else ''}Applying permissions to space: {space_key} for group: {group_name}")
    
    if not dry_run:
        response = confluence.set_space_permissions(space_key, permissions)
        logger.info(f"Response: {response}")
    else:
        logger.info("Dry-run mode: No changes were made.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Manage Confluence group space permissions.")
    parser.add_argument("space_key", help="Space key to modify permissions for")
    parser.add_argument("group", help="Confluence group name")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes without applying them")

    args = parser.parse_args()

    confluence = Confluence(
        url=CONFLUENCE_URL,
        username=USERNAME,
        password=API_TOKEN,
        cloud=True
    )

    set_space_permissions(confluence, args.space_key, args.group, args.dry_run)