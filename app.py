from flask import Flask
from flask import redirect, url_for

app = Flask(__name__)

@app.route('/admin')
def admin():
	return 'Hello Admin'
	
@app.route('/guest/<guest>')
def guest():
	return 'hello %s as guest' % guest

@app.route('/user/<name>')
def user(name):
	if name == 'admin':
		return redirect( url_for('admin'))
	else:
		return redirect( url_for('guest', guest = name))
	
if __name__ == '__main__':
	app.run(debug=True)
	