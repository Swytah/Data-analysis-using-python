import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ✅ Generate x values for plotting (100 points between -10 to 10)
x = np.linspace(-10, 10, 100)

# ----------------- BASIC PLOTTING -----------------
plt.figure(figsize=(12, 6))  # Create a figure with size 12x6 inches
plt.title('My Nice Plot')  # Set plot title

plt.plot(x, x ** 2, label="X^2")  # Plot x^2
plt.plot(x, -1 * (x ** 2), label="-X^2")  # Plot -x^2

plt.legend()  # Show legend
plt.show()  # Display the plot

# ----------------- SUBPLOTS -----------------
plt.figure(figsize=(12, 6))
plt.title('My Nice Plot')

# ✅ Creating **two subplots** (1 row, 2 columns)
plt.subplot(1, 2, 1)  # (rows, columns, subplot index)
plt.plot(x, x ** 2)
plt.plot([0, 0, 0], [-10, 0, 100])  # Adding a vertical line
plt.legend(['X^2', 'Vertical Line'])  
plt.xlabel('X')
plt.ylabel('X Squared')

plt.subplot(1, 2, 2)  
plt.plot(x, -1 * (x ** 2))
plt.plot([-10, 0, 10], [-50, -50, -50])  # Adding a horizontal line
plt.legend(['-X^2', 'Horizontal Line'])
plt.xlabel('X')
plt.ylabel('X Squared')

plt.tight_layout()  # Adjusts layout to prevent overlap
plt.show()

# ----------------- USING FIGURE & AXES -----------------
# ✅ Creating figure (`fig`) and one axes (`ax`)
fig, ax = plt.subplots(figsize=(12, 6))  

ax.plot(x, (x ** 2), color='red', linewidth=3, marker='o', markersize=8, label='X^2')
ax.plot(x, -1 * (x ** 2), 'b--', label='-X^2')

ax.set_xlabel('X')  # Set X-axis label
ax.set_ylabel('X Squared')  # Set Y-axis label
ax.set_title("My Nice Plot")  # Set title
ax.legend()  # Show legend

plt.show()

# ----------------- LINE STYLES -----------------
fig, ax = plt.subplots(figsize=(12, 6))

# ✅ Different line styles in a single figure
ax.plot(x, x + 0, linestyle='solid')
ax.plot(x, x + 1, linestyle='dashed')
ax.plot(x, x + 2, linestyle='dashdot')
ax.plot(x, x + 3, linestyle='dotted')

ax.set_title("Line Styles Example")
plt.show()

# ----------------- COLORS AND MARKERS -----------------
fig, ax = plt.subplots(figsize=(12, 6))

# ✅ Different colors and markers
ax.plot(x, x + 0, '-og', label="solid green")
ax.plot(x, x + 1, '--c', label="dashed cyan")
ax.plot(x, x + 2, '-.b', label="dashdot blue")
ax.plot(x, x + 3, ':r', label="dotted red")

ax.set_title("Line Styles with Colors & Markers")
ax.legend()
plt.show()

# ----------------- FIGURE & MULTIPLE SUBPLOTS -----------------
# ✅ Creating a 2x2 grid of subplots
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(14, 6))  

# Accessing subplots using axes array
axes[0, 0].plot(np.random.randn(50), c='red', linestyle='--')  
axes[0, 1].plot(np.random.randn(50), c='green', linestyle=':')
axes[1, 0].plot(np.random.randn(50), c='blue', marker='o', linewidth=3.0)
axes[1, 1].plot(np.random.randn(50), c='yellow')

plt.tight_layout()
plt.show()

# ----------------- GRID LAYOUT USING `subplot2grid()` -----------------
plt.figure(figsize=(14, 6))

# ✅ Creating a subplot grid manually
ax1 = plt.subplot2grid((3,3), (0,0), colspan=3)  # Top row, spans all columns
ax2 = plt.subplot2grid((3,3), (1,0), colspan=2)  # Second row, spans two columns
ax3 = plt.subplot2grid((3,3), (1,2), rowspan=2)  # Second & third row, single column
ax4 = plt.subplot2grid((3,3), (2,0))  # Bottom-left
ax5 = plt.subplot2grid((3,3), (2,1))  # Bottom-middle

plt.show()

# ----------------- SCATTER PLOTS -----------------
N = 50
X_scatter = np.random.rand(N)  # ✅ Renamed to avoid overwriting `x`
Y_scatter = np.random.rand(N)
colors = np.random.rand(N)
area = np.pi * (20 * np.random.rand(N))**2  

plt.figure(figsize=(14, 6))
plt.scatter(X_scatter, Y_scatter, s=area, c=colors, alpha=0.5, cmap='Spectral')
#plt.colorbar()  # ✅ Show color mapping
plt.show()

# ----------------- MULTIPLE SCATTER PLOTS -----------------
fig = plt.figure(figsize=(14, 6))

ax1 = fig.add_subplot(1,2,1)
ax1.scatter(X_scatter, Y_scatter, s=area, c=colors, alpha=0.5, cmap='Pastel1')
#plt.colorbar()  # ✅ Show color mapping

ax2 = fig.add_subplot(1,2,2)
ax2.scatter(X_scatter, Y_scatter, s=area, c=colors, alpha=0.5, cmap='Pastel2')
#plt.colorbar()  # ✅ Show color mapping

plt.show()

# ----------------- HISTOGRAMS -----------------
values = np.random.randn(1000)  # ✅ Random values for histogram

plt.figure(figsize=(12, 6))
plt.hist(values, bins=100, alpha=0.8, histtype='bar', color='steelblue', edgecolor='green')
plt.show()
