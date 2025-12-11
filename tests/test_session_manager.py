import os
import json
import pytest
from ativa_esperanca.utils.session_manager import (
    save_session,
    load_session,
    clear_session,
    SESSION_FILE,
)

def setup_function():
    """Executado antes de cada teste: garante ambiente limpo."""
    if os.path.exists(SESSION_FILE):
        os.remove(SESSION_FILE)

def teardown_function():
    """Executado depois de cada teste."""
    if os.path.exists(SESSION_FILE):
        os.remove(SESSION_FILE)

def test_save_session():
    save_session(1)

    assert os.path.exists(SESSION_FILE)

    with open(SESSION_FILE, "r") as f:
        data = json.load(f)

    assert data["user_id"] == 1

def test_load_session_exists():
    save_session(10)
    assert load_session() == 10

def test_load_session_not_exists():
    assert load_session() is None

def test_clear_session():
    save_session(99)
    clear_session()
    assert not os.path.exists(SESSION_FILE)
