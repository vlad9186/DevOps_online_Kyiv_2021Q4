Configuring DHCP, DNS servers
1. Use already created internal-network for three VMs (VM1-VM3). VM1 has NAT and internal, 
VM2, VM3 – internal only interfaces.
VM1:
 ![screenshot_1](screenshots/1.png)
VM2:
 ![screenshot_1](screenshots/3.png)
VM3:
 ![screenshot_1](screenshots/2.png)

2. Install and configure DHCP server on VM1. 
(3 ways: using VBoxManage, DNSMASQ and ISC-DHSPSERVER). 
You should use at least 2 of them.
 ![screenshot_1](screenshots/4.png)
 ![screenshot_1](screenshots/5.png)
 ![screenshot_1](screenshots/5.1.png)
 ![screenshot_1](screenshots/6.png)
 ![screenshot_1](screenshots/7.png)

 ![screenshot_1](screenshots/8.png)
 ![screenshot_1](screenshots/9.png)
 ![screenshot_1](screenshots/10.1.png)
 ![screenshot_1](screenshots/10.png)
 ![screenshot_1](screenshots/11.png)

3. Check VM2 and VM3 for obtaining network addresses from DHCP server.
 ![screenshot_1](screenshots/12.png)
 ![screenshot_1](screenshots/13.png)
 ![screenshot_1](screenshots/14.png)

4. Using existed network for three VMs (from p.1) install and configure DNS server on VM1. (You can use DNSMASQ, BIND9 or something else)

 ![screenshot_1](screenshots/15.png)
