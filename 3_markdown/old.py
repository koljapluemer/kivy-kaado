from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout


class EditorLayout(BoxLayout):
    pass


class MainApp(App):
    def build(self):
        return Builder.load_file("app.kv")


if __name__ == "__main__":
    MainApp().run()
