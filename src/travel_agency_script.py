# Variables:
# 1.	destinations
# 2.	exchange_rate
# 3.	num_of_families
# 4.	families
# 5.	family_name
# 6.	destination_option
# 7.	num_adults
# 8.	num_children
# 9.	destination
# 10.	transportation_cost
# 11.	base_accommodation
# 12.	adult_discount
# 13.	accommodation_cost
# 14.	total_cost
# 15.	total_cost_myr

# Initialisation Counter:
# 1.	num_of_families


destinations = {
    1: {"name": "Grand Canyon", "transport": 200, "accommodation": 1500},
    2: {"name": "Yellowstone National Park", "transport": 180, "accommodation": 1700},
    3: {"name": "Glacier National Park", "transport": 220, "accommodation": 1600},

}

exchange_rate = 4.2
num_of_families = 0
families = []

print("- Welcome to SkyHigh Adventures Travel Agency -\n")

print("Destinations:")
for option, details in destinations.items():
    print(f"{option}. {details['name']}")

print()

while True:
    family_name = input("Enter family name (or 'quit' to finish entering data): ")
    if family_name.lower() == 'quit':
        break

    while True:
        destination_option = int(input("\nEnter destination option (1-3): "))
        if destination_option in destinations:
            break
        else:
            print("Invalid destination. Please choose 1, 2, or 3.")

    num_adults = int(input("Enter number of adults: "))
    num_children = int(input("Enter number of children: "))

    families.append({
        "name": family_name,
        "destination": destination_option,
        "adults": num_adults,
        "children": num_children,

    })

    num_of_families += 1

    print("Information recorded.\n")

print("\n--- Summary ---\n")

print(f"Number of Families: {num_of_families}\n")

for family in families:
    destination = destinations[family["destination"]]

    transportation_cost = (destination["transport"] * family["adults"]) + (destination["transport"] * 0.5 * family["children"])

    base_accommodation = destination["accommodation"]
    if family["adults"] == 1:
        adult_discount = 0
    elif family["adults"] == 2:
        adult_discount = 0.15
    else:
        adult_discount = 0.25

    accommodation_cost = (base_accommodation * family["adults"] * (1 - adult_discount)) + (base_accommodation * family["children"] * 0.6)

    total_cost = transportation_cost + accommodation_cost
    total_cost_myr = total_cost * exchange_rate

    print(f"Total cost for {family['name']} family: MYR {total_cost_myr:,.2f}")
