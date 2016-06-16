from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.logger import Logger
from kivy.core.window import Window
from kivy.properties import ObjectProperty, ListProperty
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
import fileinput
import sys,os
import re


from requests.auth import HTTPBasicAuth


from collections import deque
import json
import requests


Window.size = (320, 200)

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

class HearthClientAlert(Label):
    def display(self, message, color):
        self.text = message
        self.refresh()

class LoginClientScreen(Screen):
    def on_login_call(self, touch, pseudo, password):
        Logger.info('CHDCMenu: Function Send call')

        res = requests.get('http://127.0.0.1:8000/api/hearthlog/', auth=HTTPBasicAuth(pseudo.text, password.text))

        Logger.info('CHDCMenu: status_code req :' + str(res.status_code))

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
    user_pseudo = ObjectProperty(None)
    user_password = ObjectProperty(None)
    logs_path = ObjectProperty(None)
    message = ObjectProperty("Wellcome !")
    color = ListProperty([0.5,1,0.5,1])
    def on_send_call(self,touch):
        Logger.info('CHDCMenu: Function Send call')

        self.loadConfig()

        files = {'brutLog': open('hsgame.log', 'rb')}
        res = requests.post('http://127.0.0.1:8000/api/hearthlog/', files=files, auth=HTTPBasicAuth(self.user_pseudo, self.user_password))

        if(res.status_code == 201):
            self.message = "Successful logs send !"
        else:
            self.message = "Fail to send logs ..."
        Logger.info('CHDCMenu: status_code req :'+ str(res.status_code))

    def on_connect(self,pseudo,password):
        self.user_pseudo = pseudo
        self.user_password = password

    def dismiss_popup(self):
        self._popup.dismiss()

    def config_path(self, path, filename):
        Logger.info('CHDCMenu: Path ~~> ' + str(path) + ' filename ~~> '  + str(filename))
        if(filename):
            if(re.search(r"log\.config$",filename[0])):
                self.rewrite_logconfig(filename[0])
                self.setConfigClient('LogsPath',path+'/Logs/')
                self.message = "Config match and rewrite :)"
            else:
                self.message = "That not the \"log.config\" file"
            # self.message = 'filename = ' + str(filename)
        elif(path):
            listFileRep = os.listdir(path)
            checkList = ['Logs','Cache','options.txt']
            if(set(checkList)<set(listFileRep)):
                self.rewrite_logconfig(path+'/log.config')
                self.setConfigClient('LogsPath',path+'/Logs/')
                self.message = "Config match and rewrite"
            else:
                self.message = "Bad setting repository"
            # Logger.info('CHDCMenu: path : '+ path)
            # for subpath in listFileRep:
            #     Logger.info('CHDCMenu: file : '+ subpath)
            # self.message = 'path = ' + str(path)

    def rewrite_logconfig(self,filename):
        logFile = open('config/log.config','r')
        orgLogFile = open(filename,'w')
        orgLogFile.write(logFile.read())

    def show_config(self):
        content = ConfigDialog(config=self.config_path, cancel=self.dismiss_popup)
        self._popup = Popup(title="Config file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def setConfigClient(self, champs, valeur):
        for line in fileinput.input('config/hearthdeep.config', inplace=True):
            if champs in line:
                line = champs+':'+valeur
            sys.stdout.write(line)

    def loadConfig(self):
        f = open('config/hearthdeep.config','r')
        match = re.match(r'^LogsPath:(.*)', f.read())
        self.logs_path = match.group(1)


class ConfigDialog(FloatLayout):
    config = ObjectProperty(None)
    cancel = ObjectProperty(None)


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
