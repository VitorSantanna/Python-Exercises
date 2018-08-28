#coding: utf-8

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

def build():
    btn = Button()
    btn.text = "Clique Aqui"
    btn.italic = True
    btn.on_press = click
    return btn


def click():
    print("O texto foi clicado")


janela = App()
janela.build = build
janela.run()
