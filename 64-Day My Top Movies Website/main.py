from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
from sqlalchemy import asc


# API_KEY = "10df4e9135f04e8c1acdfc0bd714f3c1"
# API_READ_ACCESS_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxMGRmNGU5MTM1ZjA0ZThjMWFjZGZjMGJkNzE0ZjNjMSIsInN1YiI6IjY1N" \
#                         "TRjOTQ5NjdiNjEzNDVjY2FlYWQwMSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.cGUS8DPS-Q0r" \
#                         "RhHee2me1Uxzu0COHKQQ8niOHIEDF2I"


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
db = SQLAlchemy()
db.init_app(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)


with app.app_context():
    db.create_all()


class RateMovieForm(FlaskForm):
    rating = StringField('Your Rating Out of 10 e.g. 7.5', validators=[DataRequired()])
    review = StringField('Your Review', validators=[DataRequired()])
    submit = SubmitField('Done')


class AddMovieForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")


@app.route("/")
def home():
    # result = db.session.execute(db.select(Movie))
    # result = db.session.execute(db.select(Movie).order_by(Movie.rating)).scalars().all()
    all_movies = db.session.query(Movie).order_by(asc(Movie.rating)).all()
    # all_movies = result.scalars()

    # Calculate the ranking
    total_movies = len(all_movies)
    for i, movie in enumerate(all_movies, start=1):
        movie.ranking = total_movies - i + 1

    # Update rankings in the database
    with app.app_context():
        for movie in all_movies:
            movie_to_update = db.get_or_404(Movie, movie.id)
            movie_to_update.ranking = movie.ranking

        db.session.commit()

    return render_template("index.html", movies=all_movies)


@app.route("/edit", methods=["GET", "POST"])
def edit():
    form = RateMovieForm()
    id = request.args.get("id")
    if form.validate_on_submit():
        with app.app_context():
            movie_to_update = db.get_or_404(Movie, id)
            movie_to_update.rating = float(form.rating.data)
            movie_to_update.review = form.review.data
            db.session.commit()
            return redirect(url_for('home'))
    return render_template("edit.html", form=form)


@app.route("/delete")
def delete():
    movie_id = request.args.get('id')
    # Delete a record by ID
    movie_to_delete = db.get_or_404(Movie, movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddMovieForm()
    if form.validate_on_submit():
        title = form.title.data
        URL = f"https://api.themoviedb.org/3/search/movie?query={title}&include_adult=false&language=en-US&page=1"
        HEADERS = {
            "accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxMGRmNGU5MTM1ZjA0ZThjMWFjZGZjMGJkNzE0ZjNjMSIsInN1"
                             "YiI6IjY1NTRjOTQ5NjdiNjEzNDVjY2FlYWQwMSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjox"
                             "fQ.cGUS8DPS-Q0rRhHee2me1Uxzu0COHKQQ8niOHIEDF2I"
        }

        response = requests.get(URL, headers=HEADERS)
        data = response.json()['results']
        return render_template("select.html", movie_data=data)
    return render_template('add.html', form=form)


@app.route('/find')
def find():
    MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"
    movie_id = request.args.get('id')
    if movie_id:
        URL = f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US"
        HEADERS = {
            "accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxMGRmNGU5MTM1ZjA0ZThjMWFjZGZjMGJkNzE0ZjNjMSIsInN1YiI6"
                             "IjY1NTRjOTQ5NjdiNjEzNDVjY2FlYWQwMSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.cGUS8DP"
                             "S-Q0rRhHee2me1Uxzu0COHKQQ8niOHIEDF2I"
        }
        response = requests.get(URL, headers=HEADERS)
        data = response.json()
        new_movie = Movie(
            title=data['title'],
            year=data['release_date'].split('-')[0],
            description=data['overview'],
            img_url=f"{MOVIE_DB_IMAGE_URL}{data['poster_path']}",
            rating=0.0,
            ranking="",
            review=""
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for('edit', id=new_movie.id))


if __name__ == '__main__':
    app.run(debug=True)