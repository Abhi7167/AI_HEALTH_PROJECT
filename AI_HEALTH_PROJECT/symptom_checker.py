import pandas as pd

class SymptomChecker:

    def __init__(self, dataset_path):
        self.df = pd.read_csv(dataset_path)

    def predict(self, symptoms):

        symptoms = symptoms.lower().strip()

        for _, row in self.df.iterrows():
            if row["symptom"].lower() == symptoms:
                return {
                    "disease": row["disease"],
                    "advice": row["advice"]
                }

        return {
            "disease": "Unknown Condition",
            "advice": "Please consult a healthcare professional."
        }