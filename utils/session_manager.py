import json
import os

SESSION_FILE = "session.json"

def save_session(user_id):
    """Salva a sessão do usuário."""
    with open(SESSION_FILE, "w") as f:
        json.dump({"user_id": user_id}, f)

def load_session():
    """Carrega a sessão existente, se houver."""
    if not os.path.exists(SESSION_FILE):
        return None
    with open(SESSION_FILE, "r") as f:
        data = json.load(f)
        return data.get("user_id")

def clear_session():
    """Remove a sessão do usuário."""
    if os.path.exists(SESSION_FILE):
        os.remove(SESSION_FILE)
