while True:
  string = input()
  if string == '.':
    break
  stack = []
  for i in string:
    if i == '(' or i == '[':
      stack.append(i)
    elif i == ')':
      if len(stack) != 0 and stack[-1] == '(':
        stack.pop()
      else:
        stack.append(i)
    elif i == ']':
      if len(stack) != 0 and stack[-1] == '[':
        stack.pop()
      else:
        stack.append(i)        
    else:
      pass

  if len(stack) == 0:
    print('yes')
  else:
    print('no')