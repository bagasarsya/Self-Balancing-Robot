# Self-Balancing Robot

A two-wheeled self-balancing robot built from scratch around an ESP32 — custom PCB, 3D-printed chassis, and a PID controller tuned live through a web interface.

> 🚧 **Status:** Planning complete · components being ordered (Nov 2026)

## Why this project

This is a learning project. Every part is built by hand to practice a specific skill:

| Part | Skill |
|---|---|
| Balancing controller | Control systems — PID, sensor fusion (complementary filter) |
| Custom PCB | Basic electronics, schematic & PCB design (KiCad) |
| 3D-printed chassis | CAD & design for manufacturing |
| Web tuning interface | Embedded networking (ESP32 WiFi) |

## Specifications (target)

| Parameter | Target |
|---|---|
| Height | 20–25 cm |
| Weight | ~0.8–1.2 kg |
| Runtime | 2–3 h |
| Required | Self-balancing, live PID tuning over WiFi |
| Optional | Animated face on a round LCD |
| Budget | €100–150 |

## Hardware

| Component | Choice | Why |
|---|---|---|
| MCU | ESP32 DevKit (WROOM-32) | Dual core: control loop on one core, WiFi on the other. Hardware pulse counter (PCNT) for encoders |
| IMU | MPU6050 | 6-axis gyro + accelerometer, I2C |
| Motors | 2× JGA25-370, 12 V, ~300 RPM, Hall encoder | Enough torque and speed (~1 m/s with 65 mm wheels) for a ~1 kg robot |
| Motor driver | 2× DRV8871 | 45 V / 3.6 A peak. Avoids the ~2 V drop of an L298N and the tight limits of a TB6612 on 3S |
| Battery | LiPo 3S 2200 mAh (XT60) | Matches 12 V motors; sized for ~3 h (see below) |
| 5 V rail | MP1584 buck converter | Efficient step-down, keeps the ESP32 stable when motor current makes the battery voltage sag |
| Display (optional) | GC9A01 1.28" round TFT | Robot face |

Full bill of materials: [`docs/BOM.csv`](docs/BOM.csv)

### Power architecture

```
LiPo 3S ──XT60──► Fuse 5A ──► Switch ──┬──► DRV8871 ×2 ──► Motors
(11.1–12.6 V)                          ├──► Buck 5 V ──► ESP32, IMU, LCD
                                       └──► Voltage divider ──► ESP32 ADC
```

## Design calculations

**Battery capacity** (using at most 80 % of a LiPo's capacity):

```
C = I_avg × t / 0.8 = 0.6 A × 3 h / 0.8 ≈ 2.25 Ah  →  2200 mAh
```

**Why a taller robot is easier to balance.** Modelled as an inverted pendulum with its center of mass at height L:

```
τ = m·g·L·sinθ,   I = m·L²   →   α = (g / L)·sinθ
```

The mass cancels out. Only L sets how fast the robot falls, so a higher center of mass falls more slowly and gives the controller more time to react. Mass still matters for the motors: a heavier robot needs more torque and current.

**Battery voltage monitoring.** The ESP32 ADC accepts at most 3.3 V, so a voltage divider scales the battery voltage down:

```
R1 = 33 kΩ, R2 = 10 kΩ
V_out,max = 12.6 V × 10 / 43 = 2.93 V      (safe margin below 3.3 V)
I_divider = 12.6 V / 43 kΩ  = 0.29 mA       (negligible drain)
V_battery = V_adc × 4.3
```

Resistors in the kΩ range keep the current wasted by the divider low. With 430 Ω instead, the divider would draw 29 mA and dissipate 0.37 W, which is more than a standard 0.25 W resistor can handle. The divider uses an ADC1 pin (GPIO 32–39), because ADC2 is unavailable while WiFi is active.

## Roadmap

- [x] **Week 1:** Requirements, component selection, BOM
- [ ] **Week 1–2:** Order components
- [ ] **Week 2–4:** Theory: IMU angle estimation (complementary filter), PID, basic electronics; rough CAD sketch
- [ ] **Week 4–6:** Breadboard prototype: IMU, motors, encoders tested individually
- [ ] **Week 6–8:** First balance + PID tuning
- [ ] **Week 8–9:** Final chassis CAD + 3D print
- [ ] **Week 9–11:** PCB design in KiCad → manufacture
- [ ] **Week 11–12:** Integration, web tuning dashboard, LCD face, final documentation

The PCB comes last on purpose: the circuit is proven on a breadboard first, so the board is designed once.

## Repository structure

```
├── docs/            Design notes, BOM, development log
├── firmware/        ESP32 code
├── hardware/
│   ├── pcb/         KiCad project
│   └── cad/         Chassis CAD files & STLs
└── media/           Photos & videos
```

## Development log

Progress, problems and lessons learned: [`docs/devlog.md`](docs/devlog.md)

## Author

**Bagas Arsya Putra Sarwono**, Mechatronics student at Hochschule Niederrhein
