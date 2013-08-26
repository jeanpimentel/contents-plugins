import sublime_plugin

from lib import contents

class ContentsEventListenerCommand(sublime_plugin.EventListener):
	
	def on_post_save(self, view):
		contents.contents(view.file_name())
		window = view.window()

		if len(window.views()) == 1:
			new_window = window.new_file()
			self.iterate_focus(window, window.views())
			new_window.window().run_command("close")
		else:
			current_view = window.active_view()
			self.iterate_focus(window, window.views())
			window.focus_view(current_view)

	def iterate_focus(self, window, views):
		for v in views: 
			window.focus_view(v)