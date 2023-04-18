from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from screens import WelcomeScreen, CardFormScreen
from utils.database_utils import initialize_database
from kivy.modules import inspector


class MainApp(App):
    def build(self):
        initialize_database()

        sm = ScreenManager()
        sm.add_widget(WelcomeScreen(name="welcome_screen"))
        sm.add_widget(CardFormScreen(name="card_form_screen"))
        return sm

if __name__ == "__main__":
    MainApp().run()
