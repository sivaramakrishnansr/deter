Run script as 

```
sudo python setup.py -n 5 -s 17.0.0.1/16
```
Where n is the number of containers and s is the prefix. Ensure that the prefix is not 0 in the last octet.

To start a continer
```
sudo docker attach cont1
sudo docker start cont1
```
