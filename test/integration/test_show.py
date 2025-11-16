"""Integration tests for show command."""

import pytest


def test_show_displays_stack_details(clean_stacks, capsys):
    """Test show command displays stack details."""
    from composer.commands.show import cmd_show
    from argparse import Namespace

    args = Namespace(stack="hello")
    cmd_show(clean_stacks, args)

    captured = capsys.readouterr()
    assert "Stack: hello" in captured.out
    assert "Description:  Test hello-world stack" in captured.out
    assert "Category:     test" in captured.out
    assert "Tags:         dev, testing" in captured.out


def test_show_displays_subcategory(clean_stacks, capsys):
    """Test show command displays subcategory."""
    from composer.commands.show import cmd_show
    from argparse import Namespace

    args = Namespace(stack="stack-c")
    cmd_show(clean_stacks, args)

    captured = capsys.readouterr()
    assert "Category:     test/integration" in captured.out


def test_show_displays_dependencies(clean_stacks, capsys):
    """Test show command displays dependencies."""
    from composer.commands.show import cmd_show
    from argparse import Namespace

    args = Namespace(stack="stack-c")
    cmd_show(clean_stacks, args)

    captured = capsys.readouterr()
    assert "Dependencies: stack-a" in captured.out


def test_show_displays_autostart(clean_stacks, capsys):
    """Test show command displays auto-start settings."""
    from composer.commands.show import cmd_show
    from argparse import Namespace

    args = Namespace(stack="stack-b")
    cmd_show(clean_stacks, args)

    captured = capsys.readouterr()
    assert "Auto-start:   yes" in captured.out
    assert "Priority:     1" in captured.out


def test_show_nonexistent_stack(clean_stacks):
    """Test show command with non-existent stack."""
    from composer.commands.show import cmd_show
    from argparse import Namespace

    args = Namespace(stack="nonexistent")
    with pytest.raises(SystemExit):
        cmd_show(clean_stacks, args)
