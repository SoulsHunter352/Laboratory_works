# TODO Найдите количество книг, которое можно разместить на дискете
pages_count = 100  # Количество страниц в книге
lines_in_page = 50  # Количество строк на странице
letters_in_line = 25  # Количество букв в строке
weight_of_letter_in_byte = 4  # Вес одной буквы в байтах
floppy_size_in_byte = 1.44 * 1024 * 1024  # Количество байт, помещающихся на дискете
one_page_size = lines_in_page * letters_in_line * weight_of_letter_in_byte  # Размер одной страницы книги
count_books = int(floppy_size_in_byte // (one_page_size * pages_count))
print("Количество книг, помещающихся на дискету:", count_books)
