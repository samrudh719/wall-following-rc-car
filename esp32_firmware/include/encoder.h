#ifndef ENCODER_H
#define ENCODER_H

void encoder_init(void);
long encoder_get_left_ticks(void);
long encoder_get_right_ticks(void);
float encoder_compute_velocity(long ticks);

#endif