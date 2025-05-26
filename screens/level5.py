from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image


class Level5Screen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.correct_order = [
            "Revoluția de la 1848",
            "Primul Război Mondial",
            "Marea Unire (1918)",
            "Al Doilea Război Mondial"
        ]

        self.current_order = self.correct_order.copy()
        self.item_rows = []

        self.build_ui()

    def build_ui(self):
        self.clear_widgets()
        self.add_widget(Image(source="assets/poza_ist.png", allow_stretch=True, keep_ratio=False))
        self.content = BoxLayout(orientation="vertical", spacing=10, padding=10)
        self.add_widget(self.content)

        self.content.add_widget(Label(text="Nivel 5 - Ordonează evenimentele cronologic", font_size=20, size_hint_y=None, height=50))

        self.refresh_display()

        check_btn = Button(text="Verifică ordinea", size_hint_y=None, height=50)
        check_btn.bind(on_press=self.check_answer)
        self.content.add_widget(check_btn)

        back_btn = Button(text="Înapoi la meniu", size_hint_y=None, height=40)
        back_btn.bind(on_press=self.go_to_menu)
        self.content.add_widget(back_btn)

    def refresh_display(self):
        for row in self.item_rows:
            self.content.remove_widget(row)
        self.item_rows.clear()

        for idx, item in enumerate(self.current_order):
            row = BoxLayout(orientation="horizontal", spacing=5, size_hint_y=None, height=40)
            label = Label(text=f"{idx+1}. {item}", font_size=16, size_hint_x=0.7)

            up_btn = Button(text="↑", size_hint_x=0.15)
            down_btn = Button(text="↓", size_hint_x=0.15)
            up_btn.bind(on_press=lambda inst, i=idx: self.move_item(i, -1))
            down_btn.bind(on_press=lambda inst, i=idx: self.move_item(i, 1))

            row.add_widget(label)
            row.add_widget(up_btn)
            row.add_widget(down_btn)

            self.content.add_widget(row, index=1)
            self.item_rows.append(row)

    def move_item(self, index, direction):
        new_index = index + direction
        if 0 <= new_index < len(self.current_order):
            self.current_order[index], self.current_order[new_index] = \
                self.current_order[new_index], self.current_order[index]
            self.refresh_display()

    def check_answer(self, instance):
        score = sum(1 for a, b in zip(self.correct_order, self.current_order) if a == b)
        self.show_result(score)

    def show_result(self, score):
        self.content.clear_widgets()
        self.content.add_widget(Label(text=f"Ai obținut {score}/{len(self.correct_order)} puncte.", font_size=20))
        btn = Button(text="Înapoi la meniu", size_hint_y=None, height=50)
        btn.bind(on_press=self.go_to_menu)
        self.content.add_widget(btn)

    def go_to_menu(self, instance):
        self.manager.current = "menu"
