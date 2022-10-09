import platform, os

if platform.system() == 'Windows':
    os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

# from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen

class BottomMenu(MDScreen):
    pass