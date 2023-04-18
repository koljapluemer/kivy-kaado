from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen


class AboutScreen(Screen):
    header_list = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Create the header list
        self.header_list = BoxLayout(orientation="vertical", spacing=10)
        self.add_widget(self.header_list)

        # Add headers to the list
        self.add_header("About Us")
        self.add_header("Our Team")
        self.add_header("Contact Us")

    def add_header(self, text):
        header = Button(text=text, size_hint=(1, None), height=50)
        self.header_list.add_widget(header)
