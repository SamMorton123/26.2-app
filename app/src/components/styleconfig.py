'''
Streamlit "component" for addressing
the page's style. Based on Piyush Mishra's
style updates in Fiona.

Sam Morton, TwentySix.Two
January 26, 2020
'''


import streamlit as st


def StyleConfig():
    style_html = f'''
        <style>
            .reportview-container .main .block-container{{
                max-width: {1350}px;
                padding-top: {0}rem;
                padding-right: {-15}rem;
                padding-left: {-15}rem;
                padding-bottom: {5}rem;
            }}
        </style>
    '''

    st.markdown(style_html, unsafe_allow_html = True)
