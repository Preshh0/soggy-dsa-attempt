#Originally written in cmd
#Interview Question 1.1
# Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
# cannot use additional data structures?
a = "hello"
for i in a:
    if a.count(i) > 1:
        print("Not unique")
    elif a.count(i) == 1:
        print("Is unique")

