import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Load RFM table
rfm = pd.read_csv("c_outputs/reports/customer_rfm.csv", index_col=0)

# Scale the features
scaler = StandardScaler()
rfm_scaled = scaler.fit_transform(rfm)

# Apply KMeans
kmeans = KMeans(n_clusters=4, random_state=42)
rfm["Cluster"] = kmeans.fit_predict(rfm_scaled)

# Save the segmented customers
rfm.to_csv("c_outputs/reports/customer_segments.csv")

print(rfm.head())
print("Customer Segmentation Completed Successfully!")

