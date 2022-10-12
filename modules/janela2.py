import platform, os

if platform.system() == 'Windows':
    os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from kivymd.uix.list import IRightBodyTouch, OneLineAvatarListItem, ThreeLineAvatarListItem, ImageLeftWidget, ThreeLineAvatarIconListItem
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.icon_definitions import md_icons


class Janela2(Screen):

    def on_pre_enter(self):
        icons = list("images/atencao.png")
        for i in range(30):
            self.ids.scroll.add_widget(ListItemWithCheckbox(
                ImageLeftWidget(source="images/atencao.png"
                                ),
                text=f"Item {i}",
                secondary_text="Secondary text here",
                tertiary_text="fit more text than usual",
            )
            )

    def callback(self, instance):
        self.on_click()


class ListItemWithCheckbox(ThreeLineAvatarIconListItem):
    '''Custom list item.'''
    icon = StringProperty("android")


class RightCheckbox(IRightBodyTouch, MDCheckbox):
    '''Custom right container.'''
