# System Design

# Objective

The objective of this project is to develop an autonomous differential-drive RC robot capable of stable wall-following behavior using ROS2 Humble and ESP32-based embedded motor control.

---

# Hardware Components

| Component | Purpose |
|---|---|
| ESP32 | Embedded motor controller |
| HC-SR04 | Ultrasonic wall sensing |
| DC Motors | Robot locomotion |
| Motor Driver | Motor actuation |
| Wheel Encoders | Odometry feedback |

---

# Embedded Firmware Design

The ESP32 firmware was implemented using PlatformIO and the Arduino framework.

The firmware architecture includes:

- modular drivers
- encoder interrupt handling
- PWM motor control
- telemetry publishing
- ultrasonic sensing
- teleoperation support

---

# Differential Drive System

The robot uses differential-drive steering.

Turning behavior is achieved by varying left and right wheel velocities independently.

---

# ROS2 Design

ROS2 Humble running on a laptop performs:

- telemetry parsing
- PID wall-following control
- velocity command generation
- ROS2 topic communication

---

# Communication System

ESP32 communicates with ROS2 using a serial telemetry bridge.

The telemetry node converts incoming serial packets into ROS2 topics.

---

# Robotics Concepts Used

- differential drive kinematics
- PID control
- real-time telemetry
- embedded motor control
- ROS2 topic communication
- serial communication
- sensor filtering

---

# Performance Metrics

| Metric | Result |
|---|---|
| Average Velocity | 0.3 m/s |
| Maximum Wall Error | <4 cm |
| Control Stability | Stable |
| Recovery Behavior | Reliable |

---

# Future Improvements

- autonomous navigation
- SLAM integration
- LiDAR support
- camera-based localization
- IMU fusion
- path planning