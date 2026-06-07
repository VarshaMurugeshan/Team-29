
import streamlit as st
import pandas as pd
from diff_engine import compare
from ai_agent import analyze

st.title("Schema Drift Detector")

changes = compare('schemas/schema_day1.json','schemas/schema_day2.json')
report = analyze(changes)

st.dataframe(pd.DataFrame(report))
