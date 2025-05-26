from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.button import Button
from kivy.uix.image import Image


class Level9Screen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.question_index = 0
        self.score = 0

        self.questions = [
            {
                "q": "Fernando Magellan a fost primul om care a condus o expediție în jurul ___.",
                "options": ["Pământului", "Africii"],
                "answer": "Pământului"
            },
            {
                "q": "Marco Polo a locuit la curtea lui Kubilai Han, conducător mongol din ___.",
                "options": ["India", "China"],
                "answer": "China"
            },
            {
                "q": "Cristofor Columb a pornit în călătorie spre un nou drum spre ___.",
                "options": ["America", "India"],
                "answer": "India"
            },
            {
                "q": "Alexander Csoma de Kőrös a ajuns la ___.",
                "options": ["Polul Nord", "Tibet"],
                "answer": "Tibet"
            },
            {
                "q": "În 1961, Iuri Gagarin a fost primul om care a pășit în ___.",
                "options": ["spațiu", "pe Lună"],
                "answer": "spațiu"
            }
        ]

        self.build_ui()

    def build_ui(self):
        self.clear_widgets()
        self.add_widget(Image(source="assets/poza_ist.png", allow_stretch=True, keep_ratio=False))

        self.content = BoxLayout(orientation='vertical', spacing=10, padding=10)
        self.add_widget(self.content)
        self.show_question()

    def show_question(self):
        self.content.clear_widgets()
        q = self.questions[self.question_index]

        self.content.add_widget(Label(
            text=f"Nivel 9 - Întrebarea {self.question_index + 1}",
            font_size=20, size_hint_y=None, height=40))
        self.content.add_widget(Label(
            text=q["q"],
            font_size=18, size_hint_y=None, height=80))

        self.answer_spinner = Spinner(text="Selectează...", values=q["options"], size_hint_y=None, height=50)
        self.content.add_widget(self.answer_spinner)

        check_btn = Button(text="Verifică răspuns", size_hint_y=None, height=50)
        check_btn.bind(on_press=self.check_answer)
        self.content.add_widget(check_btn)

        back_btn = Button(text="Înapoi la meniu", size_hint_y=None, height=40)
        back_btn.bind(on_press=self.go_to_menu)
        self.content.add_widget(back_btn)

    def check_answer(self, instance):
        user_answer = self.answer_spinner.text
        correct_answer = self.questions[self.question_index]["answer"]

        if user_answer == correct_answer:
            self.score += 1

        self.question_index += 1
        if self.question_index < len(self.questions):
            self.show_question()
        else:
            self.show_result()

    def show_result(self):
        self.content.clear_widgets()
        self.content.add_widget(Label(
            text=f"Ai terminat Nivelul 9!\nScor: {self.score}/{len(self.questions)}",
            font_size=20))

        btn = Button(text="Înapoi la meniu", size_hint_y=None, height=50)
        btn.bind(on_press=self.go_to_menu)
        self.content.add_widget(btn)

    def go_to_menu(self, instance):
        self.manager.current = "menu"
