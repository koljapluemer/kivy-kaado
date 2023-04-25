from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from screens import WelcomeScreen, CardFormScreen, AboutScreen, QueueScreen
from utils.database_utils import initialize_database
from kivy.modules import inspector
from kivy.config import Config
# import BoxLayout
from kivy.uix.boxlayout import BoxLayout

class MainApp(App):
    def build(self):
        initialize_database()


        root = BoxLayout(orientation="vertical")
        # root.add_widget(Header())

        sm = ScreenManager()
        sm.add_widget(WelcomeScreen(name="welcome_screen"))
        sm.add_widget(CardFormScreen(name="card_form_screen"))
        sm.add_widget(AboutScreen(name="about_screen"))
        sm.add_widget(QueueScreen(name="queue_screen"))
        return sm

if __name__ == "__main__":
    Config.set('modules', 'inspector', '')
    MainApp().run()
