'''
Treating the TwentySix.Two Streamlit
app like a React app by separating
things into components. This is a 
rudimentary first pass at a 
TwentySix.Two logo.
'''


import streamlit as st


def Logo(version = None):
    '''
    Streamlit "component" for rendering the TwentySix.Two
    logo.
    '''

    # display logo
    cols = st.beta_columns([3, 1.5, 3])
    cols[1].image('src/support_data/logo.jpeg', use_column_width = True)

    # add version if version is given
    if version is not None:
        cols[1].markdown(f'''
            <center> {version} </center>
        ''', unsafe_allow_html = True)
