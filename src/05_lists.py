# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# YOUR CODE HERE
print()
print("start:", x)
x.append(4)
print("add 4:", x)
print()

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE
print("start:", x)
x.extend(y)
print("add y items:", x)
print()

# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE
print("start:", x)
x.remove(8)
print("Remove 8:", x)
print()

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE
print("start:", x)
x.insert(5, 99)
print("Added 99 to Position 6:", x)
print()

# Print the length of list x
# YOUR CODE HERE
print("x's length is:", len(x))
print()

# Print all the values in x multiplied by 1000
# YOUR CODE HERE
print("All values in x multiplied by 1000")
for i in x:
    print(f"{i} X 1000 = {i * 1000}")
