import sys

from composer.stack_manager import StackManager


def cmd_up(manager: StackManager, args) -> None:
    """Start stack(s)."""
    stacks_to_start = []

    if args.all:
        stacks_to_start = list(manager.stacks.values())
    elif args.category:
        stacks_to_start = manager.get_category_stacks(args.category)
    else:
        stack = manager.get_stack(args.target)
        if not stack:
            print(f"Stack '{args.target}' not found")
            sys.exit(1)

        # Include dependencies if requested
        if args.with_deps:
            deps = manager.resolve_dependencies(stack)
            stacks_to_start = deps + [stack]
        else:
            stacks_to_start = [stack]

    # Sort by priority if requested
    if args.priority:
        stacks_to_start.sort(key=lambda s: s.priority)

    print(f"Starting {len(stacks_to_start)} stack(s)...\n")

    for stack in stacks_to_start:
        print(f"  Starting {stack.name}...", end=" ")
        if stack.up():
            print("✓")
        else:
            print("✗ FAILED")
