records = {}

def add_data():
    try:
        # Adding countries
        while True:
            country = input("Enter country: ").strip().title()
            if not country:
                print("Country name cannot be blank. Please enter a valid country name.")
                continue

            if country not in records:
                records[country] = {}
                print(f"Country {country} added.")
            else:
                print(f"Country {country} already exists.")

            choice = input("Do you want to enter another country? (Y/N): ").strip().lower()
            if choice == 'n':
                break

        # Adding states
        while True:
            state = input("Enter state: ").strip().title()
            if not state:
                print("State name cannot be blank. Please enter a valid state name.")
                continue

            # Associating the state with an existing country
            while True:
                country = input(f"Enter the country to associate with state {state}: ").strip().title()
                if country in records:
                    records[country][state] = []
                    print(f"State {state} added under Country {country}.")
                    break
                else:
                    print(f"Country {country} does not exist. Please enter a valid country.")

            choice = input("Do you want to enter another state? (Y/N): ").strip().lower()
            if choice == 'n':
                break

        # Adding cities
        while True:
            city = input("Enter city: ").strip().title()
            if not city:
                print("City name cannot be blank. Please enter a valid city name.")
                continue

            # Associating the city with an existing state and country
            while True:
                country = input(f"Enter the country to associate with city {city}: ").strip().title()
                if country in records:
                    state = input(f"Enter the state to associate with city {city}: ").strip().title()
                    if state in records[country]:
                        if city not in records[country][state]:
                            records[country][state].append(city)
                            print(f"City {city} added under State {state}, Country {country}.")
                        else:
                            print(f"City {city} already exists under State {state}, Country {country}.")
                        break
                    else:
                        print(f"State {state} does not exist under Country {country}. Please enter a valid state.")
                else:
                    print(f"Country {country} does not exist. Please enter a valid country.")

            choice = input("Do you want to enter another city? (Y/N): ").strip().lower()
            if choice == 'n':
                print("Returning to the main menu.")
                break

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
    ''' This Function will update the Country , state, city according to user input. '''
    try:
        print("What would you like to update(Country, State, City)?")
        choice = input("Enter your choice (Country, State, City): ").strip().title()

        if choice == "Country":
            
            old_country = input("Enter the current country name: ").strip().title()
            if old_country in records:
                new_country = input(f"Enter the new name for the country {old_country}: ").strip().title()
                records[new_country] = records.pop(old_country)  
                print(f"Country {old_country} updated to {new_country}.")
            else:
                print(f"Country {old_country} not found.")


        elif choice == "State":
            
            country = input("Enter the country for the state: ").strip().title()
            if country in records:
                old_state = input("Enter the current state name: ").strip().title()
                if old_state in records[country]:
                    new_state = input(f"Enter the new name for the state {old_state}: ").strip().title()
                    records[country][new_state] = records[country].pop(old_state)  
                    print(f"State {old_state} updated to {new_state} under Country = {country}.")
                else:
                    print(f"State {old_state} not found under Country = {country}.")
            else:
                print(f"Country {country} not found.")


        elif choice == "City":
            
            country = input("Enter the country for the city: ").strip().title()
            if country in records:
                state = input("Enter the state for the city: ").strip().title()
                if state in records[country]:
                    old_city = input("Enter the current city name: ").strip().title()
                    if old_city in records[country][state]:
                        new_city = input(f"Enter the new name for the city {old_city}: ").strip().title()
                        records[country][state].remove(old_city)
                        records[country][state].append(new_city)
                        print(f"City {old_city} updated to {new_city} under Country = {country}, State = {state}.")
                    else:
                        print(f"City {old_city} not found under Country = {country}, State = {state}.")
                else:
                    print(f"State {state} not found under Country = {country}.")
            else:
                print(f"Country {country} not found.")


        else:
            print("Invalid choice. Please select 1, 2, or 3.")


    except Exception as e:
        print(f"Error occurred while updating record: {e}")

def delete_data():
    ''' This Function will delete data from records like country, state, city according to user input. '''
    try:
        print("What would you like to delete? (Country, State, City)")
        choice = input("Enter your choice (Country, State, City): ").strip().title()
        
        if choice == "Country":
            country = input("Enter the country to delete: ").strip().title()
            if country in records:
                del records[country]
                print(f"All records for Country = {country} deleted successfully.")
            else:
                print(f"Country {country} not found.")
        
        elif choice == "State":
            country = input("Enter the country for the state: ").strip().title()
            if country in records:
                state = input("Enter the state to delete: ").strip().title()
                if state in records[country]:
                    del records[country][state]
                    print(f"State {state} deleted successfully under Country = {country}.")
                else:
                    print(f"State {state} not found under Country = {country}.")
            else:
                print(f"Country {country} not found.")
        
        elif choice == "City":
            country = input("Enter the country for the city: ").strip().title()
            if country in records:
                state = input("Enter the state for the city: ").strip().title()
                if state in records[country]:
                    city = input("Enter the city to delete: ").strip().title()
                    if city in records[country][state]:
                        records[country][state].remove(city)
                        print(f"City {city} deleted successfully under Country = {country}, State = {state}.")
                    else:
                        print(f"City {city} not found under Country = {country}, State = {state}.")
                else:
                    print(f"State {state} not found under Country = {country}.")
            else:
                print(f"Country {country} not found.")
        
        else:
            print("Invalid choice. Please choose either Country, State, or City.")
    
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

