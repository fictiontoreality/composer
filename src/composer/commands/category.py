import sys

from composer.stack_manager import StackManager


def cmd_category(manager: StackManager, args) -> None:
    """Category management commands."""
    if args.category_action == 'list':
        categories = manager.get_all_categories()
        if not categories:
            print("No categories found")
            return

        print(f"\nFound {len(categories)} unique categor{'ies' if len(categories) != 1 else 'y'}:\n")
        for category, subcategory in categories:
            # Count how many stacks use this category
            count = sum(1 for s in manager.stacks.values()
                       if s.category == category and s.subcategory == subcategory)

            display = f"{category}/{subcategory}" if subcategory else category
            print(f"  • {display} ({count} stack{'s' if count != 1 else ''})")

    elif args.category_action == 'set':
        stack = manager.get_stack(args.stack)
        if not stack:
            print(f"Stack '{args.stack}' not found")
            sys.exit(1)

        old_category = f"{stack.category}/{stack.subcategory}" if stack.subcategory else stack.category

        stack.category = args.new_category
        stack.subcategory = args.subcategory or ""
        stack.save_metadata()

        new_category = f"{stack.category}/{stack.subcategory}" if stack.subcategory else stack.category
        print(f"✓ Changed category for {stack.name}: {old_category} → {new_category}")

    elif args.category_action == 'rename':
        count = manager.rename_category(args.old_category, args.new_category)
        if count > 0:
            print(f"✓ Renamed category '{args.old_category}' to '{args.new_category}' across {count} stack{'s' if count != 1 else ''}")
        else:
            print(f"Category '{args.old_category}' not found on any stacks")
