#streamlit learning
import numpy as np
import pandas as pd
import streamlit as st


x = st.slider('my slider')
st.write(f" `{x}` squared is `{x*x}`")

import streamlit.components.v1 as components

def github_gist(gist_creator, gist_id, height=600, scrolling=True):

    components.html(
        f"""
	  <script src="https://gist.github.com/{gist_creator}/{gist_id}.js">
	  </script>
	""",
        height=height,
        scrolling=scrolling,
    )
    
    
    


# Render a gist
github_gist('tc87', '9382eafdb6eebde0bca0c33080d54b58')
st.__version__
dataframe = np.random.randn(10,20)
st.dataframe(dataframe)
dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(dataframe.style.highlight_max(axis=0))
dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))
st.table(dataframe)
# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)
import streamlit as st

left_column,middle_column, right_column = st.beta_columns(3)
# You can use a column just like st.sidebar:
left_column.button('Press me!')
middle_column.button("Do NOT press me,But why?")

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")