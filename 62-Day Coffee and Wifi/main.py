from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, URLField
from wtforms.validators import DataRequired, URL
import csv

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    cafe_location = URLField('Cafe Location on Google Maps(URL)', validators=[DataRequired(), URL()])
    open_time = StringField('Opening Time e.g. 8AM', validators=[DataRequired()])
    close_time = StringField('Closing Time e.g. 5:30PM', validators=[DataRequired()])
    coffee_rating = SelectField('Coffee Rating', choices=[
        "",
        "☕️",
        "☕️☕️",
        "☕️☕️☕️",
        "☕️☕️☕️☕️",
        "☕️☕️☕️☕️☕️"
    ], validators=[DataRequired()])
    wifi_rating = SelectField('Wifi Strength Rating', choices=[
        "",
        "✘",
        "💪",
        "💪💪",
        "💪💪💪",
        "💪💪💪💪",
        "💪💪💪💪💪"
    ], validators=[DataRequired()])
    power_socket_rating = SelectField('Power Socket Availability', choices=[
        "",
        "✘",
        "🔌",
        "🔌🔌",
        "🔌🔌🔌",
        "🔌🔌🔌🔌",
        "🔌🔌🔌🔌🔌"
    ], validators=[DataRequired()])
    submit = SubmitField('Submit')


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("True")
        with open("cafe-data.csv", mode="a", newline="", encoding="utf-8") as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow([
                form.cafe.data,
                form.cafe_location.data,
                form.open_time.data,
                form.close_time.data,
                form.coffee_rating.data,
                form.wifi_rating.data,
                form.power_socket_rating.data
            ])
        return render_template("index.html")
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
