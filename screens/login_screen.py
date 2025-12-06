from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from models.user_model import User
from utils.session_manager import save_session

class LoginScreen(Screen):
    def login_user(self):
        email = self.ids.email.text
        password = self.ids.password.text

        user = User.authenticate(email, password)

        if user:
            # Como authenticate retorna tuple, pegamos o primeiro elemento = id
            user_id = user[0]
            save_session(user_id)

            # Limpa campos
            self.ids.email.text = ""
            self.ids.password.text = ""

            self.manager.current = 'home'

        else:
            Popup(
                title='Erro',
                content=Label(text='Usuário ou senha inválidos.'),
                size_hint=(0.6, 0.4)
            ).open()
