from composer.stack_manager import StackManager


def cmd_validate(manager: StackManager, args) -> None:
    """Validate all stack metadata."""
    print("Validating stacks...\n")

    issues = []

    for stack in manager.stacks.values():
        # Check compose file exists
        if not stack.compose_file.exists():
            issues.append(f"  ✗ {stack.name}: docker-compose.yml not found")

        # Check dependencies exist
        for dep in stack.depends_on:
            if not manager.get_stack(dep):
                issues.append(f"  ✗ {stack.name}: dependency '{dep}' not found")

        # Warn about missing metadata
        if not stack.meta_file.exists():
            issues.append(f"  ⚠ {stack.name}: no .stack-meta.yaml file")

    if issues:
        print("\n".join(issues))
        print(f"\n{len(issues)} issue(s) found")
    else:
        print("✓ All stacks valid")
