参考 [https://git-scm.com/book]

# 1. 版本控制

什么是“版本控制”？  
　版本控制是一种记录一个或若干文件内容变化，以便将来查阅特定版本修订情况的系统。  

1. 本地版本控制系统  
 大多都是采用某种简单的数据库来记录文件的历次更新差异。其中最流行的一种叫做 RCS，它的工作原理是在硬盘上保存补丁集（补丁是指文件修订前后的变化）；通过应用所有的补丁，可以重新计算出各个版本的文件内容。  
 ![local](images/topic1/local.png 'Local Version Control Systems')

2. 集中化的版本控制系统  
 如何让在不同系统上的开发者协同工作？于是，集中化的版本控制系统（Centralized Version Control Systems，简称 CVCS）应运而生。 这类系统，诸如 CVS、Subversion 以及 Perforce 等，都有一个单一的集中管理的服务器，保存所有文件的修订版本，而协同工作的人们都通过客户端连到这台服务器，取出最新的文件或者提交更新。  
 相对于老式的本地VCS来说，每个人在一定程度山可以看到项目中其他人在干什么，而管理员也可以轻松掌控每个开发者的权限，并且管理一个 CVCS 要远比在各个客户端上维护本地数据库来得轻松容易。  
 事分两面，有好有坏。 这么做最显而易见的缺点是中央服务器的单点故障。 如果宕机一小时，那么在这一小时内，谁都无法提交更新，也就无法协同工作。 如果中心数据库所在的磁盘发生损坏，又没有做恰当备份，毫无疑问你将丢失所有数据——包括项目的整个变更历史，只剩下人们在各自机器上保留的单独快照。 本地版本控制系统也存在类似问题，只要整个项目的历史记录被保存在单一位置，就有丢失所有历史更新记录的风险。
 ![centralized](images/topic1/centralized.png 'Centralized Version Control Systems')

3. 分布式版本控制系统  
 分布式版本控制系统（Distributed Version Control System，简称 DVCS），Git、Mercurial、Bazaar 以及 Darcs 等，客户端并不只提取最新版本的文件快照，而是把代码仓库完整地镜像下来。这么一来，任何一处协同工作用的服务器发生故障，事后都可以用任何一个镜像出来的本地仓库恢复。 因为每一次的克隆操作，实际上都是一次对代码仓库的完整备份。
 ![distributed](images/topic1/distributed.png 'Ｄistributed Version Control Systems')
 更进一步，许多这类系统都可以指定和若干不同的远端代码仓库进行交互。籍此，你就可以在同一个项目中，分别和不同工作小组的人相互协作。 你可以根据需要设定不同的协作流程，比如层次模型式的工作流，而这在以前的集中式系统中是无法实现的。

# 2. Git

1. 介绍
2. 命令行
3. 安装

# 3. 初次运行Git前的配置

`git config`助设置控制 Git 外观和行为的配置变量。这些变量存储在三个不同的位置：

- `/etc/gitconfig` 文件：包含系统上每一个用户及他们仓库的通用配置。 如果使用带有 `--system` 选项的 `git config` 时，它会从此文件读写配置变量。
- `~/.gitconfig` 或 `~/.config/git/config` 文件：只针对当前用户。 可以传递 `--global` 选项让 Git 读写此文件。
- 当前使用仓库的 Git 目录中的 `config` 文件（就是 `.git/config`）：针对该仓库。

每一个级别覆盖上一级别的配置，所以 `.git/config` 的配置变量会覆盖 `/etc/gitconfig` 中的配置变量。

在 `Windows` 系统中，Git 会查找 `$HOME` 目录下（一般情况下是 `C:\Users\$USER`）的 `.gitconfig` 文件。 Git 同样也会寻找 `/etc/gitconfig` 文件，但只限于 `MSys` 的根目录下，即安装 Git 时所选的目标位置。

## 3.1 用户信息

设置用户名称与邮件地址,每一个 Git 的提交都会使用这些信息，并且它会写入到你的每一次提交中，不可更改。

```command
$ git config --global user.name "John Doe"
$ git config --global user.email johndoe@example.com  
```

如果使用了 `--global` 选项，那么该命令只需要运行一次，因为之后无论你在该系统上做任何事情， Git 都会使用那些信息。 当你想针对特定项目使用不同的用户名称与邮件地址时，可以在那个项目目录下运行没有 `--global` 选项的命令来配置。

## 3.2 文本编辑器

`$ git config --global core.editor emacs`

## 3.3 检查配置信息

使用 `git config --list` 命令来列出所有 Git 当时能找到的配置。

使用形如 `git config <key>` 来检查 Git 的某一项配置。

## 3.4 获取帮助

有三种方法可以找到 Git 命令的使用手册：

```command
$ git help <verb>
$ git <verb> --help
$ man git-<verb>
```

## 3.5 三种状态

Git 有三种状态，你的文件可能处于其中之一：已提交（committed）、已修改（modified）和已暂存（staged）。

- 已提交表示数据已经安全的保存在本地仓库中。 
- 已修改表示修改了文件，但还没保存到仓库中。 
- 已暂存表示对一个已修改文件的当前版本做了标记，使之包含在下次提交的快照中。

由此引入 Git 项目的三个工作区域的概念：Git 仓库、工作目录以及暂存区域。
![areas](images/topic1/areas.png 'areas')

# 4. Git 基础

## 4.1 初始化仓库

现有项目中，初始化仓库 `$ git init`。该命令将创建一个名为 `.git` 的子目录，这个子目录含有你初始化的 Git 仓库中所有的必须文件。

## 4.2 克隆仓库

克隆仓库的命令格式是 `git clone [url]` 。比如，要克隆 Git 的可链接库 `libgit2`，可以用下面的命令：

```$ git clone https://github.com/libgit2/libgit2```

这会在当前目录下创建一个名为 “libgit2” 的目录，并在这个目录下初始化一个 `.git` 文件夹，从远程仓库拉取下所有数据放入 `.git` 文件夹，然后从中读取最新版本的文件的拷贝。 如果你进入到这个新建的 libgit2 文件夹，你会发现所有的项目文件已经在里面了，准备就绪等待后续的开发和使用。

如果你想在克隆远程仓库的时候，自定义本地仓库的名字，你可以使用如下命令：

```$ git clone https://github.com/libgit2/libgit2 mylibgit```

这将执行与上一个命令相同的操作，不过在本地创建的仓库名字变为 mylibgit。

## 4.3 记录库的更改

Git仓库中，对仓库中某些文件做些修改,在完成了一个阶段的目标之后，提交本次更新到仓库。

工作目录下的文件都不外乎两种状态：**已跟踪** 或 **未跟踪**。跟踪的文件是指那些被纳入了版本控制的文件，在上一次快照中有它们的记录，在工作一段时间后，它们的状态可能处于未修改，已修改或已放入暂存区。 工作目录中除已跟踪文件以外的所有其它文件都属于未跟踪文件，它们既不存在于上次快照的记录中，也没有放入暂存区。初次克隆某个仓库的时候，工作目录中的所有文件都属于已跟踪文件，并处于未修改状态。

编辑过某些文件之后，由于自上次提交后你对它们做了修改，Git 将它们标记为已修改文件。 我们逐步将这些修改过的文件放入暂存区，然后提交所有暂存了的修改，如此反复。所以使用 Git 时文件的生命周期如下：

![lifecycle](images/topic1/lifecycle.png 'lifecycle')

1. 检查当前文件状态  
 要查看哪些文件处于什么状态，可以用 `git status` 命令。

2. 跟踪新文件  
 使用命令 `git add` 开始跟踪一个文件。  
 `git add` 命令使用文件或目录的路径作为参数；如果参数是目录的路径，该命令将递归地跟踪该目录下的所有文件。

3. 暂存已修改文件  
   修改一个已被跟踪的文件。如果你修改了一个名为 `CONTRIBUTING.md` 的已被跟踪的文件，然后运行 `git status` 命令，会看到下面内容：
  
    ```command
    On branch master
    Changes to be committed:
    (use "git reset HEAD <file>..." to unstage)

        new file:   README

    Changes not staged for commit:
    (use "git add <file>..." to update what will be committed)
    (use "git checkout -- <file>..." to discard changes in working directory)

        modified:   CONTRIBUTING.md
    ```

   文件 `CONTRIBUTING.md` 出现在 `Changes not staged for commit` 这行下面，说明已跟踪文件的内容发生了变化，但还没有放到暂存区。 要暂存这次更新，需要运行 `git add` 命令。 这是个多功能命令：可以用它开始跟踪新文件，或者把已跟踪的文件放到暂存区，还能用于合并时把有冲突的文件标记为已解决状态等。 将这个命令理解为 “添加内容到下一次提交中” 而不是 “将一个文件添加到项目中” 要更加合适。 现在让我们运行 `git add` 将 "CONTRIBUTING.md" 放到暂存区，然后再看看 `git status` 的输出：

    ```comand
    $ git add CONTRIBUTING.md
    $ git status
    On branch master
    Changes to be committed:
    (use "git reset HEAD <file>..." to unstage)

        new file:   README
        modified:   CONTRIBUTING.md
    ```

   现在两个文件都已暂存，下次提交时就会一并记录到仓库。 假设此时，你想要在 `CONTRIBUTING.md` 里再加条注释， 重新编辑存盘后，准备好提交。 不过且慢，再运行 `git status` 看看：

    ```command
    $ vim CONTRIBUTING.md
    $ git status
    On branch master
    Changes to be committed:
    (use "git reset HEAD <file>..." to unstage)

        new file:   README
        modified:   CONTRIBUTING.md

    Changes not staged for commit:
    (use "git add <file>..." to update what will be committed)
    (use "git checkout -- <file>..." to discard changes in working directory)

        modified:   CONTRIBUTING.md
    ```
   怎么回事？ 现在 `CONTRIBUTING.md` 文件同时出现在暂存区和非暂存区。 这怎么可能呢？ 好吧，实际上 Git 只不过暂存了你运行 `git add` 命令时的版本， 如果你现在提交，`CONTRIBUTING.md` 的版本是你最后一次运行 `git add` 命令时的那个版本，而不是你运行 `git commit` 时，在工作目录中的当前版本。