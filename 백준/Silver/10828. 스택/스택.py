from collections import deque
import sys
input = sys.stdin.readline

stack = deque()
n = int(input())

for _ in range(n):
  command = input().rstrip()
  if command[:4] == 'push':
    stack.appendleft(int(command.split()[1]))
  elif command == 'pop':
    print(-1 if len(stack)==0 else stack.popleft())
  elif command == 'size':
    print(len(stack))
  elif command == 'empty':
    print(1 if len(stack) == 0 else 0)
  elif command == 'top':
    print(-1 if len(stack) == 0 else stack[0])