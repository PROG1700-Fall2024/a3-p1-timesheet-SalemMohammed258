#Program 1 – Timesheet
#Description:   Design and write a program that accepts the number of hours worked on 
#               each of five work days from the user, then displays different 
#               information calculated about those entries as output. 

#Student #:     
#Student Name:  


    # YOUR CODE STARTS HERE, each line must be indented (one tab)
def collect_hours():
    """Prompt the user to input hours worked for five days."""
    hours = []
    for i in range(1, 6):
        while True:
            try:
                hours_worked = float(input(f"Enter hours worked for day {i}: "))
                if hours_worked < 0:
                    print("Hours cannot be negative. Please try again.")
                else:
                    hours.append(hours_worked)
                    break
            except ValueError:
                print("Invalid input. Please enter a number.")
    return hours

def get_max_hours(days):
    """Find the day(s) with the most hours worked."""
    max_hours = max(days)
    max_days = [i + 1 for i, h in enumerate(days) if h == max_hours]
    return max_hours, max_days

def calculate_total_and_average(days):
    """Calculate the total and average hours worked."""
    total_hours = sum(days)
    average_hours = total_hours / len(days)
    return total_hours, average_hours

def find_insufficient_days(days):
    """Identify days with less than 7 hours worked."""
    insufficient_days = [i + 1 for i, h in enumerate(days) if h < 7]
    return insufficient_days

def main():
    # Step 1: Collect hours worked
    hours = collect_hours()

    # Step 2: Find the day(s) with the most hours
    max_hours, max_days = get_max_hours(hours)
    print("\nThe day(s) with the most hours worked:")
    for day in max_days:
        print(f"Day {day}: {max_hours} hours")

    # Step 3: Calculate total and average hours
    total_hours, average_hours = calculate_total_and_average(hours)
    print(f"\nTotal hours worked: {total_hours}")
    print(f"Average hours worked per day: {average_hours:.2f}")

    # Step 4: Display insufficient days
    insufficient_days = find_insufficient_days(hours)
    if insufficient_days:
        print("\nDay(s) with insufficient hours (<7):")
        for day in insufficient_days:
            print(f"Day {day}")
    else:
        print("\nNo days with insufficient hours (<7).")

if __name__ == "__main__":
    main







    # YOUR CODE ENDS HERE

main()