import os

os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.screen import MDScreen



class MainScreenManager(ScreenManager):
    pass


class MainScreen(MDScreen):
    pass

class LoginScreen(MDScreen):
    pass

class Janela1(MDScreen):
    pass

class TestApp(MDApp):
    def build(self):
        # self.theme_cls.theme_style= "Dark"
        self.theme_cls.primary_palette = "Brown"
        self.title = "meu app"

        sm = ScreenManager()
        sm.add_widget(MainScreen(name="mainscreen"))
        sm.add_widget(Janela1(name="janela1"))
        sm.add_widget(LoginScreen(name="loginscreen"))
        # sm.add_widget(SettingsScreen(name='settings'))

        return sm #Builder.load_file("testapp.kv")


if __name__ == '__main__':
    TestApp().run()
