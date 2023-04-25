# Card list screen
from kivy.uix.screenmanager import Screen
from models.card import Card

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class CardListScreen(Screen):
    # get all cards from the database
    def get_cards(self):
        cards = Card.select()
        return cards
    
    # show cards in the card list screen
    def show_cards(self):
        cards = self.get_cards()
        print("EXISTING IDS", self.ids)
        card_list_box_layout = self.ids.card_list_box_layout
        card_list_box_layout.clear_widgets()
        for card in cards:
            card_entry = CardListEntry(card=card)
            card_list_box_layout.add_widget(card_entry)
    
    # called when the screen is displayed
    def on_enter(self, *args):
        self.show_cards()




class CardListEntry(BoxLayout):
    def __init__(self, card, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "horizontal"
        self.size_hint_y = None
        self.height = 50

        front_label = Label(text=card.front)
        self.add_widget(front_label)

        back_label = Label(text=card.back)
        self.add_widget(back_label)