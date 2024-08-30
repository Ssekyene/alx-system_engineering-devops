# 0x18. Webstack monitoring
* DevOps
* SysAdmin
* monitoring

## Backgtound Context
>  “You cannot fix or improve what you cannot measure” is a famous saying in the Tech industry. In the age of the data-ism, monitoring how our Software systems are doing is an important thing. In this project, we will implement one of many tools to measure what is going on our servers.

> Web stack monitoring can be broken down into 2 categories:

> Application monitoring: getting data about your running software and making sure it is behaving as expected
> Server monitoring: getting data about your virtual or physical server and making sure they are not overloaded (could be CPU, memory, disk or network overload)


## Learning Objectives
* Why is monitoring needed
*  What are the 2 main area of monitoring
* What are access logs for a web server (such as Nginx)
* What are error logs for a web server (such as Nginx)

## Requirements
* Allowed editors: vi, vim, emacs
* All your files will be interpreted on Ubuntu 16.04 LTS
* All your files should end with a new line
* A README.md file, at the root of the folder of the project, is mandatory
* All your Bash script files must be executable
* Your Bash script must pass Shellcheck (version 0.3.7) without any error
* The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
* The second line of all your Bash scripts should be a comment explaining what is the script doing

## Tasks
1. **Sign up for Datadog and install datadog-agent**

For this task head to [https://www.datadoghq.com/](https://www.datadoghq.com/) and sign up for a free `Datadog` account. When signing up, you’ll have the option of selecting statistics from your current stack that `Datadog` can monitor for you. Once you have an account set up, follow the instructions given on the website to install the `Datadog` agent.

- Sign up for Datadog - **Please make sure you are using the US website of Datagog (https://app.datadoghq.com)**
- Use the **US1** region
- Install `datadog-agent` on your `web-01` server
- Create an `application key`
- Copy-paste in your Intranet user profile your DataDog `API key` and your DataDog `application key`.
- Your server `web-01` should be visible in Datadog under the host name `XX-web-01`
    - You can validate it by using this [API](https://docs.datadoghq.com/api/latest/hosts/)
    - If needed, you will need to update the hostname of your server

2. Monitor some metrics

Among the litany of data your monitoring service can report to you are system metrics. You can use these metrics to determine statistics such as reads/writes per second, which can help your company determine if/how they should scale. Set up some `monitors` within the `Datadog` dashboard to monitor and alert you of a few. You can read about the various system metrics that you can monitor here: [System Check](https://docs.datadoghq.com/integrations/system/).

- Set up a monitor that checks the number of read requests issued to the device per second.
- Set up a monitor that checks the number of write requests issued to the device per second.

3. Create a dashboard

