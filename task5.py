
# Bus Passenger Occupancy Simulation

bus_capacity = 50
passengers = 0

# Boarding and alighting counts at each stop
stops = [
    ("Stop 1", 20, 0),
    ("Stop 2", 15, 5),
    ("Stop 3", 25, 10),
    ("Stop 4", 10, 20),
    ("Stop 5", 5, 10)
]

print("BUS PASSENGER OCCUPANCY SIMULATION")
print("-" * 65)
print(f"Bus Capacity: {bus_capacity}")
print()

print(f"{'Stop':<10}{'Boarding':<12}"
      f"{'Alighting':<12}{'Passengers':<14}{'Status'}")
print("-" * 65)

for stop, boarding, alighting in stops:

    # Validate alighting count
    if alighting > passengers:
        print(f"Error at {stop}: Not enough passengers to alight!")
        continue

    # Remove passengers who get off
    passengers -= alighting

    # Add passengers who get on
    passengers += boarding

    # Check bus capacity
    if passengers > bus_capacity:
        status = "CAPACITY VIOLATION!"
    else:
        status = "Within capacity"

    print(f"{stop:<10}{boarding:<12}"
          f"{alighting:<12}{passengers:<14}{status}")

print("-" * 65)
print("Final passenger count:", passengers)
