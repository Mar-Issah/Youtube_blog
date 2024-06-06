from datetime import datetime

# Get the current date and time
current_datetime = datetime.now()
print(current_datetime)

# Format the date and time
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

# Print the formatted date and time
print("Current date and time:", formatted_datetime)