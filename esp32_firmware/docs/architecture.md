# System Architecture

The robot uses a distributed robotics architecture combining low-level embedded motor control on ESP32 with high-level navigation and control using ROS2 Humble running on a laptop.

---

# Architecture Overview

The system is divided into two major layers:

1. Embedded Firmware Layer
2. ROS2 Control Layer

---

# Embedded Firmware Layer

The ESP32 firmware is responsible for:

- PWM motor control
- differential-drive steering
- wheel encoder acquisition
- ultrasonic distance sensing
- telemetry transmission
- manual teleoperation handling

The firmware is designed using a modular procedural architecture optimized for PlatformIO and ESP32 development.

---

# ROS2 Control Layer

ROS2 Humble running on a laptop is responsible for:

- PID wall-following control
- telemetry parsing
- ROS2 topic publishing
- velocity command generation
- robot supervision

---

# Communication Architecture

ESP32 and ROS2 communicate using a serial telemetry bridge.

Telemetry packets include:
- sonar distance
- left encoder ticks
- right encoder ticks

Example telemetry format:

DIST:31.2,LEFT:523,RIGHT:518

---

# ROS2 Topics

| Topic | Description |
|---|---|
| /sonar | Ultrasonic distance |
| /left_encoder | Left wheel encoder |
| /right_encoder | Right wheel encoder |
| /cmd_vel | Velocity commands |

---

# Data Flow

Ultrasonic Sensor
↓
ESP32 Firmware
↓
Serial Telemetry Bridge
↓
ROS2 Telemetry Node
↓
PID Controller
↓
Velocity Commands
↓
ESP32 Motor Driver

---

# Design Goals

- modular robotics architecture
- reliable telemetry
- stable wall following
- low-latency motor control
- scalable ROS2 integration
- embedded/ROS separation

---

# Future Improvements

- SLAM integration
- LiDAR support
- Nav2 integration
- IMU fusion
- camera localization
- EKF odometry