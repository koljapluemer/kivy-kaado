from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty, ObjectProperty, BooleanProperty
import random
from models.card import Card
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class QueueScreen(Screen):
    flashcard = ObjectProperty(None)

    def load_next_card(self):
        # get a random card from the database
        card = random.choice(Card.select())
        self.flashcard = card  



    # def on_enter(self, *args):
    #     self.load_next_card()      

    def on_enter(self):
        self.load_next_card()
        flashcard_widget = FlashCard(front=self.flashcard.front, back=self.flashcard.back)
        self.add_widget(flashcard_widget)

class FlashCard(BoxLayout):
    front = StringProperty("")
    back = StringProperty("")
    revealed = BooleanProperty(False)

    def reveal_card (self):
        self.flashcard.revealed = True