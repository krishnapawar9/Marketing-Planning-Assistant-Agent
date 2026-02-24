# 📈 Marketing Planning Assistant Agent

An AI-powered marketing planning system that generates structured marketing strategies using **LangChain, Streamlit, and MySQL**.

This project demonstrates an **agentic AI workflow** capable of breaking down high-level marketing goals into actionable execution plans.

---

## 🚀 Features

- ✅ **Goal Decomposition**  
  Converts broad marketing goals into structured tasks

- ✅ **Resource Validation**  
  Uses mock tools for budgets, keywords, and ad analysis

- ✅ **Dependency Management**  
  Determines optimal execution order

- ✅ **Optimized Scheduling**  
  Generates a logical plan timeline

- ✅ **Streamlit GUI**  
  Interactive, clean, and user-friendly interface

- ✅ **Dark Mode Toggle**  
  Improves readability and UX

- ✅ **Plan History (MySQL)**  
  Persistent storage of marketing plans

- ✅ **Search / Filter Plans**  
  Quickly find past plans

- ✅ **Delete Plans️**  
  Remove unwanted records

- ✅ **PDF Export**  
  Download plans as PDF

---

## 🧠 Tech Stack

- **Python**
- **LangChain**
- **Streamlit**
- **MySQL**
- **ReportLab (PDF generation)**
- **Pydantic**
- **Python Dotenv**

---

## 📂 Project Structure

```text
marketing_planner_agent/
│
├── main.py                # CLI entry point
├── streamlit_app.py       # Streamlit GUI application
├── agent.py               # Core agent orchestration logic
├── planner.py             # Planning & task decomposition engine
├── config.py              # Configuration & environment handling
├── database_mysql.py      # MySQL database operations
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation
│
└── tools/
    ├── ad_library_tool.py # Ad research / competitor insights
    ├── budget_tool.py     # Budget validation logic
    ├── keyword_tool.py    # Keyword planning logic
    └── scheduler_tool.py  # Campaign scheduling logic
```

---

## 🖥️ Usage

Using the application is simple:

1️⃣ **Enter a marketing goal**  
Describe what you want the AI agent to plan.

2️⃣ **Select response style**  
Choose how the strategy should be written (Professional, Creative, etc.).

3️⃣ **Generate structured marketing plan**  
The AI agent decomposes your goal into an actionable execution plan.

4️⃣ **Export to PDF**  
Download the generated plan for documentation or sharing.

5️⃣ **View / Search / Delete History**  
Manage previously generated plans stored in MySQL.

---

## 📊 Example Goals

Try prompts like:

- "Create a marketing plan for a fitness app"
- "Competition ads analysis"
- "Launch strategy for a SaaS startup"
- "Marketing strategy for a new e-commerce brand"
- "Social media growth plan for a personal brand"

---

## 🎯 Learning Outcomes

This project helped practice:

- ✅ Agentic AI workflows  
- ✅ LangChain orchestration  
- ✅ Streamlit UI design  
- ✅ MySQL database integration  
- ✅ Session state management  
- ✅ PDF generation with ReportLab  
- ✅ UX/UI enhancements  
- ✅ Error handling & debugging  

---

## 🔮 Future Improvements

Planned upgrades:

- 🔹 User authentication & login system  
- 🔹 Multi-user dashboards  
- 🔹 Cloud database deployment (AWS / Railway)  
- 🔹 Marketing analytics & metrics  
- 🔹 Vector memory integration  
- 🔹 REST API deployment  
- 🔹 Plan comparison features  
- 🔹 Export to DOCX / CSV  