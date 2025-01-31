records = {}
def get_valid_input(prompt):
    """Ensures the user enters only 'Y' or 'N'."""
    while True:
        choice = input(prompt).strip().lower()
        if choice in ['y', 'n']:
            return choice
        print("Invalid input. Please enter 'Y' for Yes or 'N' for No.")
def show_countries():
    """Displays the list of available countries."""
    if not records:
        print("No countries available. Please add a country first.")
    else:
        print("Available Countries:")
        for country in records:
            print(f"- {country}")
def show_states(country):
    """Displays the list of available states for a given country."""
    if not records[country]:
        print(f"No states available under Country {country}.")
    else:
        print(f"Available States under {country}:")
        for state in records[country]:
            print(f"- {state}")
def add_data():
    try:
        while True:
            # Adding country
            country = input("Enter country: ").strip().title()
            if not country:
                print("Country name cannot be blank. Please enter a valid country name.")
                continue
            if country not in records:
                records[country] = {}
                print(f"Country {country} added.")
            else:
                print(f"Country {country} already exists.")

            # Ask if the user wants to add another country
            choice = get_valid_input("Do you want to enter another country? (Y/N): ")
            if choice == 'n':
                break

        # Ask if the user wants to add a state
        choice = get_valid_input("Do you want to add a state? (Y/N): ")
        if choice == 'n':
            print("Returning to the main menu.")
            return
        
        while True:
            # Adding state
            state = input("Enter state: ").strip().title()
            if not state:
                print("State name cannot be blank. Please enter a valid state name.")
                continue
            show_countries()
            country = input(f"Enter the country to associate with state {state}: ").strip().title()

            if country in records:
                if state not in records[country]:
                    records[country][state] = []  # Empty list for cities under the state
                    print(f"State {state} added under Country {country}.")
                else:
                    print(f"State {state} already exists under Country {country}.")
            else:
                print(f"Country {country} does not exist. Please enter a valid country.")

            # Ask if the user wants to add another state
            choice = get_valid_input("Do you want to enter another state? (Y/N): ")
            if choice == 'n':
                break

        # Ask if the user wants to add a city
        choice = get_valid_input("Do you want to add a city? (Y/N): ")
        if choice == 'n':
            print("Returning to the main menu.")
            return
        
        while True:
            # Adding city
            city = input("Enter city: ").strip().title()
            if not city:
                print("City name cannot be blank. Please enter a valid city name.")
                continue
            show_countries()  # Show available countries
            country = input(f"Enter the country to associate with city {city}: ").strip().title()
            if country in records:
                # If there are no states in the country, prompt user to add a state first
                if not records[country]:
                    print(f"No states available under Country {country}. Please add a state first.")
                    break  # Exit city addition if no states exist
                show_states(country)  # Show available states for the country
                state = input(f"Enter the state to associate with city {city}: ").strip().title()
                if state in records[country]:
                    # Add city under the state if not already present
                    if city not in records[country][state]:
                        records[country][state].append(city)
                        print(f"City {city} added under State {state}, Country {country}.")
                    else:
                        print(f"City {city} already exists under State {state}, Country {country}.")
                else:
                    # State does not exist in the selected country
                    print(f"State {state} does not exist under Country {country}. Please enter a valid state.")
            else:
                # Country does not exist
                print(f"Country {country} does not exist. Please enter a valid country.")
            # Ask if the user wants to enter another city
            choice = get_valid_input("Do you want to enter another city? (Y/N): ")
            if choice == 'n':
                break
        print("Returning to the main menu.")
    except Exception as e:
        print(f"Error occurred while adding data: {e}")
def show_data():
    ''' This Function will print the all records. '''
    try:
        if not records:
            print("No records found.")
        else:
            print("All Records:")
            for country, states in records.items():
                print(f"Country: {country}")
                for state, cities in states.items():
                    print(f"  State: {state}, Cities: {', '.join(cities)}")
    except Exception as e:
        print(f"Error occurred while showing records: {e}")
def update_data():
    ''' This Function will update the Country, State, or City based on user input. '''
    try:
        print("What would you like to update? (Country, State, City)")
        choice = input("Enter your choice (Country, State, City): ").strip().title()
        if choice == "Country":
            if not records:
                print("No countries available to update. Please add a country first.")
                return
            # Show available countries
            show_countries()
            old_country = input("Enter the current country name: ").strip().title()
            if old_country in records:
                new_country = input(f"Enter the new name for the country {old_country}: ").strip().title()
                records[new_country] = records.pop(old_country)
                print(f"Country '{old_country}' updated to '{new_country}'.")
            else:
                print(f"Country '{old_country}' not found.")
        elif choice == "State":
            if not records:
                print("No countries available. Please add a country first.")
                return
            # Show available countries
            show_countries()
            country = input("Enter the country for the state: ").strip().title()
            if country in records:
                if not records[country]:
                    print(f"No states available under Country '{country}'. Please add a state first.")
                    return
                # Show available states
                show_states(country)
                old_state = input("Enter the current state name: ").strip().title()
                if old_state in records[country]:
                    new_state = input(f"Enter the new name for the state '{old_state}': ").strip().title()
                    records[country][new_state] = records[country].pop(old_state)
                    print(f"State '{old_state}' updated to '{new_state}' under Country '{country}'.")
                else:
                    print(f"State '{old_state}' not found under Country '{country}'.")
            else:
                print(f"Country '{country}' not found.")
        elif choice == "City":
            if not records:
                print("No countries available. Please add a country first.")
                return
            # Show available countries
            show_countries()
            country = input("Enter the country for the city: ").strip().title()
            if country in records:
                if not records[country]:
                    print(f"No states available under Country '{country}'. Please add a state first.")
                    return
                # Show available states
                show_states(country)
                state = input("Enter the state for the city: ").strip().title()
                if state in records[country]:
                    if not records[country][state]:
                        print(
                            f"No cities available under State '{state}', Country '{country}'. Please add a city first.")
                        return
                    # Show available cities
                    print(f"Available Cities under {state}, {country}:")
                    for city in records[country][state]:
                        print(f"- {city}")
                    old_city = input("Enter the current city name: ").strip().title()
                    if old_city in records[country][state]:
                        new_city = input(f"Enter the new name for the city '{old_city}': ").strip().title()
                        records[country][state].remove(old_city)
                        records[country][state].append(new_city)
                        print(f"City '{old_city}' updated to '{new_city}' under State '{state}', Country '{country}'.")
                    else:
                        print(f"City '{old_city}' not found under State '{state}', Country '{country}'.")
                else:
                    print(f"State '{state}' not found under Country '{country}'.")
            else:
                print(f"Country '{country}' not found.")
        else:
            print("Invalid choice. Please enter 'Country', 'State', or 'City'.")
    except Exception as e:
        print(f"Error occurred while updating record: {e}")
def delete_data():
    ''' This function deletes a Country, State, or City from records based on user input. '''
    try:
        print("What would you like to delete? (Country, State, City)")
        choice = input("Enter your choice (Country, State, City): ").strip().title()
        if choice == "Country":
            if not records:
                print("No countries available to delete.")
                return
            # Show available countries
            show_countries()
            country = input("Enter the country to delete: ").strip().title()
            if country in records:
                del records[country]
                print(f"All records for Country '{country}' deleted successfully.")
            else:
                print(f"Country '{country}' not found.")
        elif choice == "State":
            if not records:
                print("No countries available. Please add a country first.")
                return
            # Show available countries
            show_countries()
            country = input("Enter the country for the state: ").strip().title()
            if country in records:
                if not records[country]:
                    print(f"No states available under Country '{country}'.")
                    return
                # Show available states
                show_states(country)
                state = input("Enter the state to delete: ").strip().title()
                if state in records[country]:
                    del records[country][state]
                    print(f"State '{state}' deleted successfully under Country '{country}'.")
                else:
                    print(f"State '{state}' not found under Country '{country}'.")
            else:
                print(f"Country '{country}' not found.")
        elif choice == "City":
            if not records:
                print("No countries available. Please add a country first.")
                return
            # Show available countries
            show_countries()
            country = input("Enter the country for the city: ").strip().title()
            if country in records:
                if not records[country]:
                    print(f"No states available under Country '{country}'.")
                    return
                # Show available states
                show_states(country)
                state = input("Enter the state for the city: ").strip().title()
                if state in records[country]:
                    if not records[country][state]:
                        print(f"No cities available under State '{state}', Country '{country}'.")
                        return
                    # Show available cities
                    print(f"Available Cities under {state}, {country}:")
                    for city in records[country][state]:
                        print(f"- {city}")
                    city = input("Enter the city to delete: ").strip().title()
                    if city in records[country][state]:
                        records[country][state].remove(city)
                        print(f"City '{city}' deleted successfully under State '{state}', Country '{country}'.")
                    else:
                        print(f"City '{city}' not found under State '{state}', Country '{country}'.")
                else:
                    print(f"State '{state}' not found under Country '{country}'.")
            else:
                print(f"Country '{country}' not found.")
        else:
            print("Invalid choice. Please choose either 'Country', 'State', or 'City'.")
    except Exception as e:
        print(f"Error occurred while deleting record: {e}")
def main_menu():
    try:
        print("\nMenu:")
        print("1. Enter Country, State, City")
        print("2. Show All Records")
        print("3. Update Record")
        print("4. Delete Record")
        print("5. Exit")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            add_data()
            main_menu()
        elif choice == "2":
            show_data()
            main_menu()
        elif choice == "3":
            update_data()
            main_menu()
        elif choice == "4":
            delete_data()
            main_menu()
        elif choice == "5":
            print("Exiting the program. Goodbye!")
        else:
            print("Invalid choice. Please try again.")
            main_menu()
    except Exception as e:
        print(f"Error occurred: {e}")
main_menu()
