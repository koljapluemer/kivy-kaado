from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from models.card import Card


class CardFormScreen(Screen):
    front = ObjectProperty(None)
    back = ObjectProperty(None)

    def add_card(self):
        if self.front.text and self.back.text:
            card = Card.create(front=self.front.text, back=self.back.text, type="default")
            card.save()

            self.front.text = ""
            self.back.text = ""

            success_popup = Popup(title="Success", content=Label(text="Card added successfully!"), size_hint=(None, None), size=(400, 400))
            success_popup.open()
        else:
            error_popup = Popup(title="Error", content=Label(text="Please fill in both fields."), size_hint=(None, None), size=(400, 400))
            error_popup.open()

    def cancel(self):
        self.front.text = ""
        self.back.text = ""
        self.manager.current = "welcome_screen"
