import unittest

from international_clock.config import CITIES
from international_clock.core.clock_service import ClockService


class ClockServiceTests(unittest.TestCase):
    def test_city_times_include_all_configured_cities(self) -> None:
        service = ClockService(CITIES, use_24_hour_format=True)
        city_times = service.get_city_times()

        self.assertEqual({city for city, _ in CITIES}, set(city_times.keys()))

    def test_24_hour_time_format(self) -> None:
        service = ClockService(CITIES, use_24_hour_format=True)
        self.assertRegex(service.get_local_time(), r"^\d{2}:\d{2}:\d{2}$")

    def test_12_hour_time_format(self) -> None:
        service = ClockService(CITIES, use_24_hour_format=False)
        self.assertRegex(service.get_local_time(), r"^\d{2}:\d{2}:\d{2} (AM|PM)$")


if __name__ == "__main__":
    unittest.main()
