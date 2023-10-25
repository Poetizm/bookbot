import os
import sys

BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}


# Функция, возвращающая строку с текстом страницы и ее размер
def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    text2 = text[start:(start+size+1)]
    text = text[start:(start+size)]
    symbols = [',','.','!',':',';','?']
    i = -1
    while True:
        if text[-1].isalpha():
            text = text[:-1]
        elif not text[-1].isalpha():
            if (text[-1] in symbols and text2[-1] in symbols and len(text2) > len(text) or 
               text[-1] == ' ' and text[-2].isalpha() or 
               text[-1] in symbols and text[-2] in symbols):
                text = text[:-1]
            elif (text[-1] in symbols and text[-2].isalpha() or 
                  text[-1] == ' ' and text[-2] in symbols or 
                  text[-1] ==' \n' and text[-2] in symbols):
                    return (text.rstrip(), len(text.rstrip()))
                    break
            else:
                text = text[:-1] 


# Функция, формирующая словарь книги
def prepare_book(path: str) -> None:
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()
    start = 0
    for i in range(1, 14):
        stroka = _get_part_text(content, start, PAGE_SIZE)
        book[i] = stroka[0].lstrip()
        start = start + stroka[1]
        i+=1



# Вызов функции prepare_book для подготовки книги из текстового файла
prepare_book(os.path.join(sys.path[0], os.path.normpath(BOOK_PATH)))