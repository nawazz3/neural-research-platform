# import textwrap

# from crewai import Task
# from agents.data_analyst import data_analyst_agent
# from tasks.research_task import research_task


# analysis_task = Task(
#     agent=data_analyst_agent,
#     description=textwrap.dedent("""
#                 Analyze the research findings for the topic: {topic}

#                 Your tasks:
#                 1. Review the research findings from the previous task
#                 2. Identify patterns, trends, and key insights
#                 3. Analyze the implications and significance
#                 4. Provide expert interpretation of the data
#                 5. Highlight the most important conclusions

#                 Provide:
#                 - Key insights and patterns
#                 - Trend analysis
#                 - Implications and significance
#                 - Expert interpretation
#                 - Actionable conclusions
#                 """),
#     expected_output="A detailed analysis report with insights, patterns, and conclusions",
#     context=[research_task],
#     output_file="analysis_report.md"
#     )
"""
tasks/analysis_task.py
Analysis Task with error handling and dependencies
"""

import textwrap
import logging
from typing import Optional
from crewai import Task

logger = logging.getLogger(__name__)


def create_analysis_task(agent, research_task_obj=None) -> Optional[Task]:
    """Create analysis task"""
    if agent is None:
        logger.error("Cannot create analysis task: agent is None")
        return None
    
    try:
        # Prepare context from research task
        context = []
        if research_task_obj:
            context.append(research_task_obj)
            logger.info("✅ Research task added to analysis context")
        
        task = Task(
            agent=agent,
            description=textwrap.dedent("""
                Analyze the research findings for the topic.
                
                Your tasks:
                1. Review the research findings from the previous task
                2. Identify patterns, trends, and key insights
                3. Analyze the implications and significance
                4. Provide expert interpretation of the data
                5. Highlight the most important conclusions
                
                Provide:
                - Key insights and patterns
                - Trend analysis
                - Implications and significance
                - Expert interpretation
                - Actionable conclusions
                """),
            expected_output=(
                "A detailed analysis report with insights, patterns, "
                "and conclusions based on research findings"
            ),
            context=context,
            output_file="output/analysis_report.md"
        )
        
        logger.info("✅ Analysis task created successfully")
        return task
    
    except Exception as e:
        logger.error(f"Failed to create analysis task: {e}")
        logger.exception("Full traceback:")
        return None


# Create task instance
try:
    from agents.data_analyst import data_analyst_agent
    from tasks.research_task import research_task
    
    analysis_task = create_analysis_task(data_analyst_agent, research_task)
    
    if analysis_task:
        logger.info("✅ analysis_task module loaded successfully")
    else:
        logger.warning("⚠️ analysis_task is None")

except Exception as e:
    logger.error(f"Error in analysis_task.py: {e}")
    logger.exception("Full traceback:")
    analysis_task = None