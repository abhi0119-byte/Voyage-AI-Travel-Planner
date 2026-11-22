
class DestinationAgent:

    def recommend(self, destination):

        places = {
            "Manali": [
                "Solang Valley",
                "Hadimba Temple",
                "Old Manali",
                "Atal Tunnel"
            ],

            "Goa": [
                "Baga Beach",
                "Calangute Beach",
                "Fort Aguada",
                "Anjuna Market"
            ],

            "Jaipur": [
                "Amber Fort",
                "Hawa Mahal",
                "City Palace",
                "Johari Bazaar"
            ],

            "Shimla": [
                "Mall Road",
                "The Ridge",
                "Jakhoo Temple",
                "Kufri"
            ],

            "Rishikesh": [
                "Triveni Ghat",
                "Neer Garh Waterfall",
                "Ram Jhula",
                "River Rafting"
            ]
        }


        
        return places.get(destination, [])


