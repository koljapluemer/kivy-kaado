Slow attempt to rebuild kaado with kivy.

## Resources

 draws heavily on the Kivy Doc and a ChatGPT convo called *Kivy ORM CRUD App*

 ## Structure

 `0_flashcards` is a prototype doing CSV import, and a basic learn flashcard flow.

 `1_flashcards_ui` is an outdated experiment, I think.

 `2_crud` shall grow into a CRUD app for `Card` and `Tag`. I think that's a good starting point to build the whole of kaado actually. So far, it's only a very quick test of ScreenManager.

 ## Misc

 `*_screen.py` **must** inherit from `Screen`.