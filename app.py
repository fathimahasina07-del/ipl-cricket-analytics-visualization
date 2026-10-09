"""
IPL Analytics — main entry point.

Run with:
    python -m streamlit run app.py

This file sets global page config/styling and renders the home dashboard.
The other sections (Players, Teams, Matches, Venues, Comparisons) live in
pages/ and appear automatically in Streamlit's sidebar navigation.
"""

from src.constants import APP_TITLE
from src.home_view import render_home
from src.ui import setup_page

setup_page(APP_TITLE, icon="🏏")
render_home()
