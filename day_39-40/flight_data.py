class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, *args, stop_overs=0, via_city=""):
        self.price, self.city_code_from, self.fly_from, self.city_code_to,\
            self.fly_to, self.outward_departure_time, self.inward_departure_time = args
        self.stop_overs = stop_overs
        self.via_city = via_city

    def __repr__(self):

        return f'{self.price}, {self.city_code_from}, {self.fly_from}, {self.city_code_to},' \
               f' {self.fly_to}, {self.outward_departure_time}, {self.inward_departure_time},' \
               f' {self.stop_overs}, {self.via_city}'