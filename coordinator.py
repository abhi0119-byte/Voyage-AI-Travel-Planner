
from agents.destination_agent import DestinationAgent
from agents.hotel_agent import HotelAgent
from agents.transport_agent import TransportAgent
from agents.budget_agent import BudgetAgent
from agents.food_agent import FoodAgent
from agents.itinerary_agent import ItineraryAgent


class TravelCoordinator:

    def __init__(self):

        self.destination = DestinationAgent()
        self.hotel = HotelAgent()
        self.transport = TransportAgent()
        self.budget = BudgetAgent()
        self.food = FoodAgent()
        self.itinerary = ItineraryAgent()

    def create_travel_plan(self, place, days, people, budget_type):

        print("Travel agents are working...")

        # Destination Agent
        places = self.destination.recommend(place)

        # Hotel Agent
        hotel = self.hotel.recommend(place, budget_type)

        # Transport Agent
        transport = self.transport.recommend(place)

        # Budget Agent
        budget = self.budget.calculate(place, days, people)

        # Food Agent
        food = self.food.recommend(place)

        # Itinerary Agent
        itinerary = self.itinerary.create_itinerary(place, days)

        # Combine all results
        result = {
            "destination": places,
            "hotel": hotel,
            "transport": transport,
            "budget": budget,
            "food": food,
            "itinerary": itinerary
        }

        return result
