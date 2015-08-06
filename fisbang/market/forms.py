from flask.ext.wtf import Form
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required, Length, Email, Regexp, EqualTo

class CreateProjectForm(Form):

    name = StringField('Your Name')
    email = StringField('Your Email')
    description = TextAreaField('Tell us about your idea/project')
    budget = StringField('Already has budget?')
    # deadline = StringField('And deadline')
    submit = SubmitField('Submit')
