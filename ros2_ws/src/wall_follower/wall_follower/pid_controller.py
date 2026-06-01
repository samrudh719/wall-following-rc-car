class PIDController:

    def __init__(self,
                 kp,
                 ki,
                 kd):

        self.kp = kp
        self.ki = ki
        self.kd = kd

        self.previous_error = 0.0
        self.integral = 0.0

    def compute(self,
                target,
                measurement,
                dt):

        error = target - measurement

        if dt <= 0.0:
            return self.kp * error

        self.integral += error * dt

        derivative = (
            error - self.previous_error
        ) / dt

        output = (
            self.kp * error +
            self.ki * self.integral +
            self.kd * derivative
        )

        self.previous_error = error

        return output
