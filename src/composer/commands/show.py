import sys

from composer.stack_manager import StackManager


def cmd_show(manager: StackManager, args) -> None:
    """Show detailed info about a stack."""
    stack = manager.get_stack(args.stack)
    if not stack:
        print(f"Stack '{args.stack}' not found")
        sys.exit(1)

    status = stack.get_status()

    print(f"\nStack: {stack.name}")
    print(f"{'='*60}")
    print(f"Description:  {stack.description or 'N/A'}")
    print(f"Category:     {stack.category}/{stack.subcategory}" if stack.subcategory else f"Category:     {stack.category}")
    print(f"Tags:         {', '.join(stack.tags) if stack.tags else 'none'}")
    print(f"Path:         {stack.path}")
    print(f"Status:       {status['status']} ({status['running']}/{status['containers']} containers)")
    print(f"Auto-start:   {'yes' if stack.auto_start else 'no'}")
    if stack.auto_start:
        print(f"Priority:     {stack.priority}")
    print(f"Critical:     {'yes' if stack.critical else 'no'}")

    if stack.depends_on:
        print(f"Dependencies: {', '.join(stack.depends_on)}")

    if stack.owner:
        print(f"Owner:        {stack.owner}")

    if stack.documentation:
        print(f"Docs:         {stack.documentation}")

    if stack.health_check_url:
        print(f"Health:       {stack.health_check_url}")
