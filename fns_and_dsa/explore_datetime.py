from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    
    formatted_datetime = current_date.strftime("%Y-%m-%d %H:%M:%S")
    
    print(f"Current Date and Time: {formatted_datetime}")

def calculate_future_date(days_to_add):
    today = datetime.now()
    
    future_date = today + timedelta(days=days_to_add)
    
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    
    print(f"The date in {days_to_add} days will be: {formatted_future_date}")

if __name__ == "__main__":
    display_current_datetime()
    
    try:
        num_days = int(input("\nEnter the number of days to add to the current date: "))
        
        calculate_future_date(num_days)
    except ValueError:
        print("Invalid input. Please enter a whole number.")