
class BudgetAgent:

    def calculate(self, destination, days, people):

        daily_cost = {
            "Manali": 1800,
            "Goa": 2200,
            "Jaipur": 1500,
            "Shimla": 1900,
            "Rishikesh": 1400
        }

        cost_per_day = daily_cost.get(destination, 1600)

        total = cost_per_day * days * people

        breakdown = {
            "Hotel": total * 0.35,
            "Food": total * 0.25,
            "Transport": total * 0.20,
            "Activities": total * 0.20
        }

        return {
            "total": total,
            "breakdown": breakdown
        }
