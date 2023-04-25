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
        # remove old flashcard widget
        self.ids.queue_box_layout.clear_widgets()
        flashcard_widget = FlashCard(front=self.flashcard.front, back=self.flashcard.back)

        self.ids.queue_box_layout.add_widget(flashcard_widget)

    def on_enter(self):
        self.load_next_card()
   



class FlashCard(BoxLayout):
    front = StringProperty("")
    back = StringProperty("")
    revealed = BooleanProperty(False)
    
    def reveal_card (self):
        self.revealed = True

    def mark_review(self, wasCorrect):
        # call load_next-card of parent
        self.parent.parent.parent.load_next_card()