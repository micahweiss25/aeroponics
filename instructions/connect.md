1. Create the unit file in /etc/systemd/system
```
[Unit]
Description=plz work
Wants=network.target
After=network.target

[Service]
ExecStart=/home/wei_pi/Desktop/connect
RemainAfterExit=yes

[Install]
WantedBy=multi-user.target
```
and name the file {file name}.service. The "Wants" and "After" lines make sure the service waits until the pi has a connection before running the connect script. 
3. The daemon script runs
```ssh -N -i /home/wei_pi/.ssh/my_key.pem -R 2222:localhost:22```
2. The daeomon is configured to wait a set amount of time so the pi has time to connect to WREN_GUEST
3. From a remote device, connect to the aws box
```ssh -i wei_aws_key.pem ubuntu@ec2-54-147-176-224.compute-1.amazonaws.com```
4. From the aws box, connect to the pi
```ssh -p2222 wei_pi@localhost```
