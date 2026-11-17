import math
import matplotlib.pyplot as plt


g = 9.81            
L = 0.1
dt = 0.001
omega = 0.0
t = 0.0

derajat = 10
theta = math.radians(derajat)

t_max = 3.0

t_list = []
theta_list = []

while t <= t_max:
    t_list.append(t)
    theta_list.append(math.degrees(theta))
    if theta > math.radians(90):
        break
    alpha = (g/L) * math.sin(theta)
    omega = omega + alpha * dt
    theta = theta + omega * dt
    t = t + dt
print(f"falling time : {t:.4f} s (untill 90 degrees)")

plt.plot(t_list, theta_list)
plt.xlabel("Time (s)")
plt.ylabel("Angle (degrees)")
plt.title("Falling Simulation of the Robot")
plt.grid(True)
plt.savefig("../../media/falling_sim.png", dpi=150, bbox_inches="tight")
plt.show()
