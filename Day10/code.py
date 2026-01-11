import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]
# Plot 1: Simple Line Plot
plt.plot(x,y)
plt.title("Simple Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

#Plot 2: Bar Chart
categories = ['A', 'B', 'C', 'D']
values = [5, 7, 3, 8]
plt.bar(categories, values, color='skyblue')
plt.title("Bar Chart Example")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()
#Plot 3: Scatter Plot

plt.scatter(x, y, color='red')
plt.title("Scatter Plot Example")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
#Plot 4: Histogram
plt.hist(y, bins=5, color='green', edgecolor='black')
plt.title("Histogram Example")
plt.xlabel("Value Ranges")
plt.ylabel("Frequency")
plt.show()  
