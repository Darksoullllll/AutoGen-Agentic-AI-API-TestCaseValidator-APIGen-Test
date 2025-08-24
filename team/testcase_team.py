from agents.final_report_agent import create_report_generator_agent
from agents.test_case_generator import create_test_case_agent
from agents.python_code_generator import create_code_generator_agent
from agents.code_executor_agent import get_code_executor_agent
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.conditions import TextMentionTermination

from config.constant import TEXT_MENTION,MAX_TURNS

def get_test_case_team_and_docker():

    test_case_agent = create_test_case_agent()
    python_code_agent = create_code_generator_agent()
    code_executor_agent, docker = get_code_executor_agent()
    final_agent = create_report_generator_agent()

    termination_condition = TextMentionTermination(TEXT_MENTION)

    team = RoundRobinGroupChat(
        participants=[
            test_case_agent,
            python_code_agent,
            code_executor_agent,
            final_agent
        ],
        termination_condition=termination_condition,  # You can set a termination condition if needed
        max_turns=MAX_TURNS
    )
    
    return team,docker