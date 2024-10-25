import numpy as np
import matplotlib.pyplot as plt

# Load the RTT data from the file
rtt_data = np.loadtxt('tdecodehivemq0.out', delimiter=',')

# Create an array for x-axis (message index) based on the number of RTT values
x = np.arange(1, len(rtt_data) + 1)

# Plot the RTT data
plt.figure(figsize=(10, 6))
plt.plot(x, rtt_data, marker='o', color='b', label='RTT')

# Add labels and title
plt.xlabel('Message Index')
plt.ylabel('Round Trip Time (RTT) in seconds')
plt.title('RTT for MQTT Messages')
plt.legend()

# Add grid for better visualization
plt.grid(True)

# Show the plot
plt.show()