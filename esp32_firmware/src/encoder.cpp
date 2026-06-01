#include <Arduino.h>

#include "config.h"
#include "encoder.h"
#include "logger.h"

volatile long left_ticks = 0;
volatile long right_ticks = 0;

void IRAM_ATTR left_encoder_isr()
{
    left_ticks++;
}

void IRAM_ATTR right_encoder_isr()
{
    right_ticks++;
}

void encoder_init(void)
{
    pinMode(LEFT_ENCODER_PIN,
            INPUT);

    pinMode(RIGHT_ENCODER_PIN,
            INPUT);

    attachInterrupt(
        digitalPinToInterrupt(
            LEFT_ENCODER_PIN),
        left_encoder_isr,
        RISING
    );

    attachInterrupt(
        digitalPinToInterrupt(
            RIGHT_ENCODER_PIN),
        right_encoder_isr,
        RISING
    );

    log_info("Encoders Initialized");
}

long encoder_get_left_ticks(void)
{
    noInterrupts();
    const long ticks = left_ticks;
    interrupts();

    return ticks;
}

long encoder_get_right_ticks(void)
{
    noInterrupts();
    const long ticks = right_ticks;
    interrupts();

    return ticks;
}

float encoder_compute_velocity(long ticks)
{
    return ticks * 0.01f;
}
