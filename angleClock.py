class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        # Position of hour hand
        hour_angle = (hour % 12) * 30 + minutes * 0.5

        # Position of minute hand
        minute_angle = minutes * 6

        # Difference between the two angles
        angle = abs(hour_angle - minute_angle)

        # Return the smaller angle
        return min(angle, 360 - angle)
