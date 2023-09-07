### Step 1 - Store data in a .txt

## This step's instructions explains how to use the open() function, to write and read info from a .txt file. Follow the instructions to create and call a function to add a book, based off of the previous dictionaries for our file_name, to the .txt file properly formatted with commas as separators.

# Code here


def create_new_book(file_name):
    title = input('What is the title of the book you would like to add? - ')
    author = input('Who is the author of the book you would like to add? - ')
    try: 
        year = int(input('What year was this book published? - '))
    except: 
        year = int(input("Please type a number for the year? - "))
    try:
        rating = float(input('What rating out of 5 would you give this book? - '))
    except:
        rating = float(input('Please type a number for the rating? - '))
    try:
        pages = int(input('What is the page count of the book? - '))
    except:
        pages = int(input('Please type a number for the page count? - '))


    with open(file_name, "a") as file:
        file.write(f"{title}, {author}, {year}, {rating}, {pages}/n")

create_new_book("test.txt")


### Step 2 - Read data from a .txt

## Now take your previously create function which prints info about all the books in your file_name, but gets the info from a list, and make it work by reading the information in your home file_name's .txt document. This will take some new logic, but you can do it.

# Code here

def view_list(book_source):
    books_list = []
    
    with open(book_source, 'r') as f:
        file = f.readlines()

        for line in file:
            title, author, year, rating, pages = line.split(', ')
            new_book= {
                'title': title,
                'author': author,
                'year': int(year),
                'rating': float(rating),
                'pages': int(pages)
            }
    books_list.append(new_book)

    return books_list

#print(view_list("test.txt"))

### Step 3 - if __name__ == "__main__":

## Wrap your main menu function call in an "if __name__ == '__main__':" statement to ensure it doesn't accidentally run if this file is imported as a module elsewhere.

# Code this at the bottom of the script

def main_menu(view_list):
    choice = input('Select 1 to add a book. Select 2 to see all books on the shelf. Select 3 to exit. - ')

    if choice == '1':
        view_list.append(view_list())
    elif choice == '2':
        print('Thank you for using the file_name')
    else:
        print('\nSorry, please type a number to select an option.\n')

if __name__ == "__main__":
    main_menu("test.txt")

### Step 4 - Expand and refactor

## Now follow the instructions in this final step. Expand your project. Clean up the code. Make your application functional. Great job getting your first Python application finished!

def book_pages_are_even(file_name):
    if file_name["pages"] % 2 == 0:
        return True
    else:
        return False
    
def uppercase_book_title(file_name):
    for book in file_name:
        book['title'] = book['title'].upper()
    return file_name

def lowercase_book_title(file_name):
    for book in file_name:
        book['title'] = book['title'].lower()
    return file_name

