records = {}

def add_data():
   
    try:
        country = input("Enter your country:")
        state = input("Enter your state:")
        city = input("Enter your city:")
     
        if country in records:
      	    print(f"--------------Record for {country} is already exists--------------")
        else:
      	    records[country] = {"state": state, "city": city}
      	    print(f"Records for {country} added.")
   
    except Exception as e:
        print(f"Error occured : {e}")
        
def show_data():
    try:
        if not records:
            print("--------------Country does not exist--------------")
        else:
            for country,item in records.items():
              print(f"Country: {country} | State:{item['state']} | city:{item['city']}")              
    
    except Exception as e:
        print(f"Error occured : {e}")

def update_data():
    try:
        country = input("Enter the country:")
        if country in records:
           state = input("Enter state:")
           city = input("Enter city:")
           
           records[country] = {"state":state, "city":city }
           
        else:
           print("Country does not exist")
           
           
    except Exception as e:
        print(f"Error occured : {e}")

def delete_data():
    pass

def main():
    while True:
        try:
            print("1.Enter Country,state,city")
            print("2.Show records")
            print("3.Update records")
            print("4.Delete records")
            print("5.Quit")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                add_data()
            elif choice == 2:
                show_data()
            elif choice == 3:
                update_data()
            elif choice == 4:
                delete_data()
            elif choice == 5:
                print("Exit")
                break
            else:
               print("Invalid Choice")
        except ValueError:
            print("Invalid Input")
main()	
