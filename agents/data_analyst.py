# import os
# from crewai import Agent, LLM
# from crewai_tools import FileReadTool


# # LLM configurations - Agent specific config
# model = os.getenv("ANALYST_AGENT_LLM")
# temperature = float(os.getenv("ANALYST_AGENT_TEMPERATURE"))

# llm = LLM(
#     model=model,
#     temperature=temperature
# )

# data_analyst_agent = Agent(
#     role="Data Analyst",
#     goal="Analyze gathered information to extract key insights, patterns, and conclusions",
#     backstory = (
#                 "You are a skilled data analyst with expertise in synthesizing complex "
#                 "information into actionable insights. You excel at identifying patterns, trends, "
#                 "and key findings from research data."
#             ),
#     llm=llm,
#     tools=[FileReadTool()],
#     verbose=True,
# )
"""
agents/data_analyst.py
Data Analyst Agent with error handling
"""

import os
import logging
from typing import Optional
from crewai import Agent, LLM

logger = logging.getLogger(__name__)


def get_llm() -> Optional[LLM]:
    """Initialize LLM for analyst agent"""
    try:
        model = os.getenv("ANALYST_AGENT_LLM", "groq/mixtral-8x7b-32768")
        temperature = float(os.getenv("ANALYST_AGENT_TEMPERATURE", "0.5"))
        
        # Validate temperature
        if temperature < 0 or temperature > 1:
            temperature = 0.5
        
        llm = LLM(model=model, temperature=temperature)
        logger.info(f"✅ Analyst LLM initialized: {model}")
        return llm
    
    except Exception as e:
        logger.error(f"Failed to initialize Analyst LLM: {e}")
        return None


def create_data_analyst_agent() -> Optional[Agent]:
    """Create Data Analyst Agent"""
    try:
        llm = get_llm()
        if not llm:
            logger.error("Cannot create Data Analyst: LLM failed")
            return None
        
        # Try to load tools
        tools = []
        try:
            from crewai_tools import FileReadTool
            tools = [FileReadTool()]
            logger.info("✅ FileReadTool loaded")
        except Exception as e:
            logger.warning(f"FileReadTool not available: {e}")
        
        agent = Agent(
            role="Data Analyst",
            goal="Analyze gathered information to extract key insights, patterns, and conclusions",
            backstory=(
                "You are a skilled data analyst with expertise in synthesizing complex information "
                "into actionable insights. You excel at identifying patterns, trends, and key findings "
                "from research data."
            ),
            llm=llm,
            tools=tools,
            verbose=True,
            allow_delegation=False,
        )
        
        logger.info("✅ Data Analyst Agent created successfully")
        return agent
    
    except Exception as e:
        logger.error(f"Failed to create Data Analyst Agent: {e}")
        logger.exception("Full traceback:")
        return None


# Create agent instance
try:
    data_analyst_agent = create_data_analyst_agent()
except Exception as e:
    logger.error(f"Error in data_analyst.py: {e}")
    data_analyst_agent = None