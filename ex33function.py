
def ex33(i,a):
    numbers = [1,2,3,4]
    while i < 6:
        print(f"At the top i is {i}")
        numbers.append(i)
    
        i = i + a
        print("Numbers now: ", numbers) 
        print(f"At the bottom i is {i}")
     

    print("The numbers: ")

    for num in range(1,10):
        print (num)
    


ex33(5,6)
