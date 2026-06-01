# app.py
# PURPOSE: Simple web interface to test the pipeline
# Run with: streamlit run app.py

import streamlit as st
from pipeline import run_pipeline

st.set_page_config(page_title="Company LLM Gateway", page_icon="🏢")
st.title("🏢 Company LLM Gateway")
st.caption("Internal queries, enriched with company context, answered by AI.")

# Model selector
model = st.selectbox(
    "Choose external LLM:",
    ["claude-opus-4-5", "gpt-4o", "gpt-3.5-turbo"]
)

# Query input
query = st.text_area("Enter your question:", placeholder="e.g. What are our Q3 OKRs?")

if st.button("Submit", type="primary") and query:
    with st.spinner("Running pipeline..."):
        result = run_pipeline(query, model=model)

    st.subheader("Final Answer")
    st.write(result["final_response"])

    with st.expander("View Pipeline Details"):
        st.markdown("**Retrieved Context:**")
        st.text(result["retrieved_context"])
        st.markdown("**Enriched Prompt (after DeepSeek):**")
        st.text(result["enriched_prompt"])
        st.markdown("**Safe Prompt (after PII scrubbing):**")
        st.text(result["safe_prompt"])