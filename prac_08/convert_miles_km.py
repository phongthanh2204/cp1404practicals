from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.core.window import Window

class ConvertMilesKmApp(App):
    converted_km = StringProperty('0.0')

    def build(self):
        Window.size = (300, 200)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_string(kv_layout_miles_km)
        return self.root

    def convert(self):
        try:
            miles = float(self.root.ids.input_miles.text)
            km = miles * 1.60934
            self.converted_km = '{:.5f}'.format(km)
        except ValueError:
            self.converted_km = '0.0'

    def handle_increment(self, change):
        try:
            current_miles = float(self.root.ids.input_miles.text)
        except ValueError:
            current_miles = 0
        new_miles = current_miles + change
        self.root.ids.input_miles.text = str(new_miles)
        self.convert()  # Automatically convert when incremented

ConvertMilesKmApp().run()
