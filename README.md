🧠 ResearchMind – Multi-Agent AI Research Assistant

ResearchMind is an AI-powered research assistant that automates web research and generates structured reports on user-provided topics using a multi-agent architecture.

Instead of relying on a single LLM response, ResearchMind divides the research workflow into specialized AI agents and chains for searching, reading, writing, and evaluating information.

🚀 Features

AI-Powered Web Search: Uses Tavily API to retrieve relevant and up-to-date web search results.

Intelligent Web Scraping: Extracts meaningful webpage content using Requests and BeautifulSoup.

Multi-Agent Architecture: Uses specialized Search and Reader agents to automate research tasks.

Automated Report Generation: Generates structured research reports using OpenAI and LangChain.

AI-Based Evaluation: A Critic chain reviews generated reports, providing scores, strengths, and improvement suggestions.

Interactive Dashboard: Streamlit interface with pipeline status tracking and report previews.

Report Download: Export generated research reports in Markdown format.

🏗️ System Architecture

ResearchMind follows a sequential four-stage research pipeline:

Search Agent: Searches the web using the Tavily API and retrieves relevant URLs, titles, and snippets.

Reader Agent: Selects a relevant webpage and extracts its content using BeautifulSoup.

Writer Chain: Processes the research information and generates a structured Markdown report.

Critic Chain: Evaluates the generated report and provides a quality score, strengths, and improvement suggestions.

          User Research Topic
                  |
                  v
          +---------------+
          | Search Agent  |
          |  Tavily API   |
          +---------------+
                  |
                  v
          +---------------+
          | Reader Agent  |
          | BeautifulSoup |
          +---------------+
                  |
                  v
          +---------------+
          | Writer Chain  |
          |   OpenAI LLM  |
          +---------------+
                  |
                  v
          +---------------+
          | Critic Chain  |
          |   Evaluation  |
          +---------------+
                  |
                  v
          Structured Research Report

🛠️ Tech Stack

Category

Technologies

Programming Language

Python

AI Framework

LangChain

LLM

OpenAI (gpt-4o-mini)

Agent Architecture

LangChain create_agent()

Prompt Pipelines

LangChain Expression Language (LCEL)

Web Search

Tavily API

Web Scraping

Requests, BeautifulSoup

Frontend

Streamlit

Environment Management

python-dotenv

📂 Project Structure

ResearchMind/
│
├── agents.py          # Search Agent, Reader Agent,
│                      # Writer Chain and Critic Chain
│
├── tools.py           # Web search and scraping tools
│
├── pipeline.py        # Sequential research pipeline
│
├── app.py             # Streamlit web application
│
├── requirements.txt   # Project dependencies
│
├── .gitignore         # Excluded files and secrets
│
└── README.md          # Project documentation

⚙️ Installation & Setup

1. Clone the Repository

git clone https://github.com/Anurag123731/ResearchMind.git
cd ResearchMind

2. Create a Virtual Environment

python -m venv .venv

Activate it on Windows:

.venv\Scripts\activate

3. Install Dependencies

pip install -r requirements.txt

4. Configure Environment Variables

Create a .env file in the root directory and add your API keys:

OPENAI_API_KEY=your_openai_api_key
TAVILY_API_KEY=your_tavily_api_key

Note: Never share or commit your .env file or API keys to GitHub.

5. Run the Application

Launch the Streamlit interface:

streamlit run app.py

The application will open in your browser.

To run the research pipeline directly from the terminal:

python pipeline.py

📊 Research Report Output

ResearchMind generates structured reports containing:

Introduction

Key Findings

Conclusion

Sources

The Critic Chain additionally evaluates the generated report based on its quality and provides:

Overall Score (out of 10)

Strengths

Areas to Improve

Final Verdict

🔮 Future Improvements

Implement iterative report refinement using LangGraph.

Enable parallel scraping of multiple webpages.

Improve source verification and citation accuracy.

Add support for exporting reports as PDF.

Introduce additional specialized research agents.

👨‍💻 Author

Anurag Rawat

GitHub: Anurag123731

⭐ If you find this project interesting, consider giving the repository a star!