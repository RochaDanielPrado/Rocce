import platform, os

if platform.system() == 'Windows':
    os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

from kivy.app import App
import json
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

class Janela3(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    registros = []
    path = ''

    def voltar(self, window, key, *args):
        if key == 27:
            App.get_running_app().root.current = 'menu'
            return True

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.voltar)

        self.path = App.get_running_app().user_data_dir
        self.loadData()
        print(self.registros)
        self.ids.boxid.clear_widgets()
        for reg in self.registros:
            #print(reg)
            self.ids.boxid.add_widget(Insert(text=reg))

    def loadData(self, *args):
        try:
            file = os.path.join(App.get_running_app().user_data_dir, 'data.json')
            with open(file, 'r') as data:
                self.registros = json.load(data)

        except FileNotFoundError:
            pass

    def saveData(self, *args):
        file = os.path.join(App.get_running_app().user_data_dir, 'data.json')
        with open(file, 'w') as data:
            json.dump(self.registros, data)

    def removeWidget(self, tarefa):
        texto = tarefa.ids.label.text
        self.ids.boxid.remove_widget(tarefa)
        self.registros.remove(texto)
        self.saveData()

    def addWidget(self):
        texto = self.ids.texto.text
        self.ids.boxid.add_widget(Insert(text=texto))
        self.ids.texto.text = ''
        self.registros.append(texto)
        self.saveData()

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.voltar)

class Insert(BoxLayout):
    def __init__(self, text='', **kwargs):
        super(Insert, self).__init__(**kwargs)
        self.ids.label.text = text

