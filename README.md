# ⚡ Enterprise AI Customer Intelligence & Segmentation Platform

An end-to-end Machine Learning production pipeline that segments e-commerce customer databases using unsupervised **RFM Analysis (K-Means Clustering)**, builds a supervised **Random Forest Classifier** with **99% predictive accuracy**, and deploys the entire ecosystem into a cutting-edge, dark-themed interactive **Streamlit Analytics Dashboard**.

---

## 🎯 Business Case & Overview

In modern e-commerce, generic mass-marketing leads to high ad-spend waste and customer churn. This platform solves this by automatically analyzing customer purchasing behavior, grouping them into distinct behavioral personas, and serving real-time tactical marketing recommendations to optimize retention and Maximize Return on Investment (ROI).

### 👥 Discovered Customer Personas

Through automated K-Means optimization, the data pipeline isolated 3 core operational segments:

1. **Champions 🏆 (VIP Superstars):** High spending, frequent orders, and highly active.
2. **Potential Loyalists 📈 (Core Growth Group):** Recent buyers with average frequency; the prime target for cross-selling and upselling.
3. **Sleepers 💤 (Low Value / At Risk):** Customers with long periods of inactivity who require immediate win-back campaigns.

---

## 🚀 Key Platform Features

- **Advanced Production Pipeline:** Full pipeline structure handling transactional missing values, outlier elimination, and engineering of dynamic Recency, Frequency, and Monetary (RFM) schemas.
- **Supervised Feature Dominance:** Implemented a Random Forest Classifier trained on algorithmic clusters, achieving a **99% Classification Accuracy**. Feature importance assessment proved that **Recency** is the primary driver (**46.3%** impact weight).
- **Cyberspace Dark UI UI:** Built an executive Streamlit interface with automated CSS styling tailored for real-time inference without manual submission hooks.
- **Interactive 3D Workspace:** Features a fully integrated Plotly 3D scatter tracking space where active live inputs drift seamlessly across historical client galaxies.
- **Bulk Database Processing Gate:** Integrated an enterprise-grade spreadsheet upload pipeline where operators can drop massive customer CSV arrays, run batch processing, and download mapped marketing reports instantly.

---

## 🛠️ Project Architecture & File Structure

```text
├── data/                             # Secure Local Database Directory (Git Ignored)
│   └── ecommerce_transactions.csv
├── .gitignore                        # Standard protection framework for data files
├── Jupyter_Notebook.ipynb            # Core exploratory data research & model training phase
├── rfm_customer_classifier_model.pkl # Compressed serial object of the trained AI brain
├── requirements.txt                  # Complete production software dependency registry
└── app.py                            # Core Streamlit modern live UI engine script
```
