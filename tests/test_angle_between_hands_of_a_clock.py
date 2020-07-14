import unittest

from src.angle_between_hands_of_a_clock.solution import Solution


class TestAngleBetweenHandsOfAClock(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_angleClock_hour_hand_and_minute_hand_are_at_the_same_angle_returns_zero(self):
        self._assert_angleClock(0.0, 12, 0)

    def test_angleClock_minute_hand_at_greater_angle_than_hour_hand(self):
        self._assert_angleClock(165.0, 12, 30)
    
    def test_angleClock_hour_hand_at_greater_angle_than_minute_hand(self):
        self._assert_angleClock(174.0, 8, 12)

    def test_angleClock_acute_angle_minute_hand_at_greater_angle_than_hour_hand(self):
        self._assert_angleClock(76.5, 1, 57)

    def _assert_angleClock(self, expected: float, hour: int, minutes: int) -> None:
        actual = self.solution.angleClock(hour, minutes)

        self.assertEqual(expected, actual)
