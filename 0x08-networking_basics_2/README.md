# 0x08. Networking basics #1
### DevOps
- Network
- SysAdmin

|File					|Description							|
|-----------------------------|-----------------------------------------------------|
|0-change_your_home_IP		| a Bash script that configures an Ubuntu server with; `localhost` resolves to `127.0.0.2` and `facebook.com` resolves to `8.8.8.8`	|
|1-show_attached_IPs		|a Bash script that displays all active IPv4 IPs on the machine it’s executed on	|
|100-port_listening_on_localhost|a Bash script that listens on port `98` on `localhost`. On Terminal 0, start script by `sudo ./100-port_listening_on_localhost` and on Terminal 1 connect to `localhost` on port `98` using `telnet` and typing some text by `telnet localhost 98` |

## References
- [What is localhost](https://en.wikipedia.org/wiki/Localhost)
- [What is 0.0.0.0](https://en.wikipedia.org/wiki/0.0.0.0)
- [What is the hosts file](https://www.makeuseof.com/tag/modify-manage-hosts-file-linux/)
- [Netcat examples](https://www.thegeekstuff.com/2012/04/nc-command-examples/)
