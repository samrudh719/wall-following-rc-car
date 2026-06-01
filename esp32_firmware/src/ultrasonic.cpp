#include <Arduino.h>

#include "config.h"
#include "ultrasonic.h"
#include "logger.h"

static float previous_distance = 30.0f;

void ultrasonic_init(void)
{
    pinMode(TRIG_PIN,
            OUTPUT);

    pinMode(ECHO_PIN,
            INPUT);

    log_info("Ultrasonic Sensor Initialized");
}

float ultrasonic_measure_distance(void)
{
    digitalWrite(TRIG_PIN,
                 LOW);

    delayMicroseconds(2);

    digitalWrite(TRIG_PIN,
                 HIGH);

    delayMicroseconds(10);

    digitalWrite(TRIG_PIN,
                 LOW);

    unsigned long duration = pulseIn(ECHO_PIN,
                                     HIGH,
                                     ULTRASONIC_TIMEOUT_US);

    if (duration == 0)
    {
        return -1.0f;
    }

    float distance =
        duration * 0.034f / 2.0f;

    return distance;
}

float ultrasonic_filter_distance(float raw_distance)
{
    float filtered =
        (0.8f * previous_distance) +
        (0.2f * raw_distance);

    previous_distance = filtered;

    return filtered;
}
