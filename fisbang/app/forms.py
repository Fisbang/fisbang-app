from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required, Length, Email, Regexp, EqualTo


class GetUpdateForm(Form):

    email = StringField('Your Email')
    submit = SubmitField('Submit')
