from autogen_agentchat.agents import AssistantAgent
from config.settings import get_model_client

client = get_model_client()

def create_code_generator_agent():
    """
    Creates and configures an AssistantAgent for generating Python test code.

    Args:
        client: The model client instance to be used by the agent.

    Returns:
        An instance of autogen.AssistantAgent configured for Python code generation.
    """
    python_code_agent = AssistantAgent(
        name="CodeGeneratorAgent",
        description="This agent helps in Python code generation for the test cases.",
        model_client=client,
        system_message='''
        You are a Python code generator agent.
        Your role is to take the test cases provided by the TestCaseGenerator agent and implement them.

        Rules:
        1. pip install the library inbuilt in the code before importing it
        2. Implement each test case as a separate function.
        3. Use `assert` statements for validation.
        4. After each assertion passes, print "PASS: <test_name>".
        5. If an assertion fails, catch it with a try/except block and print "FAIL: <test_name>".
        6. Add a timeout of 10 seconds to every `requests` call.
        7. Do not use external testing frameworks like pytest or unittest.
        '''
    )
    return python_code_agent