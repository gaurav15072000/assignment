"""

print("ex.1")
n = int(input("Input a number: "))
sum = (n * (n + 1)) / 2
print("first", n ,"positive integers:", sum)
"""



"""
print("ex.2")
str1 = 'if you can dream it you can do it.'
print(str1.count("dream"))
"""



"""
print("ex.3")
def word(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

print( word('twinkle twinkle littel star , you are little star.'))
"""



"""
print("ex.4")
def mix(a, b):
  new_a = b[:2] + a[2:]
  new_b = a[:2] + b[2:]

  return new_a + ' ' + new_b
print(mix('abc', 'xyz'))
"""



"""
print(""ex.5)
a = input("Enter string: ")
if len(a)< 3:
    print(a)
elif a.endswith("ing"):
    print(a+"ly")
else:
    print(a+"ing")
"""





"""
print("ex.6")
str1 = "the lyrics are not so much poor"

str2 = str1.replace("poor","good")

print(str2)
str3 = str2.replace("not", "")

print(str3)
str1 = "not so much poor"
id1 = str1.index("not")
print(id1)
id2 = str1.index("poor")
print(id2)
print(str1[id1:id2+4])
str2 = str1.replace(str1[id1:id2+4], "good")
print(str2)
"""




"""
print('ex.7')
import math
a = math.gcd(40,60)
print(a)
"""





"""
print("ex.8")
list = [5, 6, 3, 8, 2, 1, 7, 1]
print("The original list : " + str(list))
sublist = [58, 22, 11]

res = False
for i in range(len(list) - len(sublist)):
    if list[i: i + len(sublist)] == sublist:
        res = True
        break
print("Is sublist present in list ? : " + str(res))
"""



"""
print("ex.9")
def find_len(list1):
    list1.sort()
    print(list1)
    print("Second Smallest number:", list1[1])

L = find_len(list1 = [102, 455, 200, 481, 351, 110, 588, 96, 74])
"""




"""
print("ex.10")
def unique(list1):
    unique_list = []

    for x in list1:

        if x not in unique_list:
            unique_list.append(x)
    for x in unique_list:
        print(x)


list1 = [10, 20,20,20,45, 10, 30, 40, 40]
print("the unique values from list is")
unique(list1)

"""



"""
print("ex.11")
l = [(1,2,5), (3,4,5), (8,9,5)]
print(list(zip(*l)))
"""



"""
print("ex.12")

def Convert(tup, di):
    for a, b in tup:
        di.setdefault(a, []).append(b)
    return di

tups = [("akash", 10), ("gaurav", 12), ("anand", 14),
        ("suraj", 20), ("akhil", 25), ("ashish", 30)]
dictionary = {}
print(Convert(tups, dictionary))
"""




"""
print("ex.13")
import operator
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print('Original dictionary : ',d)
sorted_d = sorted(d.items(), key=operator.itemgetter(1))
print('Dictionary in ascending order by value : ',sorted_d)
sorted_d = dict( sorted(d.items(), key=operator.itemgetter(1),reverse=True))
print('Dictionary in descending order by value : ',sorted_d)
"""



"""
print('ex.14')
di={"akash": 1000, "gaurav": 1200, "anand": 144, "suraj": 200, "akhil": 250, "ashish": 30}
a=sorted(di.values())

print(a)
print(a[5], a[4], a[3])
"""



"""
# print(ex15.)

# def fib(n):
    
#         if n==0:
#             return 0
#         elif n==1:
#             return 1
#         else:    
#             return (fib(n-2) + fib(n-1))
# n=int(input("enter a number :"))
# for n in range(0,n):    
#         print(fib(n), end = " ")
"""


"""
print("ex.16")
def CountFrequency(my_list):
    freq = {}
    for item in my_list:
        if (item in freq):
            freq[item] += 1
        else:
            freq[item] = 1

    for key, value in freq.items():
        print("% d : % d" % (key, value))

if __name__ == "__main__":
    my_list = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]

    CountFrequency(my_list)
"""




"""
print("ex.17")
import math

s = input("enter the type : odd or even ?")
n = int(input("sum of how many terms ? "))
sum = 0

for i in range(n):
  if(s == "odd"):
    sum = sum + ((12 + 20*i)/(math.factorial(1+2*i)))
  elif(s == "even"):
    sum = sum + ((2 + 20*(i+1))/math.factorial(2*(i+1)))
  else: 
    print(" odd or even? not entered properly..")

print(f"value of sum is {sum}")
"""




"""
print("ex.18")
def recur_factorial(n):
   if n == 1:
       return n
   else:
       return n*recur_factorial(n-1)
num = 5

if num < 0:
   print("Sorry")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   print("The factorial of", num, "is", recur_factorial(num))

"""




"""
print('ex.19')
def f(list):

    a=set(list)
    print(sorted(a))

f([1,1,1,2,2,2,10,4,3,7,3,4])
"""



"""
 Mini project : 
Problem Statement : Password Generator 
Make a program to generate a strong password using the input given by the user. To generate a password, 
randomly take some words from the user input and then include numbers, special characters and capital 
letters to generate the password. Also, keep a check that password length is more than 8 characters. 
Note: Include Exception handling wherever required. Also, make a ‘User’ class and store the details like user 
id, name and password of each user as a tuple.
"""


"""
print('ex.20')
import  random
lenof_password = int(input("Enetr len of password"))
if lenof_password >= 8:

    lower_case = ('a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z')
    upper_case = lower_case.upper()
    sym = ('!,@,#,$,%,^,&,*')
    digit = ('1,2,3,4,5,6,7,8,9,10')
    total = lower_case+upper_case+sym+digit
    a = random.sample(total,lenof_password)
    password = "".join(a)
    print(password)

else:
    print("Enter more then 8 char")

"""
