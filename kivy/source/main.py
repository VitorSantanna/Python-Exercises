

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button


class RootWidget(FloatLayout):
    pass


class EnfermagemApp(App):

    def build(self):
        return RootWidget()


EnfermagemApp().run()
