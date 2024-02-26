import streamlit as st 
import asyncio
from gpt_researcher.master.agent import GPTResearcher
from dotenv import find_dotenv, load_dotenv  # find .env file
import os 
import openai
import time 

# get openai api key #################################
_ = load_dotenv(find_dotenv())  # read local .env file
openai.api_key = os.getenv("OPENAI_API_KEY", None)


async def run_agent(query, 
                    report_type, 
                    max_search_results_per_query,
                    report_model):
    """Run the agent."""
    # run agent
    researcher = GPTResearcher(query=query, report_type=report_type, 
                               auto_generate_agent=False,
                               max_search_results_per_query=max_search_results_per_query,
                               report_model = report_model)
    report = await researcher.run()

    return report

async def main(query, 
               report_type,
               max_search_results_per_query,
               report_model
               ):
    start = time.time()
    result = await run_agent(query, report_type, max_search_results_per_query, report_model)
    elapsed = time.time()-start
    st.session_state['report'] = result
    st.session_state['report_time'] = f"Powered by {report_model}, run time {elapsed:.2f} seconds"

# sidebar ###############
with st.sidebar:
    st.header(":blue[LLM Models]")

    # select the language model ######################
    models = [
        "gpt-4-turbo-preview",  # points to gpt-4-0125-preview, 128k context window
        "gpt-4-1106-preview",  # gpt-4-turbo, 128k context window
        "gpt-4",  # points to gpt-3-0613, 8k context window, quite slow
        "gpt-3.5-turbo-1106",  # latest gpt-3.5-turbo, 16k context window
        "gpt-3.5-turbo-16k",  # points to gpt-3.5-turbo-16k-0613, 16k context window
        "gpt-3.5-turbo",  # points to gpt-3.5-turbo-0613, 4k context window
    ]

    model_type = st.selectbox(
        "Select an Open AI Chat Model:",
        models,
        help="""Select a chat model from Open AI API: \
                - 'gpt-4-turbo-preview': points to gpt-4-0125-preview, 128k context window; \
                - 'gpt-4-1106-preview': has 128k context window; \
                - 'gpt-4': points to gpt-3-0613, 8k context window, quite slow; \
                - 'gpt-3.5-turbo-1106': latest gpt-3.5-turbo, 16k context window; \
                - 'gpt-3.5-turbo-16k': points to gpt-3.5-turbo-16k-0613, with 16k context window; \
                - "gpt-3.5-turbo": points to gpt-3.5-turbo-0613, 4k context window;
            """,
    )

    st.info(
        "- Please refresh the streamlit app if you want to change the LLM model. \n - Please refresh the streamlit app if you want to change the tasks. \n - Please refresh the streamlit app if you encounter an error. "
    )


# title of the webpage 
st.header("GPT Researcher")

# add the first query with default value
if 'query' not in st.session_state:
    st.session_state['query'] = ["Are there public POC exploit of CVE-2023-38545? If there are, provide Github repos"]

if 'query_cnt' not in st.session_state:
    st.session_state['query_cnt'] = 1

if 'report' not in st.session_state:
    st.session_state['report'] = ''

# display the first query
st.session_state['query'][0] = st.text_input(label = "Enter the query/task 1",
                                             value = st.session_state['query'][0],
                                             help = "Input the task to be researched by gpt")


# increase the task count when a button is clicked
if st.button(":red[Add More Queries/Tasks]"):
    st.session_state['query_cnt'] += 1

# display the remaining queries
for i in range(1, st.session_state['query_cnt']):
    if i < len(st.session_state['query']):
        st.session_state['query'][i] = st.text_input(label = f"Enter the query/task {i+1}",
                                                     value = st.session_state['query'][i],
                                                     help = "Input the task to be researched by gpt"
                                                     )
    else:
        new_query = st.text_input(label = f"Enter the query/task {i+1}",
                                  value = "",
                                  help = "Input the task to be researched by gpt"
                                  )
        st.session_state['query'].append(new_query)


# display success message 
if st.session_state['query_cnt']>1:
    st.success(f"Add {st.session_state['query_cnt']} tasks")

# select the report type 
report_type = st.selectbox(
    "What is the report type?",
    options=['research_report','resource_report'],
    index = 1,
    help="research_report: output research report; resource_report: output list of references"
)

# number of URLs per query 
max_search_results_per_query = st.selectbox(
    "Number of search results per query",
    options=[1,3,5,10],
    index = 1,
    help="number of returned urls per query"
)

# generate report
if st.button(':red[Generate Report]'):
    with st.spinner('Researching....'):
        asyncio.run(main(st.session_state['query'], report_type, max_search_results_per_query, model_type))

# display and download report
if st.session_state['report']:
    st.write(st.session_state['report'])
    st.info(st.session_state['report_time'])
    st.download_button(
    label=":red[Download Report]",
    data=st.session_state['report'],
    file_name='report.md')