''' Array using numpy module '''
import numpy as np
import matplotlib.pyplot as plt


x=np.array([1,2,3.4,8,12])

# Printing array

print(x)

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

z=x*y;

print(z)


# Showing in graph
plt.plot(x,y)
plt.show()