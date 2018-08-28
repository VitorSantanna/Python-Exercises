#coding: utf-8

from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

def build():
    textinput = TextInput()
    textinput.text= "Relatório de Enfermagem: "
    return textinput





janela = App()
janela.build = build
janela.run()