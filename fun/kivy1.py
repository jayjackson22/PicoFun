from kivy.app import App
from kivy.uix.label import Label
 
 
class TrialApp(App):
    def build(self):
        return Label(
            text="Making an android app"
        )
 
demo=TrialApp()
demo.run()