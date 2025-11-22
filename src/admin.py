#Connect Database to admin file
from src.db_connect import Database

# Admin Panel
class Admin:
    
    def __init__(self):
        self.db = Database.connect()

    def add_movie(self):
        
        name = input("\nEnter movie name : ").upper()
        genre = input("Enter genre : ").upper()
        duration = int(input("Enter movie duration (mins) : "))
        price = float(input("Enter ticket price : "))

        cursor = self.db.cursor()
        cursor.execute("Insert into movies (NAME,GENRE,DURATION,PRICE) values (%s,%s,%s,%s)",
                       (name,genre,duration,price)
        )
        
        self.db.commit()
        print(f"\n{name} Added successfully.")


    def view_movies(self):
        
        cursor = self.db.cursor()
        cursor.execute("select * from movies")
        movies = cursor.fetchall()
        print("\nAvailable movies:")

        if not movies:
            print("\nNo movies found!")

        for m in movies:
            print(f"ID: {m[0]} | {m[1]} | {m[2]} | {m[3]} mins | {m[4]}")


    def update_movie(self):
        
        cursor = self.db.cursor()
        self.view_movies()
        movie_id = int(input("\n Enter movie id to upadate : "))
        
        print("\nWhat do you want to update? ")
        print("\n1.Name")
        print("2.Genre")
        print("3.Duration")
        print("4.Price")

        choise = input("\nEnter your choise : ")

        if choise == '1':
            new_value = input("\nEnter new movie name : ").upper()
            cursor.execute("Update movies set NAME = %s where MOVIE_ID = %s",
                          (new_value,movie_id))

        elif choise == '2':
            new_value = input("Enter new genre : ").upper()
            cursor.execute("Update movies set GENRE = %s where MOVIE_ID = %s",
                           (new_value,movie_id))
        elif choise == '3':
            new_value = int(input("Enter new duration (mins) : "))
            cursor.execute("Update movies set DURATION = %s where MOVIE_ID = %s",
                           (new_value,movie_id))
        
        elif choise == '4':
            new_value = float(input("Enter  new ticket price : "))
            cursor.execute("Update movies set PRICE = %s where MOVIE_ID = %s",
                           (new_value,movie_id))    

        else:
            print("Invalid Choise!")
            return

        self.db.commit()
        print(f"\nMovie ID:{movie_id} Updated successfully.")    

    def delete_movie(self):
        
        cursor = self.db.cursor()
        self.view_movies()
        movie_id = int(input("\nEnter movie id to delete : "))

        confirm = input("\nAre you sure you want to delete this movie (yes/no) : ").lower()

        if confirm == 'yes':
            cursor.execute("delete from movies where MOVIE_ID = %s",
                       (movie_id,))
            self.db.commit()
            print(f"Movie id {movie_id} deleted successfully.")

        else:
            print("Deletion cancelled.")