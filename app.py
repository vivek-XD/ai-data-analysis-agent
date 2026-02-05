import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="AI Data Analysis Agent",
    page_icon="🤖",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background:
    linear-gradient(rgba(10,15,25,0.75), rgba(10,15,25,0.75)),
    url("https://images.unsplash.com/photo-1666875753105-c63a6f3bdc86?auto=format&fit=crop&w=1600&q=80");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    color: #F5F6FA;
    font-family: 'Segoe UI', sans-serif;
}
.glass {
    background: rgba(255, 255, 255, 0.16);
    backdrop-filter: blur(14px);
    padding:22px;
    border-radius:20px;
    text-align:center;
    box-shadow: 0 8px 28px rgba(0,0,0,0.55);
}
.section {
    background: rgba(255,255,255,0.14);
    padding:25px;
    border-radius:20px;
    margin-top:20px;
}
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0A0F19, #141B2D);
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center;'>🤖 AI Data Analysis Agent</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;color:#C7D2FE;'>Professional Data Analytics Dashboard</p>", unsafe_allow_html=True)

st.sidebar.title("⚙️ Controls")
uploaded_file = st.sidebar.file_uploader("📂 Upload CSV File", type=["csv"])

chart_type = st.sidebar.selectbox(
    "📊 Chart Type",
    ["Histogram", "Bar Chart", "Line Chart", "Box Plot"]
)

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown(f"<div class='glass'><h2>{df.shape[0]}</h2>Rows</div>", unsafe_allow_html=True)
    with c2:
        st.markdown(f"<div class='glass'><h2>{df.shape[1]}</h2>Columns</div>", unsafe_allow_html=True)
    with c3:
        st.markdown(f"<div class='glass'><h2>{df.isnull().sum().sum()}</h2>Missing</div>", unsafe_allow_html=True)
    with c4:
        st.markdown("<div class='glass'><h2>ON</h2>AI Agent</div>", unsafe_allow_html=True)


    st.markdown("<div class='section'><h3>📑 Dataset Preview</h3></div>", unsafe_allow_html=True)
    st.dataframe(df, use_container_width=True)

    
    st.markdown("<div class='section'><h3>🔍 Explore Records</h3></div>", unsafe_allow_html=True)
    view_option = st.selectbox("Select Records", ["All", "Top 5", "Bottom 5"])

    if view_option == "Top 5":
        st.dataframe(df.head())
    elif view_option == "Bottom 5":
        st.dataframe(df.tail())
    else:
        st.dataframe(df)

    
    st.markdown("<div class='section'><h3>🎚️ Filter Data</h3></div>", unsafe_allow_html=True)
    filter_col = st.selectbox("Select Column to Filter", df.columns)

    if df[filter_col].dtype != "object":
        min_val, max_val = st.slider(
            "Select Range",
            float(df[filter_col].min()),
            float(df[filter_col].max()),
            (float(df[filter_col].min()), float(df[filter_col].max()))
        )
        filtered_df = df[(df[filter_col] >= min_val) & (df[filter_col] <= max_val)]
        st.dataframe(filtered_df)
    else:
        st.info("Selected column is not numeric")

    
    tab1, tab2, tab3 = st.tabs(["📊 Visualization", "📈 Statistics", "🧠 AI Insight"])


    with tab1:
        num_cols = df.select_dtypes(include=["int64", "float64"]).columns

        if len(num_cols) > 0:
            col = st.selectbox("Select Numeric Column", num_cols)

            fig, ax = plt.subplots()
            if chart_type == "Histogram":
                ax.hist(df[col])
            elif chart_type == "Bar Chart":
                ax.bar(df.index, df[col])
            elif chart_type == "Line Chart":
                ax.plot(df[col])
            else:
                ax.boxplot(df[col])

            ax.set_title(f"{chart_type} of {col}")
            st.pyplot(fig)

            
            if len(num_cols) > 1:
                st.markdown("### 📈 Correlation Heatmap")
                corr = df[num_cols].corr()
                fig, ax = plt.subplots()
                sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
                st.pyplot(fig)

    
    with tab2:
        st.write(df.describe())


    with tab3:
        st.success(
            f"""
            ✔ Rows: {df.shape[0]}  
            ✔ Columns: {df.shape[1]}  
            ✔ Missing values: {df.isnull().sum().sum()}  
            ✔ Numeric columns analyzed automatically  

            👉 This AI dashboard allows users to explore, filter,
            visualize and understand data easily.
            """
        )

else:
    st.markdown(
        "<div class='glass' style='margin-top:120px;'>👈 Upload a CSV file to start analysis</div>",
        unsafe_allow_html=True
    )

