import streamlit as st
import time
from supabase import create_client, Client

st.set_page_config(page_title="AutonomousFlow AI", layout="wide")

# Supabase कन्फिकेरेसन स्टेम्रलिट सेक्रेट्सबाट लोड गर्ने
@st.cache_resource
def init_supabase():
    url = st.secrets["SUPABASE_URL"]
    key = st.secrets["SUPABASE_SERVICE_ROLE_KEY"] # वा SUPABASE_KEY
    return create_client(url, key)

supabase: Client = init_supabase()

# Clean Header Presentation
st.markdown("## 🤖 AutonomousFlow AI")
st.markdown("### Enterprise Multi-Agent Control Center")
st.markdown("Real-time autonomous coordination engine powered by LangGraph & Supabase.")

session_id = st.sidebar.text_input("Session ID", value="sess_99812")

if st.sidebar.button("Run Workflow"):
    with st.spinner("Executing and saving to Supabase..."):
        time.sleep(1.5)
        
        # 1. workflow_tasks टेबलमा डेटा इन्सर्ट गर्ने
        task_data = {
            "session_id": session_id,
            "task_name": "Stock Check",
            "status": "Completed"
        }
        try:
            supabase.table("workflow_tasks").insert(task_data).execute()
            
            # 2. agent_states टेबलमा एजेन्टको स्टेट इन्सर्ट गर्ने
            state_data = {
                "session_id": session_id,
                "status": "active",
                "agent": "inventory_agent"
            }
            supabase.table("agent_states").insert(state_data).execute()
            
            st.success("Workflow executed and saved to Supabase successfully!")
        except Exception as e:
            st.error(f"Database Error: {e}")

col1, col2 = st.columns(2)
with col1:
    st.subheader("Live Agent State")
    st.json({"session_id": session_id, "status": "active", "agent": "inventory_agent"})
with col2:
    st.subheader("Task Status")
    st.dataframe({"Task": ["Stock Check", "Dispatch"], "Status": ["Completed", "Pending"]})
