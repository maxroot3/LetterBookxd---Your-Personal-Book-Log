book_log = []  # will hold one dictionary per book

running = True

while running:

    print("\n========================================")
    print("LetterBookx - Your Personal Book Log")
    print("========================================")
    print("1. Log a new book")
    print("2. View my book log")
    print("3. View summary stats")
    print("4. Exit")

    choice = input("Choose an option (1-4): ").strip()

    if choice == "1":
        print("\n--- Log a New Book ---")

        # title
        title = ""
        while title == "":
            title = input("Book title: ").strip()

            if title == "":
                print("Title can't be empty.")

        # author
        author = ""
        while author == "":
            author = input("Author: ").strip()

            if author == "":
                print("Author can't be empty.")

        # start date
        start_date = ""
        while start_date == "":
            start_date = input("Date started: ").strip()

            if start_date == "":
                print("Start date can't be empty.")

        # finish date
        finish_date = ""
        while finish_date == "":
            finish_date = input("Date finished: ").strip()

            if finish_date == "":
                print("Finish date can't be empty.")

        # favorite quote/s
        quote = ""
        while quote == "":
            quote = input("Your favorite quote from this book: ").strip()

            if quote == "":
                print("Quote can't be empty.")

        # book rating
        book_rating = 0

        while book_rating < 1 or book_rating > 5:
            raw_rating = input("Rate the book (1-5): ")

            try:
                book_rating = float(raw_rating)

                if book_rating < 1 or book_rating > 5:
                    print("Rating must be between 1 and 5.")

            except ValueError:
                print("Please enter a valid number.")

        # feeling about the book
        emotion = input("How did this book make you feel? ").strip()

        # create dictionary for the book
        entry = {
            "title": title,
            "author": author,
            "start_date": start_date,
            "finish_date": finish_date,
            "quote": quote,
            "book_rating": book_rating,
            "emotion": emotion
        }

        # add book to the list
        book_log.append(entry)

        print("\n'" + title + "' has been added to your book log!")

    elif choice == "2":
        print("\n--- Your Book Log ---")

        if len(book_log) == 0:
            print("You haven't logged any books yet.")

        else:
            for i in range(len(book_log)):
                entry = book_log[i]

                # display rating with half-star support
                full_stars = int(entry["book_rating"])
                remaining = entry["book_rating"] - full_stars

                stars = "★" * full_stars

                if remaining == 0.5:
                    stars = stars + "⯨"

                stars = stars + "-" * (
                    5 - full_stars - (1 if remaining == 0.5 else 0)
                )

                print("\nBook #" + str(i + 1))
                print("Title:          " + entry["title"])
                print("Author:         " + entry["author"])
                print("Started:        " + entry["start_date"])
                print("Finished:       " + entry["finish_date"])
                print("Favorite quote: \"" + entry["quote"] + "\"")
                print("Book rating:    " + stars +
                      " (" + str(entry["book_rating"]) + "/5)")
                print("Feeling:        " + entry["emotion"])

    elif choice == "3":
        print("\n--- Summary ---")

        total_books = len(book_log)

        if total_books == 0:
            print("No books logged yet.")

        else:
            total_book_rating = 0

            for entry in book_log:
                total_book_rating = total_book_rating + entry["book_rating"]

            average_book_rating = total_book_rating / total_books

            print("Total books logged:   " + str(total_books))
            print("Average book rating:  " +
                  str(round(average_book_rating, 2)) + "/5")

    elif choice == "4":
        print("\nThanks for using Book Log. Happy reading!")

        running = False

    else:
        print("\nInvalid option. Please choose a number from 1 to 4.")