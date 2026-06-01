#pragma once

void telemetry_init(void);

void telemetry_publish(float distance,
                       long left_ticks,
                       long right_ticks);
