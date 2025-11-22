from src.db_connect import Database

class Booking:
    
    def __init__(self):
        self.db = Database.connect()

    def book_ticket(self):
        
        user_name = input("\nEnter your name : ").upper()
        movie_id = int(input("Enter movie ID : "))
        seats = int(input("Number of seats : "))

        cursor = self.db.cursor()
        cursor.execute("select NAME,PRICE from movies where MOVIE_ID = %s",(movie_id,))
        movie = cursor.fetchone()

        if not movie:
            print("\nInvalid movie ID.")
            return
        
        movie_name,price  = movie
        total = price * seats 

        cursor.execute("insert into bookings (USER_NAME,MOVIE_ID,SEATS,TOTAL) values (%s, %s, %s ,%s)",
                       (user_name, movie_id, seats, total)
        )
        self.db.commit()

        print("\nBooking confirmend!")
        print(f"Movie : {movie_name}")
        print(f"Seats : {seats}")
        print(f"Total : {total}")

    def view_bookings(self):
        
        cursor = self.db.cursor()
        cursor.execute("""
            select b.booking_id, b.user_name, m.name, b.seats, b.total 
            from bookings b
            join movies m on b.movie_id = m.movie_id 
        """)

        rows = cursor.fetchall()

        if not rows:
            print("No bookings found!")

        else:
            print("\nAll Bookings:")
            for r in rows:
                print(f"Booking ID: {r[0]} | User: {r[1]} | Movie: {r[2]}| Seats: {r[3]} | Price: ${r[4]}")        

