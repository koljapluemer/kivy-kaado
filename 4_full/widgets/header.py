from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class Header(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "horizontal"
        self.size_hint_y = None
        self.height = 50

        home_button = Button(text="Home", size_hint_x=None, width=100)
        home_button.bind(on_release=self.go_home)
        self.add_widget(home_button)

        add_card_button = Button(text="Add Card", size_hint_x=None, width=100)
        add_card_button.bind(on_release=self.go_add_card)
        self.add_widget(add_card_button)

        about_button = Button(text="About", size_hint_x=None, width=100)
        about_button.bind(on_release=self.go_about)
        self.add_widget(about_button)

    def go_home(self, instance):
        self.parent.parent.manager.current = "welcome_screen"

    def go_add_card(self, instance):
        self.parent.parent.manager.current = "card_form_screen"

    def go_about(self, instance):
        self.parent.parent.manager.current = "about_screen"
        
    # Uncomment the following method when you implement the CardListScreen
    # def go_card_list(self, instance):
    #     self.parent.parent.manager.current = "card_list_screen"
