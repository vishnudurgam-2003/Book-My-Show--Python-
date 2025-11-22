# Connect src files into main file

from src.admin import Admin
from src.user import User

# Admin function
def admin_menu():

    # object to create connect the class of admin file
    admin = Admin()

    while True:
        print("\n- - - - - Admin Menu - - - - -")

        print("\n1.Add movie.")
        print("2.View movies.")
        print("3.Update movie.")
        print("4.Remove movie.")
        print("5.Back to Main Menu.")

        admin_choise = input("\nEnter choise : ")

        if admin_choise == '1':
            admin.add_movie()

        elif admin_choise == '2':
            admin.view_movies()

        elif admin_choise == '3':
            admin.update_movie()

        elif admin_choise == '4':
            admin.delete_movie()   

        elif admin_choise == '5':
            break

        else:
            print("Invalid choise!")

# User function
def user_menu():

    # Object to create connect the class of user file
    user = User()

    while True:
        print("\n- - - - - User Menu - - - - -")

        print("\n1.View movies.")
        print("2.Book tickets.")
        print("3.View all bookings.")
        print("4.Back to Main Menu.")

        user_choise = input("\nEnter choise : ")

        if user_choise == '1':
            user.view_movies()

        elif user_choise == '2':
            user.book_ticket()

        elif user_choise == '3':
            user.view_bookings()

        elif user_choise == '4':
            break

        else:
            print("Invalid choise!")

# Main function
def main():

    print("\n* * * * * * * * * * Welcome to Book My Show * * * * * * * * * *")

    while True:
        print("\n- - - - - Main Menu - - - - -")

        print("\n1.Admin Panel.")
        print("2.User Portal.")
        print("3.Exit.")

        choise = input("\nSelect Mode : ")

        if choise == '1':
            admin_menu()

        elif choise == '2':
            user_menu()

        elif choise == '3':
            break

        else:
            print("Invalid choise!")


if __name__ == "__main__":
    main()