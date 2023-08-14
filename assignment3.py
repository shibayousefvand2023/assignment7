from argparse import OPTIONAL
import numbers


name = ('Welcome to the Small to Large (Shiba) arrays review')
print(name)
def biger():
    n = int(input('How many arrays do you have? enter 0 to end and any other key to continue'))
    arr = []
    for i in range(n):
        what= int(input('enter your array {i+1} ='))
        arr.append(what)
        return arr

def is_saved(list):
    n = len(list)
    for i in range(n-1):
        if list[i]>list[i+1]:
            return False
        else:
                i+=1
        return True

while True:
    if numbers == 0:
        print('good lock')
        break
    else:
        if is_saved(biger()):
            print('Your data will be stored from low to high')
        else:
            print('I am sorry. Not saved. try again')



