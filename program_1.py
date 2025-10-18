# Program #1: Rainfall
# Design a program that lets the user enter the total rainfall for each of 12 months into a list.
# The program should calculate and display the total rainfall for the year, 
# the average monthly rainfall, # and the months with the highest and lowest amounts.

##
# Program 1: Rainfall
# Grant Dresser 
# 10/17/2025
##

MONTH_NAMES = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

def get_monthly_rainfall() -> list[float]:
    data = []
    for i, name in enumerate(MONTH_NAMES, start=1):
        while True:
            try:
                val = float(input(f"Enter rainfall for {name} (inches): "))
                if val < 0:
                    print("Rainfall can't be negative. Try again.")
                    continue
                data.append(val)
                break
            except ValueError:
                print("Please enter a valid number.")
    return data

def main():
    rain = get_monthly_rainfall()
    total = sum(rain)
    avg = total / 12
    hi = max(rain); lo = min(rain)
    hi_month = MONTH_NAMES[rain.index(hi)]
    lo_month = MONTH_NAMES[rain.index(lo)]

    print("\n--- Rainfall Report ---")
    print(f"Total rainfall: {total:.2f} inches")
    print(f"Average monthly: {avg:.2f} inches")
    print(f"Highest: {hi:.2f} inches in {hi_month}")
    print(f"Lowest : {lo:.2f} inches in {lo_month}")

if __name__ == "__main__":
    main()
