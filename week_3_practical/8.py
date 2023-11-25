table_number = int(input("Enter a number for the times table: "))

if table_number < 0:
 
    for i in range(12, -1, -1):
        result = i * abs(table_number)
        print(f"{i} x {abs(table_number)} = {result}")
elif table_number == 0:
    print("Error: Please enter a non-zero number for the times table.")
else:

    for i in range(13):
        result = i * table_number
        print(f"{i} x {table_number} = {result}")
