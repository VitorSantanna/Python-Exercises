#coding: utf-8
#Author: João Vitor Sant'Anna
##################
####GDM Family####
##################

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput


class TelaPrincipal(FloatLayout):
        def click(self):
            ti = self.ids.text_input
            ti.text = "Linha1\nLinha2\nLinha3\n"
            ti.readonly = False
            ti.font_name = "consola"
            ti.font_size = 25
            ti.foreground_color = .2, .5, .1, 1


class JanelaApp(App):
    pass


janela = JanelaApp()
janela.run()