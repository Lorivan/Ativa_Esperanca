from kivy.uix.screenmanager import Screen
from utils.session_manager import clear_session

class HomeScreen(Screen):
    def on_enter(self, *args):
        """
        Método opcional:
        - Executado sempre que a tela for aberta
        - Pode ser usado para atualizar dados, exibir nome do usuário, etc.
        """
        pass

    def logout(self):
        # Remove o arquivo de sessão
        clear_session()

        # Volta para a tela de login
        self.manager.current = 'login'
