import matplotlib.pyplot as plt

def create_chart(symptoms):

    symptom_list = symptoms.split()

    values = [1] * len(symptom_list)

    plt.figure(figsize=(6,4))
    plt.bar(symptom_list, values)

    plt.title("Symptoms Entered")
    plt.xlabel("Symptoms")
    plt.ylabel("Presence")

    plt.tight_layout()
    plt.savefig("reports/symptom_chart.png")

    plt.close()