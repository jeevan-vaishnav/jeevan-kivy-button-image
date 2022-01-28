from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.tabbedpanel import TabbedPanel


# Designate Our .kv design file
Builder.load_file('main.kv')


class MyLayout(Widget):

    def hello_on(self):
        self.ids.my_label.text = f"You Presses the Button"
        self.ids.img_id.source = "login.jpg"

    def hello_off(self):
        self.ids.img_id.source = "login.png"


class AwesomeApp(App):
    def build(self):
        return MyLayout()


if __name__ == "__main__":
    AwesomeApp().run()
