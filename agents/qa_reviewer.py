import os
from crewai import Agent, LLM

model = os.getenv("QA_AGENT_LLM")
temperature = float(os.getenv("QA_AGENT_TEMPERATURE"))

llm = LLM(model=model, temperature=temperature)

qa_reviewer_agent = Agent(
    role="Quality Assurance Reviewer",
    goal="Evaluate and improve the accuracy, clarity, coherence, and completeness of content produced by other agents.",
    backstory=(
        "You are a meticulous reviewer who excels at catching inconsistencies, vague reasoning, "
        "factual errors, unclear writing, and logical gaps. You provide actionable corrections "
        "to ensure the final work is polished and reliable."
    ),
    llm=llm,
    verbose=True,
)