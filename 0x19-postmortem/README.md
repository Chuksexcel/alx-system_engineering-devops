<h1 align="center">Nginx web server outage incident report </h1>

The following incident report is based on <a href="https:https://github.com/Chuksexcel/alx-system_engineering-devops/tree/master/0x0D-web_stack_debugging_0/README.md">webstack_debbging_0</a>, five days ago an incident occurred that resulted in an outage. Today we will be providing an incident report in regards to nginx web server outage that occurred on 5th December 2022.

Please find below summary by Chukwuemeka Samuel\
Attached report <a href="https://docs.google.com/document/d/1iJzntW8DC7BnMHGDQLUeJL91xq5YwllsBHkB2HWtomU/edit?usp=sharing">Report</a>

## Issue Summary

From 09:25 AM to 10:15 PM  WAT, a request to nginx web server failed on port 80, thus resulting in an empty response message 204. The Websites that rely on nginx application web servers were not able to spin up it’s content which resulted to empty responses

### Timeline (all times East Africa Time)

09:25 AM EAT: Nginx Configuration push starts\
09:45 AM EAT: Beginning Outage\
09:46 AM EAT: Get request failed\
09:58 AM EAT: Alerted by User\
10:07 AM EAT: Failed Configuration fixed\
10:10 PM EAT: Nginx server Restart\
10:15 PM EAT: status 200 for all requests.

### Root Cause

At 09:25 AM WAT, a configuration change was made to the nginx configuration file to include a subdomain, thus leading to a bug in the configuration file. Which resulted in a change of port 80 in default configuration file for nginx config file causing an outage at 09:45 AM WAT. After being notified at 09:58 AM WAT, an internal test was done and a read through the config files was done and full stop was majorly the leading cause of an empty response with status code 204.


### Resolution

At 10:07 AM WAT the changes made to the configuration file were fixed and it was ensured that all bugs were fixed, by 10:10 PM WAT nginx server was restarted and by 10:15 PM WAT all content was being served.
Corrective and preventive measures
After analyzing and having internal audits for two days in regards to the outage that occured.
The following prevent measures were introduced to avoid such outages.

Preventing the use of bash scripts as a form of patching and introduction to the use of puppet scripts.
Adding a load bancer and an additional web server as a backup.
Introduction of datadog as a monitoring tool and to avaoid relying  to users..
Introduction of page duty to have developers on call for imediate fix..
Introduction of rollback configarations.
Testing of new features and updates of the configarations in sandboxes before pushing to a production server.
