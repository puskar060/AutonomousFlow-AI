import streamlit as st
import time
from supabase import create_client, Client

st.set_page_config(page_title="Enterprise & Store Hub", layout="wide")

# Supabase Client Initialization
@st.cache_resource
def init_supabase():
    url = st.secrets["SUPABASE_URL"]
    key = st.secrets["SUPABASE_SERVICE_ROLE_KEY"]
    return create_client(url, key)

supabase: Client = init_supabase()

# Sidebar Navigation for Multiple Modules
st.sidebar.title("🚀 Navigation Hub")
app_mode = st.sidebar.selectbox("Choose App Module", ["🤖 AutonomousFlow AI", "🏪 Store Staff Activity Tracker"])

if app_mode == "🤖 AutonomousFlow AI":
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

elif app_mode == "🏪 Store Staff Activity Tracker":
    st.markdown("## 🏪 Store Multi-Role & Staff Activity Tracker")
    st.markdown("Track different staff roles and activities dynamically in Supabase.")

    staff_name = st.text_input("Staff Name", value="Puskar")
    role_position = st.selectbox("Select Post / Role", ["Cashier", "Kitchen Staff", "Inventory Manager", "Dispatcher"])

    session_id_store = st.text_input("Store Session ID", value="store_session_01")

    if st.button("Record Staff Activity"):
        data = {
            "session_id": session_id_store,
            "staff_name": staff_name,
            "role_position": role_position,
            "task_performed": f"Handled tasks as {role_position}",
            "status": "Completed"
        }
        try:
            supabase.table("staff_activity").insert(data).execute()
            st.success(f"Activity for {staff_name} ({role_position}) saved to Supabase successfully!")
        except Exception as e:
            st.error(f"Error: {e}")
