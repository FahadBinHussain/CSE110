# Get user input for range
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

# Initialize variables
prime_count = 0
perfect_count = 0
prime_numbers = ""
perfect_numbers = ""

# Count prime and perfect numbers between range
for i in range(start, end+1):
    # Check if number is prime
    is_prime = True
    if i < 2:
        is_prime = False
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        prime_count += 1
        prime_numbers += str(i) + ", "

    # Check if number is perfect
    divisors_sum = 0
    for k in range(1, i):
        if i % k == 0:
            divisors_sum += k
    if divisors_sum == i:
        perfect_count += 1
        perfect_numbers += str(i) + ", "

# Remove the extra comma and space at the end of the strings
if prime_numbers:
    prime_numbers = prime_numbers[:-2]
if perfect_numbers:
    perfect_numbers = perfect_numbers[:-2]

# Print results
print(f"Between {start} and {end},")
if prime_count > 1:
  print("Found", prime_count, "prime numbers")
else:
  print("Found", prime_count, "prime number")
if perfect_count > 1:
  print("Found", perfect_count, "perfect numbers")
else:
  print("Found", perfect_count, "perfect number")

if prime_count > 0:
  if prime_count > 1:
    print("Prime numbers:", prime_numbers)
  else:
    print("Prime number:", prime_numbers)
if perfect_count > 0:
  if perfect_count > 1:
    print("Perfect numbers:", perfect_numbers)
  else:
    print("Perfect number:", perfect_numbers)
