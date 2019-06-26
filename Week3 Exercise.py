# Exercise 1....

import numpy as np

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(arr)
arr_replace = np.where(arr % 2 == 1, -1, arr)
print(arr_replace)



# Exercise NO 2
import numpy as np
arr = np.arange(10)
print(arr)
new_array = np.reshape(arr, (-1, 5))
print(new_array)

# Exercise 3
import numpy as np
arr = np.array([1,2,3])
print("Normal Array")
print (arr)
print("Desired Array")
np.r_[np.repeat(arr, 3), np.tile(arr, 3)]

# Exercise 4
import numpy as np
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
# To get the common elements among both the array
np.intersect1d(a,b)
# Exercise 5
import numpy as np
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
# Gives the index where it matches index start with 0 1..."
np.where(a == b)

# Exercise 6
import numpy as np
# Random Number between 5 to 10 with the size 5 rows 3 column
random_array = np.random.uniform(5,10, size=(5,3))
print(random_array)

# Exercise NO 7

import numpy as np
# Invalid the print option with suppress = False
np.set_printoptions(suppress=False)
x = np.arange(15)
print(x)
#Activate the print option with threshold
np.set_printoptions(threshold=6)
print(x)


# Exercise 8
import random
np.set_printoptions(suppress=False)
np.random.seed(100)

rand_arr = np.random.random([3,3])/1e3
print(rand_arr)
np.set_printoptions(suppress=True, precision=6)
print(rand_arr)


# Exercise 9
arr = np.arange(9).reshape(3,3)
arr
print(arr)
# To swap the column 0th index column to 1 and 1 to 0
arr[:, [1,0,2]]

# Exercise 10
arr = np.arange(9).reshape(3,3)
print(arr)
# Swap the row  0th rows to 1 and 1 rows to 0th position
arr[[1,0,2],:]
