import platform, os

if platform.system() == 'Windows':
    os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from kivymd.uix.list import IRightBodyTouch, OneLineAvatarListItem, ThreeLineAvatarListItem, \
    ImageLeftWidget, ThreeLineAvatarIconListItem, MDList
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.button import MDFlatButton
from kivymd.uix.label import MDLabel
from kivymd.icon_definitions import md_icons


class Janela2(Screen):

    def on_pre_enter(self):
        icons = list("images/atencao.png")

        for i in range(2):

            self.ids.scroll.add_widget(ListItemWithCheckbox(
                 ImageLeftWidget(source="images/atencao.png"
                                 ),
                text=f"Item {i}",
                secondary_text="Secondary text here",
                tertiary_text="fit more text than usual",
                )
            )
            self.ids.box.add_widget(Quantidade())



    def callback(self, instance):
        self.on_click()


class ListItemWithCheckbox(ThreeLineAvatarIconListItem):
    '''Custom list item.'''
    icon = StringProperty("android")



class RightCheckbox(IRightBodyTouch, MDCheckbox):
    '''Custom right container.'''


class Quantidade(MDGridLayout):
    '''Custom right container.'''

    def n_plus(self):
        value = self.ids.label1.text
        if value == '':
            value = '0'
        elif int(value) >= 100:
            value = '99'
        self.ids.label1.text = str(int(value) + 1)


    def n_minus(self):
        value = self.ids.label1.text
        if value == '':
            pass
        elif int(value) >= 1:
            value_int = int(value) -1

            if value_int == 0:
                value = ''
                self.ids.label1.text = value
            else:
                self.ids.label1.text = str(value_int)







