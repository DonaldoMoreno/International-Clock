from __future__ import annotations

import tkinter as tk
from typing import Callable, Optional

from international_clock.config import (
    CITIES,
    COLORS,
    DATE_FORMAT,
    FONTS,
    REFRESH_INTERVAL_MS,
    USE_24_HOUR_FORMAT,
)
from international_clock.core.clock_service import ClockService


class MainWindow:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title("International Clock Dashboard")
        self.root.configure(bg=COLORS["background"])
        self.root.attributes("-fullscreen", True)
        self.root.bind("<Escape>", self._exit_fullscreen)

        self.clock_service = ClockService(CITIES, use_24_hour_format=USE_24_HOUR_FORMAT)

        self.local_time_var = tk.StringVar()
        self.local_date_var = tk.StringVar()
        self.city_time_vars: dict[str, tk.StringVar] = {
            city: tk.StringVar() for city, _ in CITIES
        }

        self._weather_hook: Optional[Callable[[dict[str, str]], None]] = None
        self._traffic_hook: Optional[Callable[[dict[str, str]], None]] = None
        self._second_display_hook: Optional[Callable[[dict[str, str]], None]] = None

        self._build_layout()

    def _build_layout(self) -> None:
        main_frame = tk.Frame(self.root, bg=COLORS["background"])
        main_frame.pack(fill="both", expand=True, padx=40, pady=30)

        local_frame = tk.Frame(main_frame, bg=COLORS["background"])
        local_frame.pack(pady=(10, 35))

        tk.Label(
            local_frame,
            textvariable=self.local_time_var,
            fg=COLORS["primary_text"],
            bg=COLORS["background"],
            font=FONTS["local_time"],
        ).pack()

        tk.Label(
            local_frame,
            textvariable=self.local_date_var,
            fg=COLORS["secondary_text"],
            bg=COLORS["background"],
            font=FONTS["date"],
        ).pack(pady=(8, 0))

        clocks_frame = tk.Frame(main_frame, bg=COLORS["background"])
        clocks_frame.pack(fill="x")

        columns = 3
        for idx, (city, _) in enumerate(CITIES):
            card = tk.Frame(clocks_frame, bg=COLORS["card_background"], bd=0, highlightthickness=0)
            row, column = divmod(idx, columns)
            card.grid(row=row, column=column, padx=12, pady=12, sticky="nsew")

            tk.Label(
                card,
                text=city,
                fg=COLORS["accent"],
                bg=COLORS["card_background"],
                font=FONTS["city"],
                padx=20,
            ).pack(padx=20, pady=12)

            tk.Label(
                card,
                textvariable=self.city_time_vars[city],
                fg=COLORS["primary_text"],
                bg=COLORS["card_background"],
                font=FONTS["city_time"],
            ).pack(padx=20, pady=(0, 12))

        for col in range(columns):
            clocks_frame.grid_columnconfigure(col, weight=1)

    def set_weather_hook(self, hook: Callable[[dict[str, str]], None]) -> None:
        self._weather_hook = hook

    def set_traffic_hook(self, hook: Callable[[dict[str, str]], None]) -> None:
        self._traffic_hook = hook

    def set_second_display_hook(self, hook: Callable[[dict[str, str]], None]) -> None:
        self._second_display_hook = hook

    def _exit_fullscreen(self, _event: tk.Event[tk.Misc]) -> None:
        self.root.attributes("-fullscreen", False)

    def _update_clock(self) -> None:
        self.local_time_var.set(self.clock_service.get_local_time())
        self.local_date_var.set(self.clock_service.get_local_date(DATE_FORMAT))

        city_times = self.clock_service.get_city_times()
        for city, city_time in city_times.items():
            self.city_time_vars[city].set(city_time)

        if self._second_display_hook:
            self._second_display_hook(city_times)
        if self._weather_hook:
            self._weather_hook(city_times)
        if self._traffic_hook:
            self._traffic_hook(city_times)

        self.root.after(REFRESH_INTERVAL_MS, self._update_clock)

    def run(self) -> None:
        self._update_clock()
        self.root.mainloop()
