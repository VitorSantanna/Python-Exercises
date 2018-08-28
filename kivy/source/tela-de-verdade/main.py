#coding: utf-8

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label


def click():
    print(textinput.text)


def build():
    layout = FloatLayout()

    global textinput
    textinput = TextInput(text="Enfermagem")
    textinput.size_hint = None, None
    textinput.height = 300
    textinput.width = 400
    textinput.x = 60
    textinput.y = 250

    btn = Button(text="Clique Aqui")
    btn.on_press = click
    btn.size_hint = None, None
    btn.width = 200
    btn.height = 50
    btn.x = 150
    btn.y = 170

    layout.add_widget(textinput)
    layout.add_widget(btn)

    return layout


from kivy.core.window import Window
Window.size = 600, 600



janela = App()
janela.build = build
janela.run()