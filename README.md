# ROS2 Autonomous + Teleoperation Wall Following Robot

An autonomous differential-drive RC robot using ESP32 firmware and ROS2-based control.

## Features

- Autonomous wall following
- Manual RC teleoperation
- PID control
- ESP32 motor control
- Encoder telemetry
- Ultrasonic sensing
- ROS2 topic communication
- Differential drive steering
- Real-time telemetry bridge

## Modes

### Autonomous Mode
The robot performs wall-following behavior automatically using ultrasonic sensing and PID control.

### Teleoperation Mode
The robot can be controlled manually using keyboard commands.

| Key | Action |
|---|---|
| W | Forward |
| A | Turn Left |
| D | Turn Right |
| S | Stop |
| M | Toggle Mode |
| Q | Quit |

## Hardware

- ESP32
- HC-SR04 Ultrasonic Sensor
- DC Motors
- Motor Driver
- Wheel Encoders

## Software Stack

- Embedded C
- ROS2 Humble
- Python
- PlatformIO

## Build Instructions

```bash
cd esp32_firmware
pio run
pio run --target upload
pio device monitor
```

PlatformIO automatically detects the ESP32 serial port when the board is
connected over USB. The firmware starts in teleoperation mode. Send `M` in the
serial monitor to toggle autonomous mode.

The wall-following logic assumes that the ultrasonic sensor faces the robot's
right-side wall. GPIO 34 and GPIO 35 require external pull-up resistors if the
encoders do not drive their output signals. Use a voltage divider or level
shifter between an HC-SR04 `ECHO` output and the ESP32 because ESP32 GPIO pins
are not 5 V tolerant.

To build the ROS2 workspace:

```bash
cd ros2_ws
colcon build
source install/setup.bash
```

Launch the ROS2 nodes with the ESP32 connected:

```bash
ros2 launch wall_follower bringup.launch.py serial_port:=/dev/ttyUSB0
```

Replace `/dev/ttyUSB0` with the detected serial device when needed.
For manual keyboard control, append `enable_teleop:=true`.

## VS Code will also stop showing false ROS import errors when launched from the sourced Ubuntu terminal.

## Performance Metrics

| Metric | Result |
|---|---|
| Tracking Speed | 0.3 m/s |
| Wall Distance Error | <4 cm |
| Control Stability | Stable |
| Recovery Behavior | Reliable |