# Taking input in the format: Name, mark1, mark2, mark3
user_input = input("Enter the name first and marks separated by comma (e.g., Raj, 80, 70, 90): ")

# Splitting the string by comma and stripping extra whitespace
data = [item.strip() for item in user_input.split(',')]

# Basic validation to ensure we have a name and 3 marks
if len(data) == 4:
    name = data[0]
    # Converting the marks from strings to integers
    marks = [int(m) for m in data[1:]]
    
    total = sum(marks)
    percentage = (total / 300) * 100

    if percentage >= 75:
        grade = 'A'
    elif percentage >= 60:
        grade = 'B'
    elif percentage >= 40:
        grade = 'C'
    else:
        grade = 'F'

    # Output Results
    print(f"\n{name}")
    print(f"Total: {total}/300")
    print(f"Percentage: {percentage:.1f}%")
    print(f"Grade: {grade}")
else:
    print("Error: Please provide exactly 1 name and 3 marks.")