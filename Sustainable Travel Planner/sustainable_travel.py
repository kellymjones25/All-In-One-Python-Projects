def add_trip(trips):
    """
    Add a new sustainable trip.
    """
    destination = input("Enter destination: ")
    transport = input("Enter transportation (bike/bus/train/car): ")
    activities = input("Enter eco-friendly activities (comma separated): ").split(",")

    trip = {
        "destination": destination,
        "transport": transport,
        "activities": [a.strip() for a in activities]
    }
    trips.append(trip)
    print(f"✅ Sustainable trip to {destination} added!")


def view_trips(trips):
    """
    Display all sustainable trips.
    """
    if not trips:
        print("⚠️ No trips added yet.")
        return

    print("\n🌿 Sustainable Trips")
    print("-" * 30)
    for i, trip in enumerate(trips, 1):
        print(f"{i}. Destination: {trip['destination']}")
        print(f"   Transport: {trip['transport']}")
        print("   Activities:")
        for act in trip["activities"]:
            print(f"     - {act}")
        print("-" * 30)


def run_sustainable_travel():
    trips = []
    while True:
        print("\n=== Sustainable Travel Planner ===")
        print("1. Add Trip")
        print("2. View Trips")
        print("3. Exit")

        choice = input("Choose an option (1-3): ")

        if choice == "1":
            add_trip(trips)
        elif choice == "2":
            view_trips(trips)
        elif choice == "3":
            print("👋 Goodbye! Travel sustainably!")
            break
        else:
            print("❌ Invalid choice. Try again.")


if __name__ == "__main__":
    run_sustainable_travel()
