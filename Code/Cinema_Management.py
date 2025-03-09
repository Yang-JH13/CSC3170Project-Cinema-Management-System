import mysql.connector
import getpass
import random
import os
import pandas as pd
from datetime import datetime

# Password: 3170
def connect_to_db():
    clear_screen()
    try:
        password = getpass.getpass("Enter your MySQL password: ")
        connection = mysql.connector.connect(
            host='localhost',
            user='jiahao3170',
            password=password,
            database='csc3170_db'
        )
        if connection.is_connected():
            print("Congratulations! Connected Successfully!")
            stop = input("Press Enter to Continue")
            return connection
    except Exception as e:
        print(f"Error Information: {e}")
        stop = input("Press Enter to Continue")
        return -1

def confirm_connection():
    clear_screen()
    print("You are trying to connect to the Cinema_Management_Model database")
    print("Are you sure?")
    print("Please answer yes or no. Other inputs is invalid.")
    confirmation = input("(yes/no): ").strip().lower()
    if confirmation == 'yes':
        return True
    elif confirmation == 'no':
        print("Exiting program...")
        exit(0)
    else:
        print("Sorry, the system found other inputs")
        stop = input("Press Enter and Refresh")
        confirm_connection()

def handle_connection_failure():
    clear_screen()
    print("Connection failed. Do you want to:")
    print("1. Try again")
    print("2. Exit?")
    print("Please enter 1 or 2. Other inputs is invalid.")
    choice = input("(1/2): ").strip()
    if choice == '1':
        return True
    elif choice == '2':
        print("Exiting program...")
        exit(0)
    else:
        print("Sorry, the system found other inputs")
        stop = input("Press Enter and Refresh")
        handle_connection_failure()

def print_random_sentence():
    sentences = [
        "Life was like a box of chocolates. You never know what you’re gonna get.",
        "Some birds aren't meant to be caged, that's all. Their feathers are just too bright.",
        "After all, tomorrow is another day!",
        "A boy's best friend is his mother.",
        "Greed, for lack of a better word, is good.",
        "Mrs.Robinson, you're trying to seduce me. Aren't you?",
        "Oh, Jerry, don't let's ask for the moon. We have the stars."
    ]
    print(random.choice(sentences))

def get_movie_info_all(identity, id, cursor, connection):
    clear_screen()
    print("Here is the information of all the movies:")
    print(" ")
    try:
        cursor.execute(
            "SELECT MovieID, Title, Director, Actors, Genre, ReleaseDate, IsListed, AverageRating FROM movies")
        films = cursor.fetchall()

        if not films:
            print("No movies found in the database.")
            print(" ")
            stop = input("Press Enter to Go back")
            if identity == "user":
                user_home_page(cursor, connection, id)
            else:
                admin_home_page(cursor, connection, id)

        print("-"*40)
        for film in films:
            film_id, film_name, film_dir, film_act, film_type, film_date,film_listed, film_score = film
            print(f"Movie ID: {film_id}")
            print(f"Movie Name: {film_name}")
            print(f"Movie Director: {film_dir}")
            print(f"Movie Actors: {film_act}")
            print(f"Movie Type: {film_type}")
            print(f"Movie Release Date: {film_date}")
            print(f"Movie Score: {film_score}")
            print("-"*40)

        print(" ")
        print("All movie information is above")
    except Exception as e:
        print(f"Error Information: {e}")
        print("Program terminated...")
        exit(0)
    print(" ")
    stop = input("Press Enter to Go back")
    if identity == "user":
        user_home_page(cursor, connection, id)
    else:
        admin_home_page(cursor, connection, id)

def get_movie_info_show(identity, id, cursor, connection):
    clear_screen()
    print("Here is the information of all the listed movies:")
    print(" ")
    try:
        cursor.execute(
            "SELECT MovieID, Title, Director, Actors, Genre, ReleaseDate, IsListed, AverageRating FROM movies WHERE IsListed = 1")
        films = cursor.fetchall()

        if not films:
            print("No movies found in the database.")
            print(" ")
            stop = input("Press Enter to Go back")
            if identity == "user":
                user_home_page(cursor, connection, id)
            else:
                admin_home_page(cursor, connection, id)

        print("-" * 40)
        for film in films:
            film_id, film_name, film_dir, film_act, film_type, film_date, film_listed, film_score = film
            print(f"Movie ID: {film_id}")
            print(f"Movie Name: {film_name}")
            print(f"Movie Director: {film_dir}")
            print(f"Movie Actors: {film_act}")
            print(f"Movie Type: {film_type}")
            print(f"Movie Release Date: {film_date}")
            print(f"Movie Score: {film_score}")
            print("-" * 40)

        print(" ")
        print("All listed movies information is above")
    except Exception as e:
        print(f"Error Information: {e}")
        print("Program terminated...")
        exit(0)
    print(" ")
    stop = input("Press Enter to Go back")
    if identity == "user":
        user_home_page(cursor, connection, id)
    else:
        admin_home_page(cursor, connection, id)

def movie_from_name_to_id(movie_name,cursor):
    try:
        cursor.execute("SELECT MovieID FROM movies WHERE Title = %s", (movie_name,))
        result = cursor.fetchone()

        if result is None:
            print(f"No movie found with the name: '{movie_name}'.")
            return None

        movie_id = result[0]
        return movie_id
    except Exception as e:
        print(f"Error Information: {e}")
        print("Program terminated...")
        exit(0)

def movie_from_id_to_name(movie_id,cursor):
    try:
        cursor.execute("SELECT Title FROM movies WHERE MovieID = %s", (movie_id,))
        result = cursor.fetchone()

        if result is None:
            print(f"No movie found with the ID: '{movie_id}'.")
            return None

        movie_name = result[0]
        return movie_name
    except Exception as e:
        print(f"Error Information: {e}")
        print("Program terminated...")
        exit(0)

def get_movie_info_off(identity, id, cursor, connection):
    clear_screen()
    print("Here is the information of all the offline movies:")
    print(" ")
    try:
        cursor.execute(
            "SELECT MovieID, Title, Director, Actors, Genre, ReleaseDate, IsListed, AverageRating FROM movies WHERE IsListed = 0")
        films = cursor.fetchall()

        if not films:
            print("No movies found in the database.")
            print(" ")
            stop = input("Press Enter to Go back")
            if identity == "user":
                user_home_page(cursor, connection, id)
            else:
                admin_home_page(cursor, connection, id)

        print("-" * 40)
        for film in films:
            film_id, film_name, film_dir, film_act, film_type, film_date, film_listed, film_score = film
            print(f"Movie ID: {film_id}")
            print(f"Movie Name: {film_name}")
            print(f"Movie Director: {film_dir}")
            print(f"Movie Actors: {film_act}")
            print(f"Movie Type: {film_type}")
            print(f"Movie Release Date: {film_date}")
            print(f"Movie Score: {film_score}")
            print("-" * 40)

        print(" ")
        print("All offline movie information is above")
    except Exception as e:
        print(f"Error Information: {e}")
        print("Program terminated...")
        exit(0)
    print(" ")
    stop = input("Press Enter to Go back")
    if identity == "user":
        user_home_page(cursor, connection, id)
    else:
        admin_home_page(cursor, connection, id)

def get_movie_info(identity, id, cursor, connection):
    clear_screen()
    print("What kind of movie information do you want to view?")
    print("1. Currently showing")
    print("2. Already offline")
    print("3. All Movies")
    print("Please enter 1, 2 or 3. Other inputs is invalid.")
    choice = input("(1/2/3): ").strip()
    if choice == '3':
        get_movie_info_all(identity,id, cursor, connection)
    elif choice == '1':
        get_movie_info_show(identity,id, cursor, connection)
    elif choice == '2':
        get_movie_info_off(identity,id, cursor, connection)
    else:
        print("Sorry, the system found other inputs")
        stop = input("Press Enter and Refresh")
        get_movie_info(identity, id, cursor, connection)

def view_my_review_hisory(user_id, cursor, connection):
    clear_screen()
    id = user_id
    print("You are trying to view history reviews...")
    print("Are you sure?")
    print("Please answer yes or no. Other inputs is invalid.")
    confirmation = input("(yes/no): ").strip().lower()
    if confirmation == 'yes':
        print(" ")
    elif confirmation == 'no':
        user_home_page(cursor, connection, id)
    else:
        print("Sorry, the system found other inputs")
        stop = input("Press Enter and Refresh")
        view_my_review_hisory(id, cursor, connection)

    try:
        cursor.execute(
            "SELECT ReviewID, MovieID, Rating, Comment, ReviewDate FROM reviews WHERE UserID = %s",
            (id,)
        )
        reviews = cursor.fetchall()

        if not reviews:
            print("No review history")
            print(" ")
            stop = input("Press Enter and Go back")
            user_home_page(cursor, connection, id)

        print("Your all review history")
        print(" ")
        print("-" * 40)
        for review in reviews:
            review_id, movie_id, rating, comment, review_date = review
            movie_name = movie_from_id_to_name(movie_id,cursor)
            print(f"Movie Name: {movie_name}")
            print(f"Rating: {rating}")
            print(f"Comment: {comment}")
            print(f"Review Date: {review_date}")
            print("-" * 40)

        print("Review shows successfully.")
        print(" ")
        stop = input("Press Enter and Go back")
        user_home_page(cursor, connection, id)
    except Exception as e:
        print(f"Error Information: {e}")
        connection.rollback()
        stop = input("Press Enter to Retry")
        view_my_review_hisory(id, cursor, connection)

def movie_from_showtimeid(showtimeid,cursor):
    try:
        cursor.execute("SELECT MovieID, StartTime, EndTime FROM showtimes WHERE ShowtimeID = %s", (showtimeid,))
        result = cursor.fetchone()

        if result is None:
            print(f"No movie found with the showtime_id: '{showtimeid}'.")
            return None

        movie_id, start_time, end_time = result
        return movie_id, start_time, end_time
    except Exception as e:
        print(f"Error Information: {e}")
        print("Program terminated...")
        exit(0)

def view_my_book_hisory(user_id, cursor, connection):
    clear_screen()
    id = user_id
    print("You are trying to view history bookings...")
    print("Are you sure?")
    print("Please answer yes or no. Other inputs is invalid.")
    confirmation = input("(yes/no): ").strip().lower()
    if confirmation == 'yes':
        print(" ")
    elif confirmation == 'no':
        user_home_page(cursor, connection, id)
    else:
        print("Sorry, the system found other inputs")
        stop = input("Press Enter and Refresh")
        view_my_book_hisory(user_id, cursor, connection)

    try:
        cursor.execute(
            "SELECT ShowtimeID, Bookingdate FROM bookings WHERE UserID = %s",
            (id,)
        )
        bookings = cursor.fetchall()

        if not bookings:
            print("No booking history")
            print(" ")
            stop = input("Press Enter and Go back")
            user_home_page(cursor, connection, id)

        print("Your all booking history")
        print(" ")
        print("-" * 40)
        for booking in bookings:
            showtimeid, booking_date = booking
            movie_id, start_time, end_time = movie_from_showtimeid(showtimeid,cursor)
            movie_name = movie_from_id_to_name(movie_id,cursor)
            print(f"Movie Name: {movie_name}")
            print(f"Start time: {start_time}")
            print(f"End time: {end_time}")
            print(f"Booking Date: {booking_date}")
            print("-" * 40)

        print("Bookings shows successfully.")
        print(" ")
        stop = input("Press Enter and Go back")
        user_home_page(cursor, connection, id)
    except Exception as e:
        print(f"Error Information: {e}")
        connection.rollback()
        stop = input("Press Enter to Retry")
        view_my_book_hisory(id, cursor, connection)

def unique_review_id_detection(cursor, review_id):
    try:
        cursor.execute("SELECT 1 FROM reviews WHERE ReviewID = %s", (review_id,))
        result = cursor.fetchone()
        if result:
            return 0
        else:
            return 1
    except Exception as e:
        print(f"Error Information: {e}")
        stop = input("Program terminated")
        exit(0)
def review_movie(user_id, cursor, connection):
    clear_screen()
    id = user_id
    print("You are trying to review a movie...")
    print("Are you sure?")
    print("Please answer yes or no. Other inputs is invalid.")
    confirmation = input("(yes/no): ").strip().lower()
    if confirmation == 'yes':
        print(" ")
    elif confirmation == 'no':
        user_home_page(cursor, connection, id)
    else:
        print("Sorry, the system found other inputs")
        stop = input("Press Enter and Refresh")
        review_movie(id, cursor, connection)
    print("Please follow the instructions to review.")
    print(" ")
    print("Please note: Review's digital IDs may be duplicated.")
    print("Once duplicates are detected, you will need to re-review. Sorry!")
    print(" ")
    print("Please enter the movie name your want to review")
    movie_name = input("(movie name): ")
    movie_id = movie_from_name_to_id(movie_name, cursor)
    if unique_movie_id_detection(cursor,movie_id) == 1:
        print("No movie found with the given Name.")
        print(" ")
        stop = input("Press Enter and Retry")
        review_movie(id, cursor, connection)
    print("Please enter the score you will give")
    print("-" * 40)
    print("Please enter an integer between 1-5, otherwise the program will report an error and you need to re-enter!!!")
    print("-" * 40)
    movie_score = input("(movie score): ")
    print("Please choose a numeric ID for your review")
    review_id = input("(review ID): ")
    if unique_review_id_detection(cursor,review_id) == 0:
        print("Sorry, the system found a duplicate numeric ID")
        stop = input("Press Enter and try again")
        review_movie(id, cursor, connection)
    print("Please enter the comment content")
    movie_comment = input("(movie comment): ")
    review_date = datetime.now()

    try:
        cursor.execute(
            "INSERT INTO reviews (ReviewID, UserID, MovieID, Rating, Comment, ReviewDate) VALUES (%s, %s, %s, %s, %s, %s)",
            (review_id, id, movie_id, movie_score, movie_comment,review_date)
        )
        connection.commit()

        print("Review successfully.")
        print(" ")
        stop = input("Press Enter and Go back")
        user_home_page(cursor, connection, id)
    except Exception as e:
        print(f"Error Information: {e}")
        connection.rollback()
        stop = input("Press Enter to Retry")
        review_movie(id, cursor, connection)

def unique_book_id_detection(cursor, book_id):
    try:
        cursor.execute("SELECT 1 FROM bookings WHERE BookingID = %s", (book_id,))
        result = cursor.fetchone()
        if result:
            return 0
        else:
            return 1
    except Exception as e:
        print(f"Error Information: {e}")
        stop = input("Program terminated")
        exit(0)

def book_tickets(id, cursor, connection):
    clear_screen()
    print("You are trying to book tickets...")
    print("Are you sure?")
    print("Please answer yes or no. Other inputs is invalid.")
    confirmation = input("(yes/no): ").strip().lower()
    if confirmation == 'yes':
        print(" ")
    elif confirmation == 'no':
        user_home_page(cursor, connection, id)
    else:
        print("Sorry, the system found other inputs")
        stop = input("Press Enter and Refresh")
        book_tickets(id, cursor, connection)
    print("Please follow the instructions to book.")
    print(" ")
    print("Please note: Book's digital IDs may be duplicated.")
    print("Once duplicates are detected, you will need to re-book. Sorry!")
    print(" ")
    print("Please enter the movie name your want to book")
    movie_name = input("(movie name): ")
    movie_id = movie_from_name_to_id(movie_name, cursor)
    if unique_movie_id_detection(cursor, movie_id) == 1:
        print("No movie found with the given name.")
        print(" ")
        stop = input("Press Enter and Retry")
        book_tickets(id, cursor, connection)
    try:
        cursor.execute("SELECT ShowtimeID, StartTime, EndTime FROM showtimes WHERE MovieID = %s", (movie_id,))
        showtimes = cursor.fetchall()
        if not showtimes:
            print("No showtime information found")
            print(" ")
            stop = input("Press Enter and Retry")
            book_tickets(id, cursor, connection)
        print("Available showtime:")
        for showtime in showtimes:
            showtime_id, start_time, end_time = showtime
            print(f"Showtime ID: {showtime_id}, Start Time: {start_time}, End Time: {end_time}")
        print(" ")
        print("Please select a showtime by entering its Showtime ID:")
        showtime_id_input = input("(showtime ID): ").strip()
        showtime_id_input = int(showtime_id_input)
        book_date = datetime.now()
        print("Please choose a numeric ID for yourself")
        book_id = input("(book ID): ")
        if unique_book_id_detection(cursor, book_id) == 0:
            print("Sorry, the system found a duplicate numeric ID")
            stop = input("Press Enter and try again")
            book_tickets(id, cursor, connection)
        cursor.execute(
            "INSERT INTO bookings (BookingId, UserID, ShowtimeID, BookingDate) VALUES (%s, %s, %s, %s)",
            (book_id, id, showtime_id_input, book_date)
        )
        connection.commit()
        print("Book successfully")
        print(" ")
        stop = input("Press Enter and Go back")
        user_home_page(cursor, connection, id)
    except Exception as e:
        print(f"Error Information: {e}")
        connection.rollback()
        stop = input("Press Enter to Retry")
        book_tickets(id, cursor, connection)

def view_all_reviews_user(id, cursor, connection):
    clear_screen()
    print("You are trying to show all reviews of a movie...")
    print("Are you sure?")
    print("Please answer yes or no. Other inputs is invalid.")
    confirmation = input("(yes/no): ").strip().lower()
    if confirmation == 'yes':
        print(" ")
    elif confirmation == 'no':
        user_home_page(cursor, connection, id)
    else:
        print("Sorry, the system found other inputs")
        stop = input("Press Enter and Refresh")
        view_all_reviews_user(id, cursor, connection)
    print("Which movie's review do you want to show?")
    movie_name = input("(movie name): ")
    movie_id = movie_from_name_to_id(movie_name, cursor)
    try:
        if unique_movie_id_detection(cursor, movie_id) == 1:
            print("No movie found with the given name")
            stop = input("Press Enter and Retry")
            view_all_reviews_user(id, cursor, connection)

        cursor.execute(
            "SELECT ReviewID, UserID, Rating, Comment, ReviewDate FROM reviews WHERE MovieID = %s",
            (movie_id,)
        )
        reviews = cursor.fetchall()

        if not reviews:
            print("No reviews found for movie with the given name.")
            stop = input("Press Enter and Retry")
            view_all_reviews_user(id, cursor, connection)

        print("To protect privacy, user names are not shown.")
        print("All reviews for this movie:")
        print(" ")
        print("-" * 40)
        for review in reviews:
            review_id, user_id, rating, comment, review_date = review
            print(f"User: {user_id}")
            print(f"Score: {rating}")
            print(f"Comment: {comment}")
            print(f"Date: {review_date}")
            print("-" * 40)

        print("All reviews has been shown.")
        stop = input("Press Enter and Go back")
        user_home_page(cursor, connection, id)
    except Exception as e:
        print(f"Error Information: {e}")
        connection.rollback()
        stop = input("Press Enter and Retry")
        view_all_reviews_user(id, cursor, connection)

def user_home_page(cursor, connection, user_id):
    clear_screen()
    id = user_id
    print("Welcome, you can use these features:")
    print("1. View current cinema movie information")
    print("2. Book movie tickets")
    print("3. Review Movies")
    print("4. View my review history")
    print("5. View my book history")
    print("6. View movie's review")
    print("7. Log out")
    print("8. Exit")
    print("Please enter 1, 2, 3, 4, 5, 6, 7 or 8. Other inputs is invalid.")
    choice = input("(1/2/3/4/5/6/7/8): ").strip()
    if choice == '8':
        print("Exiting program...")
        exit(0)
    elif choice == '7':
        login_prompt(cursor, connection)
    elif choice == '1':
        get_movie_info("user",id, cursor, connection)
    elif choice == '2':
        book_tickets(id, cursor, connection)
    elif choice == '3':
        review_movie(id, cursor, connection)
    elif choice == '4':
        view_my_review_hisory(id, cursor, connection)
    elif choice == '5':
        view_my_book_hisory(id, cursor, connection)
    elif choice == '6':
        view_all_reviews_user(id, cursor, connection)
    else:
        print("Sorry, the system found other inputs")
        stop = input("Press Enter and Refresh")
        user_home_page(cursor, connection, id)

def unique_movie_id_detection(cursor, movie_id):
    try:
        cursor.execute("SELECT 1 FROM movies WHERE MovieID = %s", (movie_id,))
        result = cursor.fetchone()
        if result:
            return 0
        else:
            return 1
    except Exception as e:
        print(f"Error Information: {e}")
        stop = input("Program terminated")
        exit(0)

def unique_showtime_id_detection(cursor, showtime_id):
    try:
        cursor.execute("SELECT 1 FROM showtimes WHERE ShowtimeID = %s", (showtime_id,))
        result = cursor.fetchone()
        if result:
            return 0
        else:
            return 1
    except Exception as e:
        print(f"Error Information: {e}")
        stop = input("Program terminated")
        exit(0)

def add_movie(id, cursor, connection):
    clear_screen()
    print("You are trying to add a movie...")
    print("Are you sure?")
    print("Please answer yes or no. Other inputs is invalid.")
    confirmation = input("(yes/no): ").strip().lower()
    if confirmation == 'yes':
        print(" ")
    elif confirmation == 'no':
        admin_home_page(cursor,connection,id)
    else:
        print("Sorry, the system found other inputs")
        stop = input("Press Enter and Refresh")
        add_movie(id,cursor,connection)
    print("Please follow the instructions to add the movie.")
    print(" ")
    print("Please note: Movies' digital IDs & Showtime's ID may be duplicated.")
    print("Once duplicates are detected, you will need to re-enter. Sorry!")
    print(" ")
    print("Please enter the movie's name")
    movie_title = input("(movie name): ")
    print("Please enter the movie's director")
    movie_director = input("(movie director): ")
    print("Please enter the movie's actor")
    movie_actor = input("(movie actor): ")
    print("Please enter the movie's type")
    movie_type = input("(movie type): ")
    print("Please enter the movie's released date")
    movie_date = input("(movie date): ")
    movie_is_list = 1
    print("Please choose a numeric ID for the movie")
    movie_id = input("(movie ID): ")
    if unique_movie_id_detection(cursor, movie_id) == 0:
        print("Sorry, the system found a duplicate numeric ID")
        stop = input("Press Enter and try again")
        add_movie(id, cursor, connection)
    print("Please Enter a initial score for the movie")
    movie_score = input("(movie score): ")
    print(" ")
    print("Please enter the showtime details:")
    print("Please enter the start time")
    showtime_start = input("(start time): ")
    print("Please enter the end time")
    showtime_end = input("(end time): ")
    print("Please choose a numeric ID for the showtime")
    showtime_id = input("(showtime ID): ")
    if unique_showtime_id_detection(cursor, movie_id) == 0:
        print("Sorry, the system found a duplicate numeric ID")
        stop = input("Press Enter and try again")
        add_movie(id, cursor, connection)

    try:
        cursor.execute(
            "INSERT INTO movies (MovieID, Title, Director, Actors, Genre, ReleaseDate, IsListed, AverageRating) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            (movie_id, movie_title, movie_director,movie_actor,movie_type,movie_date,movie_is_list, movie_score)
        )
        connection.commit()
        print("Movie add successfully!")

        cursor.execute(
            "INSERT INTO showtimes (ShowtimeID, MovieID, StartTime, EndTime) VALUES (%s, %s, %s, %s)",
            (showtime_id, movie_id, showtime_start, showtime_end)
        )
        connection.commit()
        print("Showtime add successfully!")
        print(" ")
        print("Back to Admin Home page")
        stop = input("Press Enter to Continue")
        admin_home_page(cursor, connection, id)
    except Exception as e:
        print(f"Error Information: {e}")
        connection.rollback()
        stop = input("Press Enter to Retry")
        add_movie(id, cursor, connection)

def remove_movie(id, cursor, connection):
    clear_screen()
    print("You are trying to offline a movie...")
    print("Are you sure?")
    print("Please answer yes or no. Other inputs is invalid.")
    confirmation = input("(yes/no): ").strip().lower()
    if confirmation == 'yes':
        print(" ")
    elif confirmation == 'no':
        admin_home_page(cursor, connection, id)
    else:
        print("Sorry, the system found other inputs")
        stop = input("Press Enter and Refresh")
        remove_movie(id, cursor, connection)
    print(" ")
    print("Which movie do you want to be taken offline?")
    movie_name = input("(movie name): ")
    movie_id = movie_from_name_to_id(movie_name, cursor)
    print(" ")

    try:
        if unique_movie_id_detection(cursor, movie_id) == 1:
            print("No movie found with the given name")
            stop = input("Press Enter and Retry")
            remove_movie(id, cursor, connection)

        cursor.execute("SELECT IsListed FROM movies WHERE MovieID = %s", (movie_id,))
        result = cursor.fetchone()
        is_listed = result[0]

        if is_listed == 0:
            print("Movie already offline")
            stop = input("Press Enter and Go back")
            admin_home_page(cursor, connection, id)

        cursor.execute("UPDATE movies SET IsListed = 0 WHERE MovieID = %s", (movie_id,))
        connection.commit()
        cursor.execute("DELETE FROM showtimes WHERE MovieID = %s", (movie_id,))
        connection.commit()
        print("Movie has been taken offline successfully.")
        print("Related showtime has been deleted.")
        stop = input("Press Enter and Go back")
        admin_home_page(cursor, connection, id)
    except Exception as e:
        print(f"Error Information: {e}")
        connection.rollback()
        stop = input("Press Enter and Retry")
        remove_movie(id, cursor, connection)

def modify_showtime_info(id, cursor, connection):
    clear_screen()
    print("You are trying to modify showtime...")
    print("Are you sure?")
    print("Please answer yes or no. Other inputs is invalid.")
    confirmation = input("(yes/no): ").strip().lower()
    if confirmation == 'yes':
        print(" ")
    elif confirmation == 'no':
        admin_home_page(cursor, connection, id)
    else:
        print("Sorry, the system found other inputs")
        stop = input("Press Enter and Refresh")
        modify_showtime_info(id, cursor, connection)
    print("Which movie's showtime do you want to be modify?")
    movie_name = input("(movie name): ")
    movie_id = movie_from_name_to_id(movie_name, cursor)
    try:
        if unique_movie_id_detection(cursor, movie_id) == 1:
            print("No movie found with the given name")
            stop = input("Press Enter and Retry")
            modify_showtime_info(id, cursor, connection)

        print("Movie's new start time")
        new_start = input("(new start): ")
        print("Movie's new end time")
        new_end = input("(new end): ")

        cursor.execute(
            "UPDATE showtimes SET StartTime = %s, EndTime = %s WHERE MovieID = %s",
            (new_start, new_end, movie_id)
        )
        connection.commit()
        print("Showtime has been modified successfully.")
        stop = input("Press Enter and Go back")
        admin_home_page(cursor, connection, id)

    except Exception as e:
        print(f"Error Information: {e}")
        connection.rollback()
        stop = input("Press Enter and Retry")
        modify_showtime_info(id, cursor, connection)

def user_from_name_to_id(user_name,cursor):
    try:
        cursor.execute("SELECT UserID FROM users WHERE Username = %s", (user_name,))
        result = cursor.fetchone()

        if result is None:
            print(f"No user found with the name: '{user_name}'.")
            return None

        movie_id = result[0]
        return movie_id
    except Exception as e:
        print(f"Error Information: {e}")
        print("Program terminated...")
        exit(0)

def user_from_id_to_name(user_id,cursor):
    try:
        cursor.execute("SELECT Username FROM users WHERE UserID = %s", (user_id,))
        result = cursor.fetchone()

        if result is None:
            print(f"No user found with the name: '{user_id}'.")
            return None

        movie_id = result[0]
        return movie_id
    except Exception as e:
        print(f"Error Information: {e}")
        print("Program terminated...")
        exit(0)

def view_all_reviews(id, cursor, connection):
    clear_screen()
    print("You are trying to show all reviews of a movie...")
    print("Are you sure?")
    print("Please answer yes or no. Other inputs is invalid.")
    confirmation = input("(yes/no): ").strip().lower()
    if confirmation == 'yes':
        print(" ")
    elif confirmation == 'no':
        admin_home_page(cursor, connection, id)
    else:
        print("Sorry, the system found other inputs")
        stop = input("Press Enter and Refresh")
        view_all_reviews(id, cursor, connection)
    print("Which movie's review do you want to show?")
    movie_name = input("(movie name): ")
    movie_id = movie_from_name_to_id(movie_name, cursor)
    try:
        if unique_movie_id_detection(cursor, movie_id) == 1:
            print("No movie found with the given name")
            stop = input("Press Enter and Retry")
            view_all_reviews(id, cursor, connection)

        cursor.execute(
            "SELECT ReviewID, UserID, Rating, Comment, ReviewDate FROM reviews WHERE MovieID = %s",
            (movie_id,)
        )
        reviews = cursor.fetchall()

        if not reviews:
            print("No reviews found for movie with the given name.")
            stop = input("Press Enter and Retry")
            view_all_reviews(id, cursor, connection)

        print("All reviews for this movie:")
        print(" ")
        print("-" * 40)
        for review in reviews:
            review_id, user_id, rating, comment, review_date = review
            user_name = user_from_id_to_name(user_id,cursor)
            print(f"User ID: {user_id}")
            print(f"User Name: {user_name}")
            print(f"Score: {rating}")
            print(f"Comment: {comment}")
            print(f"Date: {review_date}")
            print("-" * 40)

        print("All reviews has been shown.")
        stop = input("Press Enter and Go back")
        admin_home_page(cursor, connection, id)
    except Exception as e:
        print(f"Error Information: {e}")
        connection.rollback()
        stop = input("Press Enter and Retry")
        view_all_reviews(id, cursor, connection)

def update_score(id, cursor, connection):
    clear_screen()
    print("You are trying to update the score of a movie...")
    print("Are you sure?")
    print("Please answer yes or no. Other inputs is invalid.")
    confirmation = input("(yes/no): ").strip().lower()
    if confirmation == 'yes':
        print(" ")
    elif confirmation == 'no':
        admin_home_page(cursor, connection, id)
    else:
        print("Sorry, the system found other inputs")
        stop = input("Press Enter and Refresh")
        update_score(id, cursor, connection)
    print("Which movie's score do you want to be update?")
    movie_name = input("(movie name): ")
    movie_id = movie_from_name_to_id(movie_name, cursor)
    try:
        if unique_movie_id_detection(cursor, movie_id) == 1:
            print("No movie found with the given name")
            stop = input("Press Enter and Retry")
            update_score(id, cursor, connection)

        cursor.execute(
            "SELECT Rating FROM reviews WHERE MovieID = %s",
            (movie_id,)
        )
        scores = cursor.fetchall()
        if not scores:
            print("No one has rated the movie yet. The movie remains at its initial score.")
            stop = input("Press Enter and Go back")
            admin_home_page(cursor,connection,id)

        total_score = sum(score[0] for score in scores)
        average_score = total_score * 2 / len(scores)

        print(f"New score for this movie: {average_score:.2f}")
        cursor.execute(
            "UPDATE movies SET AverageRating = %s WHERE MovieID = %s",
            (average_score, movie_id)
        )
        connection.commit()

        print(" ")
        print("Score Updated.")
        stop = input("Press Enter and Go back")
        admin_home_page(cursor, connection, id)
    except Exception as e:
        print(f"Error Information: {e}")
        connection.rollback()
        stop = input("Press Enter and Retry")
        update_score(id, cursor, connection)


def admin_home_page(cursor, connection, admin_id):
    clear_screen()
    id = admin_id
    print("Welcome, you can use these features:")
    print("1. View current cinema movie information")
    print("2. Add a movie")
    print("3. Offline a movie")
    print("4. Modify movie showtime information")
    print("5. View all reviews for a movie")
    print("6. Update a movie score")
    print("7. Log out")
    print("8. Exit")
    print("Please enter 1, 2, 3, 4, 5 ,6 , 7 or 8. Other inputs is invalid.")
    choice = input("(1/2/3/4/5/6/7/8): ").strip()
    if choice == '8':
        print("Exiting program...")
        exit(0)
    elif choice == '7':
        login_prompt(cursor, connection)
    elif choice == '1':
        get_movie_info("admin",id, cursor, connection)
    elif choice == '2':
        add_movie(id, cursor, connection)
    elif choice == '3':
        remove_movie(id, cursor, connection)
    elif choice == '4':
        modify_showtime_info(id, cursor, connection)
    elif choice == '5':
        view_all_reviews(id, cursor, connection)
    elif choice == '6':
        update_score(id, cursor, connection)
    else:
        print("Sorry, the system found other inputs")
        stop = input("Press Enter and Refresh")
        admin_home_page(cursor, connection, id)

def user_log_in(cursor, connection):
    clear_screen()
    print("You are trying to log in as User...")
    print("Are you sure?")
    print("Please answer yes or no. Other inputs is invalid.")
    confirmation = input("(yes/no): ").strip().lower()
    if confirmation == 'yes':
        print(" ")
    elif confirmation == 'no':
        login_prompt(cursor, connection)
    else:
        print("Sorry, the system found other inputs")
        stop = input("Press Enter and Refresh")
        user_log_in(cursor, connection)
    print("Please follow the instructions to log in.")
    print(" ")
    print("Please Enter Your User ID")
    user_id = input("(User ID): ")
    print("Please Enter Your Passcode")
    user_passcode = getpass.getpass("(User Passcode): ")

    cursor.execute(f"SELECT Username, Password, Email FROM users WHERE UserID = %s", (user_id,))
    result = cursor.fetchone()
    if result:
        name_user, passcode_user, email_user = result
        if(user_passcode == passcode_user):
            print("The system needs to check your email")
            print("Please Enter Your Email")
            user_email = input("(User Email): ")
            if (user_email == email_user):
                print("Log in successfully, Welcome!")
                print(name_user)
                stop = input("Press Enter and continue.")
                user_home_page(cursor, connection,user_id)
            else:
                print("Email verification failed")
                stop = input("Press Enter and Retry.")
                user_log_in(cursor, connection)
    else:
        print("Sorry, the system did not find the user ID you entered.")
        stop = input("Press Enter and Retry")
        user_log_in(cursor, connection)

def admin_log_in(cursor, connection):
    clear_screen()
    print("You are trying to log in as Admin...")
    print("Are you sure?")
    print("Please answer yes or no. Other inputs is invalid.")
    confirmation = input("(yes/no): ").strip().lower()
    if confirmation == 'yes':
        print(" ")
    elif confirmation == 'no':
        login_prompt(cursor, connection)
    else:
        print("Sorry, the system found other inputs")
        stop = input("Press Enter and Refresh")
        admin_log_in(cursor, connection)
    print("Please follow the instructions to log in.")
    print(" ")
    print("Please Enter Your Admin ID")
    admin_id = input("(Admin ID): ")
    print("Please Enter Your Passcode")
    admin_passcode = getpass.getpass("(Admin Passcode): ")

    cursor.execute(f"SELECT Username, Password FROM cinemaadmins WHERE AdminID = %s", (admin_id,))
    result = cursor.fetchone()
    if result:
        name_admin, passcode_admin = result
        if (admin_passcode == passcode_admin):
            print("Log in successfully, Welcome!")
            print(name_admin)
            stop = input("Press Enter and continue.")
            admin_home_page(cursor, connection, admin_id)
    else:
        print("Sorry, the system did not find the admin ID you entered.")
        stop = input("Press Enter and Retry")
        admin_log_in(cursor, connection)

def login_log_in(cursor, connection):
    clear_screen()
    print("My identity is...")
    print("1. User")
    print("2. Admin")
    print("3. Back to last step")
    print("4. Exit")
    print("Please enter 1, 2 ,3 or 4. Other inputs is invalid.")
    choice = input("(1/2/3/4): ").strip()
    if choice == '4':
        print("Exiting program...")
        exit(0)
    elif choice == '3':
        login_prompt(cursor, connection)
    elif choice == '1':
        user_log_in(cursor, connection)
    elif choice == '2':
        admin_log_in(cursor, connection)
    else:
        print("Sorry, the system found other inputs")
        stop = input("Press Enter and Refresh")
        login_log_in(cursor, connection)

def unique_user_id_detection(cursor,user_id):
    try:
        cursor.execute("SELECT 1 FROM users WHERE UserID = %s", (user_id,))
        result = cursor.fetchone()
        if result:
            return 0
        else:
            return 1
    except Exception as e:
        print(f"Error Information: {e}")
        stop = input("Program terminated")
        exit(0)

def user_register(cursor, connection):
    clear_screen()
    print("You want to register as a user.")
    print("Are you sure?")
    print("Please answer yes or no. Other inputs is invalid.")
    confirmation = input("(yes/no): ").strip().lower()
    if confirmation == 'yes':
        print(" ")
    elif confirmation == 'no':
        login_prompt(cursor, connection)
    else:
        print("Sorry, the system found other inputs")
        stop = input("Press Enter and Refresh")
        user_register(cursor, connection)
    print("Please follow the instructions to complete registration.")
    print(" ")
    print("Please note: Users' digital IDs may be duplicated.")
    print("Once duplicates are detected, you will need to re-register. Sorry!")
    print(" ")
    print("Please enter your desired username")
    user_name = input("(User name): ")
    print("Please enter your E-mail address")
    user_email = input("(Email address): ")
    print("Please choose a numeric ID for yourself")
    user_id = input("(User ID): ")
    if unique_user_id_detection(cursor, user_id) == 0:
        print("Sorry, the system found a duplicate numeric ID")
        stop = input("Press Enter and try again")
        user_register(cursor, connection)
    print("Please set a passcode for yourself")
    user_passcode = input("(User passcode): ")

    try:
        cursor.execute(
            "INSERT INTO users (UserID, Username, Password, Email) VALUES (%s, %s, %s, %s)",
            (user_id, user_name, user_passcode, user_email)
        )
        connection.commit()
        print("Registered successfully!")
        print("Back to Home page")
        stop = input("Press Enter to Continue")
        login_prompt(cursor, connection)
    except Exception as e:
        print(f"Error Information: {e}")
        connection.rollback()
        stop = input("Press Enter to Retry")
        user_register(cursor, connection)

def unique_admin_id_detection(cursor, admin_id):
    try:
        cursor.execute("SELECT 1 FROM cinemaadmins WHERE AdminID = %s", (admin_id,))
        result = cursor.fetchone()
        if result:
            return 0
        else:
            return 1
    except Exception as e:
        print(f"Error Information: {e}")
        stop = input("Program terminated")
        exit(0)

# Verification Code is 3170
def admin_register(cursor, connection):
    clear_screen()

    print("You want to register as a Admin.")
    print("Are you sure?")
    print("Please answer yes or no. Other inputs is invalid.")
    confirmation = input("(yes/no): ").strip().lower()
    if confirmation == 'yes':
        print(" ")
    elif confirmation == 'no':
        login_prompt(cursor, connection)
    else:
        print("Sorry, the system found other inputs")
        stop = input("Press Enter and Refresh")
        admin_register(cursor, connection)

    print("Please enter the verification code")
    ver_code = input("(Verification Code): ")
    if ver_code != '3170':
        print("The verification code is incorrect, you cannot be registered as Admin")
        stop = input("Press Enter to Retry")
        admin_register(cursor, connection)
    print("The verification code is correct! You can register as an Admin")
    print(" ")

    print("Please follow the instructions to complete registration.")
    print(" ")
    print("Please note: Admins' digital IDs may be duplicated.")
    print("Once duplicates are detected, you will need to re-register. Sorry!")
    print(" ")
    print("Please enter your desired Admin name")
    admin_name = input("(Admin name): ")
    print("Please choose a numeric ID for yourself")
    admin_id = input("(Admin ID): ")
    if unique_admin_id_detection(cursor, admin_id) == 0:
        print("Sorry, the system found a duplicate numeric ID")
        stop = input("Press Enter and try again")
        admin_register(cursor, connection)
    print("Please set a passcode for yourself")
    admin_passcode = input("(Admin passcode): ")

    try:
        cursor.execute(
            "INSERT INTO cinemaadmins (AdminID, Username, Password) VALUES (%s, %s, %s)",
            (admin_id, admin_name, admin_passcode)
        )
        connection.commit()
        print("Registered successfully!")
        print("Back to Home page")
        stop = input("Press Enter to Continue")
        login_prompt(cursor, connection)
    except Exception as e:
        print(f"Error Information: {e}")
        connection.rollback()
        stop = input("Press Enter to Retry")
        admin_register(cursor, connection)

def login_register(cursor, connection):
    clear_screen()
    print("You want to register as...")
    print("1. User, let's continue")
    print("2. Admin, you need a specific verification code")
    print("3. No, back to last step")
    print("4. Exit")
    print("Please enter 1, 2 ,3 or 4. Other inputs is invalid.")
    choice = input("(1/2/3/4): ").strip()
    if choice == '4':
        print("Exiting program...")
        exit(0)
    elif choice == '3':
        login_prompt(cursor, connection)
    elif choice == '1':
        user_register(cursor, connection)
    elif choice == '2':
        admin_register(cursor, connection)
    else:
        print("Sorry, the system found other inputs")
        stop = input("Press Enter and Refresh")
        login_register(cursor, connection)

def login_prompt(cursor, connection):
    clear_screen()
    print("Welcome to our Cinema_Management_Model !!")
    print(" ")

    print_random_sentence()
    print(" ")

    print("Please log in...")
    print("1. Already have an account. Continue to log in")
    print("2. Don’t have an account yet? Register one.")
    print("3. Exit")
    print("Please enter 1, 2 or 3. Other inputs is invalid.")
    choice = input("(1/2/3): ").strip()

    if choice == '3':
        print("Exiting program...")
        exit(0)
    elif choice == '1':
        login_log_in(cursor, connection)
    elif choice == '2':
        login_register(cursor, connection)
    else:
        print("Sorry, the system found other inputs")
        stop = input("Press Enter and Refresh")
        login_prompt(cursor, connection)

def main():
    if confirm_connection():
        print("")

    connection = connect_to_db()
    while(connection == -1):
        handle_connection_failure()
        connection = connect_to_db()

    cursor = connection.cursor()
    login_prompt(cursor, connection)

    cursor.close()
    connection.close()

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

if __name__ == '__main__':
    main()
