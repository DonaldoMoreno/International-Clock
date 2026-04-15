from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from zoneinfo import ZoneInfo

from international_clock.config import TIME_FORMAT_12H, TIME_FORMAT_24H


@dataclass(frozen=True)
class CityClock:
    city: str
    time_zone: ZoneInfo


class ClockService:
    def __init__(self, city_time_zones: list[tuple[str, str]], use_24_hour_format: bool = True) -> None:
        self._city_clocks = [CityClock(city=city, time_zone=ZoneInfo(tz)) for city, tz in city_time_zones]
        self._local_zone = datetime.now().astimezone().tzinfo or ZoneInfo("UTC")
        self._time_format = TIME_FORMAT_24H if use_24_hour_format else TIME_FORMAT_12H

    def get_local_time(self) -> str:
        return datetime.now(self._local_zone).strftime(self._time_format)

    def get_local_date(self, date_format: str) -> str:
        return datetime.now(self._local_zone).strftime(date_format)

    def get_city_times(self) -> dict[str, str]:
        current_time = datetime.now(ZoneInfo("UTC"))
        return {
            city_clock.city: current_time.astimezone(city_clock.time_zone).strftime(self._time_format)
            for city_clock in self._city_clocks
        }
