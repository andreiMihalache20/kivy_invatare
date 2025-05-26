from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.button import Button
from kivy.uix.image import Image


class Level7Screen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.groups = {
            "Romii": ["fierari", "confirmare", "ouă încondeiate", "geamie", "pescuit"],
            "Maghiarii": ["confirmare", "fierari", "pescuit", "geamie", "ouă încondeiate"],
            "Ucrainenii": ["ouă încondeiate", "confirmare", "fierari", "pescuit", "geamie"],
            "Turcii": ["geamie", "confirmare", "pescuit", "ouă încondeiate", "fierari"],
            "Lipovenii": ["pescuit", "geamie", "fierari", "ouă încondeiate", "confirmare"]
        }

        self.correct = {
            "Romii": "fierari",
            "Maghiarii": "confirmare",
            "Ucrainenii": "ouă încondeiate",
            "Turcii": "geamie",
            "Lipovenii": "pescuit"
        }

        self.spinners = {}

        self.build_ui()

    def build_ui(self):
        self.clear_widgets()
        self.add_widget(Image(source="assets/poza_ist.png", allow_stretch=True, keep_ratio=False))
        self.content = BoxLayout(orientation='vertical', spacing=10, padding=10)
        self.add_widget(self.content)

        self.content.add_widget(Label(
            text="Nivel 7 - Potrivește corect fiecare grup cultural",
            font_size=20, size_hint_y=None, height=50))

        for group, options in self.groups.items():
            row = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=40)
            row.add_widget(Label(text=group, font_size=16, size_hint_x=0.4))

            spinner = Spinner(text="Selectează...", values=options, size_hint_x=0.6)
            self.spinners[group] = spinner
            row.add_widget(spinner)
            self.content.add_widget(row)

        check_btn = Button(text="Verifică răspuns", size_hint_y=None, height=50)
        check_btn.bind(on_press=self.check_answers)
        self.content.add_widget(check_btn)

        back_btn = Button(text="Înapoi la meniu", size_hint_y=None, height=40)
        back_btn.bind(on_press=self.go_to_menu)
        self.content.add_widget(back_btn)

    def check_answers(self, instance):
        correct_count = 0
        total = len(self.correct)

        for group, expected in self.correct.items():
            if self.spinners[group].text == expected:
                correct_count += 1

        self.show_result(correct_count, total)

    def show_result(self, score, total):
        self.content.clear_widgets()
        msg = "Toate asocierile corecte!" if score == total else f"Asocieri corecte: {score}/{total}"
        self.content.add_widget(Label(text=msg, font_size=20))

        btn = Button(text="Înapoi la meniu", size_hint_y=None, height=50)
        btn.bind(on_press=self.go_to_menu)
        self.content.add_widget(btn)

    def go_to_menu(self, instance):
        self.manager.current = "menu"
