from flask import Blueprint, render_template
from app.models import Book, Genre

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    latest_books = Book.query.order_by(Book.id.desc()).limit(15).all()
    return render_template('index.html', latest_books=latest_books)

@bp.route('/genre/<int:genre_id>')
def genre(genre_id):
    genre = Genre.query.get_or_404(genre_id)
    books_in_genre = genre.books
    return render_template('genre.html', genre=genre, books=books_in_genre)
