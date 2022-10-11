import platform, os

if platform.system() == 'Windows':
    os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

from os.path import join, dirname
from kivymd.app import MDApp
from kivy.app import App
from kivy.factory import Factory
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivymd.uix.screen import MDScreen
from kivymd.uix.toolbar import MDTopAppBar
from kivy.uix.image import AsyncImage, Image
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivymd.utils.set_bars_colors import set_bars_colors
import json


class Gerenciador(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    pass


class CanvasConfig(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    pass


class TopMenu(MDTopAppBar):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def callback(self, instance):
        print('The button has been pressed')
    pass


class BottomMenu(MDTopAppBar):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    pass


class Menu(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    # def on_pre_enter(self):
    #   Window.bind(on_request_close=self.confirmacao)
    def confirmacao(self, *args):
        box = BoxLayout(orientation='vertical', padding=10, spacing=10)
        botoes = BoxLayout(padding=10, spacing=10)

        pop = Popup(title='Deseja mesmo sair?', content=box, size_hint=(None, None),
                    size=(300, 180))

        sim = Button(text='Sim', on_release=App.get_running_app().stop)
        nao = Button(text='Não', on_release=pop.dismiss)

        botoes.add_widget(sim)
        botoes.add_widget(nao)

        atencao = Image(source='images/atencao.png')

        box.add_widget(atencao)
        box.add_widget(botoes)

        pop.open()
        return True


class Sair(Screen):
    tarefas = []
    path = ''

    def __init__(self, **kwargs):
        super(Sair, self).__init__(**kwargs)

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.voltar)

    def voltar(self, window, key, *args):
        if key == 27:
            App.get_running_app().root.current = 'menu'
            return True

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.voltar)


class external_image(AsyncImage):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    pass


class TestApp(MDApp):
    def build(self):
        # self.theme_cls.theme_style= "Dark"
        self.theme_cls.primary_palette = "Green"
        self.set_bars_colors()
        self.title = "meu app daniel"
        Window.size = (375, 600)  # iphone 11 Pro (375, 812)

        Factory.register('MainScreen', module='modules.mainscreen')
        Factory.register('LoginScreen', module='modules.loginscreen')
        Factory.register('Janela2', module='modules.janela2')
        Factory.register('Janela3', module='modules.janela3')

        sm = Gerenciador(transition=NoTransition())
        #sm.add_widget(MainScreen(name="mainscreen"))
        #sm.add_widget(Janela1(name="janela1"))
        #sm.add_widget(Janela2(name="janela2"))
        #sm.add_widget(Janela3(name="janela3"))
        # sm.add_widget(SettingsScreen(name='settings'))

        return sm  # Builder.load_file("testapp.kv")

    def set_screen(self, screen_name):
        self.root.current = screen_name

    def set_bars_colors(self):
        set_bars_colors(
            self.theme_cls.primary_color,  # status bar color
            self.theme_cls.primary_color,  # navigation bar color
            "Light",  # icons color of status bar
        )


if __name__ == '__main__':
    dir_kv = join(dirname(__file__), 'kv_files')
    TestApp(kv_directory=dir_kv).run()
    # TestApp().run()
