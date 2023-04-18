from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from screens import WelcomeScreen, CardFormScreen, AboutScreen
from utils.database_utils import initialize_database
from kivy.modules import inspector
from kivy.config import Config

class MainApp(App):
    def build(self):
        initialize_database()

        sm = ScreenManager()
        sm.add_widget(WelcomeScreen(name="welcome_screen"))
        sm.add_widget(CardFormScreen(name="card_form_screen"))
        sm.add_widget(AboutScreen(name="about_screen"))
        return sm

if __name__ == "__main__":
    Config.set('modules', 'inspector', '')
    MainApp().run()
