<img width="820" height="655" alt="Pasted image 20250227111242" src="https://github.com/user-attachments/assets/b7e23972-d962-400e-b346-2f1255ac0653" />

Experiments in building a flashcard-based desktop app with kivy.

## Resources

 draws heavily on the Kivy Doc and a ChatGPT convo called *Kivy ORM CRUD App*

 ## Structure

 `0_flashcards` is a prototype doing CSV import, and a basic learn flashcard flow.

 `1_flashcards_ui` is an outdated experiment, I think.

 `2_crud` shall grow into a CRUD app for `Card` and `Tag`. I think that's a good starting point to build the whole of kaado actually. So far, it's only a very quick test of ScreenManager.

 ## Misc

 `*_screen.py` **must** inherit from `Screen`.
