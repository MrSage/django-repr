"""
    Dummy conftest.py for django_better_repr.

    If you don't know what this is for, just leave it empty.
    Read more about conftest.py under:
    - https://docs.pytest.org/en/stable/fixture.html
    - https://docs.pytest.org/en/stable/writing_plugins.html
"""

import pytest

from django_better_repr.config import config


@pytest.fixture
def better_repr_config():
    yield config()
