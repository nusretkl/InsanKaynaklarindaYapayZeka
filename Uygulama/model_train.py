import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, mean_squared_error, classification_report
import numpy as np

# Veriyi oku
df = pd.read_csv("AI_Resume_Screening.csv")
df = df.dropna()

# Özellik türetme
df['Sertifika'] = df['Certifications'].apply(lambda x: 1 if x.strip().lower() != 'none' else 0)
df['Hedef'] = df['Recruiter Decision'].apply(lambda x: 1 if x.strip().lower() == 'hire' else 0)

# Label encoding
edu_enc = LabelEncoder()
role_enc = LabelEncoder()
df['Education_encoded'] = edu_enc.fit_transform(df['Education'])
df['Job_encoded'] = role_enc.fit_transform(df['Job Role'])

# Özellikler ve hedef değişken
X = df[['Experience (Years)', 'Education_encoded', 'Job_encoded', 'Salary Expectation ($)', 'Sertifika', 'Projects Count']]
y = df['Hedef']

# Veriyi ayır
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Random Forest model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Performans
y_pred = model.predict(X_test)
print("Doğruluk Oranı:", accuracy_score(y_test, y_pred))
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred)))
print("Sınıflandırma Raporu:\n", classification_report(y_test, y_pred))

# Kaydet
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

with open('encoders.pkl', 'wb') as f:
    pickle.dump({'education': edu_enc, 'job': role_enc}, f)
