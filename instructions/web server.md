# How to set up web server
1. Create apache web server  
  a. Download Ubuntu Server 22.04 iso (https://ubuntu.com/download/server)  
  b. configure network settings to NAT (default)
  c. update system and install apache2 and php  
  d. go to /var/www/html to edit pages
  e. set a static ip  
    - ```vim /etc/network/interfaces```  
    - change ```auto eth0
                  iface eth0 inet dhcp``` to ```inet static \ address 192.168.0.100
                                        netmask 255.255.255.0
                                        gateway 192.168.0.1
                                        dns-nameservers 4.4.4.4
                                        dns-nameservers 8.8.8.8```
2. Configure ufw (firewall)
  a. download ufw
  b. ```ufw allow 80/tcp```
  c. reset ``` ufw disable```  ```ufw enable```
  
4. Create the SQL server
