from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.logger import Logger
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen


from requests.auth import HTTPBasicAuth


from collections import deque
import json
import requests


Window.size = (320, 240)

# class ClientHearthDeepWidget(BoxLayout):
#     def __init__(self, **kwargs):
#         super(ClientHearthDeepWidget, self).__init__(**kwargs)
#         self.orientation = "vertical"
#
#     def display_message(self, message):
#         Logger.info('Info HearthDeepClient: '+ message)
#
#     def on_touch_down(self, touch):
#         self.display_message(message="T'a vu !!!")

class LoginClientScreen(Screen):
    def on_login_call(self, touch, pseudo, password):
        Logger.info('CHDCMenu: Function Send call')

        res = requests.get('http://127.0.0.1:8000/api/hearthlog/', auth=HTTPBasicAuth(pseudo.text, password.text))

        Logger.info('CHDCMenu: status_code req :'+ str(res.status_code))

        if(res.status_code == 200):
            pseudo.background_color = [0.5,1,0.5,1]
            password.background_color = [0.5,1,0.5,1]
            self.manager.current = 'client'
            self.manager.current_screen.on_connect(pseudo=pseudo.text, password=password.text)
        else:
            pseudo.background_color = [1,0.5,0.5,1]
            password.background_color = [1,0.5,0.5,1]
        # Logger.info('CHDCMENU: pseudo : '+ str(pseudo) + ' pass : '+ str(password))

class HearthDeepClientScreen(Screen):
    user_pseudo = ''
    user_password = ''
    def on_send_call(self,touch):
        Logger.info('CHDCMenu: Function Send call')

        files = {'brutLog': open('hsgame.log', 'rb')}
        res = requests.post('http://127.0.0.1:8000/api/hearthlog/', files=files, auth=HTTPBasicAuth(self.user_pseudo, self.user_password))

        Logger.info('CHDCMenu: status_code req :'+ str(res.status_code))

    def on_connect(self,pseudo,password):
        self.user_pseudo = pseudo
        self.user_password = password

# class ClientHearthDeepClientMenu(BoxLayout):
#     def __init__(self, **kwargs):
#         super(ClientHearthDeepClientMenu, self).__init__(**kwargs)
#         self.orientation = "vertical"
#
#         btn_send = Button(text='Send HS logs')
#         btn_send.bind(on_press=self.on_send_call)
#
#         btn_check = LoginClientScreen()
#         btn_check.bind(on_press=self.on_check_call)
#
#         for but in [btn_send, btn_check]:
#             self.add_widget(but)
#
#     def on_send_call(self,touch):
#         Logger.info('CHDCMenu: Function Send call')
#
#         files = {'brutLog': open('hsgame.log', 'rb')}
#         res = requests.post('http://127.0.0.1:8000/api/hearthlog/', files=files, auth=HTTPBasicAuth('thecoon', 'yodalapute'))
#
#         Logger.info('CHDCMenu: status_code req :'+ str(res.status_code))
#
#
#
#     def on_check_call(self, touch):
#         Logger.info('CHDCMenu: Function Check call')



class ClientHearthDeepApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginClientScreen(name='login'))
        sm.add_widget(HearthDeepClientScreen(name='client'))
        sm.current = 'login'
        # layout = BoxLayout(orientation='horizontal')
        # communication = ClientHearthDeepWidget()
        # menu = BoxLayout(orientation='vertical')
        # menu.add_widget(Button(text='Check'))
        # menu.add_widget(Button(text='Send'))
        # menu.add_widget(Button(text='Config'))
        # menu = ClientHearthDeepClientMenu()
        # layout.add_widget(communication)
        # layout.add_widget(menu)
        # return layout
        return sm

if __name__ == '__main__':
    ClientHearthDeepApp().run()
