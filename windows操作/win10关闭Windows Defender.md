# win10关闭Windows Defender

##### 1.win键+R 进入cmd

输入`regedit` 回车

##### 2.在注册表里找到如下项目并更改

- **安全中心**
  HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\SecurityHealthService
  start值 2开启 4关闭
- **Windows Denfender**
  HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender
  DisableAntiSpyware值 0或者删除值开启 1关闭