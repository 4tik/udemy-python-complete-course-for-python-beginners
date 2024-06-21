#  Python Array Implementation
my_array = [12,45,66,87,90,23] #define and declear an array
print(f"all array values : {my_array}")

# access array elements
print(f"index [1] : {my_array[1]}")
print(f"index [3] : {my_array[3]}")

print(f"index [-2] : {my_array[-2]}") # negative index
print(f"index [-3] : {my_array[-3]}") # negative index

colors = ["violet", "indigo", "blue", "green", "yellow", "orange"]
print(f"colors : {colors}")
print(f"lenght of array : {len(colors)}")

colors.append("red") #append new element
print(f"colors after append: {colors}")
print(f"lenght after append : {len(colors)}")

# remove element from array
del colors[4]        # remove element using index
colors.remove("red") # remove element using value
colors.pop(3)        # remove element using index
print(f"colors after delete : {colors}")

# modify array
colors[3]="red"  # using index
colors[-1]="orange"
print(f"colors : {colors}")

# concatenating two array using plus(+) operator
array_a = [1,3,5]
array_b = [2,4,6]
print(f"concatenating : {array_a+array_b}")

# repating elements an array
repeat_array = ["a"]
repeat_array = repeat_array*4
print(f"repeating array : {repeat_array}")

# Slicing an array
print(f"[1:3] : {colors[1:3]}")

# multidimenional array
mult_array = [
    [1,2],
    [3,4],
    [5,6],
    [7,8]
]
print(f"multidimenional array : {mult_array}")
print(f"[1] : {mult_array[1]}")
print(f"[2][1] : {mult_array[2][1]}")