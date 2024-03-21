def calculate_from_npi(expression):
  stack = []
  operators = {'+': lambda x, y: x + y,
                '-': lambda x, y: x - y,
                '*': lambda x, y: x * y,
                '/': lambda x, y: x / y}

  for item in expression.split():
      if item.isdigit() or (item[0] == '-' and item[1:].isdigit()):
          stack.append(float(item))
      elif item in operators:
          if len(stack) < 2:
              raise ValueError(f"Insufficient numbers for operator [{item}]")
          nb2 = stack.pop()
          nb1 = stack.pop()
          result = operators[item](nb1, nb2)
          stack.append(result)

      else:
          raise ValueError(f"Invalid item: {item}")

  if len(stack) != 1:
      raise ValueError("Invalid expression")

  return stack.pop()
