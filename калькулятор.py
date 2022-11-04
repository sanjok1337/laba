while True:
  x = float(input('First number: '))
  y = float(input('Second number: '))
  operation = input('Operation: ')

  result = None

  if operation == '+':
    result = x + y
  elif operation == '-':
    result = x - y
  elif operation == '*':
    result = x * y
  elif operation == '/':
    if y != 0 and x != 0:
      result = x / y
    else:
      print('Unsupported')
  else:
    print('Unsupported operation')

  if result is not None:
    print('Result', result)
