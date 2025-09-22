def add_trip(itineraries):
    """
    Add a new travel itinerary with destination, accommodation, and activities.
    """
    destination = input("Enter destination: ")
    accommodation = input("Enter accommodation: ")
    activities = input("Enter activities (comma separated): ").split(",")

    trip = {
        "destination": destination,
        "accommodation": accommodation,
        "activities": [a.strip() for a in activities]
    }
    itineraries.append(trip)
    print(f"✅ Trip to {destination} added!")


def view_trips(itineraries):
    """
    View all saved itineraries.
    """
    if not itineraries:
        print("⚠️ No trips saved yet.")
        return

    print("\n📅 Your Travel Itineraries")
    print("-" * 30)
    for i, trip in enumerate(itineraries, 1):
        print(f"{i}. Destination: {trip['destination']}")
        print(f"   Accommodation: {trip['accommodation']}")
        print("   Activities:")
        for act in trip["activities"]:
            print(f"     - {act}")
        print("-" * 30)


def run_planner():
    """
    Main loop for travel itinerary planner.
    """
    itineraries = []

    while True:
        print("\n=== Travel Itinerary Planner ===")
        print("1. Add Trip")
        print("2. View Trips")
        print("3. Exit")

        choice = input("Choose an option (1-3): ")

        if choice == "1":
            add_trip(itineraries)
        elif choice == "2":
            view_trips(itineraries)
        elif choice == "3":
            print("👋 Goodbye! Safe travels!")
            break
        else:
            print("❌ Invalid choice, try again.")


if __name__ == "__main__":
    run_planner()
