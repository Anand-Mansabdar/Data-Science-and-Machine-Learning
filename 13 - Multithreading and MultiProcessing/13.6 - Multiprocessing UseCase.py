# Real World Example:- Multiprocessing for CPU-bound tasks
# Scenario: Factorial Calculation
# Especially for large numbers, it involves significant computational work. Multiprocessing can be used to distribute the workload across multiple CPU cores, improving performace

import multiprocessing
import math
import sys
import time

# Increase the maximum number of digits for integer conversion
sys.set_int_max_str_digits(100000)

# Function to compute factorials of a given number
def compute_factorial(number):
  print(f'Computing Factorials of {number}')
  result = math.factorial(number)
  print(f'Factorial of {number} is {result}\n')
  return result

if __name__ == '__main__':
  numbers = [5000, 6000, 7000, 3563, 8354]
  start_time = time.time()
  
  # Creating a pool of worker processors
  with multiprocessing.Pool() as pool:
    results = pool.map(compute_factorial, numbers)
    
  end_time = time.time()
  print(f'Total time taken: {end_time - start_time} seconds')