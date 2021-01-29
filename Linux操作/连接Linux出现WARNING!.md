连接Linux出现

WARNING! The remote SSH server rejected X11 forwarding request.



解决方法：

```
yum install xorg-x11-xauth
```

或者

```
vi /etc/ssh/sshd_config

修改
X11Forwarding yes
UseLogin no
如果注释掉了，去掉注释

然后重启ssh服务
systemctl restart sshd
```

