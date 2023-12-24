
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

class DynamicLabelsApp(App):
    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_string(kv_layout_dynamic_labels)
        self.names = ["Alice", "Bob", "Charlie", "Diana"]
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)
        return self.root

DynamicLabelsApp().run()
