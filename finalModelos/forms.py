from wtforms import Form, StringField, TextField, validators, PasswordField
from wtforms.fields.html5 import EmailField

class CreateForm(Form):

	user= StringField('usuario', 
		[
			validators.Required('Ingrese un unsuario'),
			validators.length(min=3,max=25,message='Ingrese un usuario que tenga de 3 a 25 caracteres')
		])
	password = PasswordField('Password', [validators.Required(message='Se requiere contraseña')])

class LoginForm(Form):
	user= StringField('usuario', 
		[
			validators.Required('Ingrese un unsuario'),
			validators.length(min=3,max=25,message='Ingrese un usuario que tenga de 3 a 25 caracteres')
		])
	password = PasswordField('Password', [validators.Required(message='Se requiere contraseña')])