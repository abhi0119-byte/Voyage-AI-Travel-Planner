
class HotelAgent:

    def recommend(self, destination, budget):

        hotels = {
            "Manali": {
                "Budget": "Zostel Manali",
                "Medium": "Hotel Mountain Face",
                "Luxury": "Span Resort and Spa"
            },

            "Goa": {
                "Budget": "Hostel near Anjuna",
                "Medium": "Resort near Calangute",
                "Luxury": "Luxury beach resort"
            },

            "Jaipur": {
                "Budget": "Budget guesthouse",
                "Medium": "Hotel near MI Road",
                "Luxury": "Heritage luxury hotel"
            },

            "Shimla": {
                "Budget": "Budget guesthouse",
                "Medium": "Hotel near Mall Road",
                "Luxury": "Luxury mountain resort"
            },

            "Rishikesh": {
                "Budget": "Budget hostel",
                "Medium": "Riverside hotel",
                "Luxury": "Luxury riverside resort"
            }
        }

        options = hotels.get(destination, {})

        return options.get(budget, "Hotel not found")
