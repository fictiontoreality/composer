#! /usr/bin/env python3
"""
composer - Docker Compose Stack Manager with Metadata Support

Usage:
    composer list [--category=CAT] [--tag=TAG]
    composer show <stack>
    composer up <stack|category|--all> [--priority]
    composer down <stack|category|--all>
    composer restart <stack>
    composer status [--category=CAT]
    composer search <term>
    composer autostart
    composer validate
    composer tag list
    composer tag add <stack> <tag> [<tag> ...]
    composer tag remove <stack> <tag> [<tag> ...]
    composer tag rename <old-tag> <new-tag>
    composer category list
    composer category set <stack> <category> [subcategory]
    composer category rename <old-category> <new-category>
"""

import argparse
import sys

from .stack_manager import StackManager
from .commands import (
    cmd_list,
    cmd_show,
    cmd_up,
    cmd_down,
    cmd_restart,
    cmd_status,
    cmd_search,
    cmd_autostart,
    cmd_validate,
    cmd_tag,
    cmd_category,
)


def main():
    parser = argparse.ArgumentParser(
        description="Docker Compose Stack Manager",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    subparsers = parser.add_subparsers(dest='command', help='Commands')

    # list
    list_parser = subparsers.add_parser('list', help='List stacks')
    list_parser.add_argument('--category', help='Filter by category')
    list_parser.add_argument('--tag', help='Filter by tag')

    # show
    show_parser = subparsers.add_parser('show', help='Show stack details')
    show_parser.add_argument('stack', help='Stack name')

    # up
    up_parser = subparsers.add_parser('up', help='Start stack(s)')
    up_parser.add_argument('target', nargs='?', help='Stack name or category')
    up_parser.add_argument('--all', action='store_true', help='Start all stacks')
    up_parser.add_argument('--category', help='Start all stacks in category')
    up_parser.add_argument('--priority', action='store_true', help='Start in priority order')
    up_parser.add_argument('--with-deps', action='store_true', help='Start dependencies first')

    # down
    down_parser = subparsers.add_parser('down', help='Stop stack(s)')
    down_parser.add_argument('target', nargs='?', help='Stack name or category')
    down_parser.add_argument('--all', action='store_true', help='Stop all stacks')
    down_parser.add_argument('--category', help='Stop all stacks in category')

    # restart
    restart_parser = subparsers.add_parser('restart', help='Restart a stack')
    restart_parser.add_argument('stack', help='Stack name')

    # status
    status_parser = subparsers.add_parser('status', help='Show status of stacks')
    status_parser.add_argument('--category', help='Filter by category')

    # search
    search_parser = subparsers.add_parser('search', help='Search stacks')
    search_parser.add_argument('term', help='Search term')

    # autostart
    subparsers.add_parser('autostart', help='Start all auto-start stacks')

    # validate
    subparsers.add_parser('validate', help='Validate stack metadata')

    # tag
    tag_parser = subparsers.add_parser('tag', help='Manage tags')
    tag_subparsers = tag_parser.add_subparsers(dest='tag_action', help='Tag actions')

    # tag list
    tag_subparsers.add_parser('list', help='List all unique tags')

    # tag add
    tag_add_parser = tag_subparsers.add_parser('add', help='Add tag(s) to a stack')
    tag_add_parser.add_argument('stack', help='Stack name')
    tag_add_parser.add_argument('tags', nargs='+', help='Tag(s) to add')

    # tag remove
    tag_remove_parser = tag_subparsers.add_parser('remove', help='Remove tag(s) from a stack')
    tag_remove_parser.add_argument('stack', help='Stack name')
    tag_remove_parser.add_argument('tags', nargs='+', help='Tag(s) to remove')

    # tag rename
    tag_rename_parser = tag_subparsers.add_parser('rename', help='Rename a tag across all stacks')
    tag_rename_parser.add_argument('old_tag', help='Old tag name')
    tag_rename_parser.add_argument('new_tag', help='New tag name')

    # category
    category_parser = subparsers.add_parser('category', help='Manage categories')
    category_subparsers = category_parser.add_subparsers(dest='category_action', help='Category actions')

    # category list
    category_subparsers.add_parser('list', help='List all unique categories')

    # category set
    category_set_parser = category_subparsers.add_parser('set', help='Set category for a stack')
    category_set_parser.add_argument('stack', help='Stack name')
    category_set_parser.add_argument('new_category', help='Category name')
    category_set_parser.add_argument('subcategory', nargs='?', help='Subcategory name (optional)')

    # category rename
    category_rename_parser = category_subparsers.add_parser('rename', help='Rename a category across all stacks')
    category_rename_parser.add_argument('old_category', help='Old category name')
    category_rename_parser.add_argument('new_category', help='New category name')

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    # Initialize manager
    manager = StackManager()

    # Dispatch to command
    commands = {
        'list': cmd_list,
        'show': cmd_show,
        'up': cmd_up,
        'down': cmd_down,
        'restart': cmd_restart,
        'status': cmd_status,
        'search': cmd_search,
        'autostart': cmd_autostart,
        'validate': cmd_validate,
        'tag': cmd_tag,
        'category': cmd_category,
    }

    commands[args.command](manager, args)


if __name__ == '__main__':
    main()
