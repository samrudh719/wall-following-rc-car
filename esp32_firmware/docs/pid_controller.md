# PID Wall Following Controller

# Objective

The PID controller maintains a constant wall distance during autonomous navigation.

Target wall distance:
0.30 m

---

# PID Equation

Control Output =
Kp × Error +
Ki × Integral(Error) +
Kd × Derivative(Error)

---

# Error Calculation

Error =
Target Distance − Measured Distance

Positive error:
- robot turns toward wall

Negative error:
- robot turns away from wall

---

# PID Gains

| Parameter | Value |
|---|---|
| Kp | 2.5 |
| Ki | 0.02 |
| Kd | 0.5 |

---

# Control Behavior

The PID output is applied to robot angular velocity while maintaining constant forward velocity.

Forward velocity:
0.3 m/s

---

# Stability Improvements

Several improvements were implemented:

- sensor filtering
- derivative damping
- bounded steering output
- reduced update interval
- encoder-based feedback

---

# Performance Results

| Metric | Result |
|---|---|
| Average Velocity | 0.3 m/s |
| Wall-Distance Error | <4 cm |
| Oscillation | Minimal |
| Recovery Stability | Stable |

---

# Experimental Testing

The controller was tuned experimentally in a straight corridor environment.

Multiple gain combinations were tested to minimize oscillation and maintain stable tracking behavior.

---

# Future Improvements

- adaptive PID tuning
- model predictive control
- LiDAR-based control
- dynamic obstacle avoidance