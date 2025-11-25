''''
Group Members: Ng Yi Zhi, Tan Yee Lim, Tiffany Sim Ling Lin, Hew Jia Le, Sum Hon You(Leader)
Latest Updated Date: 10/12/2023
Purpose of this program: To create a personal book management system to keep track of all
                        the books in your collection.
'''
import os
from datetime import datetime  # Import datetime module


# Function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')








# Function to display the main menu
def display_menu():
    # Print the Header when display_menu is call
    print("", ("=" * 32))
    print(f"{'|'.ljust(5)}{'Personal Books Management':^20}{'|'.rjust(6)}")
    print(" ", ("=" * 32))

    # Print the choices
    print("1. Add Book Record(s)")
    print("2. Delete Book Record(s)")
    print("3. Update/Edit Book Record(s)")
    print("4. Display")
    print("5. Search for Book(s)")
    print("6. Exit\n")








# Function to add single / multiple books
# :param books_dict: The dictionary containing information about various books.
def add_book(books_dict):
    clear_screen()

    while True:
        # Print the Header
        print("", ("=" * 28))
        print(f"{'|'.ljust(5)}{'Add Books':^20}{'|'.rjust(6)}")
        print(" ", ("=" * 28))

        # Prompt the user by providing 3 choices
        print("\n1. Add a single book")
        print("2. Add multiple books")
        print("3. Return to the main menu")
        choice = input("Enter your choice (1/2/3): ")

        # Error Handling when user did not enter "1" or "2" or "3"
        while choice not in ["1", "2", "3"]:
            print("\nInvalid choice. Please enter 1, 2, or 3.\n")
            choice = input("\nEnter your choice (1/2/3): ")

        # When user choose 1
        if choice == "1":
            clear_screen()

            # Error Handling when user did not enter ISBN in 13 digits
            while True:
                try:
                    ISBN = input(
                        "Enter Book ISBN:").strip()  # Using .strip() to remove the spacing in the leading and trailing
                    if ISBN.isdigit() and len(ISBN) == 13:
                        ISBN = int(ISBN)  # Convert to integer
                        break  # Execute the next statement
                    else:
                        print("Invalid input. ISBN must be a number with 13 digits.")
                except ValueError:
                    print("Invalid input. Please enter a valid ISBN.")

            # Prompting User to enter Author of the book
            Author = input("\nEnter Book Author: ").strip()
            while not Author:  # Error handling when user did not enter anything for Author
                print("Please enter the valid author's name or "
                      "put [N/A] if did not have any information: ")
                Author = input("Enter Book Author: ").strip()

            # Prompting User to enter Ttile of the book
            Title = input("\nEnter Book Title: ").strip()
            while not Title:  # Error handling when user did not enter anything for title
                print("Title cannot be empty. Please enter the book title or "
                      "put [N/A] if did not have any information.")
                Title = input("Enter Book Title: ").strip()

            # Prompting User to enter Publisher of the book
            Publisher = input("\nEnter Book Publisher: ").strip()
            while not Publisher:  # Error handling when user did not enter anything for Publisher
                print("Publisher cannot be empty. Please enter the book Publisher or "
                      "put N/A if did not have any information.")
                Publisher = input("Enter Book Publisher: ").strip()

            # Prompting User to enter Genre of the book
            Genre = input("\nEnter Book Genre: ").strip()
            while not Genre:  # Error handling when user did not enter anything for Genre
                print("Genre cannot be empty. Please enter the book Genre or "
                      "put N/A if did not have any information.")
                Genre = input("Enter Book Genre: ").strip()

            # Error Handling when user did not enter proper format in Year_Published
            Year_Published = input("\nEnter Year Published: ")
            while True:
                if Year_Published.isdigit() and len(Year_Published) == 4:
                    break
                else:
                    print("\nInvalid input. Please enter a valid year as a number.\n")
                    Year_Published = input("\nEnter Year Published: ")

            # Error Handling when user did not enter proper format in date_purchased_str
            while True:
                date_purchased_str = input("\nEnter Date Purchased (dd-mm-yyyy): ").strip()
                try:
                    date_purchased = datetime.strptime(date_purchased_str, "%d-%m-%Y")
                    date_purchased_str = date_purchased.strftime("%d-%m-%Y")
                    break
                except ValueError:
                    print("\nInvalid date format. Please use dd-mm-yyyy format.\n")

            # Prompting User to enter status of the book
            status = input("\nEnter Book Status [read/to-read]: ").lower().strip()
            while status not in ("read", "to-read"):  # Error handling when program did not detect "read" or "to-read"
                status = input("Please enter the book Status [read/to-read]: ").lower().strip()

            # Put all the information in variable: book in dictionary type
            book = {
                'ISBN': ISBN,
                'Author': Author,
                'Title': Title,
                'Publisher': Publisher,
                'Genre': Genre,
                'Year Published': Year_Published,
                'Date Purchased': date_purchased_str,
                'Status': status
            }

            clear_screen()
            print(f"Successfully added the book '{Title}'\n")
            books_dict[ISBN, Author, Title, Publisher, Genre, Year_Published, date_purchased_str, status] = book


        # When user choose 2
        elif choice == "2":
            clear_screen()

            # Error handling when user did not enter integer for number of times to loop
            while True:
                try:
                    times = int(input("Enter number of books that you want to add: "))
                    break
                except ValueError:
                    print("Please enter valid number!")

            # This for loop is looping those information based on the user enter how many books that they want to add
            for num in range(times):
                print(f"Please enter the informations for book {num + 1}")

                # Error Handling when user did not enter ISBN in 13 digits
                while True:
                    try:
                        ISBN = input(
                            "Enter Book ISBN:").strip()  # Using .strip() to remove the spacing in the leading and trailing
                        if ISBN.isdigit() and len(ISBN) == 13:
                            ISBN = int(ISBN)  # Convert to integer
                            break  # Execute the next statement
                        else:
                            print("Invalid input. ISBN must be a number with 13 digits.")
                    except ValueError:
                        print("Invalid input. Please enter a valid ISBN.")

                # Prompting User to enter Author of the book
                Author = input("\nEnter Book Author: ").strip()
                while not Author:  # Error handling when user did not enter anything for Author
                    print("Author cannot be empty. Please enter the author's name or "
                          "put [N/A] if did not have any information: ")
                    Author = input("Enter Book Author: ").strip()

                # Prompting User to enter Ttile of the book
                Title = input("\nEnter Book Title: ").strip()
                while not Title:  # Error handling when user did not enter anything for title
                    print("Title cannot be empty. Please enter the book title or "
                          "put [N/A] if did not have any information.")
                    Title = input("Enter Book Title: ").strip()

                # Prompting User to enter Publisher of the book
                Publisher = input("\nEnter Book Publisher: ").strip()
                while not Publisher:  # Error handling when user did not enter anything for Publisher
                    print("Publisher cannot be empty. Please enter the book Publisher or "
                          "put N/A if did not have any information.")
                    Publisher = input("Enter Book Publisher: ").strip()

                # Prompting User to enter Genre of the book
                Genre = input("\nEnter Book Genre: ").strip()
                while not Genre:  # Error handling when user did not enter anything for Genre
                    print("Genre cannot be empty. Please enter the book Genre or "
                          "put N/A if did not have any information.")
                    Genre = input("Enter Book Genre: ").strip()

                # Error Handling when user did not enter proper format in Year_Published
                Year_Published = input("\nEnter Year Published: ")
                while True:
                    if Year_Published.isdigit() and len(Year_Published) == 4:
                        break
                    else:
                        print("\nInvalid input. Please enter a valid year as a number.\n")
                        Year_Published = input("\nEnter Year Published: ")

                # Error Handling when user did not enter proper format in date_purchased_str
                while True:
                    date_purchased_str = input("\nEnter Date Purchased (dd-mm-yyyy): ").strip()
                    try:
                        date_purchased = datetime.strptime(date_purchased_str, "%d-%m-%Y")
                        date_purchased_str = date_purchased.strftime("%d-%m-%Y")
                        break
                    except ValueError:
                        print("\nInvalid date format. Please use dd-mm-yyyy format.\n")

                # Prompting User to enter status of the book
                status = input("\nEnter Book Status [read/to-read]: ").lower().strip()
                while status not in (
                        "read", "to-read"):  # Error handling when program did not detect "read" or "to-read"
                    status = input("Please enter the book Status [read/to-read]: ").lower().strip()

                # Put all the information in variable: book in dictionary type
                book = {
                    'ISBN': ISBN,
                    'Author': Author,
                    'Title': Title,
                    'Publisher': Publisher,
                    'Genre': Genre,
                    'Year Published': Year_Published,
                    'Date Purchased': date_purchased_str,
                    'Status': status
                }

                clear_screen()
                print(f"Successfully added the book '{Title}'\n")
                books_dict[ISBN] = book


            # Prompt user whether to exit this add book or continue to add book
            user_input = input("\nEnter (1) to exit, (2) to Add book again: ")

            # Error handling when user did not enter 1 or 2
            while user_input not in ("1", "2"):
                print("\nInvalid input. Please enter 1 to exit or 2 to continue.\n")
                user_input = input("\nEnter (1) to exit, (2) to Add book again: ")

            if user_input == "1":
                clear_screen()
                break
            elif user_input == "2":
                clear_screen()
                continue
            else:
                print("\nInvalid input. Please enter 1 to exit or 2 to continue.\n")
                clear_screen()


        # When user choose 3
        elif choice == "3":
            clear_screen()
            return  # will return to display_menu








# Function to delete single/ multiple books
def delete_book(books_dict):
    clear_screen()

    """
    A function to delete book information from the system.
    :param books_dict: The dictionary containing information about various books.
    """

    while True:
        print("\n1. Delete a single book")
        print("2. Delete multiple books")
        print("3. Return to the main menu")
        choice = input("Enter your choice (1/2/3): ")

        while choice not in ["1", "2", "3"]:
            print("\nInvalid choice. Please enter 1, 2, or 3.\n")
            choice = input("\nEnter your choice (1/2/3): ")

        if choice == "1":
            clear_screen()
            title_to_delete = input("\nEnter the title of the book you want to delete: ").strip()
            found = False
            for title, book in list(books_dict.items()):
                if book['Title'] == title_to_delete:
                    found = True
                    del books_dict[title]  # Delete the book from the dictionary
                    print(f"\nThe book '{title_to_delete}' has been deleted from the system.")
                    break

            if not found:
                print(f"\nThe book '{title_to_delete}' does not exist in the system.")


        elif choice == "2":
            clear_screen()
            titles_to_delete = input("\nEnter titles of the books you want to delete (separated by comma): ")
            titles_to_delete = [title.strip() for title in titles_to_delete.split(',')]
            deleted_count = 0  # track of the number of books deleted.

            for title in titles_to_delete:
                for key, book in list(books_dict.items()):
                    if book['Title'] == title:
                        del books_dict[key]  # Delete the book from the dictionary
                        deleted_count += 1
                        break

            if deleted_count > 0:
                print(f"\n{deleted_count} book(s) have been deleted from the system.\n")
            else:
                print("\nNo matching books found in the system\n")


        elif choice == "3":
            clear_screen()
            return  # Return to the main menu








# Function to update/edit book record(s)
def update_book_records(books_dict):
    clear_screen()

    print("\n=================================\n Update/Edit Book Record(s) \n=================================")

    while True:  # Outer Loop
        # Prompt the user to choose ISBN and author/title for updating

        while True:
            choice = input("Choose an option for (1) for ISBN / (2) for Author & Title to update: ").strip()
            if choice == "1" or choice == "2":
                break
            else:
                print("\nInvalid input, please enter either (1) or (2).\n")
                continue

        # Prompt the user to enter how many books they want to update
        while True:
            try:
                number_books_to_update = int(input("\nEnter the number of books you want to update: "))
                break  # Exit the loop if the input is a valid integer
            except ValueError:
                print("\nInvalid input. Please enter a valid integer.\n")

        for _ in range(number_books_to_update):
            if choice == "1" or choice == "(1)":
                while True:
                    isbn_to_update = input("\nEnter the ISBN of the book to update: ")
                    books_to_update = []  # Create an empty list to store the matching books.

                    # Iterate through each book in the books_dict list.
                    for book in books_dict.values():
                        if book['ISBN'] == isbn_to_update:
                            books_to_update.append(book)

                    if not books_to_update:
                        clear_screen()
                        print("\nNo matching records found.\n")


                    else:
                        for book in books_to_update:
                            clear_screen()
                            print(f"\nEditing book with ISBN: {book['ISBN']}")
                            print(
                                "\nIf that particular book's information did not have changes, please type again the original information.")

                            while True:
                                try:
                                    print(f"ISBN:({book['ISBN']})")
                                    new_ISBN = input("Enter New ISBN: ").strip()
                                    if new_ISBN.isdigit() and len(new_ISBN) == 13:
                                        new_ISBN = int(new_ISBN)  # Convert to integer
                                        break  # Exit loop if input is valid
                                    else:
                                        print("Invalid input. ISBN must be a number with 13 digits.")
                                except ValueError:
                                    print("Invalid input. Please enter a valid ISBN.")
                            book['ISBN'] = new_ISBN

                            while True:
                                try:
                                    new_Author = input(f"Author: ({book['Author']}): ").strip()
                                    if not new_Author:  # Check for an empty input
                                        print("\nAuthor Cannot Be Empty")
                                    else:
                                        book['Author'] = new_Author
                                        break  # Exit the loop if the input is not empty
                                except ValueError:
                                    print("Invalid input. Please enter an Author Name again.")

                            while True:
                                try:
                                    new_Title = input(f"Title: ({book['Title']}): ").strip()
                                    if not new_Title:  # Check for an empty input
                                        print("\nTitle Cannot Be Empty")
                                    else:
                                        book['Title'] = new_Title
                                        break  # Exit the loop if the input is not empty
                                except ValueError:
                                    print("Invalid input. Please enter the Title again.")

                            while True:
                                try:
                                    new_Publisher = input(f"Publisher: ({book['Publisher']}): ").strip()
                                    if not new_Publisher:  # Check for an empty input
                                        print("\nPublisher Cannot Be empty")
                                    else:
                                        book['Publisher'] = new_Publisher
                                        break  # Exit the loop
                                except ValueError:
                                    print("Invalid input. Please enter the Publisher again.")

                            while True:
                                try:
                                    new_Genre = input(f"Genre: ({book['Genre']}): ").strip()
                                    if not new_Genre:  # Check for an empty input
                                        print("\nGenre Cannot Be Empty")
                                    else:
                                        book['Genre'] = new_Genre
                                        break  # Exit the loop
                                except ValueError:
                                    print("Invalid input. Please enter the Genre again.")

                            while True:
                                try:
                                    new_YearPublished = int(input(f"Year Published: ({book['Year Published']}): "))
                                    break  # Exit the loop if the input is an integer
                                except ValueError:
                                    print("\nInvalid input. Please enter a valid year as a number.\n")
                            book['Year Published'] = new_YearPublished

                            while True:
                                # Check if the input is a valid date
                                Date_purchased_str = input(
                                    f"Date Purchased:({book['Date Purchased']})(dd-mm-yyyy):").strip()
                                try:
                                    Date_purchased = datetime.strptime(Date_purchased_str, "%d-%m-%Y")
                                    book['Date Purchased'] = Date_purchased.strftime("%d-%m-%Y")
                                    break
                                except ValueError:
                                    print("\nInvalid date format. Please use dd-mm-yyyy format.\n")

                            while True:
                                new_Status = input(f"Status: ({book['Status']}): ").strip()
                                try:
                                    if new_Status == 'to-read' or new_Status == 'read':
                                        book['Status'] = new_Status  # Set the new status
                                        break  # Allow transitioning from 'read' to 'to-read'
                                    else:
                                        print("\nPlease enter either 'to-read' or 'read'.")
                                except ValueError:
                                    print("\nPlease enter either 'to-read' or 'read'.")

                        clear_screen()
                        print("\nRecord updated successfully!\n")
                        break  # Exit the loop when the update is done


            elif choice == "2" or choice == "(2)":
                while True:
                    author_to_update = input("\nEnter the Author of the book to update: ")
                    title_to_update = input("Enter the Title of the book to update: ")
                    books_to_update = []
                    clear_screen()
                    print(f"\nSearching for books with Author: {author_to_update} and Title: {title_to_update}\n")

                    # Iterate through each book in the books_dict list.
                    for book in books_dict.values():

                        if book['Author'] == author_to_update and book['Title'] == title_to_update:
                            books_to_update.append(book)

                    if not books_to_update:
                        clear_screen()
                        print("\nNo matching records found.\n")


                    else:
                        for book in books_to_update:
                            clear_screen()
                            print(f"\nEditing book with Author: {author_to_update} and Title: {title_to_update}")
                            print(
                                "\nIf that particular book's information did not have changes, please type again the original information.")

                            while True:
                                try:
                                    print(f"ISBN:({book['ISBN']})")
                                    new_ISBN = input("Enter New ISBN: ").strip()
                                    if new_ISBN.isdigit() and len(new_ISBN) == 13:
                                        new_ISBN = int(new_ISBN)  # Convert to integer
                                        break  # Exit loop if input is valid
                                    else:
                                        print("Invalid input. ISBN must be a number with 13 digits.")
                                except ValueError:
                                    print("Invalid input. Please enter a valid ISBN.")
                            book['ISBN'] = new_ISBN

                            while True:
                                try:
                                    new_Author = input(f"Author: ({book['Author']}): ").strip()
                                    if not new_Author:  # Check for an empty input
                                        print("\nAuthor Cannot Be Empty")
                                    else:
                                        book['Author'] = new_Author
                                        break  # Exit the loop if the input is not empty
                                except ValueError:
                                    print("Invalid input. Please enter an Author Name again.")

                            while True:
                                try:
                                    new_Title = input(f"Title: ({book['Title']}): ").strip()
                                    if not new_Title:  # Check for an empty input
                                        print("\nTitle Cannot Be Empty")
                                    else:
                                        book['Title'] = new_Title
                                        break  # Exit the loop if the input is not empty
                                except ValueError:
                                    print("Invalid input. Please enter the Title again.")

                            while True:
                                try:
                                    new_Publisher = input(f"Publisher: ({book['Publisher']}): ").strip()
                                    if not new_Publisher:  # Check for an empty input
                                        print("\nPublisher Cannot Be empty")
                                    else:
                                        book['Publisher'] = new_Publisher
                                        break  # Exit the loop
                                except ValueError:
                                    print("Invalid input. Please enter the Publisher again.")

                            while True:
                                try:
                                    new_Genre = input(f"Genre: ({book['Genre']}): ").strip()
                                    if not new_Genre:  # Check for an empty input
                                        print("\nGenre Cannot Be Empty")
                                    else:
                                        book['Genre'] = new_Genre
                                        break  # Exit the loop
                                except ValueError:
                                    print("Invalid input. Please enter the Genre again.")

                            while True:
                                try:
                                    new_YearPublished = int(input(f"Year Published: ({book['Year Published']}): "))
                                    break  # Exit the loop if the input is an integer
                                except ValueError:
                                    print("\nInvalid input. Please enter a valid year as a number.\n")
                            book['Year Published'] = new_YearPublished

                            while True:
                                # Check if the input is a valid date
                                Date_purchased_str = input(
                                    f"Date Purchased:({book['Date Purchased']})(dd-mm-yyyy):").strip()
                                try:
                                    Date_purchased = datetime.strptime(Date_purchased_str, "%d-%m-%Y")
                                    book['Date Purchased'] = Date_purchased.strftime("%d-%m-%Y")
                                    break
                                except ValueError:
                                    print("\nInvalid date format. Please use dd-mm-yyyy format.\n")

                            while True:
                                new_Status = input(f"Status: ({book['Status']}): ").strip()
                                try:
                                    if new_Status == 'to-read' or new_Status == 'read':
                                        book['Status'] = new_Status  # Set the new status
                                        break  # Allow transitioning from 'read' to 'to-read'
                                    else:
                                        print("\nPlease enter either 'to-read' or 'read'.")
                                except ValueError:
                                    print("\nPlease enter either 'to-read' or 'read'.")

                        clear_screen()
                        print("\nRecord updated successfully!\n")
                        break  # Exit the loop when the update is done


            else:
                print("\nInvalid option. Please choose '1' for ISBN or '2' for Author & Title.\n")

        while True:
            select = input("Do you want to exit? Enter 1 for Exit / 2 for Continue: ")
            if select == "1":
                clear_screen()
                return  # Exit the function
            elif select == "2":
                clear_screen()
                break  # Continue to the next iteration of the outer loop
            else:
                print("Invalid input. Please choose (1) for Exit or (2) for Continue.")








# Function to display all books' information
def display(books_dict):
    clear_screen()
    # Declare variables for maximum length of (title, author and genre)
    Maximum_len_of_Title = 35
    Maximum_len_of_Author = 17
    Maximum_len_of_Genre = 27

    # Make a heading for the name of the programme
    print(" ", ("=" * 34))
    print(f"{'|'.ljust(5)}{'The collection of the books':^20}{'|'.rjust(6)}")
    print(" ", ("=" * 34))

    # Create some space
    print("\n\n")
    while True:
        # Print out the heading of the display programme
        print(
            f"{'ISBN':<16}{'Title':<38}{'Genre':<30}{'Author':<20}{'Publisher':<30}{'Published Year':<24}"
            f"{'Purchased Date':<20}{'Status':<10}"
        )

        print("=" * 190)

        # Extract the information from the file and arrange it in accordingly with the heading of the display programme
        for book_info in books_dict.values():

            # Declare variable for ISBN, Title, Genre, Authors, Publisher, Published Year, Purchased Date, Status
            ISBN = book_info['ISBN']
            Author = book_info['Author']
            Title = book_info['Title']
            Publisher = book_info['Publisher']
            Genre = book_info['Genre']
            Published_Year = book_info['Year Published']
            Puchased_Date = book_info['Date Purchased']
            Status = book_info['Status']

            # Find how many additional line if the length of the title, author, genre have exceeds the allocated space in table
            addtional_line_of_Title = len(Title) // Maximum_len_of_Title
            addtional_line_of_Author = len(Author) // Maximum_len_of_Author
            addtional_line_of_Genre = len(Genre) // Maximum_len_of_Genre

            # Find the highest number of additional line
            addtional_line = max(addtional_line_of_Genre, addtional_line_of_Author, addtional_line_of_Title)

            # Print the results for the first part which the text is within the allocated space in the table
            print(
                f"{ISBN:<16}{Title[:Maximum_len_of_Title]:<38}{Genre[:Maximum_len_of_Genre]:<30}"
                f"{Author[:Maximum_len_of_Author]:<20}{Publisher:<35}{Published_Year:<20}{Puchased_Date:<20}{Status:<10}"
            )

            # Print the exceeds text by extracting from the book info
            for i in range(1, (addtional_line + 1)):
                print(
                    f"{' ':<16}{Title[(Maximum_len_of_Title * i):(Maximum_len_of_Title * (i + 1))]:<38}"
                    f"{Genre[(Maximum_len_of_Genre * i):(Maximum_len_of_Genre * (i + 1))]:<30}"
                    f"{Author[(Maximum_len_of_Author * i):(Maximum_len_of_Author * (i + 1))]:<20}{' ':<35}{' ':<20}"
                    f"{' ':<20}{' ':<10}"
                )

        user_input = input("\nEnter (1) to exit, (2) to display again: ")
        if user_input == "1":
            clear_screen()
            break
        elif user_input == "2":
            clear_screen()
            continue
        else:
            print("\nInvalid input. Please enter 1 to exit or 2 to continue.\n")








# Function to search books
def search_book(books_dict):
    clear_screen()

    while True:  # Add an outer loop to continue searching or exiting

        while True:
            print("Search for Book(s)")
            search_criteria = {
                'ISBN': input("Enter ISBN (leave blank to skip): "),
                'Author': input("Enter Author (leave blank to skip): "),
                'Title': input("Enter Title (leave blank to skip): ")
            }

            # Check if all three criteria are blank
            if not any(search_criteria.values()):
                clear_screen()
                print("Please enter at least one of ISBN, Author, or Title.")
                continue  # Continue the loop to prompt for input again

            found_books = []

            # Iterate through the books in the dictionary
            for book in books_dict.values():

                match = False  # Assume it's not a match by default

                # Check the condition ,if ISBN, Author, or Title match the user input
                if search_criteria['ISBN'] == book['ISBN']:
                    match = True
                elif search_criteria['Author'] == book['Author']:
                    match = True
                elif search_criteria['Title'] == book['Title']:
                    match = True
                else:
                    continue

                if match:
                    found_books.append(book)

            if found_books:
                clear_screen()
                print("Search results:")
                for book in found_books:
                    print(book)
            else:
                print("No book found matching the criteria.")

            select = input("Do you want to exit? Enter (1) for Exit or (2) for Continue: ")
            if select == "1":
                clear_screen()
                return  # Exit the function
            elif select == "2":
                clear_screen()
                break  # Continue to the next iteration of the outer loop
            else:
                print("Invalid input. Please choose (1) for Exit or (2) for Continue.")








# Function to create a book dictionary to store books
def create_books_dict():
    # Initialize an empty dictionary to store the book information
    books_dict = {}

    # Open the file and read its contents
    with open('Books_Database', 'r+') as file:

        # Iterate through each line in the file
        for line in file:

            # Split the line into individual pieces of information
            book_info = line.strip().split('|')

            # Check if the line has enough elements
            if len(book_info) >= 7:

                # Create a dictionary to store book information
                book = {
                    "ISBN": book_info[0],
                    "Author": book_info[1],
                    "Title": book_info[2],
                    "Publisher": book_info[3],
                    "Genre": book_info[4],
                    "Year Published": book_info[5],
                    "Date Purchased": book_info[6],
                    "Status": book_info[7]
                }

                # Add the book information to the main dictionary using the title as the key
                books_dict[
                    book_info[0], book_info[1], book_info[2], book_info[3], book_info[4], book_info[5], book_info[6],
                    book_info[7]
                ] = book

            else:
                print(f"Invalid data for book: {book_info[2]}")  # Or handle the invalid data in some other way
                print(f"Title: {book_info[2]}")
                print("\n\n\n")

    return books_dict  # Return the dictionary


clear_screen()
books_dict = create_books_dict()

while True:
    display_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        add_book(books_dict)
    elif choice == '2':
        delete_book(books_dict)
    elif choice == '3':
        update_book_records(books_dict)
    elif choice == '4':
        display(books_dict)
    elif choice == '5':
        search_book(books_dict)
    elif choice == '6':
        with open('Books_Database', 'w') as file:
            for book_info, book in books_dict.items():
                file.write(f"{book['ISBN']}|{book['Author']}|{book['Title']}|{book['Publisher']}|"
                           f"{book['Genre']}|{book['Year Published']}|{book['Date Purchased']}|{book['Status']}\n")

        clear_screen()
        print("\nSuccessfully updated data in 'books_StudentID.txt' and Exiting...\n")
        break
    else:
        print("\nPlease enter a valid input:\n")