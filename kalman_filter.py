import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from itertools import repeat

time_steps = 100

# position list
# v = dx / dt -> GPS needs x
# dx = v / dt
# dim: [m]
position = range(0,20,2)    #np.arrange(0.0, 1.0, 0.1)
position.extend(range(20,40,1))
position.extend(range(40,60,3))
position.extend(range(60,80,2))
position.extend(repeat(80, 40))
position.extend(range(80,0,-2))
position.extend(repeat(0, 20))

# calc velocity
# v = dx / dt -> (x[i] - x[i-1])/t2-t1 -> x[i] - x[i-1
velocity = []
velocity_noise = np.random.normal(0, 1, len(position))
for idx, val in enumerate(position, 0):
    if(idx  < len(position) - 1):
        velocity.append((position[idx+1] - position[idx]) +velocity_noise[idx])

# calculated position
# s = v /t = v
calc_position = [0]
for idx, val in enumerate(velocity, 0):
    calc_position.append(calc_position[idx] + val)

#print(calc_position)

# GPS position
position_list = range(0, 100, 1)
gps_noise = np.random.normal(0, 1, len(position))
noisy_signal = []

for i, value in enumerate(position):
    noisy_signal.append(value + (gps_noise[i]))

# plotting
matplotlib.rcParams['axes.unicode_minus'] = False
fig, ax = plt.subplots()
fig1, ax1 = plt.subplots()
ax.plot(noisy_signal, 'r') # gps signal
#ax.plot(position, 'x')
ax.plot(calc_position, 'b') # calculated position
ax1.plot(velocity, 'g')
ax1.set_title('Velocity')
ax.set_title('GPS signal')
#ax1.ylim(ymin=-4, ymax=4)
plt.xlim(xmin=0, xmax=150)
plt.ylim(ymin=-80, ymax=100)
plt.show()