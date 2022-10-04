import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
"""
This is an example of kaki app usin kivymd modules.
"""

from kivymd.app import MDApp
from kaki.app import App
from kivy.factory import Factory

# main app class for kaki app with kivymd modules
class LiveApp(MDApp, App):
    """ Hi Windows users """

    DEBUG = 1 # set this to 0 make live app not working

    # *.kv files to watch
    KV_FILES = {
        os.path.join(os.getcwd(), "screens/screenmanager.kv"),
        os.path.join(os.getcwd(), "screens/loginscreen.kv"),
    }

    # class to watch from *.py files
    CLASSES = {
        "MainScreenManager": "screens.screenmanager",
        "LoginScreen": "screens.loginscreen",
    }

    # auto reload path
    AUTORELOADER_PATHS = [
        (".", {"recursive": True}),
    ]


    def build_app(self):
        #self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"
        return Factory.MainScreenManager()




# finally, run the app
if __name__ == "__main__":
    LiveApp().run()