from autogen_agentchat.agents import AssistantAgent
from config.settings import get_model_client

client = get_model_client()

def create_report_generator_agent():
    """
    Creates and configures an AssistantAgent for generating a final test report.

    Args:
        client: The model client instance to be used by the agent.

    Returns:
        An instance of autogen.AssistantAgent configured for report generation.
    """
    report_agent = AssistantAgent(
        name="ReportGeneratorAgent",
        description="This agent helps in the Report Generation.",
        model_client=client,
        system_message='''
        You are a Final Report Agent.
        Your role is to convert execution results into a structured report.

        Rules:
        1. Parse the PASS/FAIL results from the CodeExecutor agent's output.
        2. Create a clean and concise markdown table with the following columns:
           - Test Case
           - Expected Result
           - Status (PASS/FAIL)
           - Fail Cause
        3. If no Fail Cause Mark None
        3. If execution errors occur, mark the corresponding test as FAIL and include the error message.
        4. End your final report with the word STOP.
        '''
    )
    return report_agent