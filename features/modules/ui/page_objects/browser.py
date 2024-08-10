class Browser:
	def go_to_url(self, url):
		self.browser.goto(url)

	def window_maximize(self):
		self.browser.window().maximize()