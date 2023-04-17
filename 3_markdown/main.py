from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label


class MainApp(App):
    def build(self):
        layout = BoxLayout(orientation="horizontal")
        
        text_input = TextInput(
            text="",
            font_size=16,
            size_hint_x=0.5,
            background_color=(1, 1, 1, 1),
            foreground_color=(0, 0, 0, 1),
        )
        
        rendered_label = Label(
            text=text_input.text,
            markup=True,
            font_size=16,
            size_hint_x=0.5,
            valign='top',
            padding=(10, 10),
        )
        
        text_input.bind(text=rendered_label.setter('text'))
        
        layout.add_widget(text_input)
        layout.add_widget(rendered_label)
        
        return layout


if __name__ == "__main__":
    MainApp().run()
