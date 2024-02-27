# 🔎 GPT Researcher

This is a fork of the original [gpt-researcher](https://github.com/assafelovic/gpt-researcher) project specialized to the **cybersecurity** use case (the bot only does research for cybersecurity topics). We also added two features:
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
```
sudo port install python310 py310-pip
```
- The following **optional** commands will set `python 3.10` as the default python environment
```
sudo port select --set python python310
sudo port select --set python3 python310
sudo port select --set pip pip310
sudo port select --set pip3 pip310
```
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
- If you encounter a `401 Error, Credentials not correct`, then run the following commands in the terminal
```
CODEARTIFACT_DOMAIN='infra-ark-target'
CODEARTIFACT_DOMAIN_OWNER=199883727417
CODEARTIFACT_REPOSITORY="infra-ark-target-prod"

aws codeartifact login --tool pip --region us-west-2 --domain ${CODEARTIFACT_DOMAIN} --domain-owner ${CODEARTIFACT_DOMAIN_OWNER} --repository ${CODEARTIFACT_REPOSITORY}
```
- Obtain the `awn-corp-ca-bundle.pem` from [Here](https://arcticwolf.egnyte.com/fl/JWQWMURrsc) (see also this [Guide](https://arcticwolf.atlassian.net/wiki/spaces/ENTSECARCH/pages/3503751721/Tool+Configuration+for+SASE+TLS+Inspection#Prisma-Access-CA-Certificate)) and **put** it in your `gpt-researcher-test` repo. 
- Create a `.env` file 
```
touch .env
```
and place your `OpenAI API Key` and `Tavily API Key` and the CA certificates inside 
```
OPENAI_API_KEY=<your OpenAI key>
TAVILY_API_KEY=<your Tavily key>
REQUESTS_CA_BUNDLE="awn-corp-ca-bundle.pem"
CURL_CA_BUNDLE="awn-corp-ca-bundle.pem"
SSL_CERT_FILE="awn-corp-ca-bundle.pem"
NODE_EXTRA_CA_CERTS="awn-corp-ca-bundle.pem"
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

