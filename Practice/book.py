import os
class Book:
    '''This class is used to create objects of books that are to be added to the library. It has attributes such as Tittle, Author, Publisher, Year of publication, ISBN number, and a boolean value to check if the book is available in the library or not.'''
    number_of_books=0
    def __init__(self,serial,tittle,author,publisher,year,isbn) -> None:
        self.tittle=tittle
        self.author=author
        self.publisher=publisher
        self.year=year
        self.isbn=isbn
        self.inlibrary=True
        self.serial=serial
        Book.number_of_books+=1

    def get_book_info(self):
        return f'Sr.No. {self.serial}, Tittle: {self.tittle}, Author: {self.author}, Publisher: {self.publisher}, Year published: {self.year}, ISBN: {self.isbn}, In Library: {self.inlibrary}'


class Library:
    '''This class is used to create objects of library that will have a dictionary of books that are available in the library. It has methods to add, borrow, return, and remove books from the library. It also has a method to display all the books that are available in the library.'''
    def __init__(self):
        self.librarybooks={}

    def get_info_from_user(self,i):
        '''It allow user to fill information in the system where information cosist of Book's Tittle, Author, Publisher, Publishing Year, and it's ISBN and then return an object of class Book'''

        while True:
            tittle=input('Enter the tittle of book: ')
            if tittle:break
            else:print('Tittle can\'t be empty')
     
        while True:
            author=input('Enter the name of the author of book: ')
            if author:break
            else:print('Tittle can\'\t be empty')
     
        while True:
            publisher=input('Enter the name of the publisher of book: ')
            if publisher:break
            else:print('Tittle can\'\t be empty')
     
        while True:
            try:
                year=int(input('Enter the year in which book was published (eg.2024): '))
                if year>2024 or year<618:
                    raise ValueError
                else:break
            except ValueError:print('Wrong input')
        
        while True:
            try:
                isbn=int(input('Enter the book ISBN number: '))
                if len(str(isbn))>=10:
                    print('Invalid ISBN enter a valid ISBN such as 978-3-16-148410-0/    9783161484100')
                else:break
            except ValueError:print('Invalid ISBN enter a valid ISBN such as 978-3-16-148410-0/9783161484100')
       
        return Book(i,tittle,author,publisher,year,isbn)

    def add_book_to_library(self,book_to_be_added):
        '''It take Object of class Book and add that to a dictionary of Object \'library\' of class \'Library\''''
        if book_to_be_added.isbn in self.librarybooks:
            print('Book already exist in the library')
        else:
            self.librarybooks[book_to_be_added.isbn]=book_to_be_added
            print(f'Book with ISBN {book_to_be_added.isbn} and Tittle {book_to_be_added.tittle} has been added to the library')
        while True:
            print()
            break_or_exit=int(input('Do you want to go back(1) or quit(2)'))
            if break_or_exit==1:
                print()
                break
            elif break_or_exit==2:exit()
            else:print('Invalid')

    def borrow_book_from_library(self):
        '''It allow user to borrow books from the library by asking them which available search method they would like to choose and then also mark the borrowed book as not available so it can't be borrowed again before it is returned.'''
        while True:
            choice=int(input('Do you wish to find book with ISBN(1) or Year Wise(2) or Go Back(3)? '))
            
            if choice==1:
                isbn_of_book_to_be_borrowed=int(input('Enter the ISBN of book to borrow: '))
                book_available_in_the_library=[book for book in self.librarybooks.values() if book.inlibrary and book.isbn==isbn_of_book_to_be_borrowed]
                
                for book in book_available_in_the_library:
                    print(book.get_book_info())
                confimation=input('Is this the book (Yes/No)? ')
               
                if confimation=='Yes' or 'yes':
                 if book_available_in_the_library:
                    for book in self.librarybooks.values():
                        if book.isbn==isbn_of_book_to_be_borrowed:
                            book.inlibrary=False
                            print('Book borrowed successfully')
                        # print(book.get_book_info())
                 break
                
                elif confimation=='No' or 'NO' or 'no':
                    print('Let\'s retry')
                else:print('Invalid Choice')
           
            elif choice==2:
                year_book_was_published=int(input('Enter the Year of book publication to borrow: '))
                book_available_in_the_library=[book for book in self.librarybooks.values() if book.inlibrary and book.year==year_book_was_published]
                for book in book_available_in_the_library:
                    print(book.get_book_info())
                    
                confimation=int(input('If book you want is one of these enter serial number. '))
               
                book_choosen=[book for book in book_available_in_the_library if book.serial==confimation]
                if book_choosen:
                    for book in book_choosen:
                        book.inlibrary=False
                        print('Book borrowed successfully')
                    # print(book.get_book_info())
                    break

                elif confimation=='No' or 'NO' or 'no':
                    print('Let\'s retry')
                else:print('Invalid Choice')
            
            elif choice==3:break
            else:print('Invalid Choice')

        while True:
            print()
            break_or_exit=int(input('Do you want to go back(1) or quit(2)'))
            if break_or_exit==1:
                print()
                break
            elif break_or_exit==2:exit()
            else:print('Invalid')

    def return_book_to_library(self):
        '''It allow user to return the books they have borrowed from library and mark then as available to be borrowed again.'''
        while True:
            borrow_method=int(input('Do you wish to return the book using ISBN(1) or Year(2) or go Back(3)'))
            if borrow_method==1:
                isbn_of_borrowed_book=int(input('Enter the ISBN of book you borrowed.'))
                for book in self.librarybooks.values():
                    if book.isbn==isbn_of_borrowed_book:
                        print(book.get_book_info())
                        while True:
                            confirm=int(input('Is this the book you borrowed Yes(1)/No(2)'))
                            if confirm is 1:
                                book.inlibrary=True
                                print('Book returned successfully')
                                break
                            elif confirm==2:
                                print('Let\'s retry')
                                break
                            else:print('Invalid input')
                break

            elif borrow_method==2:
                year_book_borrowed=int(input('In which year the book you borrowed was published? '))
                books_in_stated_year=[book for book in self.librarybooks.values() if book.year==year_book_borrowed and book.inlibrary==False]
                for book in books_in_stated_year:
                    print(book.get_book_info())
                serial_of_borrowed_book=int(input('Enter the serial number of book you borrowed.'))
                for book in books_in_stated_year:
                    if book.serial==serial_of_borrowed_book:
                        book.inlibrary=True
                        print('Book returned successfully')
                break
            
            elif borrow_method==3:break
            else:print('Invalid choise')

        while True:
            print()
            break_or_exit=int(input('Do you want to go back(1) or quit(2)'))
            if break_or_exit==1:
                print()
                break
            elif break_or_exit==2:exit()
            else:print('Invalid')

    def remove_book_from_library(self):
         '''It allow it\'s user to remove a book from the library.'''
         while True:
            isbn_of_book_to_be_removed=int(input('Enter the ISBN of Book you wish to remove  form library or go back(0). '))
            if isbn_of_book_to_be_removed==0:break
            for book in self.librarybooks.values():
                if book.isbn==isbn_of_book_to_be_removed:
                    print(book.get_book_info())
                choise=int(input('Is this the book Yes(1)/No(2) ? '))
                if choise==1:
                    del self.librarybooks[isbn_of_book_to_be_removed]
                    print('Book removed')
                    break
         while True:
            print()
            break_or_exit=int(input('Do you want to go back(1) or quit(2)'))
            if break_or_exit==1:
                print()
                break
            elif break_or_exit==2:exit()
            else:print('Invalid')

    def all_books_info(self):
        '''It tells it\'s user about all the books that are available at any moment.'''
        books_in_the_library=[abook for abook in self.librarybooks.values() if abook.inlibrary]
        if books_in_the_library:
            print('List of all available books is as follows: ')
            print(f'Total no of book\'s in the library is {Book.number_of_books}')
            for eachbook in books_in_the_library:
                print(eachbook.get_book_info())
        while True:
            print()
            break_or_exit=int(input('Do you want to go back(1) or quit(2)'))
            if break_or_exit==1:
                print()
                break
            elif break_or_exit==2:exit()
            else:print('Invalid')

      

def main():
    i=1
    library=Library()
    while True:
     os.system('cls')
     print('Library Menu:')
     print('1. Add a book')
     print('2. Borrow a book')
     print('3. Return a book')
     print('4. Display available books')
     print('5. Remove a book')
     print('6. Exit')
     
     while True:
         choice=int(input('Enter your choice (1-6): '))
         print()
         if choice>=1 and choice<=6:break
         else:print('Invalid choice')

     if choice==1:
         new_book=library.get_info_from_user(i)
         library.add_book_to_library(new_book)
         i=i+1
         print()
     elif choice==2:
         library.borrow_book_from_library()
         print()
     elif choice==3:
         library.return_book_to_library()
         print()
     elif choice==4:
         library.all_books_info()
         print()
     elif choice==5:
         library.remove_book_from_library()
         print()
     elif choice==6:
         print('exit')
         print()
         break
     else:
         print('invalid input')
         print()

if __name__=='__main__':
    main()
