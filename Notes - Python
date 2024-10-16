
Run the script:
python3 code.py


To get input:
usrinput = input('Type something:\n')



Methods:
#Alternative way to print with formatting options:
.format
print('{} {}!'.format('Howdy','Neighbor'))
#prints Howdy Neighbor!
.append
mylist = [ 1 , 2 , 3 ]
mylist.append(4)
#mylist now has 1,2,3, and 4
.join
joinedlist = ':'.join(mylist)
#joinedlist is now a string equal to "1:2:3:4"
.split
word = "POTATO!!"
word.split('O')
#returns ['P', 'TAT', '!!']

Modify deliverable.py and implement `guess_number` so that it repeatedly asks the user for a number between 0 and 100 inclusive. If the user correctly guesses the value of the given argument `n`, print 'WIN' and return. Otherwise indicate whether the guess was too high or too low. Test the deliverable manually or run `python3 check.py` to run the supplied unit tests.
Modify deliverable.py and implement `guess_number` so that it repeatedly asks the user for a number between 0 and 100 inclusive. If the user correctly guesses the value of the given argument `n`, print "WIN" and exit out of the loop. Otherwise indicate whether the guess was "too high" or "too low". Test the deliverable manually or run `python3 check.py` to run the supplied unit tests.

#!/usr/bin/env python3
import random
from collections import deque

if __name__ == '__main__':
    pass

n = random(0,100)

def guess_number(n):
    pass
    x = 200
    while (x != n):
        x = int(input('Enter a number: '))
        if (x > 100 or x < 0):
            print('Out of range! Must be within 0-100.')
            continue
        elif (x < n):
            print('Too low!')
            continue
        elif (x > n):
            print('Too high!')
            continue
        elif (x == n):
            print('You got it!')
            break
        else:
            print('Please input a number between 0-100.')

guess_number(n)

