# Let's try this array with some numbers.
# We will check if the number given is an Odd number or an Even number.
# Let's define the max function.
max = int(input("Enter Maximum number: "))
# Define an empty array of name odd_numbers.
odd_numbers = []
# Run the for loop to check wether the number is Odd or Even. 
for i in range(max):
  if i%2 == 1:
    odd_numbers.append(i)
# Let's print the array we got.
print("Odd Numbers: ",odd_numbers)
