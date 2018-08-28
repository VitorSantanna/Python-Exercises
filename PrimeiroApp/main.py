#coding: utf-8
#Author: João Vitor Sant' Anna
##################
####GDM Family####
##################

from kivy.app import App
from kivy.uix.label import Label


class PrimeiroApp(App):
    def build(self):
        self.icon = "icon.png"
        lbl = Label(text="PrimeiroApp")
        return lbl


primeiro = PrimeiroApp()
primeiro.run()