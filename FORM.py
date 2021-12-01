import kivy
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.app import App

#to change the background color
Window.clearcolor = (0,0,0,1)
#to change the size which is not really advicable yet cos when you convert this to app or apk it will reflect in your phone
Window.size = (350,700)

#this is to connect our python code with kv(design language)
Builder.load_file('form.kv')

#create a class where functions or backends are passed
class Form(Widget):
    #for now lets just pass it
    pass

#then  will need our app to return what the class that contains everything which is Form

class MyForm(App):
    def build(self):
        return Form()
if __name__ == '__main__':
    MyForm().run()