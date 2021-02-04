# git使用

## 基本流程

### 初始化本地仓库

```
git init # 将这个文件夹作为本地仓库

git remote add origin SSH链接 # 添加远程仓库地址

git add . # 添加所有文件

git commit -m "备注" # 托管添加到的文件，并添加备注

git push -u origin master # 推到GitHub仓库
```

### 生成SSH密匙

```
git config --global user.name 用户名

git config --global user.email 邮箱

ssh-keygen.exe -t rsa -C "邮箱"

在github中添加了ssh密匙
```

### 拉取GitHub仓库到本地

```
git clone HTTP链接
```

### 避免每次都要输入密码

将http链接改为ssh链接

```
git remote rm origin
git remote -v
git remote add origin [ssh链接]
```

### 合并分支

```
git pull拉取所有代码到本地
git merge work 合并work分支中的新内容到本地分支
```

