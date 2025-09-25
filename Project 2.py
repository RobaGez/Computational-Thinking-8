funny_points = 0
unfunny_points = 0


answer = input("in a unfunny situation would u A laugh or B stay serious?)")
if answer == "A":
    funny_points += 1
elif answer == "B":
    unfunny_points += 1
answer = input("which joke is funnier, A 67 or B 41") 
if answer == "A":
    unfunny_points += 1
elif answer == "B":
    funny_points += 1
answer = input("is your laugh infectious?")
if answer == "Yes":
    funny_points += 1
elif answer == "No":
    unfunny_points += 1
answer = input("do you laugh at yourself?")
if answer == "Yes":
    funny_points += 1
elif answer == "No":
    unfunny_points += 1
answer = input("can you read a room?")
if answer == "Yes":
    funny_points += 1
elif answer == "No":
    unfunny_points += 1
print(f"funny points = {funny_points}")
print(f"unfunny points = {unfunny_points}")

if funny_points > unfunny_points:
    print("your very funny")
elif unfunny_points > funny_points:
    print("your not very funny")
if answer == unfunny_points and funny_points > 3 
    print(" you are REALLY funny!")
if answer == "a" or answer == "b":
    funny_points +=1