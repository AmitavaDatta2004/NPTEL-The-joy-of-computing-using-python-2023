M = int(input())
N = int(input())

if M < N:
    print(M, end="")
else:
  while M >= N:
        M = M - N
  print(M , end="")
