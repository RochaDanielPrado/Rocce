import platform, os

if platform.system() == 'Windows':
    os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

from kivy.uix.screenmanager import Screen
from kivymd.uix.card import MDCard

class DashBoard(Screen):
    pass

class ElementCar(MDCard):
    pass