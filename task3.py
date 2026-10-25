
def calculate_base_fare(distance):
    """Calculate fare using illustrative distance slabs."""
    if distance <= 100:
        return distance * 1.00
    elif distance <= 300:
        return 100 * 1.00 + (distance - 100) * 1.50
    else:
        return 100 * 1.00 + 200 * 1.50 + (distance - 300) * 2.00


def calculate_ticket(age, distance, travel_class):
    base_fare = calculate_base_fare(distance)

    # Illustrative class multipliers
    class_rates = {
        "Sleeper": 1.0,
        "AC3": 2.0,
        "AC2": 3.0
    }

    reservation_fee = {
        "Sleeper": 20,
        "AC3": 40,
        "AC2": 60
    }

    fare = base_fare * class_rates[travel_class]

    # Illustrative age-based concession
    concession = 0
    if age < 5:
        fare = 0
    elif age >= 60:
        concession = fare * 0.20
        fare -= concession

    total_fare = fare + reservation_fee[travel_class]

    return base_fare, concession, total_fare


def main():
    print("=== Railway Fare and Reservation Calculator ===")

    distance = float(input("Enter journey distance (km): "))
    passengers = int(input("Enter number of passengers: "))

    print("Classes: Sleeper, AC3, AC2")
    travel_class = input("Choose travel class: ").strip()

    if distance <= 0 or passengers <= 0:
        print("Distance and passenger count must be positive.")
        return

    if travel_class not in ["Sleeper", "AC3", "AC2"]:
        print("Invalid travel class.")
        return

    total_amount = 0

    for i in range(1, passengers + 1):
        print(f"\nPassenger {i}")
        age = int(input("Enter passenger age: "))

        if age < 0:
            print("Invalid age.")
            return

        base, concession, fare = calculate_ticket(
            age, distance, travel_class
        )

        print(f"Distance-based base fare: Rs. {base:.2f}")
        print(f"Age concession: Rs. {concession:.2f}")
        print(f"Reservation fee: Rs. "
              f"{fare - (base * {'Sleeper': 1, 'AC3': 2, 'AC2': 3}[travel_class] - concession):.2f}")
        print(f"Passenger total: Rs. {fare:.2f}")

        total_amount += fare

    print("\n===================================")
    print(f"Total reservation amount: Rs. {total_amount:.2f}")

    cancel = input("Cancel the reservation? (yes/no): ").strip().lower()

    if cancel == "yes":
        penalty_rate = 0.25  # Illustrative cancellation penalty
        penalty = total_amount * penalty_rate
        refund = total_amount - penalty

        print(f"Cancellation penalty: Rs. {penalty:.2f}")
        print(f"Refund amount: Rs. {refund:.2f}")

    print("Thank you for using the calculator!")


if __name__ == "__main__":
    main()
