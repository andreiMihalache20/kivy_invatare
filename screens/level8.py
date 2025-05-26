from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.image import Image


class Level8Screen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.correct_order = [
            "România intră în război alături de Germania",
            "România devine stat comunist",
            "România aderă la NATO"
        ]

        self.current_order = self.correct_order.copy()
        self.item_rows = []

        self.personalities = {
            "Regele Carol II": ["“Epoca de Aur”", "Destrămarea României Mari", "Participarea la război", "Începutul comunismului"],
            "Nicolae Ceaușescu": ["“Epoca de Aur”", "Destrămarea României Mari", "Participarea la război", "Începutul comunismului"],
            "Regele Mihai I": ["Participarea la război", "Destrămarea României Mari", "Începutul comunismului", "“Epoca de Aur”"],
            "Gheorghe Gheorghiu-Dej": ["Începutul comunismului", "Participarea la război", "“Epoca de Aur”", "Destrămarea României Mari"]
        }

        self.correct_matches = {
            "Regele Carol II": "Destrămarea României Mari",
            "Nicolae Ceaușescu": "“Epoca de Aur”",
            "Regele Mihai I": "Participarea la război",
            "Gheorghe Gheorghiu-Dej": "Începutul comunismului"
        }

        self.spinners = {}

        self.build_ui()

    def build_ui(self):
        self.clear_widgets()
        self.add_widget(Image(source='assets/poza_ist.png', allow_stretch=True, keep_ratio=False))

        self.content = BoxLayout(orientation='vertical', spacing=10, padding=10)
        self.add_widget(self.content)

        self.content.add_widget(Label(
            text="Nivel 8 - Ordine cronologică (evenimente)", font_size=20, size_hint_y=None, height=50))

        self.refresh_order_display()

        check_btn = Button(text="Verifică ordinea", size_hint_y=None, height=50)
        check_btn.bind(on_press=self.check_order)
        self.content.add_widget(check_btn)

    def refresh_order_display(self):
        for row in self.item_rows:
            self.content.remove_widget(row)
        self.item_rows.clear()

        for idx, item in enumerate(self.current_order):
            row = BoxLayout(orientation="horizontal", spacing=5, size_hint_y=None, height=40)
            label = Label(text=f"{idx + 1}. {item}", font_size=16, size_hint_x=0.7)

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
            self.refresh_order_display()

    def check_order(self, instance):
        scor_crono = sum(1 for a, b in zip(self.correct_order, self.current_order) if a == b)
        self.show_association_section(scor_crono)

    def show_association_section(self, scor_crono):
        self.content.clear_widgets()
        self.content.add_widget(Label(text=f"Scor cronologic: {scor_crono}/3", font_size=18, size_hint_y=None, height=40))
        self.content.add_widget(Label(text="Asociază personalitățile cu evenimentele", font_size=20, size_hint_y=None, height=50))

        self.spinners.clear()

        for persoana, options in self.personalities.items():
            row = BoxLayout(orientation="horizontal", spacing=10, size_hint_y=None, height=40)
            row.add_widget(Label(text=persoana, font_size=16, size_hint_x=0.4))

            spinner = Spinner(text="Selectează...", values=options, size_hint_x=0.6)
            self.spinners[persoana] = spinner
            row.add_widget(spinner)
            self.content.add_widget(row)

        check_btn = Button(text="Verifică asocierile", size_hint_y=None, height=50)
        check_btn.bind(on_press=lambda x: self.check_associations(scor_crono))
        self.content.add_widget(check_btn)

        back_btn = Button(text="Înapoi la meniu", size_hint_y=None, height=40)
        back_btn.bind(on_press=self.go_to_menu)
        self.content.add_widget(back_btn)

    def check_associations(self, scor_crono):
        scor_asocieri = 0
        for persoana, corect in self.correct_matches.items():
            if self.spinners[persoana].text == corect:
                scor_asocieri += 1

        total = scor_crono + scor_asocieri
        self.content.clear_widgets()
        self.content.add_widget(Label(
            text=f"Scor total Nivel 8: {total}/7\n- Cronologie: {scor_crono}/3\n- Asocieri: {scor_asocieri}/4",
            font_size=20))

        btn = Button(text="Înapoi la meniu", size_hint_y=None, height=50)
        btn.bind(on_press=self.go_to_menu)
        self.content.add_widget(btn)

    def go_to_menu(self, instance):
        self.manager.current = "menu"
