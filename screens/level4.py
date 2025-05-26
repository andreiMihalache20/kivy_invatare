from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.button import Button
from kivy.uix.image import Image


class Level4Screen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.pairs = {
            "Apollo 11": ["aselenizare", "India", "America", "înconjurul Pământului"],
            "Cristofor Columb": ["America", "India", "aselenizare", "înconjurul Pământului"],
            "Ferdinand Magellan": ["înconjurul Pământului", "India", "aselenizare", "America"],
            "Vasco da Gama": ["India", "America", "aselenizare", "înconjurul Pământului"]
        }

        self.correct_matches = {
            "Apollo 11": "aselenizare",
            "Cristofor Columb": "America",
            "Ferdinand Magellan": "înconjurul Pământului",
            "Vasco da Gama": "India"
        }

        self.selected_values = {}

        self.build_ui()

    def build_ui(self):
        self.clear_widgets()
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # Fundal
        self.add_widget(Image(source='assets/poza_ist.png', allow_stretch=True, keep_ratio=False))

        # Conținut deasupra fundalului
        self.content = BoxLayout(orientation='vertical', spacing=10, padding=10)
        self.add_widget(self.content)

        self.content.add_widget(Label(text="Nivel 4 - Asociază corect perechile", font_size=20, size_hint_y=None, height=50))

        self.spinners = {}

        for person, options in self.pairs.items():
            row = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=40)
            row.add_widget(Label(text=person, font_size=16, size_hint_x=0.4))

            spinner = Spinner(text="Selectează...", values=options, size_hint_x=0.6)
            self.spinners[person] = spinner
            row.add_widget(spinner)
            self.content.add_widget(row)

        check_btn = Button(text="Verifică răspuns", size_hint_y=None, height=50)
        check_btn.bind(on_press=self.check_answers)
        self.content.add_widget(check_btn)

        back_btn = Button(text="Înapoi la meniu", size_hint_y=None, height=40)
        back_btn.bind(on_press=self.go_to_menu)
        self.content.add_widget(back_btn)

    def check_answers(self, instance):
        correct = 0
        total = len(self.correct_matches)

        for person, correct_value in self.correct_matches.items():
            if self.spinners[person].text == correct_value:
                correct += 1

        self.show_result(correct, total)

    def show_result(self, score, total):
        self.content.clear_widgets()
        msg = "Toate perechile corecte!" if score == total else f"Răspuns parțial: {score}/{total} corecte."
        self.content.add_widget(Label(text=msg, font_size=20))

        btn = Button(text="Înapoi la meniu", size_hint_y=None, height=50)
        btn.bind(on_press=self.go_to_menu)
        self.content.add_widget(btn)

    def go_to_menu(self, instance):
        self.manager.current = "menu"
