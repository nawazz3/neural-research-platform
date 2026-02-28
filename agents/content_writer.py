# import os
# from crewai import Agent, LLM
# from crewai_tools import FileWriterTool


# # LLM configurations - Agent specific config
# model = os.getenv("WRITER_AGENT_LLM")
# temperature = float(os.getenv("WRITER_AGENT_TEMPERATURE"))

# llm = LLM(
#     model=model,
#     temperature=temperature
# )

# content_writer_agent = Agent(
#     role="Content Writer",
#     goal="Create comprehensive, well-structured reports and summaries",
#     backstory = (
#                 "You are a professional content writer with expertise in creating "
#                 "clear, engaging, and well-structured documents. You can transform complex "
#                 "information into accessible and compelling content."
#             ),
#     llm=llm,
#     tools=[FileWriterTool()],
#     verbose=True,
# )
"""
agents/content_writer.py
Content Writer Agent with error handling
"""

import os
import logging
from typing import Optional
from crewai import Agent, LLM

logger = logging.getLogger(__name__)


def get_llm() -> Optional[LLM]:
    """Initialize LLM for writer agent"""
    try:
        model = os.getenv("WRITER_AGENT_LLM", "groq/mixtral-8x7b-32768")
        temperature = float(os.getenv("WRITER_AGENT_TEMPERATURE", "0.7"))
        
        # Validate temperature
        if temperature < 0 or temperature > 1:
            temperature = 0.7
        
        llm = LLM(model=model, temperature=temperature)
        logger.info(f"✅ Writer LLM initialized: {model}")
        return llm
    
    except Exception as e:
        logger.error(f"Failed to initialize Writer LLM: {e}")
        return None


def create_content_writer_agent() -> Optional[Agent]:
    """Create Content Writer Agent"""
    try:
        llm = get_llm()
        if not llm:
            logger.error("Cannot create Content Writer: LLM failed")
            return None
        
        # Try to load tools
        tools = []
        try:
            from crewai_tools import FileWriterTool
            tools = [FileWriterTool()]
            logger.info("✅ FileWriterTool loaded")
        except Exception as e:
            logger.warning(f"FileWriterTool not available: {e}")
        
        agent = Agent(
            role="Content Writer",
            goal="Create comprehensive, well-structured reports and summaries",
            backstory=(
                "You are a professional content writer with expertise in creating clear, engaging, "
                "and well-structured documents. You can transform complex information into accessible "
                "and compelling content."
            ),
            llm=llm,
            tools=tools,
            verbose=True,
            allow_delegation=False,
        )
        
        logger.info("✅ Content Writer Agent created successfully")
        return agent
    
    except Exception as e:
        logger.error(f"Failed to create Content Writer Agent: {e}")
        logger.exception("Full traceback:")
        return None


# Create agent instance
try:
    content_writer_agent = create_content_writer_agent()
except Exception as e:
    logger.error(f"Error in content_writer.py: {e}")
    content_writer_agent = None