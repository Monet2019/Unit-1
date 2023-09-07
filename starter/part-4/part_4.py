## Step 1 - Input function

## Create five input statements to gather user's book they want to input to the system. After that be sure to turn it into a function.

# Code here


### Step 2 - Type conversion

## Now convert the proper data-types front strings to either floats or ints depending on what it is. Feel free to comment out your old function so you don't get an error, or copy/paste and give it a new name.

# Code here



### Step 3 - Error handling

## Now take your previous function, and handle potential errors should the user type an answer that doesn't convert data-type properly.

# Code here

def create_new_book():
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

    book_dictionary = {
        'title': title,
        'author': author,
        'year': year,
        'rating': rating,
        'pages': pages
    }

    return book_dictionary

print(create_new_book())


### Step 4 - if/elif/else

## Now create a main menu function that gives the user options. Handle their choices with if/elif/else statements.

# Code here

def main_menu(my_book_list):
    choice = input('Select 1 to add a book. Select 2 to see all books on the shelf. Select 3 to exit. - ')

    if choice == '1':
        my_book_list.append(create_new_book())
    elif choice == '2':
        print_all_books(my_book_list)
    elif choice == '3':
        print('Thank you for using the library')
    else:
        print('\nSorry, please type a number to select an option.\n')


def print_all_books(my_book_list):
    
    for book in my_book_list:
        title = book["title"]
        author = book["author"]
        year = book["year"]
        rating = book["rating"]
        pages = book["pages"]

        print(f'Title: {title}, Author: {author}, Year: {year}, Rating: {rating}, Pages: {pages}')

### Step 5 - while loops

## Now add a while loop to your main menu to keep it alive, and continually asking for input until the user chooses to exit the program. Call the main menu to ensure it functions properly.

# Code here

current_books = [
    {
        "title": "Harry Potter and the Sorcerer's Stone",
        "author": "J.K. Rowling",
        "year": 1997,
        "rating": 4.5,
        "pages": 309
    },
]


def main_menu(my_book_list):
    while True:   
        choice = input('Select 1 to add a book. Select 2 to see all books on the shelf. Select 3 to exit. - ')

        if choice == '1':
            my_book_list.append(create_new_book())
        elif choice == '2':
            print_all_books(my_book_list)
        elif choice == '3':
            print('Thank you for using the library')
        else:
            print('\nSorry, please type a number to select an option.\n')

main_menu(current_books)
