from geopy.extra.rate_limiter import RateLimiter
from geopy.geocoders import Nominatim


class GeoHelper:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def get_zip_outer(self):
        geocoder = Nominatim(user_agent="Canada")
        geo = RateLimiter(geocoder.reverse, min_delay_seconds=2, max_retries=100, return_value_on_exception=None)
        location = geo((self.latitude, self.longitude))
        try:
            zip_code = location.raw.get("address").get("postcode").replace(" ", "")
        except Exception:
            zip_code = None
        return zip_code
