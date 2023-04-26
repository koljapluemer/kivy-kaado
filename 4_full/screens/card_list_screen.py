# Card list screen
from kivy.uix.screenmanager import Screen
from models.card import Card

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

from kivy.lang import Builder
from kivy.uix.recycleview import RecycleView
# get the header module
from widgets.header import Header


Builder.load_string('''
<RV>:
    viewclass: 'Label'
    RecycleBoxLayout:
        default_size: None, dp(56)
        default_size_hint: .9, None
        size_hint_y: None
        height: self.minimum_height
        orientation: 'vertical'
''')

class RV(RecycleView):
    def __init__(self, **kwargs):
        super(RV, self).__init__(**kwargs)
        # self.data = [{'text': str(x)} for x in range(100)]
        # cut 'front' to 50 characters, if truncated, add '...'
        self.data = [{'text': str(card.front[:50] + '...' if len(card.front) > 50 else card.front)} for card in Card.select()]


class CardListScreen(Screen):
    def on_enter(self, *args):
        # add RV widget
        rv = RV()
        self.add_widget(rv)
        return super().on_enter(*args)


# class CardListScreen(Screen):
#     # get all cards from the database
#     def get_cards(self):
#         cards = Card.select()
#         return cards
    
#     # show cards in the card list screen
#     def show_cards(self):
#         cards = self.get_cards()
#         card_list_box_layout = self.ids.card_list_box_layout
#         card_list_box_layout.clear_widgets()
#         for card in cards:
#             card_entry = CardListEntry(card=card)
#             card_list_box_layout.add_widget(card_entry)
    
#     # called when the screen is displayed
#     def on_enter(self, *args):
#         self.show_cards()




# class CardListEntry(BoxLayout):
#     def __init__(self, card, **kwargs):
#         super().__init__(**kwargs)
#         self.orientation = "horizontal"
#         self.size_hint_y = None
#         self.height = 50

#         front_label = Label(text=card.front)
#         self.add_widget(front_label)

#         back_label = Label(text=card.back)
#         self.add_widget(back_label)