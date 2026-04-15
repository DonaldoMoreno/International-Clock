from __future__ import annotations

# Time display settings
USE_24_HOUR_FORMAT: bool = True
REFRESH_INTERVAL_MS: int = 1000

# City name and IANA timezone pairs
CITIES: list[tuple[str, str]] = [
    ("Mexico City", "America/Mexico_City"),
    ("New York", "America/New_York"),
    ("London", "Europe/London"),
    ("Tokyo", "Asia/Tokyo"),
    ("Berlin", "Europe/Berlin"),
]

# Theme colors
COLORS: dict[str, str] = {
    "background": "#111827",
    "primary_text": "#F9FAFB",
    "secondary_text": "#D1D5DB",
    "accent": "#60A5FA",
    "card_background": "#1F2937",
}

# Font definitions as Tk-compatible tuples
FONTS: dict[str, tuple[str, int, str]] = {
    "local_time": ("Helvetica", 64, "bold"),
    "date": ("Helvetica", 24, "normal"),
    "city": ("Helvetica", 20, "bold"),
    "city_time": ("Helvetica", 28, "normal"),
}

DATE_FORMAT: str = "%A, %d %B %Y"
TIME_FORMAT_24H: str = "%H:%M:%S"
TIME_FORMAT_12H: str = "%I:%M:%S %p"
