from crewai import Agent, Crew, Task, LLM
from crewai_tools import SerperDevTool
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Content Researcher & Writer", page_icon="🤖", layout="wide")

st.title("Content Researcher & Writer, powered by CrewAI")
st.markdown("Generate blog post about any topic using AI agents")

with st.sidebar:
    st.header("Content Settings")
    topic = st.text_area("Enter your topic",
                height = 100,
                placeholder = "Enter your topic here")
    st.markdown("### LLM Settings")
    temperature = st.slider("Temperature", 0.0, 1.0, 0.7)

    st.markdown("---")

    generate_button = st.button("Generate Content", type = "primary", use_container_width = True)

    with st.expander("How to use"):
        st.markdown("""
        1. Enter your desired content topic
        2. Play with the temperature
        3. Click 'Generate Content' to start
        4. Wait for the AI to generate your article
        5. Download the result as a markdown file                        
        """)

def generate_content(topic):
    llm = LLM(
    model="gemini/gemini-1.5-pro-latest",
    temperature=0.7
)
#Tool 2
    search_tool = SerperDevTool(n=10)

    #Agent 1 , which be basically doing research work using serper
    senior_research_analyst = Agent(
    role="Senior Research Analyst",
    goal = "Research, analyze and synthesize complex information on the {topic} from reliable web sources",
    backstory = "You are an expert research analyst with advanced web research skills."
                "YOu are excel at finding, analyzing and synthesizing imformation from across"
                "the internet using search tools. You're skilled at"
                "distinguishing reliabke sources from unreliable one, fact-checking,"
                "cross-referencing information and indentifying key patterns and insights."
                "You provide well organized research briefs with proper citiation and source verification."
                "Your analysis include both raw data and interpreted insights, making complex information accessible and actionable.",
    allow_deligation = False, #Allow agents to delegate tasks to other agents
    verbose = True, #Prints the task details in terminal
    tools = [search_tool],
    llm = llm
    )

    # Agent 2, which will be writing the content

    content_writer = Agent(
    role = "Content Writer",
    goal = "Transform research finding into engaging blog post while maintaining accuracy",
    backstory = "You're a skilled content writer specialized in creating"
                "engaging, accessible content from technical research."
                "You work closely with the Senior Research Analyst and excel at maintaining the"
                "perfect balance between informative and entertaining writing while"
                "ensuring all facts and citations from the research are properly incorporated."
                "You have a talent for making complex topics approachable without oversimplifying them.",
    allow_delegation = False,
    verbose = True,
    llm = llm
    )

    # Now we will move onto task, we will create task in next step
    # Task 1 --> Research Task
    research_task = Task(
    description = ("""
        1. Conduct a comprehensive research on the topic "{topic}" including:
            - Recent developments and news
            - Key industry trends and innovation
            - Expert opinions and analysis
            - Statistical data and market insights
        2. Evaluate source credibility and fact-check all information.
        3. Organise finding into a structured research brief. 
        4. Include all relevent citations and sources.     
    """),
    expected_output = """A detailed reseach report comtaining:
                - Executive summary of key findings
                - Comprehensive analysis of recent trends and developments
                - List all varified facts and statistics
                - All citations and links to original sources
                - Clear categorization of main theme and pattern
                Please format with clear section and bullet points for easy reference.""",
    agent = senior_research_analyst            

    )    

    # Task 2 --> Content Writing Task
    content_writing_task = Task(
    description = (""" Using the research brief provided, create an engaging blog post that:
            1. Transforms technical information into accessible content
            2. Maintains all factual accuracy and and citation from the research
            3. Includes:
                - Attention grabbing introduction
                - Well-structured body section with clear headings
                - Compelling conclusion
            4. Preserves all source citation in [Source: url] formation
            5. Includes reference section in the end.  
    """),
    expected_output = (""" A polished blog post in markdown format that:
                - Engages readers with maintaining accuracy
                - Contains properly structure section
                - Includes Inline citations hyperlinked to the original source url
                - Presents information in an accessible yet informative way
                - Follows proper mardown formatting, use H1 for the title and H3 for the sub-headings
    """),
    agent = content_writer
    )
    
    crew = Crew(
     agents = [senior_research_analyst, content_writer],
     tasks = [research_task, content_writing_task],
     verbose = True
     )
    return crew.kickoff(inputs = {"topic": topic})

if generate_button:
    with st.spinner("Generating content... This may take a second"):
        try:
            result = generate_content(topic)
            st.markdown("### Content Generated")
            st.markdown(result)

            st.download_button(
                label = "Download Content",
                data = result.raw,
                file_name = f"{topic.lower().replace(' ', '_')}_article.md",
                mime = "text/markdown"
            )
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

st.markdown("---")
st.markdown("Built with CrewAI, chatgpt and Streamlit")            

    
