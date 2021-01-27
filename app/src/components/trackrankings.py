'''
Streamlit "component" for rendering 
track rankings.

Sam Morton, TwentySix.Two
January 26, 2020
'''


import pandas as pd
import plotly.graph_objects as go
import streamlit as st


# constants
CURR_YEAR = 2020
TABLE_WIDTH = 1350
TABLE_HEIGHT = 700



def TrackRankings(selected_event):
    '''
    Render most recent track rankings.
    '''

    # load most recent rankings for selected event
    selected_event_altered = selected_event.replace("'", '').replace(' ', '_').lower()
    event_filename = f'../data/generated_ratings_data/{selected_event_altered}_{CURR_YEAR}.csv'
    df = pd.read_csv(event_filename)
    
    # reformat data for viewing
    df = df[df['Most Recent Race Date'] >= CURR_YEAR - 2]
    df = df.drop(columns = ['Most Recent Race Date'])
    df = df[df['Number Of Races']  > 2]
    df = df.iloc[0: 20, :]
    df['Rating'] = [round(score - 1500, 2) for score in df['Rating']]
    df.columns = ['athlete', 'rating', 'num_races', 'nationality', 'dob']
    df.index = list(range(1, len(df.index) + 1))

    # create figure
    fig = go.Figure(
        data = [go.Table(
            header = dict(
                values = ['Rank', 'Athlete', 'Rating', 'Number of Races', 'Nationality', 'Date of Birth'],
                fill_color = '#D03737',
                font = dict(color = 'white')
            ),
            cells = dict(
                values = [
                    df.index, df.athlete, df.rating, df.num_races, df.nationality, df.dob
                ],
                fill_color = 'white'
            )
        )],
        layout = dict(
            width = TABLE_WIDTH,
            height = TABLE_HEIGHT
        )
    )

    # render plotly figure
    st.plotly_chart(fig)
