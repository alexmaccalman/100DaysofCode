class FlightData:
    
    def __init__(self, price, origin_city, origin_airport, destination_city, destination_airport, out_date, out_time, out_airline, out_flight, return_date, return_time, return_airline, return_flight):
        self.price = price
        self.origin_city = origin_city
        self.origin_airport = origin_airport
        self.destination_city = destination_city
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.out_time = out_time
        self.out_airline = out_airline
        self.out_flight = out_flight
        self.return_date = return_date
        self.return_time = return_time
        self.return_airline = return_airline
        self.return_flight = return_flight

    def print_flight(self):
        print(f"Price: ${self.price} from {self.origin_airport} to {self.destination_airport} departs on {self.out_date} flight {self.out_airline} {self.out_flight} returns on {self.return_date} flight {self.return_airline} {self.return_flight}")