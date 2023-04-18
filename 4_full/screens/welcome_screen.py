from kivy.uix.screenmanager import Screen

class WelcomeScreen(Screen):
    def go_to_card_form(self):
        self.manager.current = "card_form_screen"
