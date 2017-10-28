#pip install flask-mysql

import datetime
from flask import Flask, render_template, json, request, redirect, url_for
from flask.ext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'eric'
app.config['MYSQL_DATABASE_DB'] = 'Foodlist'
app.config['MYSQL_DATABASE_HOST'] = '10.1.232.217'
mysql.init_app(app)


@app.route('/')
def main():
	return render_template('index.html')

@app.route('/showSignUp')
def showSignUp():
	return render_template('signup.html')

@app.route('/showAddUp')
def showItem():
	return render_template('addItem.html')


@app.route('/addItem',methods=['POST','GET'])
def addItem():
	print("HEEEEEEE")
	_item = request.form['Item']
	_quantity = request.form['Quantity']
	_price = request.form['Price']
	_url = request.form['URL']
	print(_item)
	print(_quantity)
	print(_url)
	conn = mysql.connect()
	cursor = conn.cursor()

	user_id=1
	lat=0.5
	lon=0.2

	str_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	str_bbd = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	str_start = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	print(str_now)
	str_end = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	price_per_unit=False
	price=0.75
	category="Vege"
	img_url="google.com"

	cursor.callproc('sp_addFood',(_item,_quantity,user_id,
					lat,
					lon,
					str_now,
					str_bbd,
					str_start,
					str_end,
					price_per_unit,
					price,category,
					img_url ))
	data = cursor.fetchall()

	if len(data) is 0:
		conn.commit()
		print("TESTokfood")
		return redirect(str(request.url_root), code=302)
	else:
		print(data)
		print("TESTnotokf")
		return "Error"


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
		print("TESTin")
		return redirect(str(request.url_root), code=302)
	else:
		print(data)
		print("TEST2")
		return "Error"


@app.route('/success')
def success():
   return 'logged in successfully'


if __name__ == "__main__":
	app.run(port=5000)
