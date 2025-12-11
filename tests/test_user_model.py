import pytest
import os
from ativa_esperanca.database.db_manager import connect_db, create_tables
from ativa_esperanca.models.user_model import User

@pytest.fixture(autouse=True)
def setup_database():
    """Limpa o banco antes de cada teste"""
    if os.path.exists("ativa_esperanca.db"):
        os.remove("ativa_esperanca.db")

    create_tables()
    yield


def test_register_user():
    User.register("Teste", "teste@example.com", "123")

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email = ?", ("teste@example.com",))
    user = cursor.fetchone()
    conn.close()

    assert user is not None
    assert user[1] == "Teste"


def test_authenticate_success():
    User.register("User", "user@test.com", "abc")

    user = User.authenticate("user@test.com", "abc")
    assert user is not None


def test_authenticate_failure():
    User.register("User", "user@test.com", "abc")

    user = User.authenticate("user@test.com", "wrong")
    assert user is None
