import sys

from composer.stack_manager import StackManager


def cmd_down(manager: StackManager, args) -> None:
    """Stop stack(s)."""
    stacks_to_stop = []

    if args.all:
        stacks_to_stop = list(manager.stacks.values())
    elif args.category:
        stacks_to_stop = manager.get_category_stacks(args.category)
    else:
        stack = manager.get_stack(args.target)
        if not stack:
            print(f"Stack '{args.target}' not found")
            sys.exit(1)
        stacks_to_stop = [stack]

    # Stop in reverse priority order
    stacks_to_stop.sort(key=lambda s: -s.priority)

    print(f"Stopping {len(stacks_to_stop)} stack(s)...\n")

    for stack in stacks_to_stop:
        print(f"  Stopping {stack.name}...", end=" ")
        if stack.down():
            print("✓")
        else:
            print("✗ FAILED")
