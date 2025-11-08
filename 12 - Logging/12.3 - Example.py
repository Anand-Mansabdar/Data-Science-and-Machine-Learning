import logging

# Logging settings
logging.basicConfig(
  level=logging.DEBUG,
  format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
  datefmt='%Y-%M-%d %H:%M:%S',
  handlers= [
    logging.FileHandler('app1.log'),
    logging.StreamHandler()
  ]
)

logger = logging.getLogger("ArithemeticApp")

def add(a, b):
  result = a+b
  logger.debug(f'Adding {a} and {b}: {result}')
  return result

def subtract(a, b):
  result = a-b
  logger.debug(f'Adding {a} and {b}: {result}')
  return result

def multiply(a, b):
  result = a*b
  logger.debug(f'Adding {a} and {b}: {result}')
  return result

def divide(a, b):
  try:
    result = a/b
    logger.debug(f'Adding {a} and {b}: {result}')
    return result
  except ZeroDivisionError:
    logger.error('Division by zero error')
    return None
  
add(100, 200)
subtract(1000, 456)
multiply(3, 4)
divide(100, 10)

divide(1, 0)