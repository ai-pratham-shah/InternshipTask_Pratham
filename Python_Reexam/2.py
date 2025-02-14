class LibraryManagement:
    def __init__(self):
        self.book_record = []

    def get_book_data(self):
        """
        Function to take user input for books.
        The user will enter details like Book name, Author Name, and, Isbn number.
        Returns a list of book records entered by the user.
        """
        try:
            num_entries = int(input("Enter the number of book records: "))
            for _ in range(num_entries):
                book_name = input("Enter book title: ")
                author = input("Enter author of book: ").isalpha()
                isbn = int(input("Enter isbn number for book: "))
                self.book_record.append({
                    "book_name": book_name,
                    "author": author,
                    "isbn": isbn,
                })
        except Exception as e:
            print(f"Error occurred while adding books: {e}")

    def checkout_book(self):
        '''
        Show the all books to the user and ask which book he/she wants
        so for that ask user book name if it is found in book records
        then mark that book as an unavailable
        '''
        pass

    def search_book(self):
        '''
        Function to take user input for book title or author then
        prints that book if it is available

        logic : take variable search and find value of search
        in the book_records if it is find in book name or
        author name then print that book otherwise print No book found
        '''
        try:
            search = input("Enter a book name or author you want to search: ")
            if search in self.book_record:
                print(f"Book title:, Book author:")
            else:
                print("No book found")

        except Exception as e:
            print(f"Error occurred while searching records: {e}")

    def show_book(self):
        try:
            if not self.book_record:
                print("No records found.")
            else:
                print("All Books:", self.book_record)
        except Exception as e:
            print(f"Error occurred while showing records: {e}")

    def return_book(self):
        '''
        Function ask the user to which book he/she wants to return
        for that system prints the all the borrowed/unavailable book
        list ti the user and ask user to write the name of the book
        that he/she wants to return if that book name is found in
        unavailable book list then marked that book as an available
        if not found then print the message that this is not a valid book name
        '''
        try:
            pass
        except Exception as e:
            print(f"Error occurred while returning book: {e}")


    def display_particular_book(self):
        '''
        Function ask the user that which book data he/she want to
        display for that first print all the available books after
        that ask user for book name if that book name is found in
        book record then print particular that book record
        '''
        try:
            pass
        except Exception as e:
            print(f"Error occurred while display particular book: {e}")


def main():
    library = LibraryManagement()
    while True:
        print("\n!!!!!! Welcome to library management system !!!!!!")
        print("1.Add new books to the library.")
        print("2.Check out books (mark them as unavailable).")
        print("3.Search for books by title or author.")
        print("4.List available books.")
        print("5. Return a book (mark it as available again).")
        print("6.Display information about a particular book.")
        print("7. Exit")
        choice = input("Enter your choice (1-7): ")

        try:
            if choice == "1":
                library.get_book_data()
            elif choice == "2":
                library.checkout_book()
            elif choice == "3":
                library.search_book()
            elif choice == "4":
                library.show_book()
            elif choice == "5":
                library.return_book()
            elif choice == "6":
                library.display_particular_book()
            elif choice == "7":
                print("Thank you for using the library management system. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
        except Exception as e:
            print(f"An error occurred: {e}")
if __name__ == "__main__":
    main()

