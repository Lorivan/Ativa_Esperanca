import pytest
from ativa_esperanca.utils.session_manager import save_session, load_session, clear_session
from ativa_esperanca.models.user_model import User

def test_login_saves_session(mocker):
    """Testa se o login válido salva sessão"""

    mock_user = (1, "email@test.com", "senha")
    mocker.patch("ativa_esperanca.models.user_model.User.authenticate", return_value=mock_user)

    save_session(mock_user[0])

    assert load_session() == 1


def test_login_invalid_user(mocker):
    """Testa login inválido"""

    mocker.patch("ativa_esperanca.models.user_model.User.authenticate", return_value=None)

    clear_session()
    assert load_session() is None
