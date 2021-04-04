from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window

class AppWidget(Widget):

	def on_stop(self):
		App.get_running_app().root_window.close()
	pass
	
class WordChainApp(App):
	def build(self):
		Window.borderless = True

		return AppWidget()

	def on_stop(self):
		self.root_window.close()


if __name__ == '__main__':
	WordChainApp().run()
