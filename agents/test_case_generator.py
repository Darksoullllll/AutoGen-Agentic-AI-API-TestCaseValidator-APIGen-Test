from autogen_agentchat.agents import AssistantAgent
from config.settings import get_model_client



client = get_model_client()

def create_test_case_agent():
    """
    Creates and configures an AssistantAgent for generating API test cases.

    Args:
        client: The model client instance (e.g., OpenAIWrapper) to be used by the agent.

    Returns:
        An instance of autogen.AssistantAgent configured for test case generation.
    """
    test_case_agent = AssistantAgent(
        name="TestCaseGenerator",
        description="This agent helps in Test Case Generation",
        model_client=client,
        system_message='''
        You are a Test Case Generator for a given API URL.
        Your role is to analyze the provided API URL and generate a comprehensive set of test cases.

        Rules:
        1. Do not write any Python code.
        2. Only output a list of test cases in natural language with the following details for each:
           - Test Case Name
           - Expected Behavior
           - What should be validated
        3. Keep the test cases clear and concise so another agent can easily implement them in Python.
        4. Generate at least 10 valid test cases for the given API URL.
        '''
    )
    return test_case_agent