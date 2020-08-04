

### 玩转git三剑客

创建仓库目录
git init 初始化仓库

git 配置
用户名和密码， 可以是global或local
git config --global user.name "xxx"
git config --global user.email "xxx@gmail.com"

查看配置信息
git config --global --list


查看仓库状态
git status

添加文件
git add  xxx
如果有很多文件，可以使用git  add .  添加所有已修改的文件

提交
git commit -m "xxxxxx"


git add  是从
已修改 --- 已暂存 --- 已提交
工作区 --- 暂存区 --- 提交区

git rm --cached <file>... 从暂存区恢复到工作区


git log 可以查看所有的提交记录


## github
创建仓库
fork   or  create

fork已有的仓库
从头创建仓库

### 使用命令行给已有的本地仓库添加远程仓库
git remote add origin git@github.com:xxxxx/yyyy.git
git push -u origin master
origin 只是远程仓库的一个名字代号，可以使用其他的。使用git  remote可以查看远程仓库的名字代号。

生成公钥私钥，
ssh  -T  git@github.com



### 流程
fork
clone
coding...
add, commit, push


### 分支操作
创建分支
`git branch <branchname>`

切换分支
`git checkout <branchname>`

列出所有分支
`git branch`

删除分支
合并分支
