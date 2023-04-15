import random
import pandas as pd
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.properties import StringProperty, ObjectProperty, BooleanProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

# Set up the database
engine = create_engine('sqlite:///flashcards.db')
Base = declarative_base()

# Define the ORM models
class Card(Base):
    __tablename__ = 'cards'
    id = Column(Integer, primary_key=True)
    front = Column(String, nullable=False)
    back = Column(String, nullable=False)
    reviews = relationship("Review", back_populates="card")

class Review(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True)
    card_id = Column(Integer, ForeignKey('cards.id'))
    correct = Column(Boolean, nullable=False)
    card = relationship("Card", back_populates="reviews")

Base.metadata.create_all(engine)

# Set up the session
Session = sessionmaker(bind=engine)
session = Session()

def import_cards_from_csv(file_path):
    cards_df = pd.read_csv(file_path)
    cards = cards_df.to_dict(orient='records')

    for card_data in cards:
        card = session.query(Card).filter_by(front=card_data['front']).first()
        if not card:
            new_card = Card(front=card_data['front'], back=card_data['back'])
            session.add(new_card)
            session.commit()

    # print number of cards in db
    print(f"We now have {session.query(Card).count()} cards in the database.")

import_cards_from_csv("world_capitals.csv")


class FlashCard(BoxLayout):
    front = StringProperty("")
    back = StringProperty("")
    revealed = BooleanProperty(False)

class FlashCardApp(App):
    flashcard = ObjectProperty(None)

    def build(self):
        self.title = "Flash Card App"
        self.load_next_card()
        flashcard_widget = FlashCard(front=self.flashcard.front, back=self.flashcard.back)
        print(f"Loading Widget: {flashcard_widget.front} - {flashcard_widget.back}")
        return flashcard_widget
    
    def load_next_card(self):
        self.flashcard = random.choice(session.query(Card).all())
        print(f"Loading card: {self.flashcard.front} - {self.flashcard.back}")

    def reveal_card(self):
        self.root.ids.back_label.text = self.flashcard.back
        self.root.revealed = True

    def mark_review(self, correct):
        review = Review(card_id=self.flashcard.id, correct=correct)
        session.add(review)
        session.commit()
        self.load_next_card()
        self.root.front = self.flashcard.front
        self.root.back = self.flashcard.back
        self.root.ids.back_label.text = ""
        self.root.revealed = False

if __name__ == "__main__":
    FlashCardApp().run()
