from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, SelectMultipleField
from wtforms.validators import Required, Length, Email, Regexp, EqualTo

from flask.ext.security.forms import RegisterFormMixin, UniqueEmailFormMixin, NewPasswordFormMixin, PasswordConfirmFormMixin

class CreateProjectForm(Form):

    project_category = SelectField('Project Category', coerce=int, choices=[])
    name = StringField('Project Name')
    skills = StringField('Skills')
    description = StringField('Description')
    project_budget = SelectField('Budget', coerce=int, choices=[])
    submit = SubmitField('Create Projects')

class CreateProjectWithRegister(CreateProjectForm, RegisterFormMixin, UniqueEmailFormMixin, NewPasswordFormMixin, PasswordConfirmFormMixin):
    pass
