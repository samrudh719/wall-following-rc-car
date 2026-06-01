#include <Arduino.h>

#include "config.h"
#include "logger.h"
#include "motor_driver.h"

namespace
{
constexpr uint8_t LEFT_FORWARD_CHANNEL = 0;
constexpr uint8_t LEFT_BACKWARD_CHANNEL = 1;
constexpr uint8_t RIGHT_FORWARD_CHANNEL = 2;
constexpr uint8_t RIGHT_BACKWARD_CHANNEL = 3;

void configure_pwm(uint8_t pin, uint8_t channel)
{
    ledcSetup(channel, PWM_FREQUENCY, PWM_RESOLUTION);
    ledcAttachPin(pin, channel);
    ledcWrite(channel, 0);
}

void set_motor_speed(int speed,
                     uint8_t forward_channel,
                     uint8_t backward_channel)
{
    const int bounded_speed = constrain(speed, -MAX_PWM, MAX_PWM);

    if (bounded_speed >= 0)
    {
        ledcWrite(backward_channel, 0);
        ledcWrite(forward_channel, bounded_speed);
    }
    else
    {
        ledcWrite(forward_channel, 0);
        ledcWrite(backward_channel, -bounded_speed);
    }
}
}

void motor_driver_init(void)
{
    configure_pwm(LEFT_MOTOR_FORWARD_PIN, LEFT_FORWARD_CHANNEL);
    configure_pwm(LEFT_MOTOR_BACKWARD_PIN, LEFT_BACKWARD_CHANNEL);
    configure_pwm(RIGHT_MOTOR_FORWARD_PIN, RIGHT_FORWARD_CHANNEL);
    configure_pwm(RIGHT_MOTOR_BACKWARD_PIN, RIGHT_BACKWARD_CHANNEL);

    log_info("Motor driver initialized");
}

void motor_driver_set_speed(int left_speed,
                            int right_speed)
{
    set_motor_speed(left_speed,
                    LEFT_FORWARD_CHANNEL,
                    LEFT_BACKWARD_CHANNEL);

    set_motor_speed(right_speed,
                    RIGHT_FORWARD_CHANNEL,
                    RIGHT_BACKWARD_CHANNEL);
}

void motor_driver_stop(void)
{
    motor_driver_set_speed(0, 0);
}

void motor_driver_forward(int speed)
{
    motor_driver_set_speed(speed, speed);
}

void motor_driver_turn_left(int speed)
{
    motor_driver_set_speed(speed / 2, speed);
}

void motor_driver_turn_right(int speed)
{
    motor_driver_set_speed(speed, speed / 2);
}
