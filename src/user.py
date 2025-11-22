# Connect Database into user file
from src.db_connect import Database
from src.bookings import Booking

# User Portal
class User:
    
    def __init__(self):
        self.db = Database.connect()
        self.booking = Booking()

    def view_movies(self):

        cursor = self.db.cursor()
        cursor.execute("select * from movies")
        movies = cursor.fetchall()

        print("\nAvailable movies: ")
        if not movies:
            print("No movies found")

        for m in movies:
            print(f"ID: {m[0]} | {m[1]} | {m[2]} | {m[3]} mins | $ {m[4]} ")

    def book_ticket(self):
        self.booking.book_ticket()

    def view_bookings(self):
        self.booking.view_bookings()
        