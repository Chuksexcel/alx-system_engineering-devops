tack Debugging

This project contains tasks for 
learning about how to debug web 
stacks.

## Tasks To Complete

+ [x] 0. Nginx likes port 80<br/>_**[0-nginx_likes_port_80](0-nginx_likes_port_80)**_ contains a Bash script that fixes a failing server with the minimum number of commands.
  + Info:
    + Using your debugging skills, find out whats keeping your 
Ubuntu containers Nginx installation from listening on port 80. Feel free to install whatever tool you need, start and destroy 
as many containers as you need to debug the issue.
    + Example:
    ```powershell
    root@966c5664b21f:/# curl 0:80
    curl: (7) Failed to connect to 0 port 80: Connection refused
    root@966c5664b21f:/#
    root@966c5664b21f:/# ./0-nginx_likes_port_80 > /dev/null 2&>1
    root@966c5664b21f:/#
    root@966c5664b21f:/# curl 0:80
    <!DOCTYPE html>
    <html>
    <head>
