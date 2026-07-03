"""Ensure sources stay importable on the oldest supported Python."""

import ast
import pathlib

import pytest

PACKAGE_ROOT = pathlib.Path(__file__).parent.parent / "custom_components" / "svitlo_yeah"
SOURCES = sorted(PACKAGE_ROOT.rglob("*.py"))


@pytest.mark.parametrize("source", SOURCES, ids=lambda p: str(p.relative_to(PACKAGE_ROOT)))
def test_parses_on_python_313(source):
    """Reject syntax that only Python >= 3.14 accepts (e.g. unparenthesized except tuples)."""
    ast.parse(source.read_text(), filename=str(source), feature_version=(3, 13))
