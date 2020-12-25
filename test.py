# print("hellow world")
# import turtle
# wn = turtle.Screen()
# ayat = turtle.Turtle()
# ayat.forward(150)
# # ayat.color('red')
# vstr = "this is a string"
# print(vstr.upper())
# print(vstr.lower())
# print(vstr.capitalize())
# print(vstr.index('g'))
# print(vstr.replace('is', 'are'))
# print(len(vstr))
# print(vstr[0])  # find a specific charecter

#  functions on numbers
# import math
# num = -5
# print(abs(num))
# print(pow(2, 5))
# print(min(2, 5))
# print(max(2, 5))
# print(round(2.4))
# print(math.sqrt(2))
# print(math.ceil(2.7))
# print(math.floor(2.7))
# vv = input("enter something")
# print(vv)
# lists
# friends = ['ayat', 'sraa', 'amir', 'ahmed']
# nums = [1, 4, 5, 2, 3, 6, 7, 8]
# num = [1, 4, 5, 2, 3, 6, 7, 8]
# friends[2] = "mohammed"
# print(friends[1:])
# print(friends[1:2])
# friends.extend(nums)
# print(friends)
# friends.append('toto')
# print(friends)
# friends.insert(1, 'mohammed')
# print(friends)
# friends.remove('mohammed')
# print(friends)
# print(friends.count('mohammed'))
# num.sort()
# print(num)
# friends.reverse()
# print(friends)
# Loop 1-20 and check the index in each iteration
# if the number is divisible by 3 print 'Fizz'
# if the number is divisible by 5 print 'Buzz'
# if the number is divisible by 3 and 5 print 'FizzBuzz'
# Print the number otherwise
for item in range(1, 21):
    if item % 3 == 0 and item % 5 == 0:
        print('fizz')
    elif item % 5 == 0:
        print("buzz")
    elif item % 3 == 0:
        print('fizz buzz')
    else:
        print(item)
