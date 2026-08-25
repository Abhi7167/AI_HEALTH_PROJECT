from datetime import datetime

def generate_report(symptoms, disease, advice):

    report = f"""
------------------------------------
        HEALTH REPORT
------------------------------------

Date : {datetime.now()}

Symptoms :
{symptoms}

Predicted Disease :
{disease}

Advice :
{advice}

------------------------------------
Stay Healthy!
------------------------------------
"""

    with open("reports/health_report.txt", "w") as file:
        file.write(report)

    return report