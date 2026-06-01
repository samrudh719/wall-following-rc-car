#ifndef MOTOR_DRIVER_H
#define MOTOR_DRIVER_H

void motor_driver_init(void);
void motor_driver_set_speed(int left_speed,
                            int right_speed);
void motor_driver_stop(void);
void motor_driver_forward(int speed);
void motor_driver_turn_left(int speed);
void motor_driver_turn_right(int speed);

#endif