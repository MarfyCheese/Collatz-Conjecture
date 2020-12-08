def collat(n):
  collatz = {
  2: [2,1]
  }
  for i in range(3,n+1):
    list = [i]
    collatz[i] = list
    number = i
    while number != 1:
      if number % 2 == 1:
        number = (number * 3) + 1
        if number in collatz:
          collatz[i] += collatz[number]
          number = 1
        else:
          collatz[i].append(number)
      else:
        number = number // 2
        if number in collatz:
          collatz[i] += collatz[number]
          number = 1
        else:
          collatz[i].append(number)
  return collatz

def isPowerOfTwo(n): 
    while (n != 1): 
            if (n % 2 != 0): 
                return False
            n = n // 2     
    return True

def main():
  limit = int(input("please enter a number above 2\n"))
  collatz = collat(limit)

  long = 3
  short = 3
  average = 0

  for n in range(2,limit+1):
    if len(collatz[n]) > len(collatz[long]):
      long  = n
  print("out of 2 to the number you've given,",long,"has the longest collatz chain, the full chain is ", collatz[long],"the chain is",len(collatz[long]),"numbers long \n")

    

  for n in range(2,limit+1):
    if isPowerOfTwo(n) == False:
      if len(collatz[n]) < len(collatz[short]):
        short  = n
  print("out of 2 to the number you've given,",short,"has the shortest collatz chain that isnt a power of 2, the full chain is ", collatz[short],"the chain is",len(collatz[short]),"numbers long \n")

  for n in range(2,limit+1):
    average += len(collatz[n])
  average = average / limit
  print("the average length of a collatz chain from 2 -",limit,"is",average,"numbers")

main()