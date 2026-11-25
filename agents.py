from datetime import datetime
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from tools import web_search, scrape_url
from dotenv import load_dotenv

load_dotenv()

# model setup
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)


def _current_date_str() -> str:
    return datetime.now().strftime("%B %d, %Y")


def _current_year() -> int:
    return datetime.now().year


# 1st agent
def build_search_agent():
    today = _current_date_str()
    year = _current_year()
    return create_agent(
        model=llm,
        tools=[web_search],
        system_prompt=(
            f"You are a web research agent. Today's date is {today} (current year: {year}). "
            f"When searching for recent, latest, or current information, ALWAYS prioritize {year} developments "
            f"(include '{year}' in your search queries and pass time_range='year' to web_search unless the user explicitly asks about a past year). "
            f"Do not default to 2024 or 2025 when the user asks for recent or latest information."
        ),
    )


# 2nd agent
def build_reader_agent():
    today = _current_date_str()
    year = _current_year()
    return create_agent(
        model=llm,
        tools=[scrape_url],
        system_prompt=(
            f"You are a web reader agent. Today's date is {today} (current year: {year}). "
            f"Pick the most relevant and up-to-date URL (preferring {year} sources when available) and scrape it for deeper content."
        ),
    )


# writer chain
writer_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are an expert research writer. Today's date is {current_date}. "
        "Write clear, structured and insightful reports that accurately reflect the most recent sources provided.",
    ),
    ("human", """Write a detailed research report on the topic below.

Current Date: {current_date}
Topic: {topic}

Research Gathered:
{research}

Structure the report as:
- Introduction
- Key Findings (minimum 3 well-explained points)
- Conclusion
- Sources (list all URLs found in the research)

Be detailed, factual and professional."""),
])

writer_chain = (
    RunnablePassthrough.assign(current_date=lambda _: _current_date_str())
    | writer_prompt
    | llm
    | StrOutputParser()
)

# critic_chain
critic_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a sharp and constructive research critic. Today's date is {current_date}. "
        "Be honest and specific, and verify that the report uses up-to-date information relative to the current date.",
    ),
    ("human", """Review the research report below and evaluate it strictly.

Current Date: {current_date}
Report:
{report}

Respond in this exact format:

Score: X/10

Strengths:
- ...
- ...

Areas to Improve:
- ...
- ...

One line verdict:
..."""),
])

critic_chain = (
    RunnablePassthrough.assign(current_date=lambda _: _current_date_str())
    | critic_prompt
    | llm
    | StrOutputParser()
)