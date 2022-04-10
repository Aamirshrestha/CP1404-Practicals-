from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty

class DynamicLabelApp(App):
    status_text = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name_to_phone ={"Charile Fox": "0494710623", "Lang Buddha": "0444156697", "Ryan Howard": "0435687901"}

    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for name in self.name_to_phone:
            temp_button = Label(text=name)
            temp_button.bind(on_release=self.press_entry)
            self.root.ids.entries_box.add_widget(temp_button)

    def press_entry(self, instance):

        name = instance.text

        self.status_text = "{}'s number is {}".format(name, self.name_to_phone[name])

    def clear_all(self):

        self.root.ids.entries_box.clear_widgets()


DynamicLabelApp().run()

