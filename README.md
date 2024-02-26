# 🔎 GPT Researcher

This is a fork of the original [gpt-researcher](https://github.com/assafelovic/gpt-researcher) project. We added two features:
- Ability to select an OpenAI model. 
- Ability to add multiple queries/tasks. 

See the app in action [**Here**](https://arcticwolf.egnyte.com/dl/arfsivWOHD) (play at 2x speed).

**GPT Researcher is an autonomous agent designed for comprehensive online research on a variety of tasks.** 

The agent can produce detailed, factual and unbiased research reports, with customization options for focusing on relevant resources, outlines, and lessons. Inspired by the recent [Plan-and-Solve](https://arxiv.org/abs/2305.04091) and [RAG](https://arxiv.org/abs/2005.11401) papers, GPT Researcher addresses issues of speed, determinism and reliability, offering a more stable performance and increased speed through parallelized agent work, as opposed to synchronous operations.

**Our mission is to empower individuals and organizations with accurate, unbiased, and factual information by leveraging the power of AI.**

## How to run the app on your laptop (M1 Mac)
- Request `rnd_tas` for access to **OpenAI API Key** 
- Obtain **Tavily API Key** from [Tavily AI](https://tavily.com/) (free for 1000 requests).
- Install `python 3.10` on your Mac via MacPorts following this [Guide](https://arcticwolf.atlassian.net/wiki/spaces/PD/pages/3667199471/Tom+New+Laptop+RnD+Setup#Backend-Development). 
- On your terminal, clone the repo to your local directory
```
git clone https://github.com/huanvoAWN/gpt-researcher-test.git
cd gpt-researcher-test
```
- Check out the `development` branch 
```
git checkout development
```
- Create the python env 
```
python3.10 -m venv venv 
source venv/bin/activate 
pip install --upgrade pip 
pip install -r requirements.txt
```
- Create a `.env` file 
```
touch .env
```
and place your `OpenAI API Key` and `Tavily API Key` inside 
```
OPENAI_API_KEY=<your OpenAI key>
TAVILY_API_KEY=<your Tavily key>
```
- Run the streamlit app on your preferred port (default is 8501)
```
streamlit run st_app.py --server.port <your preferred port>
```
- Access the app on your local browser (Chrome)
```
localhost:<your preferred port>
```

## Why GPT Researcher?

- To form objective conclusions for manual research tasks can take time, sometimes weeks to find the right resources and information.
- Current LLMs are trained on past and outdated information, with heavy risks of hallucinations, making them almost irrelevant for research tasks.
- Solutions that enable web search (such as ChatGPT + Web Plugin), only consider limited resources and content that in some cases result in superficial conclusions or biased answers.
- Using only a selection of resources can create bias in determining the right conclusions for research questions or tasks. 

