# Development Log

## 2026-11-13: Planning

**Done**
- Defined target specs: 20–25 cm tall, 2–3 h runtime, live PID tuning over WiFi, €100–150 budget
- Selected components and wrote the BOM
- Sized the battery: 0.6 A × 3 h / 0.8 ≈ 2.25 Ah → LiPo 3S 2200 mAh
- Designed the battery-monitoring voltage divider (33 kΩ / 10 kΩ → max 2.93 V at the ADC)

**Learned**
- Inverted pendulum: α = (g/L)·sinθ. Mass cancels out, so only the height of the center of mass decides how fast the robot falls. Mass matters for motor torque, not falling speed.
- Units matter: V / kΩ gives mA, not kV.
- A measuring circuit should draw as little current as possible (kΩ, not Ω).
- Why ESP32 over ESP32-C3: dual core + hardware pulse counter for encoders.

**Next**
- Order components
- Theory: estimating the tilt angle from the IMU (complementary filter)
