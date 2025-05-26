
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.button import Button

class Level1Screen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.question_index = 0
        self.score = 0

        self.questions = [
            {
                "q": "Axa timpului este:",
                "options": [
                    "a. o linie pe care sunt așezate numerele naturale;",
                    "b. o linie dreaptă care trece prin centrul unui corp;",
                    "c. o linie pe care sunt fixate evenimentele istorice."
                ],
                "answer": 2
            },
            {
                "q": "Spațiul istoric este redat prin:",
                "options": [
                    "a. unelte;",
                    "b. hărți istorice;",
                    "c. podoabe."
                ],
                "answer": 1
            },
            {
                "q": "Arborele genealogic este:",
                "options": [
                    "a. un copac sădit de o familie într-o primăvară;",
                    "b. un desen care prezintă generațiile care alcătuiesc o familie;",
                    "c. arborele din care au mâncat Adam și Eva."
                ],
                "answer": 1
            }
        ]

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
        q_data = self.questions[self.question_index]
        self.selected = None
        self.option_buttons = []

        self.content.add_widget(Label(text=f"Nivel 1 - Întrebarea {self.question_index + 1}", font_size=20, size_hint_y=None, height=40))
        self.content.add_widget(Label(text=q_data["q"], font_size=18, size_hint_y=None, height=60))

        for idx, option in enumerate(q_data["options"]):
            btn = ToggleButton(text=option, group="options", size_hint_y=None, height=40)
            btn.bind(on_press=lambda instance, i=idx: self.set_selected(i))
            self.content.add_widget(btn)
            self.option_buttons.append(btn)

        submit_btn = Button(text="Trimite răspuns", size_hint_y=None, height=50)
        submit_btn.bind(on_press=self.check_answer)
        self.content.add_widget(submit_btn)

        back_btn = Button(text="Înapoi la meniu", size_hint_y=None, height=40)
        back_btn.bind(on_press=self.go_to_menu)
        self.content.add_widget(back_btn)

    def set_selected(self, index):
        self.selected = index

    def check_answer(self, instance):
        if self.selected is not None:
            if self.selected == self.questions[self.question_index]["answer"]:
                self.score += 1
        self.question_index += 1
        if self.question_index < len(self.questions):
            self.show_question()
        else:
            self.show_final_score()

    def show_final_score(self):
        self.content.clear_widgets()
        self.content.add_widget(Label(text=f"Ai terminat Nivelul 1!\nScor: {self.score}/{len(self.questions)}", font_size=20))
        btn = Button(text="Înapoi la meniu", size_hint_y=None, height=50)
        btn.bind(on_press=self.go_to_menu)
        self.content.add_widget(btn)

    def go_to_menu(self, instance):
        self.manager.current = "menu"

