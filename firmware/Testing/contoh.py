"""
Simulasi 1: Robot jatuh (pendulum terbalik) — TANPA kontrol.

Tujuan: melihat seberapa cepat robot jatuh kalau tidak ada PID.
Model : alpha = (g / L) * sin(theta)       <- rumus yang sudah kita turunkan
Metode: integrasi Euler (waktu dipotong jadi langkah kecil dt)
"""

import math
import matplotlib.pyplot as plt

# ---------------------------------------------------------------
# 1. PARAMETER ROBOT  (hasil desain kamu sendiri)
# ---------------------------------------------------------------
g = 9.81            # percepatan gravitasi [m/s^2]
L = 0.10            # tinggi titik berat dari poros roda [m]  -> tahap 2

# ---------------------------------------------------------------
# 2. PARAMETER SIMULASI
# ---------------------------------------------------------------
dt = 0.001          # langkah waktu [s]  (1 ms)
t_max = 3.0         # batas waktu simulasi [s], biar loop pasti berhenti

# ---------------------------------------------------------------
# 3. KONDISI AWAL
# ---------------------------------------------------------------
theta = math.radians(2.0)   # sudut awal 2 derajat -> HARUS radian untuk math.sin
omega = 0.0                 # kecepatan sudut awal [rad/s] (diam)
t = 0.0                     # waktu [s]

# list untuk menyimpan riwayat, supaya bisa diplot
t_list = []
theta_list = []

# ---------------------------------------------------------------
# 4. LOOP SIMULASI (Euler)
# ---------------------------------------------------------------
while t < t_max:
    # simpan keadaan sekarang (sudut disimpan dalam derajat biar gampang dibaca)
    t_list.append(t)
    theta_list.append(math.degrees(theta))

    # robot dianggap sudah jatuh kalau miring lebih dari 90 derajat
    if abs(theta) > math.radians(90):
        break

    # --- fisika ---
    alpha = (g / L) * math.sin(theta)   # percepatan sudut  [rad/s^2]

    # --- TODO (simulasi 2): di sinilah nanti PID masuk! ---
    # PID akan menghasilkan "koreksi" yang melawan alpha,
    # supaya theta kembali ke 0. Untuk sekarang: tidak ada kontrol.

    # --- update keadaan (Euler) ---
    omega = omega + alpha * dt          # kecepatan sudut bertambah
    theta = theta + omega * dt          # sudut bertambah
    t = t + dt                          # waktu maju

# ---------------------------------------------------------------
# 5. HASIL
# ---------------------------------------------------------------
print(f"Sudut awal     : {theta_list[0]:.1f} derajat")
print(f"L              : {L*100:.0f} cm")
print(f"Waktu jatuh    : {t:.3f} detik (sampai 90 derajat)")
print(f"Skala waktu √(L/g): {math.sqrt(L/g):.3f} detik")

plt.plot(t_list, theta_list)
plt.axhline(90, color="red", linestyle="--", label="rebahan (90°)")
plt.xlabel("Waktu [s]")
plt.ylabel("Sudut θ [derajat]")
plt.title(f"Robot jatuh tanpa kontrol (L = {L*100:.0f} cm, θ awal = {theta_list[0]:.1f}°)")
plt.grid(True)
plt.legend()
plt.show()
