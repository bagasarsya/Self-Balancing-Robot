import math

#parameter awal
g = 9.81            # percepatan gravitasi [m/s^2]
L = 0.1
dt = 0.001
omega = 0.0
t = 0.0

derajat = 10
theta = math.radians(derajat)

print(f"Sudut awal     : {theta:.4f} rad")

# batas waktu simulasi (biar loop pasti berhenti)
#   → bikin variabel baru, misalnya 3 detik
t_max = 3.0
# ulangi SELAMA waktu masih di bawah batas
#   → loop apa di Python yang berjalan "selama kondisi benar"?
while t <= t_max:
    # cek: kalau robot sudah miring lebih dari 90°, keluar dari loop
    #   → ingat, theta dalam radian, jadi 90° juga harus radian
    if theta > math.radians(90):
        break

    # 1. hitung percepatan sudut dari rumus fisika
    alpha = (g/L) * math.sin(theta)
    # 2. update kecepatan sudut
    omega = omega + alpha * dt
    # 3. update sudut
    theta = theta + omega * dt
    # 4. majukan waktu
    t = t + dt
# setelah loop selesai: print waktu t
print(f"waktu jatuh : {t:.4f} detik (sampai 90 derajat)")
