# ROS2 Topics

# Topic Overview

The system uses ROS2 topics for communication between telemetry and control nodes.

---

# Topics

| Topic | Type | Description |
|---|---|---|
| /sonar | sensor_msgs/Range | Ultrasonic wall distance |
| /cmd_vel | geometry_msgs/Twist | Velocity commands |
| /left_encoder | std_msgs/Int32 | Left wheel encoder ticks |
| /right_encoder | std_msgs/Int32 | Right wheel encoder ticks |

---

# Topic Workflow

ESP32 Firmware
↓
Serial Telemetry
↓
ROS2 Telemetry Node
↓
ROS2 Topics
↓
PID Controller
↓
Velocity Commands

---

# Node Responsibilities

## telemetry_node

Responsibilities:
- reads serial telemetry
- parses telemetry packets
- publishes ROS2 topics

---

## wall_follower_node

Responsibilities:
- subscribes to sonar topic
- computes PID correction
- publishes cmd_vel

---

## teleop_node

Responsibilities:
- keyboard teleoperation
- publishes manual cmd_vel
- mode switching

---

# ROS2 Middleware

The project uses ROS2 Humble DDS middleware for node communication.

---

# Future Improvements

- Nav2 integration
- TF tree publishing
- odometry node
- SLAM support