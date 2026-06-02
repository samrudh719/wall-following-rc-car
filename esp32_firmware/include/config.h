#ifndef CONFIG_H
#define CONFIG_H

#define LEFT_MOTOR_FORWARD_PIN     18
#define LEFT_MOTOR_BACKWARD_PIN    19
#define RIGHT_MOTOR_FORWARD_PIN    21
#define RIGHT_MOTOR_BACKWARD_PIN   22

#define LEFT_ENCODER_PIN           34
#define RIGHT_ENCODER_PIN          35

#define TRIG_PIN                   5
#define ECHO_PIN                   17

#define PWM_FREQUENCY              1000
#define PWM_RESOLUTION             8

#define MAX_PWM                    255

#define WALL_DISTANCE_CM           30.0f

#define CONTROL_INTERVAL_MS        50
#define COMMAND_TIMEOUT_MS         500
#define ULTRASONIC_TIMEOUT_US       30000UL

#define SERIAL_BAUDRATE            115200

#endif
