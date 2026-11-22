
class FoodAgent:

    def recommend(self, destination):

        food = {
            "Manali": [
                "Siddu",
                "Himachali Dham",
                "Thukpa"
            ],

            "Goa": [
                "Goan Fish Curry",
                "Bebinca",
                "Poi Bread"
            ],

            "Jaipur": [
                "Dal Baati Churma",
                "Ghewar",
                "Pyaaz Kachori"
            ],

            "Shimla": [
                "Chana Madra",
                "Siddu",
                "Babru"
            ],

            "Rishikesh": [
                "Aloo Puri",
                "Local Thali",
                "Fresh Lassi"
            ]
        }

        return food.get(destination, [])
