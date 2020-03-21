import time

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None # BinarySearchTree
        self.right = None # BinarySearchTree 

    # Insert the given value into the tree
    def insert(self, value):
        # compare value to the current node

        if value < self.value:
            if self.left == None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        if value >= self.value:
            if self.right == None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # compare value to the current node value
        # if smaller, go left 
        # if bigger, go right
        # if equal, return True!

        # if smaller, but we cant go left, return false
        # if bigger, but we cant go right, return false
        contained = False

        if target == self.value:
            contained = True
            return contained
        if target < self.value and self.left:
            contained = self.left.contains(target)
        if target > self.value and self.right:
            contained = self.right.contains(target)

        return contained

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure
BSTNames = BinarySearchTree("N")
# Replace the nested for loops below with your improvements
for name_1 in names_1:
    BSTNames.insert(name_1)

for name_2 in names_2:
    if BSTNames.contains(name_2):
        duplicates.append(name_2)
# for name_2 in names_2:
#     if name_1 == name_2:
#         duplicates.append(name_1)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
