
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

Modify deliverable.py so that it takes a number from the user and prints it (the number) if it isn’t divisible by 3 or 5. For multiples of 3 print 'fizz' instead. For multiples of 5 print 'buzz' instead.
For multiples of 3 and 5 print 'fizzbuzz'.

#!/usr/bin/env python3
num = float(input('Enter any number:\n'))
if ( num % 5 == 0 and num % 3 == 0):
    print('fizzbuzz')
elif (num % 5 == 0):
    print('buzz')
elif (num % 3 == 0):
    print('fizz')
else:
    print(num)
