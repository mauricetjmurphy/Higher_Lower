from os import system, name
import random
from game_data import data
from art import logo, vs

print(logo)
print("Welcome to higher or lower\n")

# Create a clear screen function
def clear(): 
    # for mac and linux(here, os.name is 'posix') 
    _ = system('clear') 

# Pick a random object from the data list
def Random_Pick():
    rand_obj = data[random.randint(0, len(data)-1)]
    return rand_obj

# Check which has more followers
def calc_followers():
    if obj_a.get('follower_count') > obj_b.get('follower_count'):
        return 'a'
    else:
        return 'b'

# Show the details of the object
def Show_object(obj, l):
    print(f"Compare {l}: {obj.get('name')}, a {obj.get('description')}, from {obj.get('country')}")

# Check if the object are the same, if they are, chose another one
def Check_Same(a, b, obj):
    while True:
            if a.get('name') == b.get('name'):
                obj = Random_Pick()
            else:
                break

obj_a = None
obj_b = None
compar_answer = None
score = 0

ans1 = input("Type start to begin:").lower()
if ans1 == 'start':
    clear()

print(logo)
obj_a = Random_Pick()
Show_object(obj_a, 'a')
print(vs)
obj_b = Random_Pick()
Show_object(obj_b, 'b')

while True:
    compar_answer = calc_followers()
    ans2 = input("Who has more followers? Type 'A' or 'B':").lower()
    if ans2 == compar_answer and ans2 == 'a':
        clear()
        Show_object(obj_a, 'a')
        print(vs)
        obj_b = Random_Pick()
        Check_Same(obj_b, obj_a, obj_b)
        Show_object(obj_b, 'b')
        score += 1
    elif ans2 == compar_answer and ans2 == 'b':
        clear()
        obj_a = obj_b
        Show_object(obj_a, 'a')
        print(vs)
        obj_b = Random_Pick()
        Check_Same(obj_b, obj_a, obj_b)
        Show_object(obj_b, 'b')
        score += 1
    else:
        print(f"Wrong, you got {score} right answers")
        break