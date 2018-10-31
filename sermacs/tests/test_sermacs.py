"""
Unit and regression test for the sermacs package.
"""

# Import package, test suite, and other packages as needed
import sermacs
import pytest
import sys

def test_sermacs_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "sermacs" in sys.modules
