# Lab2-CST8919: Web App with Threat Detection using Azure Monitor and KQL

## Objective
This lab demonstrates the deployment of a Python Flask web application to Azure App Service with built-in threat detection using Azure Monitor, Log Analytics, and KQL. The app simulates login behavior, and an alert is triggered based on failed login attempts to detect failed login activity.

---

## What I Did

- Developed a Python Flask app with a `/login` route to log both successful and failed login attempts.
- Deployed the app using Azure App Service and GitHub Actions CI/CD workflow.
- Configured the app to run with the following startup command:
  ```bash
  gunicorn --bind=0.0.0.0 --timeout 600 threat-detection-app:app
  
- Enabled diagnostic logging and sent logs to a Log Analytics Workspace.
- Used Kusto Query Language (KQL) to detect repeated failed login attempts.
- Created an alert rule to notify via email when failed logins exceed a threshold.

---

## KQL Query Used
Below query looks for "Failed login attempt" entries in the ResultDescription column of AppServiceConsoleLogs. It helps identify failed login attemps.
```bash
AppServiceConsoleLogs
| where ResultDescription contains "Failed login attempt"
| project TimeGenerated, ResultDescription
| sort by TimeGenerated desc

---

Vidoe link
[https://youtu.be/pc1Hyvyhhi0]
