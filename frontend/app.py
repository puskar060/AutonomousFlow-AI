import streamlit as st
import time

st.set_page_config(page_title="OmniWorker AI", layout="wide")
st.title("🤖 AutonomousFlow AI: Multi-Agent Enterprise Control Center")
st.markdown("Real-time autonomous coordination engine powered by LangGraph & Supabase.")

session_id = st.sidebar.text_input("Session ID", value="sess_99812")
if st.sidebar.button("Run Workflow"):
    with st.spinner("Executing..."):
        time.sleep(1.5)
    st.success("Workflow executed!")

col1, col2 = st.columns(2)
with col1:
    st.subheader("Live Agent State")
    st.json({"session_id": session_id, "status": "active", "agent": "inventory_agent"})
with col2:
    st.subheader("Task Status")
    st.dataframe({"Task": ["Stock Check", "Dispatch"], "Status": ["Completed", "Pending"]})
