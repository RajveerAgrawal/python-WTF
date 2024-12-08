from flask import Flask, render_template, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import (
    StringField, BooleanField, DecimalField, IntegerField, RadioField,
    SelectField, TextAreaField, PasswordField, SubmitField
)
from wtforms.validators import DataRequired, Email, NumberRange

app = Flask(__name__)
app.config['SECRET_KEY'] = 'test'  # Replace with a secure secret key

# Define the form class
class EnhancedForm(FlaskForm):
    text_field = StringField('Your Name', validators=[DataRequired()])
    email_field = StringField('Email', validators=[DataRequired(), Email()])
    password_field = PasswordField('Password', validators=[DataRequired()])
    decimal_field = DecimalField('Decimal (Rating: 0.0 - 5.0)', validators=[DataRequired(), NumberRange(min=0, max=5)])
    integer_field = IntegerField('Age', validators=[DataRequired()])
    text_area_field = TextAreaField('Your Feedback', validators=[DataRequired()])
    boolean_field = BooleanField('Accept Terms', validators=[DataRequired()])
    submit_field = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = EnhancedForm()
    if form.validate_on_submit():
        # Gather data from form fields
        data = {
            'Name': form.text_field.data,
            'Email': form.email_field.data,
            'Password': form.password_field.data,
            'Rating': form.decimal_field.data,
            'Age': form.integer_field.data,
            'Feedback': form.text_area_field.data,
            'Terms Accepted': form.boolean_field.data,
        }
        flash(f'Form submitted successfully! Data: {data}', 'success')
        return redirect(url_for('index'))
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
