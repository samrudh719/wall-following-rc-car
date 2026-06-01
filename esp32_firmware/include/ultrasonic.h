#ifndef ULTRASONIC_H
#define ULTRASONIC_H

void ultrasonic_init(void);
float ultrasonic_measure_distance(void);
float ultrasonic_filter_distance(float raw_distance);

#endif