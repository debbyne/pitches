from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed, FileRequired

class PitchForm(FlaskForm):
    pitch = TextAreaField('Tell us about you.', validators=[DataRequired()], render_kw={"placeholder": "Type a pitch..."})
    title = StringField('title', validators = [DataRequired()])
    category = SelectField('Type',choices=[('Pick Up line'),('Interview Pitch'),('Product Pitch')] ,validators=[DataRequired()])
    submit = SubmitField('Submit')
class CommentForm(FlaskForm):
  comment = TextAreaField('Comments',validators=[DataRequired()],  render_kw={"placeholder": "Type a comment..."} )
  submit = SubmitField('Submit')

class UpdateProfilePicture(FlaskForm):
    bio = TextAreaField('Change Profile Picture',validators = [FileRequired(), FileAllowed(['jpg','png'], 'Images only allowed.')] )
    submit = SubmitField('Change')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [DataRequired()])
    submit = SubmitField('Submit')
    