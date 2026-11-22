
class TransportAgent:

    def recommend(self, destination):

        transport = {
            "Manali": [
                "Volvo Bus",
                "Private Taxi",
                "Local Cab"
            ],

            "Goa": [
                "Flight",
                "Train",
                "Rental Scooter"
            ],

            "Jaipur": [
                "Train",
                "Bus",
                "Auto Rickshaw"
            ],

            "Shimla": [
                "Train",
                "Bus",
                "Local Taxi"
            ],

            "Rishikesh": [
                "Train",
                "Bus",
                "Local Taxi"
            ]
        }

        return transport.get(destination, [])
