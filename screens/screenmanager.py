import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

from kivy.uix.screenmanager import ScreenManager

sm = ScreenManager()

class MainScreenManager(ScreenManager):
    pass
