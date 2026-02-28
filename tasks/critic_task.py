# import textwrap

# from crewai import Task
# from agents.qa_reviewer import qa_reviewer_agent
# from tasks.writing_task import writing_task


# critic_task = Task(
#     agent=qa_reviewer_agent,
#     description=textwrap.dedent("""
#                 Review and critique the final report for the topic: {topic}

#                 Your tasks:
#                 1. Evaluate the final written report for accuracy, clarity, and completeness
#                 2. Identify logical gaps, unclear explanations, or weak arguments
#                 3. Check for consistency between research, analysis, and writing
#                 4. Suggest improvements in structure, tone, and readability
#                 5. Ensure conclusions are well-supported and sources are correctly used

#                 Provide:
#                 - A detailed critique of the report
#                 - A list of corrections or improvements
#                 - Suggestions for enhancing clarity and coherence
#                 - Specific notes on factual or logical issues
#                 """),
#     expected_output="A thorough critique with detailed suggestions for improvements and corrections",
#     context=[writing_task],
#     output_file="critic_review.md"
# )
"""
tasks/critic_task.py
Critic/QA Task with error handling and dependencies
"""

import textwrap
import logging
from typing import Optional
from crewai import Task

logger = logging.getLogger(__name__)


def create_critic_task(agent, writing_task_obj=None) -> Optional[Task]:
    """Create critic/QA task"""
    if agent is None:
        logger.error("Cannot create critic task: agent is None")
        return None
    
    try:
        # Prepare context from writing task
        context = []
        if writing_task_obj:
            context.append(writing_task_obj)
            logger.info("✅ Writing task added to critic context")
        
        task = Task(
            agent=agent,
            description=textwrap.dedent("""
                Review and critique the final report for the topic.
                
                Your tasks:
                1. Evaluate the final written report for accuracy, clarity, and completeness
                2. Identify logical gaps, unclear explanations, or weak arguments
                3. Check for consistency between research, analysis, and writing
                4. Suggest improvements in structure, tone, and readability
                5. Ensure conclusions are well-supported and sources are correctly used
                
                Provide:
                - A detailed critique of the report
                - A list of corrections or improvements
                - Suggestions for enhancing clarity and coherence
                - Specific notes on factual or logical issues
                - Final quality assessment
                """),
            expected_output=(
                "A thorough critique with detailed suggestions for improvements, "
                "corrections, and a quality assessment"
            ),
            context=context,
            output_file="output/critic_review.md"
        )
        
        logger.info("✅ Critic task created successfully")
        return task
    
    except Exception as e:
        logger.error(f"Failed to create critic task: {e}")
        logger.exception("Full traceback:")
        return None


# Create task instance
try:
    from agents.qa_reviewer import qa_reviewer_agent
    from tasks.writing_task import writing_task
    
    critic_task = create_critic_task(qa_reviewer_agent, writing_task)
    
    if critic_task:
        logger.info("✅ critic_task module loaded successfully")
    else:
        logger.warning("⚠️ critic_task is None")

except Exception as e:
    logger.error(f"Error in critic_task.py: {e}")
    logger.exception("Full traceback:")
    critic_task = None