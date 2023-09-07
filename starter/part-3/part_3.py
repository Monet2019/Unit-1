my_book = {
    "title": "Then Hunger Games",
    "author": "Suzanne Collins",
    "year": 2008,
    "rating": 4.32,
    "pages": 374
}

# Follow the instructions in this part of the project. Define and flesh out your function below, which should accept a dictionary as an argument when called, and return a string of the info in that book-dictionary in a user-friendly readable format.

# Code below

def get_book(book_dictionary):
    book_string = f'This books name is {book_dictionary}[["title"], and was written by {book_dictionary}[["author"] and was published in {book_dictionary}[["year"]. It has a rating of {book_dictionary}[["rating"] and is {book_dictionary}[["pages"] long.'
    return book_string

print(get_book(my_book))


# Once you are finished with that function, create several more functions which return individual pieces of information from the book.

# Code below
def get_title(book_dictionary):
    title_string = f'The book title is {book_dictionary["title"]}'
    return title_string
print(get_title(my_book))

def get_author(book_dictionary):
    author_string = f'The author of the book is {book_dictionary["author"]}'
    return author_string
print(get_author(my_book))

def get_year(book_dictionary):
    year_string = f'The year the book was published is {book_dictionary["year"]}'
    return year_string
print(get_year(my_book))

def get_rating(book_dictionary):
    rating_string = f'The rating of the book is {book_dictionary["rating"]}'
    return rating_string
print(get_rating(my_book))

def get_pages(book_dictionary):
    pages_string = f'The amount of pages the book has is {book_dictionary["pages"]}'
    return pages_string
print(get_pages(my_book))

# Finally, create at least three new functions that might be useful as we expand our home library app. Perhaps thing of a way you could accept additional arguments when the function is called? Also, imagine you have a list filled with dictionaries like above.

# Code below

books = [
    {
        "title": "Queen Charlotte: Before the Bridgertons came the love story that changed the ton",
        "author": "Julia Quinn",
        "year": 2023,
        "rating": 5.00,
        "pages": 352
    }
]

def search_by_author(books, author):
    searched_authors = []
    for book in books:
        if book['author'] == author:
            searched_authors.append(book)
    return searched_authors

print(search_by_author(books, 'Julia Quinn'))
