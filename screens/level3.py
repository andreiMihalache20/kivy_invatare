from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox
from kivy.uix.button import Button
from kivy.uix.image import Image


class Level3Screen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.correct_answers = {0, 1, 2, 3}
        self.checkbox_vars = []

        self.build_ui()

    def build_ui(self):
        self.clear_widgets()
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        self.add_widget(Image(source='assets/poza_ist.png', allow_stretch=True, keep_ratio=False))

        self.content = BoxLayout(orientation='vertical', spacing=10, padding=10)
        self.add_widget(self.content)

        self.show_question()

    def show_question(self):
        self.content.clear_widgets()
        self.checkbox_vars.clear()

        question = "Care dintre afirmațiile de mai jos sunt adevărate?"
        options = [
            "a. Românii, grecii și bulgarii trăiesc în sud-estul Europei.",
            "b. Ungurii sunt situați în centrul continentului Europei.",
            "c. Rușii locuiesc în partea de nord-est a Europei.",
            "d. Turcii sunt așezați la granița dintre două continente."
        ]

        self.content.add_widget(Label(text="Nivel 3 - Selectează toate variantele corecte", font_size=20, size_hint_y=None, height=50))
        self.content.add_widget(Label(text=question, font_size=18, size_hint_y=None, height=60))

        for idx, text in enumerate(options):
            row = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=40)
            checkbox = CheckBox()
            self.checkbox_vars.append((idx, checkbox))
            row.add_widget(checkbox)
            row.add_widget(Label(text=text, font_size=16))
            self.content.add_widget(row)

        check_btn = Button(text="Verifică răspuns", size_hint_y=None, height=50)
        check_btn.bind(on_press=self.check_answer)
        self.content.add_widget(check_btn)

        back_btn = Button(text="Înapoi la meniu", size_hint_y=None, height=40)
        back_btn.bind(on_press=self.go_to_menu)
        self.content.add_widget(back_btn)

    def check_answer(self, instance):
        selected_indices = {idx for idx, cb in self.checkbox_vars if cb.active}
        correct_selected = len(selected_indices & self.correct_answers)
        incorrect_selected = len(selected_indices - self.correct_answers)
        total_correct = len(self.correct_answers)
        score = max(0, correct_selected - incorrect_selected)

        self.show_result(score, total_correct)

    def show_result(self, score, total):
        self.content.clear_widgets()
        result_text = "Răspuns complet corect!" if score == total else f"Răspuns parțial. Ai obținut {score}/{total} puncte."
        self.content.add_widget(Label(text=result_text, font_size=20))
        btn = Button(text="Înapoi la meniu", size_hint_y=None, height=50)
        btn.bind(on_press=self.go_to_menu)
        self.content.add_widget(btn)

    def go_to_menu(self, instance):
        self.manager.current = "menu"
