#include <Arduino.h>
#include <cctype>

#include "config.h"
#include "encoder.h"
#include "logger.h"
#include "motor_driver.h"
#include "telemetry.h"
#include "ultrasonic.h"

namespace
{
constexpr int DRIVE_PWM = 180;
constexpr float DISTANCE_TOLERANCE_CM = 3.0f;

bool autonomous_mode = false;
unsigned long previous_control_time = 0;

void system_initialize()
{
    telemetry_init();
    motor_driver_init();
    encoder_init();
    ultrasonic_init();
    motor_driver_stop();

    log_info("System initialized in teleop mode");
}

void autonomous_control_loop()
{
    const float raw_distance = ultrasonic_measure_distance();

    if (raw_distance <= 0.0f)
    {
        motor_driver_stop();
        log_warning("Ultrasonic reading timed out; motors stopped");
        return;
    }

    const float distance = ultrasonic_filter_distance(raw_distance);

    telemetry_publish(distance,
                      encoder_get_left_ticks(),
                      encoder_get_right_ticks());

    if (distance < WALL_DISTANCE_CM - DISTANCE_TOLERANCE_CM)
    {
        motor_driver_turn_left(DRIVE_PWM);
    }
    else if (distance > WALL_DISTANCE_CM + DISTANCE_TOLERANCE_CM)
    {
        motor_driver_turn_right(DRIVE_PWM);
    }
    else
    {
        motor_driver_forward(DRIVE_PWM);
    }
}

void telemetry_control_loop()
{
    const float raw_distance = ultrasonic_measure_distance();

    if (raw_distance <= 0.0f)
    {
        return;
    }

    telemetry_publish(ultrasonic_filter_distance(raw_distance),
                      encoder_get_left_ticks(),
                      encoder_get_right_ticks());
}

void teleop_control(char command)
{
    switch (std::tolower(static_cast<unsigned char>(command)))
    {
        case 'w':
            motor_driver_forward(DRIVE_PWM);
            break;

        case 'a':
            motor_driver_turn_left(DRIVE_PWM);
            break;

        case 'd':
            motor_driver_turn_right(DRIVE_PWM);
            break;

        case 's':
            motor_driver_stop();
            break;

        case 'm':
            autonomous_mode = !autonomous_mode;
            motor_driver_stop();
            log_info(autonomous_mode
                         ? "Autonomous mode enabled"
                         : "Teleop mode enabled");
            break;

        default:
            break;
    }
}
}

void setup()
{
    system_initialize();
}

void loop()
{
    while (Serial.available() > 0)
    {
        teleop_control(static_cast<char>(Serial.read()));
    }

    const unsigned long current_time = millis();

    if (current_time - previous_control_time >= CONTROL_INTERVAL_MS)
    {
        previous_control_time = current_time;

        if (autonomous_mode)
        {
            autonomous_control_loop();
        }
        else
        {
            telemetry_control_loop();
        }
    }
}
