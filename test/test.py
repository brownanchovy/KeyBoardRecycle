# main.py

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy_garden.filebrowser import FileBrowser
from kivy.lang import Builder
import os

# Load the KV file
Builder.load_file('fileexplorer.kv')

class FileExplorer(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.current_path = os.getcwd()
        self.update_path_label()

    def update_path_label(self):
        self.file_path_label.text = f"Current Path: {self.current_path}"

    def show_file_browser(self):
        filebrowser = FileBrowser(select_string='Select', cancel_string='Cancel', filters=['*.txt'])  # Change the filter to desired extension
        filebrowser.bind(on_success=self._fbrowser_success, on_canceled=self._fbrowser_cancel)

        self.popup = Popup(title='File Browser', content=filebrowser, size_hint=(0.9, 0.9))
        self.popup.open()

    def _fbrowser_success(self, instance):
        self.file_input.text = instance.selection[0]
        self.popup.dismiss()

    def _fbrowser_cancel(self, instance):
        self.popup.dismiss()

    def navigate_up(self):
        self.current_path = os.path.dirname(self.current_path)
        self.update_path_label()

    def navigate_down(self):
        # This is a placeholder for navigating into a selected directory.
        # Implement the logic as needed.
        pass

class FileExplorerApp(App):
    def build(self):
        return FileExplorer()

if __name__ == '__main__':
    FileExplorerApp().run()
