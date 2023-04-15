from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.properties import StringProperty


class FlashCard(BoxLayout):
    front = StringProperty("")
    back = StringProperty("")


class FlashCardApp(App):
    def build(self):
        self.title = "Flash Card App"
        return FlashCard(front="France", back="Paris")

    def reveal_card(self):
        self.root.ids.back_label.text = self.root.back


if __name__ == "__main__":
    FlashCardApp().run()
