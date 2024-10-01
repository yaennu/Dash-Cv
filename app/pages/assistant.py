import dash
from dash import dcc, html, callback, Input, Output
import dash_bootstrap_components as dbc
from openai import OpenAI
import os
import time
import re

dash.register_page(__name__, name="Assistant")

# Create the OpenAI client
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
)


############## put in other script?
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
        assistant_id=os.getenv("ASSISTANT_ID"),
        thread=thread,
        user_message=user_input,
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


##############


layout = dbc.Container(
    children=[
        html.H1("Ask my CV"),
        html.P(
            """Here you can ask my OpenAI assistant questions about my CV. 
            The assistant will answer in the language in which you asked the 
            question. The assistant will perform a file search on my CV and 
            should not answer if it has not found the answer in my CV. But it 
            is an AI, so watch out for hallucinations."""
        ),
        dbc.Input(
            id="user-input",
            placeholder="Ask something about my CV.",
            type="text",
            debounce=True,
            maxLength=500,
            size="md",
            style={"margin-bottom": "1rem"},
        ),
        dbc.Button(
            children="Submit",
            id="submit-btn",
            style={"margin-bottom": "1rem"},
        ),
        dcc.Loading(
            html.Div(
                id="response-space",
                children="",
            ),
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
        thread1, run1 = create_thread_and_run(input_value)
        run1 = wait_on_run(run1, thread1)
        response1 = get_response(thread1)
        clean_response = re.sub(
            "【.*?†source】",
            "",
            response1.data[1].content[0].text.value,
        )
        return clean_response
