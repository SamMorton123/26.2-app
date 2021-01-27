'''
Streamlit "component" to render a sidebar
for the user to select the rankings for the
event they'd like to view.

Sam Morton, TwentySix.Two
January 26, 2020
'''


import json
import streamlit as st


def EventSelect():
    '''
    Sidebar "component" to allow the
    user to see any of the supported 
    rankings.
    '''

    # read into support data file
    with open('src/support_data/support_data.json') as f:
        SUPPORT_DATA = json.load(f)
    f.close()

    # get list of supported events
    supported_events = SUPPORT_DATA['supported_events']

    # render sidebar title
    st.markdown(f'''
        <div class="header">
            <h2> Select Any Event To View Rankings </h2>
        </div>
        <style>
            h2 {{
                display: flex;
                flex-direction: row;
                justify-content: center;
                align-items: center;
            }}
            .header {{
                padding: 50px 0px 0px 0px;
            }}
        </style>
    ''', unsafe_allow_html = True)

    # render sidebar with user options for supported events
    selected_event = st.selectbox('', supported_events)
    return selected_event
