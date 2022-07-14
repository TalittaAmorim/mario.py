def main():
  while(True):
    n = int(input("N: "))
    if n > 0 and n <= 8:
         break
  draw(n)
  
def draw(n):
    for i in range(n):
       print((n-1-i) * " ", end="")
       print((i+1) * "#")  
      
main()     
