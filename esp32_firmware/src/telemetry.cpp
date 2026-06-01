#include <Arduino.h>
#include "config.h"
#include "telemetry.h"
#include "logger.h"

void telemetry_init(void)
{
    Serial.begin(SERIAL_BAUDRATE);
    log_info("Telemetry Interface Initialized");
}

void telemetry_publish(float distance,
                       long left_ticks,
                       long right_ticks)
{
    Serial.print("DIST:");
    Serial.print(distance);

    Serial.print(",LEFT:");
    Serial.print(left_ticks);

    Serial.print(",RIGHT:");
    Serial.println(right_ticks);
}

