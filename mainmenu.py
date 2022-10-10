import platform, os

if platform.system() == 'Windows':
    os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

from os.path import join, dirname
from kivymd.app import MDApp
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivymd.uix.screen import MDScreen
from kivymd.uix.toolbar import MDTopAppBar
from kivy.uix.image import AsyncImage, Image
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivymd.utils.set_bars_colors import set_bars_colors
import json



class Gerenciador(ScreenManager):
    pass

class CanvasConfig(Screen):
    pass

class TopMenu(MDTopAppBar):
    pass
class BottomMenu(MDTopAppBar):
    pass
class Menu(Screen):
    #def on_pre_enter(self):
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

class Tarefaxx(Screen):
    pass
class Tarefas(Screen):
    tarefas = []
    path = ''

    def on_pre_enter(self):
        self.path = App.get_running_app().user_data_dir+'/'
        self.loadData()
        for tarefa in self.tarefas:
            self.ids.box.add_widget(Tarefa(text=tarefa))
        print('entrou')
    def loadData(self, *args):
        try:
            with open(self.path+'data.json', 'r') as data:
                self.tarefas = json.load(data)
            print("entrou")
        except FileNotFoundError:
            pass

    def saveData(self,*args):
        with open(self.path+'data.json','w') as data:
            json.dump(self.tarefas, data)


    def removeWidget(self,tarefa):
        texto = tarefa.ids.label.text
        self.ids.box.remove_widget(tarefa)
        self.tarefas.remove(texto)
        self.saveData()

    def addWidget(self):
        texto = self.ids.texto.text
        self.ids.box.add_widget(Tarefa(text=texto))
        self.ids.texto.text = ''
        self.tarefas.append(texto)
        self.saveData()

class Tarefa(BoxLayout):
    def __init__(self,text='',**kwargs):
        super(Tarefa,self).__init__(**kwargs)
        self.ids.label.text = text
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


class MainScreen(Screen):
    pass


class LoginScreen(Screen):
    pass


class Janela1(Screen):
    pass

class Janela2(Screen):
    pass

class Janela3(Screen):
    pass

class external_image(AsyncImage):
    pass


class TestApp(MDApp):
    def build(self):

        # self.theme_cls.theme_style= "Dark"
        self.theme_cls.primary_palette = "Green"
        self.set_bars_colors()
        self.title = "meu app daniel"
        Window.size = (375, 812) #iphone 11 Pro

        sm = Gerenciador(transition=NoTransition())
        sm.add_widget(MainScreen(name="mainscreen"))
        sm.add_widget(Janela1(name="janela1"))
        sm.add_widget(LoginScreen(name="Janela3"))
        # sm.add_widget(SettingsScreen(name='settings'))

        return sm  # Builder.load_file("testapp.kv")

    def set_bars_colors(self):
        set_bars_colors(
            self.theme_cls.primary_color,  # status bar color
            self.theme_cls.primary_color,  # navigation bar color
            "Light",  # icons color of status bar
        )


if __name__ == '__main__':
    dir_kv = join(dirname(__file__), 'kv_files')
    TestApp(kv_directory=dir_kv).run()
    #TestApp().run()
