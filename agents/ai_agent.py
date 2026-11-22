
from groq import Groq
import streamlit as st


class AIAgent:

    def __init__(self):
        self.client = Groq(
            api_key=st.secrets["GROQ_API_KEY"]
        )

    def generate_plan(self, destination, days, budget, people):

        prompt = f"""
        You are an expert Indian travel planner.

        Create a personalized travel plan.

        Destination: {destination}
        Duration: {days} days
        Total Budget: Rs. {budget}
        Travellers: {people}

        Include:
        1. Best places to visit
        2. Day-wise itinerary
        3. Hotel suggestions
        4. Transport recommendations
        5. Local food
        6. Estimated budget breakdown

        Use simple English and clear headings.
        Mention that prices are estimates.
        """

        response = self.client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message.content
