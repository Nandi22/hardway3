people = 30
cars = 40 
trucks = 150 

if cars > people:
    print("We should take the cars." )
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide.")
    
if trucks > cars:
    print("Thats too may trucks.")
elif trucks < cars:# If the last thing is false and this is true do this 
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")
    
if people > trucks:# if there are more people than trucks do that is in the indent
    print("Alright, let's just take the trucks.")
else:# otherwise do this
    print("Fine, let's stay home then")

if not(cars > people and trucks < cars ):
    print("there are not more cars than people and not more cars than trucks, (both are not)")