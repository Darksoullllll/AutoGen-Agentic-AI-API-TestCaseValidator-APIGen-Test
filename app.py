import streamlit as st
from team.testcase_team import get_test_case_team_and_docker
from config.docker_utils import start_docker_container,stop_docker_container
from autogen_agentchat.messages import TextMessage
from autogen_agentchat.base import TaskResult
import asyncio




st.title("APIGen-Test")
st.write("Welcome to APIGen-Test, your personal API URL Tester! Here you can paste the API Url and our system test the API on our half")

task = st.text_input("Enter your API url here: ")
task = "Generate test cases for"+task

async def run(team,docker,task):
    try:
        await start_docker_container(docker)
        async for message in team.run_stream(task=task):
            if isinstance(message, TextMessage):
                print(msg:= f"{message.source} : {message.content}")
                yield msg
            elif isinstance(message, TaskResult):
                print(msg:= f"Stop Reason: {message.stop_reason}")
                yield msg
        print("Task Completed")
    except Exception as e:
        print(f"Error: {e}")
        yield f"Error: {e}"
    finally:
        await stop_docker_container(docker)


if st.button("Run"):
    st.write("Running the Task..")

    team,docker = get_test_case_team_and_docker()

    async def collect_messages():
        async for msg in run(team,docker,task):
            if isinstance(msg, str):
                if msg.startswith("user"):
                    with st.chat_message('user',avatar='👤'):
                        st.markdown(msg)
                elif msg.startswith('TestCaseGenerator'):
                    with st.chat_message('Case Assistant',avatar='🧑‍💻'):
                        st.markdown(msg)
                elif msg.startswith('CodeGeneratorAgent'):
                    with st.chat_message('code Assistant',avatar='🧑‍💻'):
                        st.code(msg)
                elif msg.startswith('CodeExecutorAgent'):
                    with st.chat_message('assistant',avatar='🤖'):
                        st.code(msg)
                elif msg.startswith('ReportGeneratorAgent'):
                    with st.chat_message('Final Assistant',avatar='🧑‍💻'):
                        st.markdown(msg)
            elif isinstance(msg, TaskResult):
                with st.chat_message('stopper',avatar='🚫'):
                    st.markdown(f"Task Completed: {msg.result}")
    
    asyncio.run(collect_messages())
            
