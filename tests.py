import pytest

from main import BooksCollector


class TestBooksCollector:

    @pytest.mark.parametrize(
        'book_name, book_genre',
        [
            ['Hamlet', 'Мультфильмы'],
            ['Otella', 'Детективы']
        ]
    )
    def test_add_new_book_new_name_is_added_to_books_genre(self, book_name, book_genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert collector.get_books_genre() == {book_name: ''}

    def test_add_new_book_long_name_is_not_added_to_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book('HamletHamletHamletHamletHamletHamletHamletHamletHamlet')
        assert collector.get_books_genre() == {}

    @pytest.mark.parametrize(
        'book_name, book_genre',
        [
            ['Hamlet', 'Мультфильмы'],
            ['Otella', 'Детективы']
        ]
    )
    def test_set_book_genre_existed_name_genre_is_set_for_book(self, book_name, book_genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, book_genre)
        assert collector.get_books_genre() == {book_name: book_genre}

    def test_get_book_genre_existed_name_is_returned_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Hamlet')
        collector.set_book_genre('Hamlet', 'Мультфильмы')
        assert collector.get_book_genre('Hamlet') == 'Мультфильмы'

    def test_get_books_with_specific_genre_existed_genre_is_returned_books_with_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Hamlet')
        collector.add_new_book('Otella')
        collector.set_book_genre('Hamlet', 'Мультфильмы')
        collector.set_book_genre('Otella', 'Детективы')
        assert collector.get_books_with_specific_genre('Мультфильмы') == ['Hamlet']

    def test_get_books_genre_is_returned_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Hamlet')
        collector.add_new_book('Otella')
        assert collector.get_books_genre() == {'Hamlet': '', 'Otella': ''}

    def test_get_books_for_children_is_returned_chiledren_books_only(self):
        collector = BooksCollector()
        collector.add_new_book('Hamlet')
        collector.add_new_book('Otella')
        collector.set_book_genre('Hamlet', 'Мультфильмы')
        collector.set_book_genre('Otella', 'Ужасы')
        assert collector.get_books_for_children() == ['Hamlet']

    def test_add_book_in_favorites_existed_name_is_added_to_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Hamlet')
        collector.add_new_book('Otella')
        collector.add_book_in_favorites('Hamlet')
        assert collector.get_list_of_favorites_books() == ['Hamlet']

    def test_delete_book_from_favorites_existed_name_in_favorites_is_deleted_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Hamlet')
        collector.add_new_book('Otella')
        collector.add_book_in_favorites('Hamlet')
        collector.delete_book_from_favorites('Hamlet')
        assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books_is_returned_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Hamlet')
        collector.add_new_book('Otella')
        collector.add_book_in_favorites('Hamlet')
        assert collector.get_list_of_favorites_books() == ['Hamlet']
