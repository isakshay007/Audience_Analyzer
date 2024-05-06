import streamlit as st
from lyzr_automata.ai_models.openai import OpenAIModel
from lyzr_automata import Agent, Task
from lyzr_automata.pipelines.linear_sync_pipeline import LinearSyncPipeline
from PIL import Image
from lyzr_automata.tasks.task_literals import InputType, OutputType
import os

# Set the OpenAI API key
os.environ["OPENAI_API_KEY"] = st.secrets["apikey"]

st.markdown(
    """
    <style>
    .app-header { visibility: hidden; }
    .css-18e3th9 { padding-top: 0; padding-bottom: 0; }
    .css-1d391kg { padding-top: 1rem; padding-right: 1rem; padding-bottom: 1rem; padding-left: 1rem; }
    </style>
    """,
    unsafe_allow_html=True,
)

image = Image.open("./logo/lyzr-logo.png")
st.image(image, width=150)

# App title and introduction
st.title("Audience Navigator")
st.markdown("Built using Lyzr SDK🚀")

input = st.text_input("Welcome to Audience Navigator, powered by Lyzr SDK! Simply input your company's name, core values, and goals to receive tailored marketing strategies and actionable steps from our expert COPYWRITER agent, designed to resonate with your target audience and achieve your marketing objectives. Let's navigate your audience together!",placeholder=f"""Type here""")

open_ai_text_completion_model = OpenAIModel(
    api_key=st.secrets["apikey"],
    parameters={
        "model": "gpt-4-turbo-preview",
        "temperature": 0.2,
        "max_tokens": 1500,
    },
)


def generation(input):
    generator_agent = Agent(
        role=" COPYWRITER expert",
        prompt_persona=f"  Your task is to utilize the PROVIDED COMPANY INFORMATION and its goals to thoroughly understand the TARGET AUDIENCE, including DEMOGRAPHICS, INTERESTS, PAIN POINTS, and PREFERRED SOCIAL MEDIA PLATFORMS. You MUST also deliver TAILORED MARKETING STRATEGIES and ACTIONABLE STEPS.")

    prompt = f"""
You are an Expert COPYWRITER with a focus on MARKET RESEARCH and STRATEGY DEVELOPMENT. Your task is to utilize the PROVIDED COMPANY INFORMATION and its goals to thoroughly understand the TARGET AUDIENCE, including DEMOGRAPHICS, INTERESTS, PAIN POINTS, and PREFERRED SOCIAL MEDIA PLATFORMS. You MUST also deliver TAILORED MARKETING STRATEGIES and ACTIONABLE STEPS.

Here's how you should proceed:

1. ANALYZE the company information provided to grasp the ESSENCE of the brand, its products or services, and its overarching goals.

2. CONDUCT RESEARCH to identify the target audience's demographics such as age, gender, location, income level, education, and occupation.

3. IDENTIFY common pain points that your client's product or service can solve for this audience.

4. FIND OUT which social media platforms are most frequented by this demographic to ensure effective reach.

5. DEVELOP marketing strategies that are SPECIFICALLY TAILORED to resonate with the identified target audience.

6. CREATE actionable steps that can be implemented immediately for each strategy to guide your client towards achieving their marketing goals.
 """

    generator_agent_task = Task(
        name="Generation",
        model=open_ai_text_completion_model,
        agent=generator_agent,
        instructions=prompt,
        default_input=input,
        output_type=OutputType.TEXT,
        input_type=InputType.TEXT,
    ).execute()

    return generator_agent_task 
   
if st.button("Ok"):
    solution = generation(input)
    st.markdown(solution)

with st.expander("ℹ️ - About this App"):
    st.markdown("""
    This app uses Lyzr Automata Agent . For any inquiries or issues, please contact Lyzr.

    """)
    st.link_button("Lyzr", url='https://www.lyzr.ai/', use_container_width=True)
    st.link_button("Book a Demo", url='https://www.lyzr.ai/book-demo/', use_container_width=True)
    st.link_button("Discord", url='https://discord.gg/nm7zSyEFA2', use_container_width=True)
    st.link_button("Slack",
                   url='https://join.slack.com/t/genaiforenterprise/shared_invite/zt-2a7fr38f7-_QDOY1W1WSlSiYNAEncLGw',
                   use_container_width=True)
