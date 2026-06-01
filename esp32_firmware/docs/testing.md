# System Testing

# Motor Driver Testing

| Test | Result |
|---|---|
| PWM Generation | PASS |
| Differential Steering | PASS |
| Motor Direction Control | PASS |

---

# Encoder Testing

| Test | Result |
|---|---|
| Interrupt Detection | PASS |
| Tick Counting | PASS |
| Velocity Estimation | PASS |

---

# Ultrasonic Sensor Testing

| Test | Result |
|---|---|
| Distance Measurement | PASS |
| Sensor Filtering | PASS |
| Stable Detection | PASS |

---

# ROS2 Communication Testing

| Test | Result |
|---|---|
| Topic Publishing | PASS |
| Topic Subscription | PASS |
| Serial Telemetry Parsing | PASS |
| Launch File Execution | PASS |

---

# PID Controller Validation

The robot was evaluated in a straight-corridor indoor environment.

---

# PID Results

| Metric | Result |
|---|---|
| Average Velocity | 0.3 m/s |
| Wall-Distance Error | <4 cm |
| Oscillation | Minimal |
| Recovery Stability | Stable |

---

# Controller Gains

| Parameter | Value |
|---|---|
| Kp | 2.5 |
| Ki | 0.02 |
| Kd | 0.5 |

---

# Teleoperation Testing

| Test | Result |
|---|---|
| Forward Control | PASS |
| Turning Control | PASS |
| Stop Command | PASS |
| Mode Switching | PASS |

---

# Fault Injection Tests

## Sensor Noise Injection

Artificial ultrasonic noise was introduced.

Result:
- filtering maintained stable control.

---

## Serial Disconnect Test

Serial communication interruptions were simulated.

Result:
- telemetry node recovered successfully.

---

## Motor Saturation Test

Maximum steering commands were tested.

Result:
- stable differential steering maintained.