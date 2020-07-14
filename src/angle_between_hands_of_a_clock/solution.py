class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        min_perc_rotation = minutes / 60 
        hour_perc_rotation = (0 if hour == 12 else hour) / 12
        min_degrees = 360 * min_perc_rotation
        hour_degrees = 360 * hour_perc_rotation + 30 * min_perc_rotation
        clockwise_rotation = max(min_degrees, hour_degrees) - min(min_degrees, hour_degrees)
        if clockwise_rotation <= 180:
            return clockwise_rotation
        return 360 - max(min_degrees, hour_degrees) + min(min_degrees, hour_degrees)
