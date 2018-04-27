import pytest

from dbhelpers.updaters import create_all_db_tables
from helpers.settings import DB_PRESET


@pytest.yield_fixture(scope="module")
def test_base():
    create_all_db_tables(DB_PRESET['user_base'])
    yield
    create_all_db_tables(DB_PRESET['guest_base'])
