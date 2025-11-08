
# Multiprocessing allows us to run multiple tasks in parallel
# Used for CPU bound tasks such as mathematical computation and data processing
# Parallel execution:- Multiple cores of the CPU


import multiprocessing
import time

def square_numbers():
  for i in range(1,6):
    time.sleep(1)
    print(f'Square: {i*i}')
    
def cube_numbers():
  for i in range(1,6):
    time.sleep(1.5)
    print(f'Cube: {i**3}')
  
if __name__ == '__main__':
  # Creating 2 processes
  p1 = multiprocessing.Process(target=square_numbers)
  p2 = multiprocessing.Process(target=cube_numbers)

  t = time.time()
  print(t)
  # Start the process
  p1.start()
  p2.start()

  # Wait for the process to complete
  p1.join()
  p2.join()

  # 
  finished_time = time.time() - t
  print(finished_time)
  