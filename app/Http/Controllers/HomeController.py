from flask import render_template

class HomeController():
	# function handle index
	def index():
		return render_template('blog/home.html')
	def about():
		return render_template('blog/about.html')