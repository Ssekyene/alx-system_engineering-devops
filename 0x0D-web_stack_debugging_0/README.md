# 0x0D. Web stack debugging #0

## Concepts 
* DevOps
* SysAdmin
* Scripting
* Debugguing

## Environment
* Language: Bash script
* OS: Ubuntu 20.04 LTS
* Container: Docker
* Web Server: Apache

> Intro

Debugging usually takes a big chunk of a software engineer’s time. The art of debugging is tough and it takes years, even decades to master, and that is why seasoned software engineers are the best at it… experience. They have seen lots of broken code, buggy systems, weird edge cases and race conditions.

![k-e.PNG](./k-e.PNG)

## Non-exhaustive guide to debugging
### School specific
If you are struggling to get something right that is run on the checker, like a Bash script or a piece of code, keep in mind that you can simulate the flow by starting a Docker container with the distribution that is specified in the requirements and by running your code. Check the Docker concept page for more info.

### Test and verify your assumptions
The idea is to ask a set of questions until you find the issue. For example, if you installed a web server and it isn’t serving a page when browsing the IP, here are some questions you can ask yourself to start debugging:

- Is the web server started? - You can check using the service manager, also double check by checking process list.
- On what port should it listen? - Check your web server configuration
- Is it actually listening on this port? - `netstat -lpdn` - run as `root` or `sudo` so that you can see the process for each listening port
- It is listening on the correct server IP? - `netstat` is also your friend here
- Is there a firewall enabled?
- Have you looked at logs? - usually in `/var/log` and `tail -f` is your friend
- Can I connect to the HTTP port from the location I am browsing from? - `curl` is your friend

There is a good chance that at this point you will already have found part of the issue.

### Get a quick overview of the machine state

[References](#References)

When you connect to a server/machine/computer/container you want to understand what’s happened recently and what’s happening now, and you can do this with [5 commands](https://www.linux.com/training-tutorials/first-5-commands-when-i-connect-linux-server/) in a minute or less

### Machine
Debugging is pretty much about verifying assumptions, in a perfect world the software or system we are working on would be working perfectly, the server is in perfect shape and everybody is happy. But actually, it NEVER goes this way, things ALWAYS fail (it’s tremendous!).

For the machine level, you want to ask yourself these questions:
- Does the server have free disk space? - `df`
- Is the server able to keep up with CPU load? - `w`, `top`, `ps`
- Does the server have available memory? `free`
- Are the server disk(s) able to keep up with read/write IO? - `htop`

If the answer is no for any of these questions, then that might be the reason why things are not going as expected. There are often 3 ways of solving the issue:
- free up resources (stop process(es) or reduce their resource consumption)
- increase the machine resources (adding memory, CPU, disk space…)
- distributing the resource usage to other machines

### Network issue
For the machine level, you want to ask yourself these questions:

- Does the server have the expected network interfaces and IPs up and running? `ifconfig`
- Does the server listen on the sockets that it is supposed to? `netstat` (`netstat -lpd` or `netstat` -`lpn`)
- Can you connect from the location you want to connect from, to the socket you want to connect to? `telnet` to the IP + PORT (`telnet 8.8.8.8 80`)
- Does the server have the correct firewall rules? `iptables`, `ufw`:
    - `iptables -L`
    - `sudo ufw status`

### Process issue
If a piece of Software isn’t behaving as expected, it can obviously be because of above reasons… but the good news is that there is more to look into (there is ALWAYS more to look into actually).

- Is the software started? `init`, `init.d`:
    - `service NAME_OF_THE_SERVICE status`
    - `/etc/init.d/NAME_OF_THE_SERVICE status`

- Is the software process running? `pgrep`, `ps`:
    - `pgrep -lf NAME_OF_THE_PROCESS`
    - `ps auxf`

Is there anything interesting in the logs? look for log files in `/var/log/` and `tail -f` is your friend

### Debugging is fun
Debugging can be frustrating, but it will definitely be part of your job, it requires experience and methodology to become good at it. The good news is that bugs are never going away, and the more experienced you become, trickier bugs will be assigned to you! Good luck :smiley:


> Docker
## Readme
- [What is Docker and why is it popular?](https://www.zdnet.com/article/what-is-docker-and-why-is-it-so-darn-popular/)

_Take note: The following instructions are run in a ubuntu-xenial virtual machine setup using Vagrant. To do the same, you can also install docker in any Vagrant virtual machine, or install docker on your host OS (Windows, Linux or Mac OS)_

Let’s first pull a Docker image and run a container:
```
vagrant@ubuntu-xenial:~$ docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
vagrant@ubuntu-xenial:~$ docker run -d -ti ubuntu:16.04
Unable to find image 'ubuntu:16.04' locally
16.04: Pulling from library/ubuntu
34667c7e4631: Pull complete
d18d76a881a4: Pull complete
119c7358fbfc: Pull complete
2aaf13f3eff0: Pull complete
Digest: sha256:58d0da8bc2f434983c6ca4713b08be00ff5586eb5cdff47bcde4b2e88fd40f88
Status: Downloaded newer image for ubuntu:16.04
e1fc0d4bbb5d3513b8f7666c91932812da7640346f6e05b7cfc3130ddbbb8278
vagrant@ubuntu-xenial:~$ docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED              STATUS              PORTS               NAMES
e1fc0d4bbb5d        ubuntu:16.04        "/bin/bash"         About a minute ago   Up About a minute                       keen_blackwell
vagrant@ubuntu-xenial:~$
```
Note that `docker` command will pull the Ubuntu docker container image from the Internet and run it. I let you look at the meaning of the flags using the command `docker run --help`, the main idea is that it keeps the container up and running.

To execute a command on the Docker container, use `docker exec`:
```
vagrant@ubuntu-xenial:~$ docker exec -i e1fc0d4bbb5d hostname
e1fc0d4bbb5d
vagrant@ubuntu-xenial:~$ hostname
ubuntu-xenial
vagrant@ubuntu-xenial:~$
```

If you want to connect to your Docker container and use Bash, you need to use `docker exec -ti`:
```
vagrant@ubuntu-xenial:~$ docker exec -ti e1fc0d4bbb5d /bin/bash
root@e1fc0d4bbb5d:/# echo "I am in $(hostname) Docker container"
I am in e1fc0d4bbb5d Docker container
root@e1fc0d4bbb5d:/# exit
exit
vagrant@ubuntu-xenial:~$
```
If you want to stop a container, use `docker stop`:
```
vagrant@ubuntu-xenial:~$ docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
e1fc0d4bbb5d        ubuntu:16.04        "/bin/bash"         5 minutes ago       Up 5 minutes                            keen_blackwell
vagrant@ubuntu-xenial:~$ docker stop e1fc0d4bbb5d
e1fc0d4bbb5d
vagrant@ubuntu-xenial:~$ docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
vagrant@ubuntu-xenial:~$
```

> Task

Be sure to read the Docker concept page

In this first debugging project, you will need to get `Apache` to run on the container and to return a page containing `Hello Holberton` when querying the root of it.

Example:
```
vagrant@vagrant:~$ docker run -p 8080:80 -d -it holbertonschool/265-0
47ca3994a4910bbc29d1d8925b1c70e1bdd799f5442040365a7cb9a0db218021
vagrant@vagrant:~$ docker ps
CONTAINER ID        IMAGE                   COMMAND             CREATED             STATUS              PORTS                  NAMES
47ca3994a491        holbertonschool/265-0   "/bin/bash"         3 seconds ago       Up 2 seconds        0.0.0.0:8080->80/tcp   vigilant_tesla
vagrant@vagrant:~$ curl 0:8080
curl: (52) Empty reply from server
vagrant@vagrant:~$
```
Here we can see that after starting my Docker container, I `curl` the port `8080` mapped to the Docker container port `80`, it does not return a page but an error message. Note that you might also get the error message `curl: (52) Empty reply from server`.
```
vagrant@vagrant:~$ curl 0:8080
Hello Holberton
vagrant@vagrant:~$
```
After connecting to the container and fixing whatever needed to be fixed (here is your mission), you can see that curling port 80 return a page that contains `Hello Holberton`. Paste the command(s) you used to fix the issue in your answer file.

## References
- [Youtube video First 5 Commands When I Connect on a Linux Server](https://www.youtube.com/watch?v=1_gqlbADaAw&feature=youtu.be)
- [First 5 Commands When I Connect on a Linux Server](https://www.linux.com/training-tutorials/first-5-commands-when-i-connect-linux-server/)

> Author
[Ssekyene Robert](https://github.com/Ssekyene/)
