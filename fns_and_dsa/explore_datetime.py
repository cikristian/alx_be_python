from datetime import datetime, timedelta

def display_current_datetime():
    # Get current date and time
    current_date = datetime.now()
    # Format and print it
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))
    return current_date

def calculate_future_date(current_date):
    try:
        # Prompt user for number of days
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        # Calculate future date
        future_date = current_date + timedelta(days=days_to_add)
        # Print result
        print("Future date:", future_date.strftime("%Y-%m-%d"))
    except ValueError:
        print("Please enter a valid integer for the number of days.")

# Main logic
if __name__ == "__main__":
    current = display_current_datetime()
    calculate_future_date(current)
