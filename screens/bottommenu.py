import platform, os

if platform.system() == 'Windows':
    os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivymd.uix.screen import MDScreen
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
import json

class BottomMenu(Screen):
    pass

class Tarefas(Screen):
    tarefas = []
    path = ''

    def on_pre_enter(self):
        #self.path = App.get_running_app().user_data_dir+'/'
        self.loadData()
        for tarefa in self.tarefas:
            self.ids.box.add_widget(Tarefa(text=tarefa))

    def loadData(self, *args):
        try:
            with open('data.json', 'r') as data:
                self.tarefas = json.load(data)
            print("entrou")
        except FileNotFoundError:
            pass

    def saveData(self,*args):
        with open('data.json','w') as data:
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
