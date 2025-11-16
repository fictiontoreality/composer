"""Integration tests for validate command."""


def test_validate_all_stacks_valid(clean_stacks, capsys):
    """Test validate command with all valid stacks."""
    from composer.commands.validate import cmd_validate
    from argparse import Namespace

    args = Namespace()
    cmd_validate(clean_stacks, args)

    captured = capsys.readouterr()
    assert "✓ All stacks valid" in captured.out


def test_validate_detects_missing_dependency(clean_stacks, capsys, tmp_path):
    """Test validate detects missing dependencies."""
    from composer.commands.validate import cmd_validate
    from argparse import Namespace

    # Temporarily modify stack-c to depend on non-existent stack
    stack_c = clean_stacks.get_stack("stack-c")
    original_deps = stack_c.depends_on.copy()
    stack_c.depends_on = ["nonexistent-stack"]

    try:
        args = Namespace()
        cmd_validate(clean_stacks, args)

        captured = capsys.readouterr()
        assert "dependency 'nonexistent-stack' not found" in captured.out
        assert "stack-c" in captured.out
    finally:
        # Restore original dependencies
        stack_c.depends_on = original_deps
