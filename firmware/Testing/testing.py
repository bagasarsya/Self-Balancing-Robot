import math
import matplotlib.pyplot as plt


g = 9.81            
L = 0.1
dt = 0.001
omega = 0.0
t = 0.0

derajat = 10
theta = math.radians(derajat)
batas_jatuh = math.radians(90)

t_max = 3.0

Kp = 500
setpoint = 0

t_list = []
theta_list = []

while t <= t_max:
    t_list.append(t)
    theta_list.append(math.degrees(theta))
    if abs(theta) > batas_jatuh:
        break
    error = setpoint - theta
    u = Kp * error
    alpha = (g/L) * math.sin(theta) + u
    omega = omega + alpha * dt
    theta = theta + omega * dt
    t = t + dt
    
if abs(theta) > batas_jatuh:
    print(f"Robot jatuh pada waktu: {t:.4f} detik")
else:
    print(f"Robot masih berdiri selama: {t:.4f} detik.")

plt.plot(t_list, theta_list)
plt.xlabel("Time (s)")
plt.ylabel("Angle (degrees)")
plt.title("Falling Simulation of the Robot")
plt.grid(True)
plt.savefig(f"../../media/p_control_{Kp}.png", dpi=150, bbox_inches="tight")
plt.show()
