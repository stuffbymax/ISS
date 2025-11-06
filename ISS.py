
# todo intead of having the functions in same code it will be divied into smaller .py files
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset once at the start
df = pd.read_csv('DgVeneto AstroPi Sensor data 2023 - data.csv')



# colors

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
RESET = "\033[0m"

# usage
#print(f"{RED}This text is red{RESET}")


# def speed():
#     #calculate the speed of ISS base on Latitude & Longitude and date_time
# def latitude_longitude():
    
# def humidity():

def Date_Time():
    # Submenu for date & time-related options.
    print("Temperature Menu")
    df_temp = pd.read_csv('DgVeneto AstroPi Sensor data 2023 - data.csv', usecols=['temperature'])
    
    while True:
        print("\nTemperature Menu:")
        print("1. Show first 10 temperature readings")
        print("2. calculate avg)")
        print("3. calculate median)")
        print("4. calculate mode)")
        print("5. calculate Range)")
        print("6. Return to Main Menu")
        print("7. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nShowing first 10 temperature readings:")
            print(df_temp.head(10))
        
        elif choice == "2":
            pass  # Placeholder for calculation

def temperature_menu():
    # Submenu for temperature-related options.
    print("Temperature Menu")
    df_temp = pd.read_csv('DgVeneto AstroPi Sensor data 2023 - data.csv', usecols=['temperature'])
    
    while True:
        print("\nTemperature Menu:")
        print("1. Show first 10 temperature readings")
        print("2. calculate avg)")
        print("3. calculate median)")
        print("4. calculate mode)")
        print("5. calculate Range)")
        print("6. Return to Main Menu")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nShowing first 10 temperature readings:")
            print(df_temp.head(10))

        elif choice == "2":
            print("calculating avarage")
            average_temperature = df['temperature'].mean()
            print(f"The average temperature is: {average_temperature}")
            plt.axhline(y=average_temperature, color='red', linestyle='--', linewidth=2,
                        label=f'Mean: {average_temperature:.2f}')
            plt.title('Temperature with average Line')
            plt.xlabel('Index')
            plt.ylabel('Temperature')
            plt.legend()
            plt.show()
            
        elif choice == "3":
            print("calculating median")
            median_temperature = df['temperature'].median()
            print(f"The median temperature is: {median_temperature}")
            plt.axhline(y=median_temperature, color='red', linestyle='--', linewidth=2,
                        label=f'Median: {median_temperature:.2f}')
            plt.title('Temperature with Median Line')
            plt.xlabel('Index')
            plt.ylabel('Temperature')
            plt.legend()
            plt.show()
            
        elif choice == "4":
            print("calculating mode")
            mode_temperature = df['temperature'].mode()
            print(f"The mode temperature is: {mode_temperature}")
            mode_value = mode_temperature.iloc[0]
            plt.axhline(y=mode_value, color='red', linestyle='--', linewidth=2,
                        label=f'Mode: {mode_value:.2f}')
            plt.title('Temperature with Mode Line')
            plt.xlabel('Index')
            plt.ylabel('Temperature')
            plt.legend()
            plt.show()
        
        elif choice == "5":
            print("calculating range")
            range_temperature = df['temperature'].max() - df['temperature'].min()
            print(f"The range temperature is: {range_temperature}")
            plt.axhline(y=range_temperature, color='red', linestyle='--', linewidth=2,
                        label=f'range: {range_temperature:.2f}')
            plt.title('Temperature with range Line')
            plt.xlabel('Index')
            plt.ylabel('Temperature')
            plt.legend()
            plt.show()
            
        elif choice == "6":
            print("Returning to Main Menu...")
            break

        elif choice == "7":
            print("Exiting the program. Goodbye!")
            exit()

        else:
            print("Invalid choice. Please try again.")


def main_menu():
    #Main menu for dataset exploration.
    while True:
        print("\nMain Menu:")
        print("1. Date & Time")
        print("2. Latitude & Longitude")
        print("3. Temperature")
        print("4. Humidity")
        print("5. callculate speed")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("You selected Date & Time (not yet implemented).")

        elif choice == "2":
            print("You selected Latitude & Longitude (not yet implemented).")

        elif choice == "3":
            print("Opening Temperature Menu...")
            temperature_menu()

        elif choice == "4":
            print("You selected Humidity (not yet implemented).")

        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


# Run the menu
if __name__ == "__main__":
    main_menu()
