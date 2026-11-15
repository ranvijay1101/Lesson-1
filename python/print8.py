n = 10
guess = int(input("Double Loop at n =  10 checks n x n pairs. How many?"))
input("Formula: one calculation, done. Press Enter to run ")
steps = 1
print(" steps = ", steps, " -> 0(1) constant time -> steps never changes")
steps = 0
for i in range(n):
    for j in range(n):
        steps += 1
print(" steps = ", steps, " -> 0(n) linear time -> steps grows with n")
input("Double Loop at n =  10 checks n x n pairs. How many? Press Enter to run ")
steps = 0
for i in range(n):
    for j in range(n):
        steps += 1
print(" steps = ", steps, " -> 0(n^2) quadratic time -> steps grows with n^2")
input("Two more notatations. Press Enter to run ")
print(" Big Omega 0 -> best case lower bound")
print(" Big Theta 0 -> exact bound (worst = best)")



#02-best-average-worst.py
scores =[3, 7, 2, 9, 4, 1, 8, 5, 6]
input("List: " + str(scores) + " n = 9 Linear search - checks left to right. Press Enter to run")
target = int(input("Enter a number to search for: "))
input("Searching for " + str(target) + " Press Enter to run")
steps = 0
for score in scores:
    steps += 1
    if score == target:
        break
print(" target =", target, " found at position", steps, "checks = ", steps)
input("compare with best and worst case. Press Enter to run")
mid = len(scores) // 2
print(" Best: 1 check -> 0(1) Average:", mid, "check -> 0(n) Worst: 9 checks -> 0(n) Yours:", steps)
input("All three cases. Press Enter to run")
print(" Best 0(1) Average 0(n) Worst 0(n) -> Big-0 = worst case = 0(n).")


#03-notation.py
n = int(input("Enter any n (try 5, 10, or 50): "))

input("One loop — runs once per item. Press Enter to run ")

for i in range(n):

pass

print(" n =", n, " steps =", n, " -> O(n) linear time")

input("Two nested loops — runs n x n times. Press Enter to run ")

for i in range(n):

for j in range(n):

pass

print(" n =", n, " steps =", n * n, " -> O(n^2) quadratic time")

input("Rule: count the loops. Press Enter ")

print(" 0 loops -> O(1) 1 loop -> O(n) 2 nested -> O(n^2)")