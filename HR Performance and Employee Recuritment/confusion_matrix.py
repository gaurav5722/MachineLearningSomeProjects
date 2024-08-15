

import numpy as np
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Replace these with actual test labels and predictions
Y_test = [0, 1, 0, 1, 0, 1, 1, 0, 1, 0]  
knn_Y_pred = [0, 1, 0, 0, 0, 1, 1, 1, 1, 0]  

# Generate the confusion matrix
conf_mat = confusion_matrix(Y_test, knn_Y_pred)

# Define group names and calculate group counts
group_names = ['True Neg','False Pos','False Neg','True Pos']
group_counts = ["{0:0.0f}".format(value) for value in conf_mat.flatten()]

# Create labels for the heatmap
labels = [f"{v1}\n{v2}" for v1, v2 in zip(group_names, group_counts)]
labels = np.asarray(labels).reshape(2,2)

# Plotting the heatmap with improved formatting
plt.figure(figsize=(8, 6))
sns.heatmap(conf_mat, annot=labels, fmt='', cmap='Blues', cbar=False, annot_kws={"size": 16})
plt.title("Confusion Matrix", fontsize=18)
plt.xlabel("Predicted Label", fontsize=14)
plt.ylabel("True Label", fontsize=14)
plt.xticks(ticks=[0.5, 1.5], labels=["Class 0", "Class 1"], fontsize=12)
plt.yticks(ticks=[0.5, 1.5], labels=["Class 0", "Class 1"], fontsize=12)
plt.show()
