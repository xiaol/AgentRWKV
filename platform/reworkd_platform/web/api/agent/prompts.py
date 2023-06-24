from langchain import PromptTemplate

# Create initial tasks using plan and solve prompting
# https://github.com/AGI-Edgerunners/Plan-and-Solve-Prompting
# start_goal_prompt = PromptTemplate(
#     template="""You are a task creation AI called AgentGPT. You answer in the
#     "{language}" language. You are not a part of any system or device. You first
#     understand the problem, extract relevant variables, and make and devise a
#     complete plan.\n\n You have the following objective "{goal}". Create a list of step
#     by step actions to accomplish the goal. Use at most 4 steps.

#     Return the response as a formatted array of strings that can be used in JSON.parse()

#     Examples:
#     ["Search the web for NBA news relating to Stephen Curry", "Write a report on the financial state of Nike"]
#     ["Create a function to add a new vertex with a specified weight to the digraph."]
#     ["Search for any additional information on Bertie W.", "Research the best kentucky fried Chicken recipe"]
#     """,
#     input_variables=["goal", "language"],
# )
start_goal_prompt_system = PromptTemplate(
    template="""I am a task creation AI called AgentRWKV. my answer in the
    "{language}" language. I am not a part of any system or device. I first
    understand the problem, extract relevant variables, and make and devise a
    complete plan. 
    """,
    input_variables=["language"],
)

start_goal_prompt = PromptTemplate(
    template="""You have the following objective "{goal}". Create a list of 4 step actions to accomplish the goal. Use at most 4 steps.\nlist:1.""",
    input_variables=["goal"],
)

# analyze_task_prompt = PromptTemplate(
#     template="""
#     High level objective: "{goal}"
#     Current task: "{task}"

#     Based on this information, use the best function to make progress or accomplish the task entirely.
#     Select the correct function by being smart and efficient. Ensure "reasoning" and only "reasoning" is in the 
#     {language} language.
    
#     Note you MUST select a function.
#     """,
#     input_variables=["goal", "task", "language"],
# )

analyze_task_prompt = PromptTemplate(
    template="""
    High level objective: "{goal}"
    Current task: "{task}"
    Function: [Reason, Conclude, Search, Code]

    Based on this information, use the best function to make progress or accomplish the task entirely.
    Select the correct function by being smart and efficient. 
    
    Note you MUST select a function from list [Reason, Conclude, Search, Code]
    """,
    input_variables=["goal", "task"],
)

code_prompt = PromptTemplate(
    template="""
    You are a world-class software engineer and an expert in all programing languages,
    software systems, and architecture.

    For reference, your high level goal is {goal}

    Write code in English but explanations/comments in the "{language}" language.
    
    Provide no information about who you are and focus on writing code.
    Ensure code is bug and error free and explain complex concepts through comments
    Respond in well-formatted markdown. Ensure code blocks are used for code sections.
    Approach problems step by step and file by file, for each section, use a heading to describe the section.

    Write code to accomplish the following:
    {task}
    """,
    input_variables=["goal", "language", "task"],
)

execute_task_prompt = PromptTemplate(
    template="""Answer in the "{language}" language. Given
    the following overall objective `{goal}` and the following sub-task, `{task}`.

    Perform the task by understanding the problem, extracting variables, and being smart
    and efficient. Write a detailed response that address the task.
    When confronted with choices, make a decision yourself with reasoning.
    """,
    input_variables=["goal", "language", "task"],
)

# create_tasks_prompt = PromptTemplate(
#     template="""You are an AI task creation agent. You must answer in the "{language}"
#     language. You have the following objective `{goal}`. You have the
#     following incomplete tasks `{tasks}` and have just executed the following task
#     `{lastTask}` and received the following result `{result}`.

#     Based on this, create a single new task to be completed by your AI system
#     such that your goal is more closely reached or completely reached.
#     Make the task as specific as possible and ensure it is a single task. 
#     If there are no more tasks to be done, return nothing. Do not add quotes to the task.

#     Examples:
#     "Search the web for NBA news"
#     "Create a function to add a new vertex with a specified weight to the digraph."
#     "Search for any additional information on Bertie W."
#     ""
#     """,
#     input_variables=["goal", "language", "tasks", "lastTask", "result"],
# )

create_tasks_prompt_system = PromptTemplate(
    template="""I am an AI task creation agent. I must answer in the "{language}" language. 
    """,
    input_variables=["language"],
)

create_tasks_prompt = PromptTemplate(
    template="""You have the following objective `{goal}`. You have the following incomplete tasks `{tasks}` and have just executed the following task `{lastTask}` and received the following result `{result}`.

    Based on this, create a single new task to be completed by your AI system such that your goal is more closely reached or completely reached.Make the task as specific as possible and ensure it is a single task. If there are no more tasks to be done, return nothing. Do not add quotes to the task.
    """,
    input_variables=["goal", "language", "tasks", "lastTask", "result"],
)

# summarize_prompt = PromptTemplate(
#     template="""You must answer in the "{language}" language. 
    
#     Parse and summarize the following text snippets "{snippets}".
#     Write using clear markdown formatting in a style expected of the goal "{goal}".
#     Be as clear, informative, and descriptive as necessary and attempt to
#     answer the query: "{query}" as best as possible.
    
#     Cite sources for as many sentences as possible via the source link. Use the index as the citation text.
#     Site the source using a markdown link directly at the end of the sentence that the source is used in. 
#     Do not list sources at the end of the writing. 
    
#     Example: "So this is a cited sentence at the end of a paragraph[1](https://test.com). This is another sentence." 
#     """,
#     input_variables=["goal", "language", "query", "snippets"],
# )

summarize_prompt = PromptTemplate(
    template="""You must answer in the "{language}" language. 
    
    Parse and summarize the following text snippets "{snippets}".
    Write using clear markdown formatting in a style expected of the goal "{goal}".
    Be as clear, informative, and descriptive as necessary and attempt to
    answer the query: "{query}" as best as possible.
    
    Cite sources for as many sentences as possible via the source link. Use the index as the citation text.
    Site the source using a markdown link directly at the end of the sentence that the source is used in. 
    Do not list sources at the end of the writing. 
    """,
    input_variables=["goal", "language", "query", "snippets"],
)

