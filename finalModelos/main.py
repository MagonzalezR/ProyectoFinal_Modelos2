from flask import Flask, request, render_template, make_response, session, url_for, redirect
from flask_wtf import CSRFProtect
from config import DevelopmentConfig
from modelos import db, User
import forms
import json
app= Flask(__name__)
app.config.from_object(DevelopmentConfig())
csrf= CSRFProtect(app)

@app.route('/')
def index():
	if 'user' in session:
		username = session['user']
		print (username)
	else: return redirect(url_for('login'))
	return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
	loginForm= forms.LoginForm(request.form)
	if (request.method=='POST' and loginForm.validate()):
		user= loginForm.user.data
		contraseña= loginForm.password.data
		usuario= User.query.filter_by(user= user).first()
		if (user is not None and usuario.verifyPassword(contraseña)):
			session['user']=user
			return redirect(url_for('index'))
		session['user'] = loginForm.user.data
	return render_template('login.html', form=loginForm)

@app.route('/logout')
def logout():
	if 'user' in session:
		session.pop('user')
	return redirect(url_for('login'))

@app.route('/crear', methods=['GET', 'POST'])
def crear():
	crearForm= forms.CreateForm(request.form)
	if (request.method=='POST' and crearForm.validate()):
		user = User(crearForm.user.data,
					crearForm.password.data)
		db.session.add(user)
		db.session.commit()
		session['user'] = crearForm.user.data
	if 'user' in session:
		return redirect(url_for('login'))
	return render_template('crear.html', form=crearForm)

@app.route('/juegoCal')
def juego1():
	return render_template('Calav.html')
	
@app.route('/juegoRun')
def juego2():
	return render_template('CovidRuner.html')
	
@app.route('/juegoSalt')
def juego3():
	return render_template('Saltarin.html')
	
@app.route('/juegoBuscF')
def juego4():
	return render_template('BuscF.html')
	
@app.route('/juegoGalaga')
def juego5():
	return render_template('Galaga.html')

if __name__=='__main__':
	csrf.init_app(app)
	db.init_app(app)
	with app.app_context():
		db.create_all()
		
	app.run(port=8000)
