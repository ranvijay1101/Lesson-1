# 01-binary-search.py
scores =[1, 3, 5, 7, 9, 11, 13, 15, 17]
input("List: " + str(scores) + " n = 9 Press Enter")
guess =  input("Max checks to find any number in this list? ")
target = int(input("Enter the number to search for: "))
input("Binary search - checks the middle, drops half each round.")
low, high = 0, len(scores) - 1
steps = 0
while low <= high:
    steps += 1
    mid = (low + high) // 2
    if scores[mid] == target:
        print(" target =", target, " found at position", mid, "checks = ", steps)
        break
    elif scores[mid] < target:
        low = mid + 1
    else:
        high = mid - 1
print(" found", target, "at position", mid + 1, "in", steps, "steps your guess:", guess, " -> 0(log n)")
input("Steps grow slowly with n. Press Enter ")
for n, s in [(9,4), (100, 7), (1000, 10)]:
    print("n =", n, "max steps = ", s, " -> 0(log n)")



#02-recursion.py
n = int(input("Enter n (try 3 or 5): "))
guess = input("How many times does the countdown call itself for n = " + str(n) + "? ")
input("Recursion - watch each call. Press Enter to run ")
def countdown(num):
    print(" call - n =" + str(num))
    if num > 0:
        countdown(num - 1)
countdown(n)
print(" calls =", n + 1, "your guess:", guess, "  -> 0(n) ")
input("Watch calls grow with n. Press Enter ")
for size in [5, 10, 100]:
    print(" n= ", size, " calls= ", size + 1, " -> 0(n)")



# 03-space-complexity.py
guess = input("At n = 1000, 0(n^2) takes how many steps? ")
input(" Watch 0(n) and 0(n^2) grow. Press Enter ")
for n in [10, 100, 1000]:
    input("n = " + str(n) + " Press Enter ")
    print(" 0(n) = ", n, " 0(n^2) = ", n * n, )
print("  your guess:", guess)
input("Full ladder at n = 1000. Press Enter ")
print(" 0(1)=1 0(log n)=10 0(n)=1000 0(n^2)=1,000,000 ")