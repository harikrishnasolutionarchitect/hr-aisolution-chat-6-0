import streamlit as st
from streamlit_option_menu import option_menu
import hraichatgpt as hr

st.set_page_config(page_title="HR-AISOLUTIONS-ChatGPT", page_icon=":robot_face:", layout="wide")

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({ "title": title, "function": func })
    def run(self):
        app = st.sidebar.selectbox(
            'Navigation',
            self.apps,
            format_func=lambda app: app['title']
        )
        app['function']()