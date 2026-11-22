
class ItineraryAgent:

    def create_itinerary(self, destination, days):

        places = {
            "Manali": [
                "Hadimba Temple",
                "Old Manali",
                "Solang Valley",
                "Atal Tunnel",
                "Mall Road"
            ],

            "Goa": [
                "Baga Beach",
                "Calangute Beach",
                "Fort Aguada",
                "Anjuna Market",
                "Candolim Beach"
            ],

            "Jaipur": [
                "Hawa Mahal",
                "City Palace",
                "Amber Fort",
                "Jal Mahal",
                "Johari Bazaar"
            ],

            "Shimla": [
                "Mall Road",
                "The Ridge",
                "Jakhoo Temple",
                "Kufri",
                "Christ Church"
            ],

            "Rishikesh": [
                "Ram Jhula",
                "Triveni Ghat",
                "Neer Garh Waterfall",
                "River Rafting",
                "Beatles Ashram"
            ]
        }

        selected_places = places.get(destination, [])
        itinerary = {}

        for day in range(days):

            place_index = day % len(selected_places)

            itinerary[f"Day {day + 1}"] = selected_places[place_index]

        return itinerary
