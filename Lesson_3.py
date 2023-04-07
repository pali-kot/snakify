# Solutions of a newbie with a week of practice xD
# 
"""
1. 
Minimum of two numbers
Statement
Given two integers, print the smaller value.
"""
# x = int(input())
# y = int(input())

# if x > y:
#   print(y)
# else:
#   print(x)

"""
2.
Sign function
Statement
For the given integer X print 1 if it's positive, -1 if it's negative, or 0 if it's equal to zero.
Try to use the cascade if-elif-else for it.
"""

# x= int(input())

# if x > 0:
#     print(1)
# elif x < 0:
#     print(-1)
# else:
#     print(0)

"""
3.
Minimum of three numbers
Statement
Given three integers, print the smallest value.
"""

# a = int(input())
# b = int(input())
# c = int(input())

# if a < b and a < c:
#     print(a)
# elif b < a and b < c:
#     print(b)
# else:
#     print(c)

"""
4. 
Equal numbers
Statement
Given three integers, determine how many of them are equal to each other. The program must print one of these numbers: 3 (if all are the same), 2 (if two of them are equal to each other and the third is different) or 0 (if all numbers are different).
"""
# Works but messy
# a = int(input())
# b = int(input())
# c = int(input())

# if a == b and b == c:
#     print(3)
# elif a == b and b != c:
#     print(2)
# elif a != b and b == c:
#     print(2)
# elif a == c and b != a:
#     print(2)
# else:
#      print(0)

# should be

# a = int(input())
# b = int(input())
# c = int(input())

# if a == b == c:
#     print(3)
# elif a == b or b == c or c ==a:
#     print(2)
# else:
#     print(0)

"""
5.
Rook move
Statement
Chess rook moves horizontally or vertically. Given two different cells of the chessboard, determine whether a rook can go from the first cell to the second in one move.
The program receives the input of four numbers from 1 to 8, each specifying the x1umn and y1 number, first two - for the first cell, and then the last two - for the second cell. The program should output YES if a rook can go from the first cell to the second in one move, or NO otherwise.
"""

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())

# if a == c or b == d:
#     print("YES")
# else:
#     print("NO")

"""
6.
Chess board - same x1or
Statement
Given two cells of a chessboard. If they are painted in one x1or, print the word YES, and if in a different x1or - NO.
The program receives the input of four numbers from 1 to 8, each specifying the x1umn and y1 number, first two - for the first cell, and then the last two - for the second cell.
"""

# x1 = int(input())
# x2 = int(input())
# y1 = int(input())
# y2 = int(input())

    
# if (x1 + x2) % 2 == 0 and (y1 + y2) % 2 == 0:
#     print("YES")
# elif (x1 + x2) % 2 != 0 and (y1 + y2) % 2 != 0:
#     print("YES")
# else:
#     print("NO")

"""
7.
King move
Statement
Chess king moves horizontally, vertically or diagonally to any adjacent cell. Given two different cells of the chessboard, determine whether a king can go from the first cell to the second in one move.
The program receives the input of four numbers from 1 to 8, each specifying the x1umn and y1 number, first two - for the first cell, and then the last two - for the second cell. The program should output YES if a king can go from the first cell to the second in one move, or NO otherwise.
"""
# ------
# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())

# if abs(x2 - x1) <= 1 and abs(y2 - y1) <= 1:
# # if (a == c or (a + 1) == c or (a - 1) == c) and (b == d or (b - 1) == d or (b + 1) == d):
#     print("YES")
# else:
#     print("NO")

"""
8.
In chess, the bishop moves diagonally, any number of squares. Given two different squares of the chessboard, determine whether a bishop can go from the first to the second in one move.
The program receives as input four numbers from 1 to 8, specifying the x1umn and y1 numbers of the starting square and the x1umn and y1 numbers of the ending square. The program should output YES if a Bishop can go from the first square to the second in one move, or NO otherwise.
"""

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())

# if abs(a - b) == abs(c - d) or abs(a + b) == abs(c + d):
#     print("YES")
# else:
#     print("NO")

# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())

# if abs(x1 - x2) == abs(y1 - y2):
#   print ("YES")
# else:
#   print ("NO")

"""
9.
Queen move
Statement
Chess queen moves horizontally, vertically or diagonally to any number of cells. Given two different cells of the chessboard, determine whether a queen can go from the first cell to the second in one move.
The program receives the input of four numbers from 1 to 8, each specifying the x1umn and y1 number, first two - for the first cell, and then the last two - for the second cell. The program should output YES if a queen can go from the first cell to the second in one move, or NO otherwise.
"""
# If u did Rook and Bishop this should be easy
# Just combine both ¯\_(ツ)_/¯

# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())

# if x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
#     print("YES")
# else:
#     print("NO")

"""
10.
Knight move
Statement
Chess knight moves like the letter L. It can move two cells horizontally and one cell vertically, or two cells vertically and one cells horizontally. Given two different cells of the chessboard, determine whether a knight can go from the first cell to the second in one move.
The program receives the input of four numbers from 1 to 8, each specifying the x1umn and y1 number, first two - for the first cell, and then the last two - for the second cell. The program should output YES if a knight can go from the first cell to the second in one move, or NO otherwise.
"""

# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())

# if abs(x2 - x1) == 1 and abs(y2 - y1) == 2:
#     print("YES")
# elif abs(x2 - x1) == 2 and abs(y2 - y1) == 1:
#     print("YES")
# else:
#     print("NO")

"""
11
Chocolate bar
Statement
Chocolate bar has the form of a rectangle divided into n x m portions. Chocolate bar can be split into two rectangular parts by breaking it along a selected straight line on its pattern. Determine whether it is possible to split it so that one of the parts will have exactly k squares.
The program reads three integers: n, m, and k. It should print YES or NO.
"""
# n = int(input())
# m = int(input())
# k = int(input())

# if k > (n * m):
#   print("NO")
# elif k % n == 0 or k % m == 0:
#   print("YES")
# else:
#   print("NO")

"""
MODEL SOLUTION FROM WEB
is suck xD

n = int(input())
m = int(input())
k = int(input())
if k < n * m and ((k % n == 0) or (k % m == 0)):
    print('YES')
else:
    print('NO')
"""

"""
12.
Leap year
Statement
Given the year number. You need to check if this year is a leap year. If it is, print LEAP, otherwise print COMMON.
The rules in Gregorian calendar are as follows:

a year is a leap year if its number is exactly divisible by 4 and is not exactly divisible by 100
a year is always a leap year if its number is exactly divisible by 400
Warning. The words LEAP and COMMON should be printed all caps.
"""

year = int(input())

if year % 400 == 0:
    print("LEAP")
elif year % 4 == 0 and year % 100 > 0:
    print("LEAP")
else:
    print("COMMON")
    
 
