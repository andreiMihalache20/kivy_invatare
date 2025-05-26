from  kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from screens.level1 import Level1Screen
from screens.level2 import Level2Screen
from screens.level3 import Level3Screen
from screens.level4 import Level4Screen
from screens.level5 import Level5Screen
from screens.level6 import Level6Screen
from screens.level7 import Level7Screen
from screens.level8 import Level8Screen
from screens.level9 import Level9Screen


Window.size = (1000, 667)

class MainMenu(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()

        # Fundal
        bg = Image(source="assets/poza_ist.png", allow_stretch=True, keep_ratio=False)
        layout.add_widget(bg)

        content = BoxLayout(orientation='vertical', spacing=20,
                            size_hint=(0.9, 0.9), pos_hint={'center_x': 0.5, 'center_y': 0.5})

        title = Label(text="Selectează un nivel", font_size=32, size_hint=(1, 0.2), color=(0, 0, 0, 1))
        content.add_widget(title)

        grid = GridLayout(cols=3, spacing=20, size_hint=(1, 0.8))
        for i in range(9):
            level_number = i + 1
            btn = Button(
                text=f"Nivel {level_number}",
                font_size=22,
                background_normal='',
                background_color=(0.85, 0.73, 0.55, 1),
            )
            btn.bind(on_press=self.build_level_callback(level_number))
            grid.add_widget(btn)
        content.add_widget(grid)
        layout.add_widget(content)
        self.add_widget(layout)

    def build_level_callback(self, level_number):
        def callback(instance):
            screen_name = f"nivel{level_number}"
            if self.manager.has_screen(screen_name):
                self.manager.current = screen_name
        return callback

class InvatareApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainMenu(name="menu"))
        sm.add_widget(Level1Screen(name="nivel1"))
        sm.add_widget(Level2Screen(name="nivel2"))
        sm.add_widget(Level3Screen(name="nivel3"))
        sm.add_widget(Level4Screen(name="nivel4"))
        sm.add_widget(Level5Screen(name="nivel5"))
        sm.add_widget(Level6Screen(name="nivel6"))
        sm.add_widget(Level7Screen(name="nivel7"))
        sm.add_widget(Level8Screen(name="nivel8"))
        sm.add_widget(Level9Screen(name="nivel9"))

        return sm

if __name__ == "__main__":
    InvatareApp().run()
