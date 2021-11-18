(MAX_ANGLE, MAX_HOUR, MAX_MINUTES) = (360, 12, 60);

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        (hourAngle, minutesAngle) = (((hour % MAX_HOUR) * (MAX_ANGLE / MAX_HOUR)) + (minutes * ((MAX_ANGLE / MAX_HOUR) / MAX_MINUTES)), minutes * (MAX_ANGLE / MAX_MINUTES));
        angleDiff = max(hourAngle, minutesAngle) - min(hourAngle, minutesAngle);
        return min(angleDiff, MAX_ANGLE - angleDiff);
