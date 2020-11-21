# 配置静态ip

## windows系统

在控制面板中打开网络和internet选项

点击已经连接的网络

进入最下面的属性中

找到Internet协议ipv4，双击进行配置相关信息

## Linux系统

修改网卡信息配置文件

```
vim /etc/sysconfig/network-scripts/ifcfg-ens33
```

将ip获取方式`BOOTPROTO`从`dhcp`变为`static`

增加属性

```
ip地址:IPADDR=
子网掩码：NETMASK=255.255.255.0
DNS服务器：DNS=
网关：GETWAY=
```

重启网卡：`service network restart`