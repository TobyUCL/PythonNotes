"""
Create a scatter plot.
Change the scatter plot marker shape (marker), colour (c), size(s) in the plt.scatter function call.  
"""

x_scatter = 
y_scatter = 
x_scatter_name = 
y_scatter_name = 

plt.scatter(x_scatter, y_scatter, marker='o', c='b', s=1)
x_identline = np.linspace(start= np.min(x_scatter),stop=np.max(x_scatter),num=100)
plt.plot(x_identline, x_identline, 'r-')
plt.gca().set_aspect('equal', adjustable='box')
plt.xlabel(x_scatter_name)
plt.ylabel(y_scatter_name)
plt.show()
