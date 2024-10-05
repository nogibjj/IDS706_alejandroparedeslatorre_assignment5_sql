import pytest
from click.testing import CliRunner
from main import cli


@pytest.fixture
def runner():
    return CliRunner()


# test ETL
def test_extract_data(runner):
    result = runner.invoke(cli, ["extract"])
    assert result.exit_code == 0, result.exit_code
    assert "Data extracted successfully." in result.output
    print(result.output)


def test_load_data(runner):
    result = runner.invoke(cli, ["load"])
    assert result.exit_code == 0
    assert "Data loaded into UniversitiesDB.db" in result.output
    print(result.output)


# test CRUD operations
def test_create(runner):
    result = runner.invoke(
        cli,
        ["create", "John Doe", "USA", "US", "California", "example.com", "example.com"],
    )
    assert result.exit_code == 0
    print(result.output)


def test_read(runner):
    result = runner.invoke(cli, ["read"])
    assert result.exit_code == 0
    print(result.output)


def test_update(runner):
    result = runner.invoke(
        cli,
        [
            "update",
            "1",
            "John Campbell",
            "BOL",
            "BO",
            "Santa Cruz",
            "example2.com",
            "example2.com",
        ],
    )
    assert result.exit_code == 0
    print(result.output)


def test_delete(runner):
    result = runner.invoke(cli, ["delete", "1"])
    assert result.exit_code == 0
    print(result.output)
