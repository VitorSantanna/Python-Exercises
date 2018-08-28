#coding: utf-8

from kivy.app import App
from kivy.uix.label import Label


def build():
    lb = Label()
    lb.text = "Enfermagem"
    lb.font_size = 50
    lb.italic = True
    return lb


app = App()
app.build = build
app.run()