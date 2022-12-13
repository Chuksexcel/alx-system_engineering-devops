<h1 align="center">Nginx web server outage incident report </h1>

The following incident report is based on <a href="https://github.com/Chuksexcel/alx-system_engineering-devops/blob/master/0x0D-web_stack_debugging_0/README.md">webstack_debbging_0</a>, five days ago an incident occurred that resulted in an outage. Today we will be providing an incident report in regards to nginx web server outage that occurred on 5th December 2022.

Please find below summary by Chukwuemeka Samuel\
Attached report <a href="https://docs.google.com/document/d/1iJzntW8DC7BnMHGDQLUeJL91xq5YwllsBHkB2HWtomU/edit?usp=sharing">Report</a>

## Summary

From 09:25 AM to 10:15 PM  WAT, a request to the Nginx web server failed on port 80, thus resulting to an empty response message 204. The Websites that rely on Nginx application web servers were not able to spin up their content which resulted to empty responses

### Timeline (All time West Africa Time)

09:25 AM WAT: Nginx Configuration push starts\
09:45 AM WAT: Beginning Outage\
09:46 AM WAT: Get request failed\
09:58 AM WAT: Alerted by User\
10:07 AM WAT: Failed Configuration fixed\
10:10 PM WAT: Nginx server Restart\
10:15 PM WAT: status 200 for all requests.

### Root Cause

At 09:25 AM WAT, a configuration change was made to the Nginx configuration file to include a subdomain, thus leading to a bug in the configuration file. This resulted in a change of port 80 in the default configuration file for the Nginx config file causing an outage at 09:45 AM WAT. After being notified at 09:58 AM WAT, an internal test was done and a read of the config files was done full stop was majorly the leading cause of an empty response with status code 204.


### Resolution

At 10:07 AM WAT the changes made to the configuration file were fixed and it was ensured that all bugs were fixed, by 10:10 PM WAT Nginx server was restarted and by 10:15 PM WAT all content was being served.
Corrective and preventive measures
After analyzing and having internal audits for two days in regard to the outage that occurred.
The following preventive measures were introduced to avoid such outages.

Preventing the use of bash scripts as a form of patching and introduction to the use of puppet scripts.
Adding a load balancer and an additional web server as a backup.
Introduction of datadog as a monitoring tool and to avoid relying on users.
Introduction of page duty to have developers on call for an immediate fix..
Introduction of rollback configurations.
Testing of new features and updates of the configurations in sandboxes before pushing to a production server.

