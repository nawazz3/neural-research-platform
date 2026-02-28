# import textwrap

# from crewai import Task
# from agents.research_specialist import research_specialist_agent


# research_task = Task(
#     agent=research_specialist_agent,
#     description=textwrap.dedent("""
#                 Conduct comprehensive research on the topic: {topic}

#                 Your tasks:
#                 1. Search for the most current and relevant information
#                 2. Gather data from multiple reliable sources
#                 3. Identify key facts, statistics, and expert opinions
#                 4. Organize findings in a structured format
#                 5. Ensure information is accurate and up-to-date

#                 Provide a detailed research summary with:
#                 - Key findings
#                 - Important statistics
#                 - Expert opinions
#                 - Recent developments
#                 - Reliable sources used
#                 """),
#     expected_output="A comprehensive research summary with key findings, statistics, expert opinions, recent developments, and sources",
#     output_file="research_findings.md"
#     )
"""
tasks/research_task.py
Research Task with error handling
"""

import textwrap
import logging
from typing import Optional
from crewai import Task

logger = logging.getLogger(__name__)


def create_research_task(agent) -> Optional[Task]:
    """Create research task"""
    if agent is None:
        logger.error("Cannot create research task: agent is None")
        return None
    
    try:
        task = Task(
            agent=agent,
            description=textwrap.dedent("""
                Conduct comprehensive research on the given topic.
                
                Your tasks:
                1. Search for the most current and relevant information
                2. Gather data from multiple reliable sources
                3. Identify key facts, statistics, and expert opinions
                4. Organize findings in a structured format
                5. Ensure information is accurate and up-to-date
                
                Provide a detailed research summary with:
                - Key findings
                - Important statistics
                - Expert opinions
                - Recent developments
                - Reliable sources used
                """),
            expected_output=(
                "A comprehensive research summary with key findings, statistics, "
                "expert opinions, recent developments, and sources"
            ),
            output_file="output/research_findings.md"
        )
        
        logger.info("✅ Research task created successfully")
        return task
    
    except Exception as e:
        logger.error(f"Failed to create research task: {e}")
        logger.exception("Full traceback:")
        return None


# Create task instance
try:
    from agents.research_specialist import research_specialist_agent
    research_task = create_research_task(research_specialist_agent)
    
    if research_task:
        logger.info("✅ research_task module loaded successfully")
    else:
        logger.warning("⚠️ research_task is None")

except Exception as e:
    logger.error(f"Error in research_task.py: {e}")
    logger.exception("Full traceback:")
    research_task = None