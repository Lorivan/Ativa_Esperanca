from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from database.db_manager import create_tables
from screens.login_screen import LoginScreen
from screens.register_screen import RegisterScreen
from screens.home_screen import HomeScreen
from kivy.lang import Builder
from utils.session_manager import load_session

class MainApp(App):
    def build(self):
        create_tables()
        Builder.load_file('assets/style.kv')

        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(RegisterScreen(name='register'))
        sm.add_widget(HomeScreen(name='home'))

        # Verificar sessão ao iniciar
        session_user = load_session()

        if session_user:
            sm.current = 'home'
        else:
            sm.current = 'login'

        return sm

if __name__ == '__main__':
    MainApp().run()

