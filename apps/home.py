import streamlit as st

def app():
    st.title('Home')

    st.markdown("""
    # Multi-Page App 

    This multi-page app is using the [streamlit-multiapps](https://github.com/upraneelnihar/streamlit-multiapps) framework developed by [Praneel Nihar](https://medium.com/@u.praneel.nihar). Also check out his [Medium article](https://medium.com/@u.praneel.nihar/building-multi-page-web-app-using-streamlit-7a40d55fa5b4).

    """)

    st.write('This is the `home page` of this multi-page app.')

    st.write('In this app, we will be building a simple classification model using the Iris dataset.')
