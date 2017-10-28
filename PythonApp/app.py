#pip install flask-mysql


from flask import Flask, render_template, json, request
from flask.ext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'eric'
app.config['MYSQL_DATABASE_DB'] = 'BucketList'
app.config['MYSQL_DATABASE_HOST'] = '10.1.232.217'
mysql.init_app(app)


@app.route('/')
def main():
	return render_template('index.html')

@app.route('/showSignUp')
def showSignUp():
	return render_template('signup.html')

@app.route('/signUp',methods=['POST','GET'])
def signUp():
	_name = request.form['inputName']
	_email = request.form['inputEmail']
	_password = request.form['inputPassword']
	print(_name)
	print(_email)
	print(_password)
	conn = mysql.connect()
	cursor = conn.cursor()

	cursor.callproc('sp_createUser',(_name,_email,_password))
	data = cursor.fetchall()

	if len(data) is 0:
		conn.commit()
		return "Sign"
	else:
		return "Error"


if __name__ == "__main__":
	app.run(port=5000)
