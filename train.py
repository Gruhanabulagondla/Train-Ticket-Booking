trains = {
    1: {
        "name": "Vande Bharat Express",
        "from": "Hyderabad",
        "to": "Bangalore",
        "fare": 850,
        "seats": 5
    },
    2: {
        "name": "Intercity Express",
        "from": "Chennai",
        "to": "Bangalore",
        "fare": 600,
        "seats": 5
    },
    3: {
        "name": "Godavari Express",
        "from": "Hyderabad",
        "to": "Visakhapatnam",
        "fare": 750,
        "seats": 5
    },
    4: {
        "name": "Krishna Express",
        "from": "Vijayawada",
        "to": "Hyderabad",
        "fare": 500,
        "seats": 5
    }
}

bookings = {}
booking_id = 1001


def display_trains():
    print("\n========== AVAILABLE TRAINS ==========")

    for number, train in trains.items():
        print(f"\nTrain Number: {number}")
        print(f"Train Name: {train['name']}")
        print(f"Route: {train['from']} -> {train['to']}")
        print(f"Fare: ₹{train['fare']}")
        print(f"Available Seats: {train['seats']}")


def search_train():
    source = input("\nEnter source: ").strip().lower()
    destination = input("Enter destination: ").strip().lower()

    found = False

    print("\n========== SEARCH RESULTS ==========")

    for number, train in trains.items():

        if (train["from"].lower() == source and
                train["to"].lower() == destination):

            print(f"\nTrain Number: {number}")
            print(f"Train Name: {train['name']}")
            print(f"Route: {train['from']} -> {train['to']}")
            print(f"Fare: ₹{train['fare']}")
            print(f"Available Seats: {train['seats']}")

            found = True

    if not found:
        print("No trains found for this route.")


def book_ticket():
    global booking_id

    display_trains()

    try:
        train_number = int(input("\nEnter train number: "))

        if train_number not in trains:
            print("Invalid train number.")
            return

        train = trains[train_number]

        if train["seats"] <= 0:
            print("Sorry! No seats available.")
            return

        name = input("Enter passenger name: ").strip()
        age = int(input("Enter passenger age: "))

        if not name:
            print("Passenger name cannot be empty.")
            return

        if age <= 0:
            print("Invalid age.")
            return

        seat_count = int(input("Enter number of seats: "))

        if seat_count <= 0:
            print("Number of seats must be greater than 0.")
            return

        if seat_count > train["seats"]:
            print(f"Only {train['seats']} seats are available.")
            return

        total_fare = train["fare"] * seat_count

        current_booking_id = booking_id
        booking_id += 1

        bookings[current_booking_id] = {
            "passenger": name,
            "age": age,
            "train_number": train_number,
            "train_name": train["name"],
            "source": train["from"],
            "destination": train["to"],
            "seats": seat_count,
            "fare": total_fare
        }

        train["seats"] -= seat_count

        print("\n========== BOOKING SUCCESSFUL ==========")
        print(f"Booking ID: {current_booking_id}")
        print(f"Passenger Name: {name}")
        print(f"Age: {age}")
        print(f"Train: {train['name']}")
        print(f"Route: {train['from']} -> {train['to']}")
        print(f"Seats Booked: {seat_count}")
        print(f"Total Fare: ₹{total_fare}")

    except ValueError:
        print("Please enter valid numbers.")


def view_bookings():
    print("\n========== ALL BOOKINGS ==========")

    if not bookings:
        print("No bookings available.")
        return

    for booking_id, booking in bookings.items():

        print(f"\nBooking ID: {booking_id}")
        print(f"Passenger: {booking['passenger']}")
        print(f"Age: {booking['age']}")
        print(f"Train: {booking['train_name']}")
        print(f"Route: {booking['source']} -> {booking['destination']}")
        print(f"Seats: {booking['seats']}")
        print(f"Total Fare: ₹{booking['fare']}")


def cancel_ticket():
    try:
        booking_id_input = int(input("\nEnter booking ID: "))

        if booking_id_input not in bookings:
            print("Booking not found.")
            return

        booking = bookings[booking_id_input]

        train_number = booking["train_number"]
        seats = booking["seats"]

        trains[train_number]["seats"] += seats

        del bookings[booking_id_input]

        print("\nTicket cancelled successfully.")
        print(f"Booking ID {booking_id_input} has been cancelled.")

    except ValueError:
        print("Please enter a valid booking ID.")


def main():
    print("========== TRAIN TICKET BOOKING SIMULATOR ==========")

    while True:

        print("\n1. View Available Trains")
        print("2. Search Train")
        print("3. Book Ticket")
        print("4. View Bookings")
        print("5. Cancel Ticket")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            display_trains()

        elif choice == "2":
            search_train()

        elif choice == "3":
            book_ticket()

        elif choice == "4":
            view_bookings()

        elif choice == "5":
            cancel_ticket()

        elif choice == "6":
            print("\nThank you for using Train Ticket Booking Simulator!")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()