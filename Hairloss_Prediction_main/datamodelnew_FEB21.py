'''import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
data = pd.read_csv('Predict Hair Fall.csv')

df = pd.DataFrame(data)

le = LabelEncoder()
categorical_columns = ["Genetics", "Hormonal Changes", "Medical Conditions", "Medications & Treatments",
                        "Nutritional Deficiencies", "Stress", "Poor Hair Care Habits", "Environmental Factors",
                        "Smoking", "Weight Loss","Hair Loss"]


for col in categorical_columns:
    df[col] = le.fit_transform(df[col])

df.to_csv('hair_loss_intggggg.csv', index=False)

df.dropna(inplace=True)
#print(df.isnull().sum())
x=df["Genetics", "Hormonal Changes", "Medical Conditions", "Medications & Treatments",
                        "Nutritional Deficiencies", "Stress", "Poor Hair Care Habits", "Environmental Factors",
                        "Smoking", "Weight Loss"]
y=df["Hair Loss"]
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
rmf=RandomForestClassifier(n_estimators=100)
rmf.fit(x_train,y_train)
pre=rmf.predict(x_test)
print(pre)
rmf_score=rmf.score(x_test,y_test)
print(rmf_score)'''

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Read the CSV file
data = pd.read_csv('hair_loss_intggggg.csv')

# Create a DataFrame
df = pd.DataFrame(data)
'''
# Initialize LabelEncoder
le = LabelEncoder()

# Encode categorical columns
categorical_columns = ["Genetics", "Hormonal Changes", "Medical Conditions", "Medications & Treatments",
                        "Nutritional Deficiencies", "Stress", "Poor Hair Care Habits", "Environmental Factors",
                        "Smoking", "Weight Loss", "Hair Loss"]

for col in categorical_columns:
    df[col] = le.fit_transform(df[col])
'''
# Drop rows with missing values
df.dropna(inplace=True)

# Separate features (X) and target variable (y)
X = df.drop("Hair Loss", axis=1)
y = df["Hair Loss"]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize RandomForestClassifier
rmf = RandomForestClassifier(n_estimators=100)

# Fit the model on the training data
rmf.fit(X_train, y_train)

# Make predictions on the test data
pre = rmf.predict(X_test)

# Print predictions and model score
print("Predictions:", pre)
rmf_score = rmf.score(X_test, y_test)
print("Random Forest Classifier Score:", rmf_score)







'''
#Genetics
#print(df['Genetics'].unique())
g_dic={'Yes':0,'No':1}
df['Genetics'] = df['Genetics'].map(g_dic)
#print(df['Genetics'])

#Hormonal Changes
#print(df['Hormonal Changes'].unique())
g_dic={'Yes':0,'No':1}
df['Hormonal Changes'] = df['Hormonal Changes'].map(g_dic)
#print(df['Hormonal Changes'])

#Medical Conditions
#print(df['Medical Conditions'].unique())
mc_dic ={ 'Eczema':0, 'Dermatosis':1, 'Ringworm':2, 'Psoriasis':3, 'Alopecia Areata ':4,
 'Scalp Infection':5, 'Seborrheic Dermatitis':6 ,'Dermatitis':7, 'Thyroid Problems':8,
'Androgenetic Alopecia':9}
df['Medical Conditions'] = df['Medical Conditions'].map(mc_dic)
#print(df['Medical Conditions'])

#Medications & Treatments
#print(df['Medications & Treatments'].unique())
mt_dic ={ 'Antibiotics':0, 'Antifungal Cream':1, 'Accutane':2, 'Chemotherapy':3, 'Steroids ':4,
 'Rogaine':5, 'Blood Pressure Medication':6 ,'Immunomodulators':7, 'Antidepressants':8,
'Heart Medication':9}
df['Medications & Treatments'] = df['Medications & Treatments'].map(mt_dic)
#print(df['Medications & Treatments'])

#Nutritional Deficiencies
print(df['Nutritional Deficiencies'].unique())


'''