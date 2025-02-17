import streamlit as st

def get_blooms_taxonomy_distribution():
    st.markdown("### 📊 Bloom's Taxonomy Difficulty Adjustment")

    create_pct = st.slider("🛠️ Creating (%)", 0, 100, 10)
    analyze_pct = st.slider("🔎 Analyzing (%)", 0, 100, 20)
    apply_pct = st.slider("💡 Applying (%)", 0, 100, 30)
    understand_pct = st.slider("📖 Understanding (%)", 0, 100, 20)
    remember_pct = st.slider("📚 Remembering (%)", 0, 100, 10)
    eval_pct = st.slider("⚖️ Evaluating (%)", 0, 100, 10)

    # Validate distribution (must add up to 100%)
    if create_pct + analyze_pct + apply_pct + understand_pct + remember_pct + eval_pct != 100:
        st.error("⚠️ The total percentage must equal 100!")
        return None  # Stop execution if invalid

    return {
        "Create": create_pct,
        "Analyze": analyze_pct,
        "Apply": apply_pct,
        "Understand": understand_pct,
        "Remember": remember_pct,
        "Evaluation": eval_pct
    }