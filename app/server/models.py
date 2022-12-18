class Flats:
    def __init__(self, latitude, longitude, fsa, average_price):
        self.latitude = latitude
        self.longitude = longitude
        self.fsa = fsa
        self.average_price = average_price

    def __repr__(self):
        return '<fsa {}>'.format(self.fsa)

    def serialize(self):
        return {
            'latitude': self.latitude,
            'longitude': self.longitude,
            'fsa': self.fsa,
            'average_price': self.average_price
        }
