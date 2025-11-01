# practical2_email_spam.py
# Requirements: pandas, sklearn, matplotlib, seaborn

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

df = pd.read_csv("emails.csv").dropna()   # ensure columns exist
# If dataset columns differ, set text_col and label_col accordingly:
text_col = 'text'    # change if needed
label_col = 'spam'   # change if needed

texts = df[text_col].astype(str)
labels = df[label_col].astype(int)

# Vectorize text
vec = TfidfVectorizer(max_features=3000)
X = vec.fit_transform(texts)
y = labels

# Train/test split
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)

models = {
    "KNN": KNeighborsClassifier(n_neighbors=5),
    "SVM": SVC(kernel='linear', probability=True, random_state=42)
}

for name, m in models.items():
    m.fit(Xtr, ytr)
    pred = m.predict(Xte)
    print(f"\n{name} Accuracy: {accuracy_score(yte, pred):.4f}")
    print(classification_report(yte, pred, digits=4))

    # Confusion matrix heatmap
    cm = confusion_matrix(yte, pred)
    plt.figure(figsize=(4,3))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.title(f"{name} Confusion Matrix")
    plt.xlabel("Predicted"); plt.ylabel("Actual")
    plt.show()
