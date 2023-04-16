from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import App
from kivy.config import Config

class WelcomeScreen(Screen):
    pass

class AddCardScreen(Screen):
    pass

class MainApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(WelcomeScreen(name='welcome'))
        # sm.add_widget(AddCardScreen(name='add_card'))
        return sm

if __name__ == '__main__':
    Config.set('modules', 'inspector', '')
    MainApp().run()
