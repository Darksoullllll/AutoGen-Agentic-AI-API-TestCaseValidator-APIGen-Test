import asyncio
from team.testcase_team import get_test_case_team_and_docker
from config.docker_utils import start_docker_container,stop_docker_container
from autogen_agentchat.messages import TextMessage
from autogen_agentchat.base import TaskResult


async def main():
    test_team , docker = get_test_case_team_and_docker()

    try:
        await start_docker_container(docker)
        print("Docker container started successfully.")
        
        task = "Generate test cases for API: https://reqres.in/api"

        async for message in test_team.run_stream(task=task):
            if isinstance(message, TextMessage):
                print('==' * 20)
                print(message.source, ":", message.content)
            elif isinstance(message,TaskResult):
                print('Stop Reason:',message.stop_reason)
    except Exception as e:
        print(f"Error: {e}")
    finally:
            #print("Stopping docker executor")
            await stop_docker_container(docker)

if __name__ == "__main__":
    asyncio.run(main())