# import os
# from crewai import Agent, LLM
# from crewai_tools import SerperDevTool


# # LLM configurations - Agent specific config
# model = os.getenv("RESEARCH_AGENT_LLM")
# temperature = float(os.getenv("RESEARCH_AGENT_TEMPERATURE"))

# llm = LLM(
#     model=model,
#     temperature=temperature
#  )  # llm object

# research_specialist_agent = Agent(
#     role="Research Specialist",
#     goal="Gather comprehensive and accurate information on given topics from multiple sources",
#     backstory = (
#                 "You are an expert research specialist with years of experience in information gathering "
#                 "and fact-checking. You have a keen eye for reliable sources and can quickly identify the "
#                 "most relevant and up-to-date information on any topic."
#             ),
#     llm=llm,
#     tools=[SerperDevTool()],
#     verbose=True,
# )
"""
agents/research_specialist.py
Research Specialist Agent with error handling
"""

import os
import logging
from typing import Optional
from crewai import Agent, LLM

logger = logging.getLogger(__name__)


def get_llm() -> Optional[LLM]:
    """Initialize LLM for research agent"""
    try:
        model = os.getenv("RESEARCH_AGENT_LLM", "groq/mixtral-8x7b-32768")
        temperature = float(os.getenv("RESEARCH_AGENT_TEMPERATURE", "0.3"))
        
        # Validate temperature
        if temperature < 0 or temperature > 1:
            temperature = 0.3
        
        llm = LLM(model=model, temperature=temperature)
        logger.info(f"✅ Research LLM initialized: {model}")
        return llm
    
    except Exception as e:
        logger.error(f"Failed to initialize Research LLM: {e}")
        return None


def create_research_specialist_agent() -> Optional[Agent]:
    """Create Research Specialist Agent"""
    try:
        llm = get_llm()
        if not llm:
            logger.error("Cannot create Research Specialist: LLM failed")
            return None
        
        # Try to load tools
        tools = []
        try:
            from crewai_tools import SerperDevTool
            tools = [SerperDevTool()]
            logger.info("✅ SerperDevTool loaded")
        except Exception as e:
            logger.warning(f"SerperDevTool not available: {e}")
        
        agent = Agent(
            role="Research Specialist",
            goal="Gather comprehensive and accurate information on given topics from multiple sources",
            backstory=(
                "You are an expert research specialist with years of experience in information gathering "
                "and fact-checking. You have a keen eye for reliable sources and can quickly identify the "
                "most relevant and up-to-date information on any topic."
            ),
            llm=llm,
            tools=tools,
            verbose=True,
            allow_delegation=False,
        )
        
        logger.info("✅ Research Specialist Agent created successfully")
        return agent
    
    except Exception as e:
        logger.error(f"Failed to create Research Specialist Agent: {e}")
        logger.exception("Full traceback:")
        return None


# Create agent instance
try:
    research_specialist_agent = create_research_specialist_agent()
except Exception as e:
    logger.error(f"Error in research_specialist.py: {e}")
    research_specialist_agent = None