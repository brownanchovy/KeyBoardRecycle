from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy_garden.filebrowser import FileBrowser
from ..keyBind import keyboardInput

CSV_FILE = 'last_directory.csv'

class Modify(Popup):
    def __init__(self, **kwargs):
        super(Modify, self).__init__(**kwargs)

class ShortcutSettingPopup(Popup):
    def __init__(self, **kwargs):
        super(ShortcutSettingPopup, self).__init__(**kwargs)
        self.ids.save_button.bind(on_release=self.save_shortcut)
        self.ids.close_button.bind(on_release=self.dismiss)

    def show_file_browser(self):
        filebrowser = FileBrowser(select_string='Select', cancel_string='Cancel',
                                  filters=['*.txt'])  # Change the filter to desired extension
        filebrowser.bind(on_success=self._fbrowser_success, on_canceled=self._fbrowser_cancel)

        self.popup = Popup(title='File Browser', content=filebrowser, size_hint=(0.9, 0.9))
        self.popup.open()
    def _fbrowser_success(self, instance):
        print(instance.selection)
        self.ids.event_input.text = instance.selection[0]
        self.popup.dismiss()
    def _fbrowser_cancel(self, instance):
        self.popup.dismiss()
    def save_shortcut(self, instance):
        shortcut = self.ids.shortcut_input.text
        event = self.ids.event_input.text
        if shortcut and event:
            App.get_running_app().root.add_shortcut(shortcut, event)
            self.dismiss()

class MainScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)

    def open_popup(self, select):
        if select == 'ShortcutSettingPopup':
            popup = ShortcutSettingPopup()
        else:
            popup = Modify()
        popup.open()

    def add_shortcut(self, shortcut, event):
        icon = Button(text=f'Shortcut: {shortcut}, Event: {event}', size_hint_y=None, height='40dp')
        self.ids.shortcuts_layout.add_widget(icon)


class ShortcutApp(App):
    def build(self):
        return MainScreen()

if __name__ == '__main__':
    ShortcutApp().run()
