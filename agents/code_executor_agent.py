from autogen_agentchat.agents import CodeExecutorAgent
from config.docker_executor import get_docker_executor


def get_code_executor_agent():
    """
    Function to get the code executor agent.
    This agent is responsible for executing code.
    It will work with the problem solver agent to execute the code.
    """
    docker = get_docker_executor()
    code_executor_agent = CodeExecutorAgent(
        name='CodeExecutorAgent',
        code_executor=docker,
        system_message='''  
    
        You are a Code Executor Agent.  
        Your role is to execute the provided Python test script.
        1. Collect all outputs:  
            - PASS messages  
            - Any AssertionErrors (FAIL)  
            - Any runtime errors (if occur).
        2. Return results in plain text so the FinalReportAgent can parse them.  
        '''
    )

    return code_executor_agent,docker
