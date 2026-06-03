import streamlit as st
import joblib
import pandas as pd
import numpy as np
import plotly.express as px

# ==============================================================================
# 1. PAGE CONFIGURATION & LUXURY DARK THEME
# ==============================================================================
st.set_page_config(
    page_title="Enterprise AI Customer Intelligence Platform",
    page_icon="⚡",
    layout="wide"
)

# Custom Premium Dark CSS Theme
st.markdown("""
    <style>
    /* Main Background adjustments if system default isn't dark */
    .stApp { background-color: #0e1117; }
    
    .main-title { font-size:38px; font-weight:800; text-align:center; color:#ffffff; margin-bottom:5px; }
    .subtitle { font-size:16px; text-align:center; color:#a4b0be; margin-bottom:40px; }
    
    /* Dark Premium Persona Card */
    .persona-card { padding: 22px; border-radius: 12px; color: white; text-align: center; font-size: 28px; font-weight: bold; box-shadow: 0 4px 15px rgba(0,0,0,0.3); }
    
    /* Luxury Dark Strategy & Metric Containers */
    .strategy-box { padding: 20px; border-radius: 10px; background-color: #1c202a; color: #f1f2f6; border-left: 6px solid #57606f; box-shadow: 0 4px 12px rgba(0,0,0,0.2); margin-top: 20px; }
    .metric-container { background-color: #1c202a; padding: 18px; border-radius: 10px; text-align: center; border: 1px solid #2f3542; box-shadow: 0 4px 10px rgba(0,0,0,0.15); }
    
    /* Sidebar styling enhancements */
    section[data-testid="stSidebar"] { background-color: #12161f; }
    h1, h2, h3, h4, h5, h6, p { color: #ffffff !important; }
    small { color: #a4b0be !important; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">⚡ Enterprise AI Customer Intelligence Platform</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Next-generation customer lifecycle management powered by real-time Machine Learning and 3D behavioral analytics.</div>', unsafe_allow_html=True)

# ==============================================================================
# 2. LOAD TRAINED MODEL
# ==============================================================================
@st.cache_resource
def load_model():
    return joblib.load('rfm_customer_classifier_model.pkl')

try:
    model = load_model()
except Exception as e:
    st.error("🚨 Model file 'rfm_customer_classifier_model.pkl' not found! Please check your file path.")
    st.stop()

# Business logic mapping (Vibrant Glow Colors for Dark Mode)
personas = {
    0: {"name": "Sleepers (Low Value / At Risk) 💤", "color": "#ff4d4d", "strategy": "Target with urgent win-back email sequences, aggressive clearance discounts, and feedback surveys to understand churn reasons."},
    1: {"name": "Champions (VIP Superstars) 🏆", "color": "#2ed573", "strategy": "Maintain premium status! Provide dedicated account support, early product drop invitations, and zero-fee premium perks."},
    2: {"name": "Potential Loyalists (Core Growth) 📈", "color": "#1e90ff", "strategy": "Drive cross-selling actions. Offer multi-buy bundles and recommend personalized complementary items to boost frequency."}
}

vip_monetary_benchmark = 5000.0

# ==============================================================================
# 3. TABS INFRASTRUCTURE
# ==============================================================================
tab1, tab2 = st.tabs(["🎯 Live 3D Customer Predictor", "📂 Enterprise Batch Automation"])

# ------------------------------------------------------------------------------
# TAB 1: LIVE 3D CUSTOMER PREDICTOR
# ------------------------------------------------------------------------------
with tab1:
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("### 🎛️ Real-Time Behavioral Sliders")
        st.write("Modify parameters to observe instant automated persona drifting:")
        
        recency = st.slider("Recency (Days since last interaction)", 0, 365, 14)
        frequency = st.slider("Frequency (Total successful checkouts)", 1, 100, 12)
        monetary = st.slider("Monetary (Lifetime Gross Value in $)", 10, 15000, 3500, step=50)
        
        # Build live inference dataframe
        live_df = pd.DataFrame([{'Recency': recency, 'Frequency': frequency, 'Monetary': monetary}])
        predicted_cluster = int(model.predict(live_df)[0])
        result = personas[predicted_cluster]
        
        st.markdown("---")
        st.markdown("### 💡 Strategic Advisory")
        st.markdown(f'<div class="strategy-box"><b style="color:#1e90ff;">Automated Next-Best-Action:</b><br><span style="color:#dcdde1;">{result["strategy"]}</span></div>', unsafe_allow_html=True)

    with col2:
        st.markdown("### 🔮 Predictive Intelligence Hub")
        
        # Dynamic Dark Metric Indicators
        m1, m2, m3 = st.columns(3)
        with m1:
            st.markdown(f'<div class="metric-container"><small>RECENCY</small><br><b style="font-size:22px; color:#ffffff;">{recency} Days</b></div>', unsafe_allow_html=True)
        with m2:
            st.markdown(f'<div class="metric-container"><small>FREQUENCY</small><br><b style="font-size:22px; color:#ffffff;">{frequency} Orders</b></div>', unsafe_allow_html=True)
        with m3:
            st.markdown(f'<div class="metric-container"><small>MONETARY</small><br><b style="font-size:22px; color:#ffffff;">${monetary:,.0f}</b></div>', unsafe_allow_html=True)
            
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(f'<div class="persona-card" style="background-color: {result["color"]}; text-shadow: 0px 2px 4px rgba(0,0,0,0.5);">{result["name"]}</div>', unsafe_allow_html=True)
        
        # Smart Contextual Insights based on business logic
        if predicted_cluster == 2:
            gap = vip_monetary_benchmark - monetary
            if gap > 0:
                st.info(f"💡 **Upsell Opportunity:** Nudge this customer with an additional **${gap:,.0f}** in sales to unlock **VIP Champions** status traits.")
        elif predicted_cluster == 0:
            st.warning("⚠️ **Churn Alert:** High Recency detected. Customer has broken standard platform re-engagement window limits.")
            
        # Advanced Interactive 3D Scatter Plot via Plotly
        st.markdown("#### 🌐 3D Behavioral Space Alignment")
        
        np.random.seed(42)
        bg_records = 300
        bg_data = pd.DataFrame({
            'Recency': np.concatenate([np.random.randint(0, 40, 100), np.random.randint(10, 90, 100), np.random.randint(100, 365, 100)]),
            'Frequency': np.concatenate([np.random.randint(15, 60, 100), np.random.randint(4, 18, 100), np.random.randint(1, 5, 100)]),
            'Monetary': np.concatenate([np.random.randint(6000, 14000, 100), np.random.randint(800, 4500, 100), np.random.randint(20, 700, 100)]),
            'Segment': np.concatenate([['VIP']*100, ['Potential']*100, ['Sleepers']*100])
        })
        
        user_point = pd.DataFrame({'Recency': [recency], 'Frequency': [frequency], 'Monetary': [monetary], 'Segment': ['CURRENT CUSTOMER 🎯']})
        combined_plot_df = pd.concat([bg_data, user_point], ignore_index=True)
        
        point_sizes = combined_plot_df['Segment'].map({'VIP': 6, 'Potential': 6, 'Sleepers': 6, 'CURRENT CUSTOMER 🎯': 18}).tolist()
        
        # Plotly Cyberspace Dark Theme Layout
        fig = px.scatter_3d(
            combined_plot_df, x='Recency', y='Frequency', z='Monetary',
            color='Segment',
            color_discrete_map={'VIP': '#10ac84', 'Potential': '#2e86de', 'Sleepers': '#ee5253', 'CURRENT CUSTOMER 🎯': '#ecc94b'}, # Neon Gold for active point
            size=point_sizes,
            height=450,
            template="plotly_dark" # Natively switches the plot axis to dark mode
        )
        
        fig.update_traces(marker=dict(opacity=0.3), selector=dict(name='VIP'))
        fig.update_traces(marker=dict(opacity=0.3), selector=dict(name='Potential'))
        fig.update_traces(marker=dict(opacity=0.3), selector=dict(name='Sleepers'))
        fig.update_traces(marker=dict(opacity=1.0, line=dict(color='white', width=2)), selector=dict(name='CURRENT CUSTOMER 🎯'))
        
        fig.update_layout(
            margin=dict(l=0, r=0, b=0, t=0), 
            scene=dict(
                aspectmode='cube',
                bgcolor="#12161f" # FIXED HERE
            ),
            paper_bgcolor="#12161f"
        )
        st.plotly_chart(fig, use_container_width=True)

# ------------------------------------------------------------------------------
# TAB 2: ENTERPRISE BATCH AUTOMATION
# ------------------------------------------------------------------------------
with tab2:
    st.subheader("📂 Bulk Database Processing Pipeline")
    st.write("Upload client lists to run scalable predictions. If you don't have a dataset ready, click the generator tool below to test integration performance:")
    
    if st.button("🛠️ Generate & Download Mock Customer Database CSV"):
        mock_size = 250
        mock_df = pd.DataFrame({
            'CustomerID': np.arange(15001, 15001 + mock_size),
            'Recency': np.random.randint(1, 365, mock_size),
            'Frequency': np.random.randint(1, 50, mock_size),
            'Monetary': np.random.uniform(20.0, 12000.0, mock_size).round(2)
        })
        mock_csv = mock_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Click Here to Save Sample_Customers.csv",
            data=mock_csv,
            file_name="Sample_Customers.csv",
            mime="text/csv"
        )
        st.success("Sample database built successfully! Now upload it in the section below.")
        
    st.markdown("---")
    uploaded_file = st.file_uploader("Upload Target Database Pipeline (CSV format)", type="csv")
    
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        required_fields = {'Recency', 'Frequency', 'Monetary'}
        
        if required_fields.issubset(df.columns):
            batch_preds = model.predict(df[['Recency', 'Frequency', 'Monetary']])
            df['Cluster_ID'] = batch_preds
            df['Predicted_Segment'] = df['Cluster_ID'].map(lambda x: personas[x]['name'])
            
            st.balloons()
            st.success(f"⚡ Pipeline Complete: Categorized {df.shape[0]} customers natively inside the Random Forest matrix.")
            
            c1, c2 = st.columns([1, 1])
            with c1:
                st.markdown("#### 📊 Segment Allocation Split")
                fig_count = px.bar(df['Predicted_Segment'].value_counts().reset_index(), x='count', y='Predicted_Segment', 
                                   orientation='h', color='Predicted_Segment', 
                                   color_discrete_map={personas[0]['name']: '#ff4d4d', personas[1]['name']: '#2ed573', personas[2]['name']: '#1e90ff'},
                                   template="plotly_dark")
                fig_count.update_layout(showlegend=False, height=250, paper_bgcolor="#12161f", plot_bgcolor="#12161f")
                st.plotly_chart(fig_count, use_container_width=True)
                
            with c2:
                st.markdown("#### 📥 System Export Gate")
                exported_csv = df.to_csv(index=False).encode('utf-8')
                st.download_button(
                    label="💾 Download Fully Labeled Marketing Report (CSV)",
                    data=exported_csv,
                    file_name="AI_Segmented_Customer_Report.csv",
                    mime="text/csv",
                    use_container_width=True
                )
            
            st.markdown("#### 📋 Processed Registry Preview (Top 10 Records)")
            st.dataframe(df.head(10), use_container_width=True)
        else:
            st.error(f"🚨 Integration Error: Database columns must match schemas exactly: {required_fields}")