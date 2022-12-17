class Flats:
    def __init__(self, latitude, longitude, postal_code, fsa, rent_price):
        self.latitude = latitude
        self.longitude = longitude
        self.postal_code = postal_code
        self.fsa = fsa
        self.rent_price = rent_price

    def __repr__(self):
        return '<fsa {}>'.format(self.fsa)

    def serialize(self):
        return {
            'latitude': self.latitude,
            'longitude': self.longitude,
            'postal_code': self.postal_code,
            'fsa': self.fsa,
            'rent_price': self.rent_price
        }
