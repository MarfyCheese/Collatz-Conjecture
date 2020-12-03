def collat(n):
  collatz = {
  "2": [2,1]
  }
  for i in range(3,n+1):
    list = [str(i)]
    collatz[str(i)] = list
    number = i
    while number != 1:
      if number % 2 == 1:
        number = (number * 3) + 1
        collatz[str(i)].append(number)
        for c in range(3,n+1):
          if number == c:
            collatz[str(i)].append(collatz[str(c)])
      else:
        number = number // 2
        collatz[str(i)].append(number)
        for c in range(3,n+1):
          if number == c:
            collatz[str(i)].append(collatz[str(c)])
  return collatz


for n in range(2,int(input("please enter a number above 2\n"))):
  collatz = collat(n)
  print(collatz[str(n)])