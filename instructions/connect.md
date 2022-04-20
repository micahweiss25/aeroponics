1. The daemon script runs
```ssh -N -i /home/wei_pi/.ssh/my_key.pem -R 2222:localhost:22```
2. The daeomon is configured to wait a set amount of time so the pi has time to connect to WREN_GUEST
3. From a remote device, connect to the aws box
```ssh -i wei_aws_key.pem ubuntu@ec2-54-147-176-224.compute-1.amazonaws.com```
4. From the aws box, connect to the pi
```ssh -p2222 wei_pi@localhost```
