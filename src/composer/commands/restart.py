from composer.stack_manager import StackManager


def cmd_restart(manager: StackManager, args) -> None:
    """Restart a stack."""
    stack = manager.get_stack(args.stack)
    if stack:
        stack.restart()
