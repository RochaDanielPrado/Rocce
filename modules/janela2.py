import platform, os

if platform.system() == 'Windows':
    os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

from kivy.uix.screenmanager import Screen

class Janela2(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    pass