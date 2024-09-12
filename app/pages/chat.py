import dash
from dash import dcc, html, callback, Input, Output
import dash_bootstrap_components as dbc
from openai import OpenAI
import os
import time

dash.register_page(__name__, name="Chat")

# Create the OpenAI client
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
)


############## put in other script
# Submitting a message
def submit_message(assistant_id, thread, user_message):
    client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=user_message,
    )
    return client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=assistant_id,
    )


# Retrieving a response
def get_response(thread):
    return client.beta.threads.messages.list(
        thread_id=thread.id,
        order="asc",
    )


# Creating a thread and running a message
def create_thread_and_run(user_input):
    thread = client.beta.threads.create()
    run = submit_message(
        os.getenv("ASSISTANT_ID"),
        thread,
        user_input,
    )
    return thread, run


# Waiting in a loop
def wait_on_run(run, thread):
    while run.status == "queued" or run.status == "in_progress":
        run = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id,
        )
        time.sleep(0.5)
    return run


############## put in other script


layout = dbc.Container(
    children=[
        html.H1("Chat with my CV"),
        html.P("This is a chat where you can ask questions about my CV."),
        dcc.Input(
            id="user-input",
            placeholder="This is a chat where you can ask questions about my CV.",
            type="text",
            debounce=True,
        ),
        html.Div(
            id="response-space",
            children="",
        ),
    ]
)


@callback(
    Output("response-space", "children"),
    Input("user-input", "value"),
    prevent_initial_call=True,
)
def activate_chat(input_value):
    if not input_value:
        return "Please enter a question."
    else:
        # chat_completion = client.chat.completions.create(
        #    model="gpt-4o-mini",
        #    max_tokens=150,
        #    messages=[
        #        {
        #            "role": "system",
        #            "content": "You are a helpful data science tutor.",
        #        },
        #        {
        #            "role": "user",
        #            "content": input_value,
        #        },
        #    ],
        #    stream=False,
        # )
        # print(chat_completion)
        # response = chat_completion.choices[0].message.content
        thread1, run1 = create_thread_and_run(input_value)
        run1 = wait_on_run(run1, thread1)
        response1 = get_response(thread1)
        return response1.data[1].content[0].text.value
