import unittest

from src.validate_ip_address.solution import Solution


NEITHER = "Neither"
IPV4 = "IPv4"
IPV6 = "IPv6"


class TestValidateIpAddress(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_validIPAddress_none_returns_neither(self):
        self._assert_validIPAddress(NEITHER, None)

    def test_validIPAddress_empty_string_returns_neither(self):
        self._assert_validIPAddress(NEITHER, "")

    def test_validIPAddress_not_at_all_an_ip_address_returns_neither(self):
        self._assert_validIPAddress(NEITHER, "not at all an IP address")

    # IPv4

    def test_validIPAddress_ipv4_address_but_first_octet_is_too_large_returns_neither(self):
        self._assert_validIPAddress(NEITHER, "256.0.0.0")

    def test_validIPAddress_ipv4_address_but_second_octet_is_too_large_returns_neither(self):
        self._assert_validIPAddress(NEITHER, "0.256.0.0")

    def test_validIPAddress_ipv4_address_but_third_octet_is_too_large_returns_neither(self):
        self._assert_validIPAddress(NEITHER, "0.0.256.0")

    def test_validIPAddress_ipv4_address_but_last_octet_is_too_large_returns_neither(self):
        self._assert_validIPAddress(NEITHER, "0.0.0.256")

    def test_validIPAddress_ipv4_address_but_too_few_octets_returns_neither(self):
        self._assert_validIPAddress(NEITHER, "0.0.0")

    def test_validIPAddress_ipv4_address_but_too_many_octets_returns_neither(self):
        self._assert_validIPAddress(NEITHER, "0.0.0.1.123")

    def test_validIPAddress_ipv4_address_but_blank_first_octets_returns_neither(self):
        self._assert_validIPAddress(NEITHER, ".2.3.4")

    def test_validIPAddress_ipv4_address_but_blank_second_octets_returns_neither(self):
        self._assert_validIPAddress(NEITHER, "1..3.4")

    def test_validIPAddress_ipv4_address_but_blank_third_octets_returns_neither(self):
        self._assert_validIPAddress(NEITHER, "1.2..4")

    def test_validIPAddress_ipv4_address_but_blank_last_octets_returns_neither(self):
        self._assert_validIPAddress(NEITHER, "1.2.3.")

    def test_validIPAddress_ipv4_address_but_first_octet_has_leading_zero_returns_neither(self):
        self._assert_validIPAddress(NEITHER, "01.2.3.4")

    def test_validIPAddress_ipv4_address_but_second_octet_has_leading_zero_returns_neither(self):
        self._assert_validIPAddress(NEITHER, "1.02.3.4")

    def test_validIPAddress_ipv4_address_but_third_octet_has_leading_zero_returns_neither(self):
        self._assert_validIPAddress(NEITHER, "1.2.03.4")

    def test_validIPAddress_ipv4_address_but_fourth_octet_has_leading_zero_returns_neither(self):
        self._assert_validIPAddress(NEITHER, "1.2.3.04")

    def test_validIPAddress_ipv4_address_but_wrong_octet_separator_returns_neither(self):
        self._assert_validIPAddress(NEITHER, "100,101,102,103")

    def test_validIPAddress_ipv4_address_is_valid_returns_ipv4(self):
        self._assert_validIPAddress(IPV4, "192.0.0.1")

    # IPv6

    def test_validIPAddress_ipv6_address_but_first_octet_is_too_large_returns_neither(self):
        self._assert_validIPAddress(NEITHER, "f2001:0db8:85a3:0012:0000:8a2e:0370:7334")

    def test_validIPAddress_ipv6_address_but_inner_octet_is_too_large_returns_neither(self):
        self._assert_validIPAddress(NEITHER, "2001:0db8:85a3:40012:0000:8a2e:0370:7334")

    def test_validIPAddress_ipv6_address_but_last_octet_is_too_large_returns_neither(self):
        self._assert_validIPAddress(NEITHER, "2001:0db8:85a3:0012:0000:8a2e:0370:57334")

    def test_validIPAddress_ipv6_address_but_first_octet_is_missing_returns_neither(self):
        self._assert_validIPAddress(NEITHER, ":0db8:85a3:0012:0000:8a2e:0370:7334")

    def test_validIPAddress_ipv6_address_but_single_inner_octet_is_missing_returns_neither(self):
        self._assert_validIPAddress(NEITHER, "2001:0db8:85a3:0012::8a2e:0370:7334")

    def test_validIPAddress_ipv6_address_but_multiple_inner_octets_are_missing_returns_neither(self):
        self._assert_validIPAddress(NEITHER, "2001:0db8:85a3:::::7334")

    def test_validIPAddress_ipv6_address_but_last_octet_is_missing_returns_neither(self):
        self._assert_validIPAddress(NEITHER, "2001:0db8:85a3:0012:0000:8a2e:0370:")

    def test_validIPAddress_ipv6_address_but_first_octet_has_extra_leading_zero_returns_neither(self):
        self._assert_validIPAddress(NEITHER, "02001:0db8:85a3:0012:0000:8a2e:0370:7334")

    def test_validIPAddress_ipv6_address_but_inner_octet_has_extra_leading_zero_returns_neither(self):
        self._assert_validIPAddress(NEITHER, "2001:0db8:85a3:0012:00000:8a2e:0370:7334")

    def test_validIPAddress_ipv6_address_but_last_octet_has_extra_leading_zero_returns_neither(self):
        self._assert_validIPAddress(NEITHER, "2001:0db8:85a3:0012:0000:8a2e:0370:07334")

    def test_validIPAddress_ipv6_address_octet_with_minus_sign_returns_neither(self):
        self._assert_validIPAddress(NEITHER, "1081:db8:85a3:01:-0:8A2E:0370:7334")

    def test_validIPAddress_ipv6_address_is_valid_returns_ipv6(self):
        self._assert_validIPAddress(IPV6, "2001:0db8:85a3:0012:0000:8a2e:0370:7334")

    def _assert_validIPAddress(self, expected: str, IP: str):
        actual = self.solution.validIPAddress(IP)

        self.assertEqual(expected, actual)
