print("Welcome to Love Calculator:")
name1 = input("what is Your Name:\n")
name2 = input("What is their Name\n")

name1 = name1.lower()
t = name1.count("t")
r = name1.count("r")
u = name1.count("u")
e = name1.count("e")
t1 = t+r+u+e
name2 = name2.lower()
t = name2.count("t")
r = name2.count("r")
u = name2.count("u")
e = name2.count("e")

t2 = t+r+u+e
n1Total = t1+t2
# # Or we can add both names like
# combinedName = name1 + name2
#  then check true in combine name
# t = combinedName.count("t") etc

name2 = name2.lower()
l = name1.count("l")
o = name1.count("o")
v = name1.count("v")
e = name1.count("e")

t3= l + o + v + e
name2 = name2.lower()
l = name2.count("l")
o = name2.count("o")
v = name2.count("v")
e = name2.count("e")

t4 = l + o + v + e
n2Total = t3 + t4
score = str(n1Total) + str(n2Total)


if int(score) <=10 or int(score) > 90:
    print(f"your Score is {score} You go togather like Coke and Mentos:")
elif int(score) >=40 and int(score) <=50:
    print(f"your Score is {score}: your All good to go")
else:
    print(f"Your Score is {score}")