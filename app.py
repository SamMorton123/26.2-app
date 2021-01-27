'''
Simple Streamlit app to showcase TwentySix.Two's
track rankings.

Sam Morton, TwentySix.Two
January 26, 2020
'''


import streamlit as st

# local
from src.components.logo import Logo
from src.components.eventselect import EventSelect
from src.components.styleconfig import StyleConfig
from src.components.trackrankings import TrackRankings


# app info
PAGE_TITLE = 'TwentySix.Two - Professional Track Ratings and More'
VERSION = 'Version 1.1'

# set page config
st.set_page_config(
    page_title = PAGE_TITLE,
    layout = 'centered'
)


# --------- Main ---------- #

# style page
StyleConfig()

# import logo
Logo(version = VERSION)

# user selects event to view from sidebar
selected_event = EventSelect()

# rankings are rendered
TrackRankings(selected_event)
