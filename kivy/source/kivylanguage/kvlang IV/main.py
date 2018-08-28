

#Author: João Vitor Sant' Anna

import kivy
kivy.require("1.9.1")
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class MinhaTela(BoxLayout):
    def click(self):
        print("oi")
        self.ids.lbl1.text = ""
        self.ids.lbl2.text = "10"


class Estudo4App(App):
    pass


janela = Estudo4App()
janela.run()