
import streamlit as st
from coordinator import TravelCoordinator
from agents.ai_agent import AIAgent
from io import BytesIO
from xml.sax.saxutils import escape
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


def create_pdf(ai_text):
    import re
    from reportlab.platypus import Table, TableStyle
    from reportlab.lib import colors
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.lib.enums import TA_CENTER
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont

    buffer = BytesIO()

    # Windows font supports the rupee symbol
    font_path = "C:/Windows/Fonts/arial.ttf"
    pdfmetrics.registerFont(TTFont("VoyageArial", font_path))

    styles = getSampleStyleSheet()
    body = ParagraphStyle(
        "VoyageBody",
        parent=styles["BodyText"],
        fontName="VoyageArial",
        fontSize=10,
        leading=16,
        spaceAfter=8
    )
    heading = ParagraphStyle(
        "VoyageHeading",
        parent=styles["Heading2"],
        fontName="VoyageArial",
        textColor=colors.HexColor("#17365D"),
        spaceBefore=16,
        spaceAfter=10
    )
    title = ParagraphStyle(
        "VoyageTitle",
        parent=styles["Title"],
        fontName="VoyageArial",
        fontSize=20,
        textColor=colors.HexColor("#0B1220"),
        alignment=TA_CENTER,
        spaceAfter=22
    )

    doc = SimpleDocTemplate(
        buffer,
        rightMargin=40,
        leftMargin=40,
        topMargin=45,
        bottomMargin=45
    )

    story = [
        Paragraph("VOYAGE AI", title),
        Paragraph("PERSONALIZED TRAVEL ITINERARY", heading),
        Spacer(1, 15)
    ]

    
    def format_text(text):
        text = text.replace("\u2011", "-")
        text = text.replace("\u2011", "-")
        text = text.replace("\u2013", "-")
        text = text.replace("\u2014", "-")
        text = text.replace("\u00a0", " ")
        text = text.replace("\u202f", " ")
        text = text.replace("\u25a0", "-")
        text = text.replace("\u2019", "'")

        text = escape(text)

        text = re.sub(
            r"\*\*(.*?)\*\*",
            r"<b>\1</b>",
            text
        )

        text = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<i>\1</i>", text)

        return text

        text = escape(text)
        return re.sub(
            r"\*\*(.*?)\*\*",
            r"<b>\1</b>",
            text
        )

    lines = ai_text.splitlines()
    i = 0

    while i < len(lines):
        line = lines[i].strip()

        if not line or line == "---":
            i += 1
            continue

        if line.startswith("#"):
            story.append(Paragraph(
                format_text(line.lstrip("#").strip()),
                heading
            ))

        elif line.startswith("|") and line.endswith("|"):
            rows = []

            while i < len(lines):
                current = lines[i].strip()
                if not (current.startswith("|") and current.endswith("|")):
                    break

                cells = [c.strip() for c in current.strip("|").split("|")]

                # Skip Markdown table separator rows
                if not all(re.fullmatch(r":?-{3,}:?", c) for c in cells):
                    rows.append(cells)

                i += 1

            if rows:
                count = max(len(row) for row in rows)
                widths = doc.width / count
                data = [
                    [
                        Paragraph(
                            format_text(row[j]) if j < len(row) else "",
                            body
                        )
                        for j in range(count)
                    ]
                    for row in rows
                ]

                table = Table(
                    data,
                    colWidths=[widths] * count,
                    repeatRows=1,
                    hAlign="LEFT"
                )
                table.setStyle(TableStyle([
                    ("BACKGROUND", (0, 0), (-1, 0),
                     colors.HexColor("#E8EFF8")),
                    ("GRID", (0, 0), (-1, -1),
                     0.4, colors.HexColor("#D4DCE8")),
                    ("VALIGN", (0, 0), (-1, -1), "TOP"),
                    ("LEFTPADDING", (0, 0), (-1, -1), 7),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 7),
                    ("TOPPADDING", (0, 0), (-1, -1), 7),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
                ]))
                story.append(table)
                story.append(Spacer(1, 12))

            continue

        else:
            story.append(Paragraph(format_text(line), body))

        i += 1

    doc.build(story)
    buffer.seek(0)
    return buffer.getvalue()

st.set_page_config(
    page_title="Multi-Agent Travel Planner",
    page_icon="✈️",
    layout="wide"
)


st.markdown("""
<style>
.hero {
    background: #0B1220;
    border: 1px solid #26364B;
    border-radius: 16px;
    padding: 38px 32px;
    margin-bottom: 24px;
    font-family: 'Segoe UI', sans-serif;
}
.brand {
    color: #8BB8FF;
    font-size: 15px;
    font-weight: 700;
    letter-spacing: 3px;
}
.hero h1 {
    color: #FFFFFF;
    font-size: 42px;
    font-weight: 650;
    letter-spacing: -1.5px;
    margin: 22px 0 12px;
}
.hero p {
    color: #A9B9CD;
    font-size: 16px;
    line-height: 1.7;
}
.tagline {
    color: #8BB8FF;
    font-size: 12px;
    letter-spacing: 2px;
    margin-top: 22px;
}
</style>

<div class="hero">
    <div class="brand">VOYAGE AI / TRAVEL INTELLIGENCE</div>
    <h1>Travel beyond the ordinary.</h1>
    <p>
        Intelligent journeys, powered by multiple AI agents.
        Discover destinations, compare options and build
        personalized travel itineraries.
    </p>
    <div class="tagline">DISCOVER / PLAN / EXPLORE</div>
</div>
""", unsafe_allow_html=True)



st.markdown("## Plan your journey")
st.caption("Customize your next travel experience.")

col1, col2 = st.columns(2, gap="large")

with col1:
    
    
    destination = st.selectbox(
        "Destination",
        ["Manali", "Goa", "Jaipur", "Shimla", "Rishikesh"]
    )


    budget = st.number_input(
        "Total Budget (INR)",
        min_value=1000,
        value=20000,
        step=1000
    )

with col2:
    days = st.number_input(
        "Duration (Days)",
        min_value=1,
        max_value=30,
        value=5
    )

    people = st.number_input(
        "Number of Travellers",
        min_value=1,
        value=2
    )

st.markdown("""
<style>
div.stButton > button {
    background-color: #2563EB;
    color: white;
    border: none;
    border-radius: 9px;
    padding: 0.65rem 1.5rem;
    font-weight: 600;
}
div.stButton > button:hover {
    background-color: #1D4ED8;
    color: white;
    border: none;
}
</style>
""", unsafe_allow_html=True)



if st.button("Generate Travel Plan", type="primary", use_container_width=True):
    st.session_state["generate_ai"] = True
else:
    st.session_state["generate_ai"] = False

if st.session_state["generate_ai"]:
    coordinator = TravelCoordinator()


    plan = coordinator.create_travel_plan(
        destination, days, people, "Budget"
    )

    
    st.success("Travel plan generated successfully.")

    st.markdown("### Trip Overview")

    col1, col2, col3 = st.columns(3, gap="medium")

    with col1:
        with st.container(border=True):
            st.caption("DESTINATION")
            st.subheader(destination)

    with col2:
        with st.container(border=True):
            st.caption("DURATION")
            st.subheader(f"{days} Days")

    with col3:
        with st.container(border=True):
            st.caption("TRAVELLERS")
            st.subheader(f"{people} People")

    st.divider()


   
    st.markdown("### Travel Recommendations")
    st.caption("Recommendations prepared by your specialized travel agents.")

    left, right = st.columns(2, gap="large")

    with left:
        with st.container(border=True):
            st.subheader("Places to Visit")
            for place in plan["destination"]:
                st.write("•", place)

        with st.container(border=True):
            st.subheader("Recommended Hotel")
            st.write(plan["hotel"])

        with st.container(border=True):
            st.subheader("Local Food")
            for food in plan["food"]:
                st.write("•", food)

    with right:
        with st.container(border=True):
            st.subheader("Transport Options")
            for transport in plan["transport"]:
                st.write("•", transport)

        with st.container(border=True):
            st.subheader("Estimated Trip Cost")
            st.metric(
                "Total Estimated Cost",
                f"₹{plan['budget']['total']:,}"
            )

            if plan["budget"]["total"] <= budget:
                st.success("Within your budget")
            else:
                st.warning("Exceeds your budget")

    st.divider()
  
    
    st.markdown("### Day-wise Itinerary")
    st.caption("Your daily travel schedule, organized by destination.")

    for day, activity in plan["itinerary"].items():
        with st.expander(
            f"{day}  |  {activity}",
            expanded=False
        ):
            st.markdown(f"**Destination:** {activity}")

            st.write("Morning — Explore the attraction")
            st.write("Afternoon — Enjoy local food")
            st.write("Evening — Relax and explore nearby areas")

    st.divider()



    travel_report = f"""
MULTI-AGENT TRAVEL PLANNER
--------------------------

Destination: {destination}
Duration: {days} Days
Travellers: {people}
User Budget: Rs. {budget}

PLACES TO VISIT
{chr(10).join(plan["destination"])}

RECOMMENDED HOTEL
{plan["hotel"]}

TRANSPORT OPTIONS
{chr(10).join(plan["transport"])}

ESTIMATED TRIP COST
Rs. {plan["budget"]["total"]}

LOCAL FOOD
{chr(10).join(plan["food"])}

DAY-WISE ITINERARY
{chr(10).join(f"{day}: {activity}" for day, activity in plan["itinerary"].items())}

Note: Costs are estimates, not live booking prices.
"""

    
    st.download_button(
        label="Download Travel Plan PDF",
        data=create_pdf(travel_report),
        file_name=f"Voyage_AI_{destination}_Travel_Plan.pdf",
        mime="application/pdf",
        key="download_standard_pdf"
    )



st.divider()

st.header("🤖 AI-Powered Travel Planner")

st.write("Generate a personalized travel plan using Groq AI.")

if st.session_state.get("generate_ai", False):

    with st.spinner("AI is planning your trip..."):
        try:
            ai_agent = AIAgent()

            ai_plan = ai_agent.generate_plan(
                destination, days, budget, people
            )
            st.session_state["ai_plan"] = ai_plan

            st.success("AI travel plan generated successfully.")

            st.markdown("### Your Personalized AI Itinerary")

            st.markdown(ai_plan)

            st.download_button(
                label="Download AI Itinerary",
                data=ai_plan,
                file_name=f"Voyage_AI_{destination}_Itinerary.md",
                mime="text/markdown",
                key="download_ai_itinerary"
            )

            st.download_button(
                label="Download PDF",
                data=create_pdf(ai_plan),
                file_name=f"Voyage_AI_{destination}_Itinerary.pdf",
                mime="application/pdf",
                key="download_ai_pdf"
            )



        
        except Exception as e:
            st.error("Unable to generate AI plan.")
            st.write("Error type:", type(e).__name__)
            st.write("Error details:", str(e))


elif "ai_plan" in st.session_state:

    st.download_button(
        label="Download PDF",
        data=create_pdf(st.session_state["ai_plan"]),
        file_name="Voyage_AI_Itinerary.pdf",
        mime="application/pdf",
        key="download_saved_pdf"
    )

    st.markdown("### Your Personalized AI Itinerary")
    st.markdown(st.session_state["ai_plan"])

    st.download_button(
        label="Download AI Itinerary",
        data=st.session_state["ai_plan"],
        file_name="Voyage_AI_Itinerary.md",
        mime="text/markdown",
        key="download_saved_ai"
    )


