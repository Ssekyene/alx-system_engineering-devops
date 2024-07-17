# 0x0C. Web server

## Concepts
* DevOps
* SysAdmin

## Learning Objectives
> General
* What is the main role of a web server
* What is a child process
* Why web servers usually have a parent process and child processes
* What are the main HTTP requests

> DNS
* What DNS stands for
* What is DNS main role

> DNS Record Types
* A, CNAME, TXT, MX

## Tasks
- [0-transfer_file](./0-transfer_file)
Example
```
sylvain@ubuntu$ ./0-transfer_file
Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY
sylvain@ubuntu$
sylvain@ubuntu$ ssh ubuntu@8.8.8.8 -i /vagrant/sylvain 'ls ~/'
afile
sylvain@ubuntu$
sylvain@ubuntu$ touch some_page.html
sylvain@ubuntu$ ./0-transfer_file some_page.html 8.8.8.8 sylvain /vagrant/private_key
some_page.html                                     100%   12     0.1KB/s   00:00
sylvain@ubuntu$ ssh ubuntu@8.8.8.8 -i /vagrant/private_key 'ls ~/'
afile
some_page.html
sylvain@ubuntu$
```
- [1-install_nginx_web_server](./1-install_nginx_web_server)
Server terminal:
```
root@sy-web-01$ ./1-install_nginx_web_server > /dev/null 2>&1
root@sy-web-01$ 
root@sy-web-01$ curl localhost
Hello World!
root@sy-web-01$ 
```
Local terminal:
```
sylvain@ubuntu$ curl 34.198.248.145/
Hello World!
sylvain@ubuntu$ curl -sI 34.198.248.145/
HTTP/1.1 200 OK
Server: nginx/1.4.6 (Ubuntu)
Date: Tue, 21 Feb 2017 23:43:22 GMT
Content-Type: text/html
Content-Length: 30
Last-Modified: Tue, 21 Feb 2017 07:21:32 GMT
Connection: keep-alive
ETag: "58abea7c-1e"
Accept-Ranges: bytes

sylvain@ubuntu$
```
If things are not going as expected, make sure to check out Nginx logs, they can be found in `/var/log/`.

**Maarten’s PRO-tip:** When you use `sudo su` on your server you can become root like this to test your file:
```
sylvain@ubuntu$ sudo su
root@ubuntu#
```

- [2-setup_a_domain_name](./2-setup_a_domain_name)(contains my domain name)
[.TECH Domains](https://get.tech/) is one of the top domain providers. They are known for the stability and quality of their DNS hosting solution. Github partnered with .TECH Domains so that you can learn about DNS.

**YOU** can have a **free .tech domain** for 1 year by following these steps:
	- Unlock [GitHub student pack](https://github.com/education). If you have any issue, please contact [GitHub education support](https://support.github.com/)
	- When registered, access your benefits:
	- And scroll to **.Tech domain:**
	- Start to register your domain and checkout
	- At the Checkout step, please click on “Login with GitHub”
	- The cost of the domain should be now at $0
	- You can finalize it by creating an account in .Tech domains
	- And manage your domain there!
	- configure your DNS records with an A entry so that your root domain points to your server's IP address 
Example:
```
sylvain@ubuntu$ cat 2-setup_a_domain_name
myschool.tech
sylvain@ubuntu$
sylvain@ubuntu$ dig myschool.tech

; <<>> DiG 9.10.6 <<>> myschool.tech
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 26785
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 512
;; QUESTION SECTION:
;myschool.tech.     IN  A

;; ANSWER SECTION:
myschool.tech.  7199    IN  A   184.72.193.201

;; Query time: 65 msec
;; SERVER: 8.8.8.8#53(8.8.8.8)
;; WHEN: Fri Aug 02 09:44:36 PDT 2019
;; MSG SIZE  rcvd: 65

sylvain@ubuntu$
```
When your domain name is setup, please verify the Registrar here: [https://whois.whoisxmlapi.com/](https://whois.whoisxmlapi.com/) and you must see in the JSON response: `"registrarName": "Dotserve Inc"`

- [3-redirection](./3-redirection)
Example:
```
sylvain@ubuntu$ curl -sI 34.198.248.145/redirect_me/
HTTP/1.1 301 Moved Permanently
Server: nginx/1.4.6 (Ubuntu)
Date: Tue, 21 Feb 2017 21:36:04 GMT
Content-Type: text/html
Content-Length: 193
Connection: keep-alive
Location: https://www.youtube.com/watch?v=QH2-TGUlwu4

sylvain@ubuntu$
```
- [4-not_found_page_404](./4-not_found_page_404)
Example:
```
sylvain@ubuntu$ curl -sI 34.198.248.145/xyz
HTTP/1.1 404 Not Found
Server: nginx/1.4.6 (Ubuntu)
Date: Tue, 21 Feb 2017 21:46:43 GMT
Content-Type: text/html
Content-Length: 26
Connection: keep-alive
ETag: "58acb50e-1a"

sylvain@ubuntu$ curl 34.198.248.145/xyzfoo
Ceci n'est pas une page

sylvain@ubuntu$
```

