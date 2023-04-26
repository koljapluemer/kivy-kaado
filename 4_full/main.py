from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from screens import WelcomeScreen, CardFormScreen, AboutScreen, QueueScreen, CardListScreen
from utils.database_utils import initialize_database
from kivy.modules import inspector
from kivy.config import Config
# import BoxLayout
from kivy.uix.boxlayout import BoxLayout
import pandas as pd
from models.card import Card, Tag
import csv

class MainApp(App):
    def build(self):
        initialize_database()
            # import from csv with header front	back	type	tags	is_active	is_priority	is_started	interval	interval_unit
        with open('cards.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # see if card with same front already exists
                try:
                    card = Card.get(Card.front == row['front'])
                    continue
                except Card.DoesNotExist:
                    pass
                card = Card.create(front=row['front'], back=row['back'], type=row['type'], is_active=row['is_active'], is_priority=row['is_priority'], is_started=row['is_started'], interval=row['interval'], interval_unit=row['interval_unit'])
                # get tags from Tag model, or create if not exist
                # add tags to card
                # for tag_name in row['tags'].split(' '):
                #     # see if Tag with name exists
                #     try:
                #         tag =Tag.get(Tag.name == tag_name)
                #     except Tag.DoesNotExist:
                #         tag = Tag.create(name=tag_name)
                #     # add tag to card, but only if no tag of that name is already added
                #     if tag not in card.tags:
                #         card.tags.add(tag)
                card.save()


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