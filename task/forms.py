# Flask modules
from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField
from wtforms.validators import DataRequired, Length, Regexp


class CreatTaskForm(FlaskForm):
    name = StringField('Task name', validators=[
        DataRequired(),
        Length(min=2, max=80),
        Regexp(r'^[a-zA-Z0-9_]+$', message='Name must contain only letters, numbers, and underscores.')],
                       render_kw={'placeholder': 'Task name'})
    status = SelectField('Status', choices=[('To-Do','To Do'),('Complete', 'Completed'), ('In-Progress', 'In Progress')])
   
    submit = SubmitField('Done')
