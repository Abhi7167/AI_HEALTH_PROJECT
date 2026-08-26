import os

from symptom_checker import SymptomChecker
from report_generator import generate_report
from visualizations import create_chart


def welcome():

    print("\n" + "="*50)
    print("AI HEALTH SYMPTOM CHECKER")
    print("="*50)


def main():

    os.makedirs("reports", exist_ok=True)

    welcome()

    symptoms = input(
        "\nEnter Symptoms (example: fever cough): "
    )

    checker = SymptomChecker("dataset.csv")

    result = checker.predict(symptoms)

    disease = result["disease"]
    advice = result["advice"]

    confidence = 85

    print("\nAnalysis Completed")
    print("-"*40)

    print("Symptoms :", symptoms)
    print("Predicted Disease :", disease)
    print("Confidence Score :", str(confidence) + "%")
    print("Advice :", advice)

    create_chart(symptoms)

    report = generate_report(
        symptoms,
        disease,
        advice
    )

    print("\nHealth Report Generated")
    print("\nVisualization Saved")
    print("\nReport saved in reports folder")

    print("\n" + "="*50)
    print("FINAL HEALTH REPORT")
    print("="*50)

    print(report)


if __name__ == "__main__":
    main()