from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image


class Level6Screen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.question_index = 0
        self.score = 0

        self.questions = [
            {"q": "Moldova este situată în nord-estul României.", "answer": True},
            {"q": "Crișana se află în estul țării.", "answer": False},
            {"q": "Dobrogea este în sud-estul României.", "answer": True},
            {"q": "Muntenia se află în partea de sud.", "answer": True},
            {"q": "Banatul este în vestul țării.", "answer": True},
            {"q": "Oltenia este în centrul țării.", "answer": False}
        ]

        self.build_ui()

    def build_ui(self):
        self.clear_widgets()
        self.add_widget(Image(source='assets/poza_ist.png', allow_stretch=True, keep_ratio=False))
        self.content = BoxLayout(orientation='vertical', spacing=10, padding=10)
        self.add_widget(self.content)
        self.show_question()

    def show_question(self):
        self.content.clear_widgets()
        q_data = self.questions[self.question_index]

        self.content.add_widget(Label(
            text=f"Nivel 6 - Enunțul {self.question_index + 1}",
            font_size=20, size_hint_y=None, height=40))
        self.content.add_widget(Label(
            text=q_data["q"],
            font_size=18, size_hint_y=None, height=100))

        true_btn = Button(text="Adevărat", size_hint_y=None, height=50)
        false_btn = Button(text="Fals", size_hint_y=None, height=50)
        true_btn.bind(on_press=lambda x: self.check_answer(True))
        false_btn.bind(on_press=lambda x: self.check_answer(False))

        self.content.add_widget(true_btn)
        self.content.add_widget(false_btn)

        back_btn = Button(text="Înapoi la meniu", size_hint_y=None, height=40)
        back_btn.bind(on_press=self.go_to_menu)
        self.content.add_widget(back_btn)

    def check_answer(self, user_answer):
        correct = self.questions[self.question_index]["answer"]
        if user_answer == correct:
            self.score += 1

        self.question_index += 1
        if self.question_index < len(self.questions):
            self.show_question()
        else:
            self.show_result()

    def show_result(self):
        self.content.clear_widgets()
        self.content.add_widget(Label(
            text=f"Ai terminat Nivelul 6!\nScor: {self.score}/{len(self.questions)}",
            font_size=20))
        btn = Button(text="Înapoi la meniu", size_hint_y=None, height=50)
        btn.bind(on_press=self.go_to_menu)
        self.content.add_widget(btn)

    def go_to_menu(self, instance):
        self.manager.current = "menu"
