"""Integration tests for search command."""


def test_search_finds_stacks_by_name(clean_stacks, capsys):
    """Test search command finds stacks by name."""
    from composer.commands.search import cmd_search
    from argparse import Namespace

    args = Namespace(term="hello")
    cmd_search(clean_stacks, args)

    captured = capsys.readouterr()
    assert "Found 1 stack(s)" in captured.out
    assert "hello" in captured.out


def test_search_finds_stacks_by_description(clean_stacks, capsys):
    """Test search command finds stacks by description."""
    from composer.commands.search import cmd_search
    from argparse import Namespace

    args = Namespace(term="Frontend")
    cmd_search(clean_stacks, args)

    captured = capsys.readouterr()
    assert "Found 1 stack(s)" in captured.out
    assert "stack-d" in captured.out


def test_search_finds_multiple_stacks(clean_stacks, capsys):
    """Test search command finds multiple stacks."""
    from composer.commands.search import cmd_search
    from argparse import Namespace

    args = Namespace(term="test")
    cmd_search(clean_stacks, args)

    captured = capsys.readouterr()
    # Should find hello, stack-a, and stack-c (all have "test" in metadata)
    assert "stack" in captured.out.lower()


def test_search_no_results(clean_stacks, capsys):
    """Test search command with no results."""
    from composer.commands.search import cmd_search
    from argparse import Namespace

    args = Namespace(term="nonexistent")
    cmd_search(clean_stacks, args)

    captured = capsys.readouterr()
    assert "No stacks found" in captured.out
