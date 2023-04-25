from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from screens import WelcomeScreen, CardFormScreen, AboutScreen, QueueScreen, CardListScreen
from utils.database_utils import initialize_database
from kivy.modules import inspector
from kivy.config import Config
# import BoxLayout
from kivy.uix.boxlayout import BoxLayout
import pandas as pd
from models.card import Card


def import_cards_from_csv(file_path):
    cards_df = pd.read_csv(file_path)
    cards = cards_df.to_dict(orient='records')

    for card_data in cards:
        card = Card.filter(front=card_data['front']).first()
        if not card:
            new_card = Card(front=card_data['front'], back=card_data['back'], type="learn")
            new_card.save()

    # print number of cards in db
    print(f"We now have {Card.count()} cards in the database.")

# import_cards_from_csv("world_capitals.csv")


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
        sm.add_widget(CardListScreen(name="card_list_screen"))
        return sm

if __name__ == "__main__":
    Config.set('modules', 'inspector', '')
    MainApp().run()
