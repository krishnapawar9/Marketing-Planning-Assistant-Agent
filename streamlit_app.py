import streamlit as st
from datetime import datetime
from agent import MarketingAgent
from database_mysql import save_plan, load_plans, delete_plan

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

# Page config
st.set_page_config(
    page_title="Marketing Planning Agent",
    page_icon="📈",
    layout="wide"
)

# ✅ THEN LOAD DATA
if "history" not in st.session_state:
    st.session_state.history = load_plans()

# Session state for selected plan (NEW)
if "selected_plan" not in st.session_state:
    st.session_state.selected_plan = None

def generate_pdf(text):
    file_path = "marketing_plan.pdf"

    styles = getSampleStyleSheet()
    style = ParagraphStyle('Normal', fontSize=10, spaceAfter=6)

    doc = SimpleDocTemplate(file_path, pagesize=A4)
    elements = []

    for line in text.split("\n"):
        elements.append(Paragraph(line, style))
        elements.append(Spacer(1, 6))

    doc.build(elements)
    return file_path

# Custom CSS (makes UI beautiful)
st.markdown("""
    <style>
        .main-title {
            font-size: 40px;
            font-weight: bold;
            color: #4CAF50;
        }
        .subtitle {
            font-size: 18px;
            color: #666666;
            margin-bottom: 20px;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            font-size: 16px;
            border-radius: 10px;
            padding: 10px 24px;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="main-title">📈 Marketing Planning Assistant</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Generate AI-powered structured marketing plans</div>', unsafe_allow_html=True)

# Sidebar
st.sidebar.title("⚙ Settings")

tone = st.sidebar.selectbox(
    "Response Style",
    ["Professional", "Creative", "Aggressive Marketing", "Startup Friendly"]
)

show_resources = st.sidebar.checkbox("Show Resource Checks", value=True)

st.sidebar.markdown("---")
st.sidebar.title("🎨 Appearance")

dark_mode = st.sidebar.toggle("🌙 Dark Mode")

if dark_mode:
    st.markdown("""
        <style>
            .stApp {
                background-color: #0E1117;
                color: #FFFFFF;
            }

            section[data-testid="stSidebar"] {
                background-color: #161A23;
            }

            /* Titles */
            .main-title {
                color: #4CAF50;
            }

            .subtitle {
                color: #CFCFCF;
            }

            /* Text input & text area */
            textarea, input {
                background-color: #1E1E1E !important;
                color: #FFFFFF !important;
                border-radius: 8px !important;
                border: 1px solid #333 !important;
            }

            /* Labels */
            label {
                color: #E0E0E0 !important;
                font-weight: 500;
            }

            /* Expanders */
            details {
                background-color: #1A1F2B;
                border-radius: 10px;
                padding: 10px;
                border: 1px solid #2A2F3A;
            }

            details p {
                color: #FFFFFF !important;
            }

            /* Buttons */
            .stButton>button {
                background-color: #4CAF50;
                color: white;
                border-radius: 10px;
            }
        </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
        <style>
            .stApp {
                background-color: white;
                color: black;
            }
        </style>
    """, unsafe_allow_html=True)

st.sidebar.markdown("---")
st.sidebar.title("📜 Plan History")

search_query = st.sidebar.text_input("🔎 Search Plans")

# 🔄 HARD REFRESH BUTTON (NEW)
if st.sidebar.button("🔄 Refresh History"):
    st.session_state.history = load_plans()
    st.session_state.selected_plan = None
    st.sidebar.success("History refreshed from database ✅")
    st.rerun()

filtered_history = [
    plan for plan in st.session_state.history
    if search_query.lower() in plan["goal"].lower()
] if search_query else st.session_state.history

st.sidebar.caption(f"Showing {len(filtered_history)} plans")

if filtered_history:
    for i, item in enumerate(reversed(filtered_history), 1):
        with st.sidebar.expander(f"Plan {i}: {item['goal'][:25]}..."):

            st.markdown("**Goal:**")
            st.write(item["goal"])

            created_time = item["created_at"].strftime("%d %b %Y • %I:%M %p")
            st.markdown(f"🕒 **Created:** {created_time}")

            colA, colB = st.columns(2)

            with colA:
                if st.button("📂 Load", key=f"load_{i}"):
                    st.session_state.selected_plan = item["plan"]

            with colB:
                if st.button("🗑 Delete", key=f"delete_{i}"):

                    if item.get("id"):  # ✅ Safety check
                        delete_plan(item["id"])
                        st.session_state.history = load_plans()
                        st.rerun()
                    else:
                        st.warning("⚠ Cannot delete: Plan not synced with database")
else:
    st.sidebar.write("No matching plans found.")

# ✅ CLEAR HISTORY BUTTON (NEW)
st.sidebar.markdown("---")

if st.sidebar.button("🗑 Clear History"):
    from database_mysql import clear_history  # ensure function exists
    clear_history()

    st.session_state.history = load_plans()
    st.session_state.selected_plan = None

    st.sidebar.success("History cleared!")
    st.rerun()

# Layout columns
col1, col2 = st.columns([2, 3])

with col1:
    st.markdown("### 🎯 Enter Your Marketing Goal")
    goal = st.text_area(
        "Describe what you want:",
        placeholder="Example: Create a marketing plan for a fitness app targeting busy professionals",
        height=150
    )

    generate = st.button("🚀 Generate Plan")

with col2:
    st.markdown("### 📊 Generated Plan")

    # ✅ SHOW LOADED PLAN FROM HISTORY
    if st.session_state.selected_plan:
        st.info("📂 Viewing previously generated plan")

        with st.expander("✅ Loaded Marketing Plan", expanded=True):
            st.markdown(st.session_state.selected_plan)

            if st.button("❌ Close Loaded Plan"):
                st.session_state.selected_plan = None
                st.rerun()

            if st.session_state.selected_plan:
                pdf_path = generate_pdf(st.session_state.selected_plan)

                if pdf_path:  # ✅ Safety guard
                    with open(pdf_path, "rb") as pdf_file:
                        st.download_button(
                            label="⬇ Download Loaded Plan as PDF",
                            data=pdf_file,
                            file_name="Marketing_Plan.pdf",
                            mime="application/pdf"
                        )

    if generate:
        if goal.strip():
            with st.spinner("AI Agent is thinking... 🤖"):
                try:
                    agent = MarketingAgent()
                    enhanced_goal = f"{goal} | Tone: {tone}"
                    result = agent.run(enhanced_goal)

                    try:
                        save_plan(goal, result["output"])  # ✅ Save to MySQL

                        st.success("✅ Plan saved to MySQL successfully!")

                        st.session_state.history = load_plans()  # reload silently

                    except Exception as db_error:
                        st.error(f"❌ Database Save Failed: {db_error}")
                        st.stop()

                    st.success("Plan generated successfully!")

                    # Expandable result container
                    with st.expander("✅ View Full Marketing Plan", expanded=True):
                        st.markdown(result["output"])

                        pdf_path = generate_pdf(result["output"])

                        with open(pdf_path, "rb") as pdf_file:
                            st.download_button(
                                label="⬇ Download Plan as PDF",
                                data=pdf_file,
                                file_name="Marketing_Plan.pdf",
                                mime="application/pdf"
                            )

                    if show_resources:
                        with st.expander("🔎 Resource Checks"):
                            st.write("Mock tools verification included in output.")

                except Exception as e:
                    st.error(f"Error: {e}")
        else:
            st.warning("Please enter a marketing goal.")