''' Array using numpy module '''
import numpy as np
import matplotlib.pyplot as plt


x=np.array([1,2,3.4,8,12])

# Printing array
print(x)

# Find type
print(type(x))

# Find shape
print(x.shape)

# Finding mean value from array
mean_val=np.mean(x)

print(mean_val)


# Finding max value from array

max_val=np.max(x)

print(max_val)

# Finding min value from array

min_val=np.min(x)

print(min_val)


y=np.linspace(0,1,5)

print(y)


# Array multiplication

z=x*y

print(z)

# Zeros
a = np.zeros((2,2))
print(a)

# Ones
one = np.ones((2,2))
print(one)

# Full
ful = np.full((2,2), 7)
print(ful)

# Random
e = np.random.random((2,2))
print(e)

# Showing in graph
#plt.plot(x,y)
#plt.show()

# Array shape (3, 4)
a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
row_r1 = a[1, :]
print(row_r1)

row_r2 = a[1:3, :]
print(row_r2)

col_r1 = a[:, 1]
print(col_r1)

col_r2 = a[:, 1:2]
print(col_r2)

print(a.flags)

# As array
asArr = np.asarray(a,dtype=int)
print(asArr)

