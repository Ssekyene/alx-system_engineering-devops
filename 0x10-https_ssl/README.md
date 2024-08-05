# 0x10. HTTPS SSL

## Concepts
* DevOps
* SysAdmin
* Security

## Learning Objectives
* What is HTTPS SSL 2 main roles
* What is the purpose encrypting traffic
* What SSL termination means

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
>
+ [0-world_wide_web](./0-world_wide_web)

Configure the domain zone in your domain name provider account (for my case [get.tech](https://get.tech/)) to have more subdomains of A record type eg subdomain `www` points to your load-balancer IP (`lb-01`).

Example:
```
sylvain@ubuntu$ dig www.holberton.online | grep -A1 'ANSWER SECTION:'
;; ANSWER SECTION:
www.holberton.online.   87  IN  A   54.210.47.110
sylvain@ubuntu$ dig lb-01.holberton.online | grep -A1 'ANSWER SECTION:'
;; ANSWER SECTION:
lb-01.holberton.online. 101 IN  A   54.210.47.110
sylvain@ubuntu$ dig web-01.holberton.online | grep -A1 'ANSWER SECTION:'
;; ANSWER SECTION:
web-01.holberton.online. 212    IN  A   34.198.248.145
sylvain@ubuntu$ dig web-02.holberton.online | grep -A1 'ANSWER SECTION:'
;; ANSWER SECTION:
web-02.holberton.online. 298    IN  A   54.89.38.100
sylvain@ubuntu$
sylvain@ubuntu$
sylvain@ubuntu$ ./0-world_wide_web holberton.online
The subdomain www is a A record and points to 54.210.47.110
The subdomain lb-01 is a A record and points to 54.210.47.110
The subdomain web-01 is a A record and points to 34.198.248.145
The subdomain web-02 is a A record and points to 54.89.38.100
sylvain@ubuntu$
sylvain@ubuntu$ ./0-world_wide_web holberton.online web-02
The subdomain web-02 is a A record and points to 54.89.38.100
sylvain@ubuntu$
```
>
+ [1-haproxy_ssl_termination](./1-haproxy_ssl_termination)

“Terminating SSL on HAproxy” means that HAproxy is configured to handle encrypted traffic, unencrypt it and pass it on to its destination.

Create a certificate using `certbot` and configure `HAproxy` to accept encrypted traffic for your subdomain `www..`.

Follow the steps below to help you to set up cerbot:

### Install cerbot
```
sudo apt-get update
sudo apt-get install certbot
```

### Generate Certificates
```
sudo certbot certonly --standalone -d www.robkj.tech
```
### Create a Combined PEM File
```
sudo cat /etc/letsencrypt/live/www.robkj.tech/fullchain.pem /etc/letsencrypt/live/www.robkj.tech/privkey.pem | sudo tee /etc/letsencrypt/live/www.robkj.tech/haproxy.pem
```
### Set Correct Permissions
```
sudo chown root:haproxy /etc/letsencrypt/live/www.robkj.tech/haproxy.pem
sudo chmod 640 /etc/letsencrypt/live/www.robkj.tech/haproxy.pem
```
### Reload HAProxy
```
sudo systemctl reload haproxy
```

The file [1-haproxy_ssl_termination](./1-haproxy_ssl_termination) is the HAproxy configuration file ie `/etc/haproxy/haproxy.cfg`.

Make sure to install HAproxy 1.5 or higher, [SSL termination](https://en.wikipedia.org/wiki/TLS_termination_proxy) is not available before v1.5.

Example:
```
sylvain@ubuntu$ curl -sI https://www.holberton.online
HTTP/1.1 200 OK
Server: nginx/1.4.6 (Ubuntu)
Date: Tue, 28 Feb 2017 01:52:04 GMT
Content-Type: text/html
Content-Length: 30
Last-Modified: Tue, 21 Feb 2017 07:21:32 GMT
ETag: "58abea7c-1e"
X-Served-By: 03-web-01
Accept-Ranges: bytes
sylvain@ubuntu$
sylvain@ubuntu$ curl https://www.holberton.online
Holberton School for the win!
sylvain@ubuntu$
```

>
+ [100-redirect_http_to_https](./100-redirect_http_to_https)

A good habit is to enforce HTTPS traffic so that no unencrypted traffic is possible. Configure HAproxy to automatically redirect HTTP traffic to HTTPS.

HAproxy should return a [301](https://en.wikipedia.org/wiki/HTTP_301)

The file [100-redirect_http_to_https](./100-redirect_http_to_https) is the HAproxy configuration file is `/etc/haproxy/haproxy.cfg`.

Example:
```
sylvain@ubuntu$ curl -sIL http://www.holberton.online
HTTP/1.1 301 Moved Permanently
Content-length: 0
Location: https://www.holberton.online/
Connection: close

HTTP/1.1 200 OK
Server: nginx/1.4.6 (Ubuntu)
Date: Tue, 28 Feb 2017 02:19:18 GMT
Content-Type: text/html
Content-Length: 30
Last-Modified: Tue, 21 Feb 2017 07:21:32 GMT
ETag: "58abea7c-1e"
X-Served-By: 03-web-01
Accept-Ranges: bytes

sylvain@ubuntu$
```

## References
- [What is HTTPS?](https://www.instantssl.com/http-vs-https)
- [What are the 2 main elements that SSL is providing](https://www.sslshopper.com/why-ssl-the-purpose-of-using-ssl-certificates.html)
- [SSL termination](https://en.wikipedia.org/wiki/TLS_termination_proxy)
- [Bash function](https://tldp.org/LDP/abs/html/complexfunct.html)

