# Program #3: US_Populationif
def main():
    # Have the user input (using a loop) various information that contains three pieces of data: 
    # year, name of state, and population.  
    # Store all of this information in a list of lists.  For example it might be stored like this:
    
    # [[2010, "Maine", 1987435], [2010,"Minnesota",6873202], [2011, "Iowa", 3421988]]
    all_entered_values = []

    print("Enter state data (year, state name, population).")
    print("Type 'done' when you are finished.\n")

    while True:
        year_input = input("Enter year (or 'done' to stop): ")
        if year_input.lower() == "done":
            break
        try:
            year = int(year_input)
            state = input("Enter state name: ")
            population = int(input("Enter population: "))
            all_entered_values.append([year, state, population])
        except ValueError:
            print("Invalid input. Please try again.\n")

    print("\nYou entered the following data:")
    for entry in all_entered_values:
        print(entry)

    try:
        year_to_sum = int(input("\nEnter a year to total the population for: "))
        sum_population_for_year(all_entered_values, year_to_sum)
    except ValueError:
        print("Invalid year entered.")

def sum_population_for_year(all_entered_values, year_to_sum):

    total_population = 0
    for entry in all_entered_values:
        year, state, population = entry
        if year == year_to_sum:
            total_population += population

   
    print(f"\nTotal population for {year_to_sum}: {total_population:,}") 
    
    # The program will add the populations from all states in the list of list for that year only.
    # Pass the list and year to the sum_population_for_year

def sum_population_for_year(all_entered_values, year_to_sum):
    pass


# Call the main function.

if __name__ == '__main__':
    main()