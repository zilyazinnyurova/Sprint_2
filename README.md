# qa_python

1. test_add_new_book_new_name_is_added_to_books_genre 
Проверяет добавление книги.Книга изначально не должна быть в словаре, а так же  длина названия должна быть меньше 41 и больше 0.
2. test_add_new_book_long_name_is_not_added_to_books_genre
Негативный тест. Добавляем книгу, где длина больше 41.
3. test_set_book_genre_existed_name_genre_is_set_for_book
Проверяем, что для книги устанавляивается жанр
4. test_get_book_genre_existed_name_is_returned_book_genre
Проверяем, что книга возвращается после добавления по указанному ключу.
5. test_get_books_with_specific_genre_existed_genre_is_returned_books_with_genre
Выводим список книг с определённым жанром, перед этим убеждаемся что книга существует в словаре, а жанр в списке.
6. test_get_books_genre_is_returned_books_genre
Метод get_books_genre возвращает словарь книг
7. test_get_books_for_children_is_returned_chiledren_books_only
Проверяем, что книга есть в словаре, убеждаемся что жанр книги не указан в списке genre_age_rating и возвращаем книги, подходящие детям.
8. test_add_book_in_favorites_existed_name_is_added_to_favorites
Проверяем, что книга есть в словаре, убеждаемся что этой же книги нету в избранных и добавляем.
9. test_delete_book_from_favorites_existed_name_in_favorites_is_deleted_from_favorites.
Проверяем, что книга есть в избранных и удаляем.
10. test_get_list_of_favorites_books_is_returned_favorites
Создаем избранные книги и возвращаем его.
