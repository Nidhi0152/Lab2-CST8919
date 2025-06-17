# Lab2-CST8919: Web App with Threat Detection using Azure Monitor and KQL

## Objective
This lab demonstrates the deployment of a Python Flask web application to Azure App Service with built-in threat detection using Azure Monitor, Log Analytics, and KQL. The app simulates login behavior, and an alert is triggered based on failed login attempts to detect failed login activity.

---

## What I Did

- Developed a Python Flask app with a /login route to log both successful and failed login attempts.
- Created requirements.txt with flask and gunicorn.
- Deployed the app to Azure App Service using GitHub Actions.
- Configured the startup command in Azure:
  ```bash
  gunicorn --bind=0.0.0.0 --timeout 600 threat-detection-app:app
  
- Enabled AppServiceConsoleLogs and linked to a Log Analytics Workspace.
- Used Kusto Query Language (KQL) to detect repeated failed login attempts.
- Created an alert rule to notify via email when failed logins exceed a threshold.

---

## KQL Query Used
Below query looks for "Failed login attempt" entries in the ResultDescription column of AppServiceConsoleLogs. It helps identify failed login attemps.
```kql
AppServiceConsoleLogs
| where ResultDescription contains "Failed login attempt"
| project TimeGenerated, ResultDescription
| sort by TimeGenerated desc 
```

## Reflection and Key Takeaways
During this lab, I learned how to deploy a Python Flask app to Azure App Service using GitHub Actions and configure monitoring through Azure Monitor and Log Analytics. I gained hands-on experience writing Kusto Query Language (KQL) queries to detect suspicious activity and creating alert rules for real-time threat detection. One challenge I faced was ensuring the app's startup command matched the Python file name, which initially caused deployment issues. Another challenge was identifying the correct log field (ResultDescription) for KQL filtering. In a real-world scenario, I would improve the detection logic by incorporating IP-based rate limiting, storing logs in long-term storage

## Vidoe Demo link
[https://youtu.be/pc1Hyvyhhi0]
