input_line = input().strip()
numbers = list(map(int, input_line.split()))
odd_numbers = [num for num in numbers if num % 2 != 0]
even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers.sort(reverse=True)  
even_numbers.sort()            
result = odd_numbers + even_numbers
print(" ".join(map(str, result)))