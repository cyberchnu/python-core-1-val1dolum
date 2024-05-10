def calculate_fuel(distance):
    fuel_needed = distance * 10
    if fuel_needed < 100:
        return 100
    else:
        return fuel_needed
print(calculate_fuel(25))
print(calculate_fuel(88.8))
print(calculate_fuel(4))
