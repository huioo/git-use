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

    ```command
    $ git add CONTRIBUTING.md
    $ git status
    On branch master
    Changes to be committed:
    (use "git reset HEAD <file>..." to unstage)

        new file:   README
        modified:   CONTRIBUTING.md
    ```

   `git commit`命令只会提交暂存区中的修改内容，如果添加参数标识`-a`，则会自动提交所有修改，包括未放入暂存区的修改。

## 4.4 状态简览

`git status` 命令的输出十分详细，但其用语有些繁琐。 如果你使用 `git status -s` 命令或 `git status --short` 命令，你将得到一种更为紧凑的格式输出。运行 git status -s ，状态报告输出如下：

```command
$ git status -s
 M README
MM Rakefile
A  lib/git.rb
M  lib/simplegit.rb
?? LICENSE.txt
AD delete.md
```

- `??`标记：新添加的未跟踪文件（新建的文件，未`git add`）
- `A`标记：新添加到暂存区中的文件（新建的文件，已`git add`）
- `M`标记：修改过的文件。可能存在2个`M`标记，右边的`M`标记表示该文件被修改了但是没放入暂存区，左边的`M`标记表示该文件被修改并放入暂存区，这种情况表示，该已跟踪文件有的修改已经放入暂存区，有的修改未放入暂存区。
- `D`标记：已经删除的文件

例如，上面的状态报告显示： `README` 文件在工作区被修改了但是还没有将修改后的文件放入暂存区，`lib/simplegit.rb` 文件被修改了并将修改后的文件放入了暂存区。 而 `Rakefile` 在工作区被修改并提交到暂存区后又在工作区中被修改了，所以在暂存区和工作区都有该文件被修改了的记录。

## 4.5 忽略文件

一般我们总会有些文件无需纳入 `Git` 的管理，也不希望它们总出现在未跟踪文件列表。通常都是些自动生成的文件，比如日志文件，或者编译过程中创建的临时文件等。

在这种情况下，我们可以创建一个名为 `.gitignore` 的文件，列出要忽略的文件模式。 来看一个实际的例子：

```command
$ cat .gitignore
*.[oa]
*~
```

- 第一行告诉 Git 忽略所有以 `.o` 或 `.a` 结尾的文件。一般这类对象文件和存档文件都是编译过程中出现的。
- 第二行告诉 Git 忽略所有以波浪符（~）结尾的文件，许多文本编辑软件（比如 Emacs）都用这样的文件名保存副本。
- 此外，你可能还需要忽略 `log`，`tmp` 或者 `pid` 目录，以及自动生成的文档等等。

要养成一开始就设置好 `.gitignore` 文件的习惯，以免将来误提交这类无用的文件。

文件 `.gitignore` 的格式规范如下：

- 所有空行或者以 ＃ 开头的行都会被 Git 忽略，类似注释。
- 可以使用标准的 glob 模式匹配。
- 匹配模式可以以（/）开头防止递归。
- 匹配模式可以以（/）结尾指定目录。
- 要忽略指定模式以外的文件或目录，可以在模式前加上惊叹号（!）取反。

所谓的 glob 模式是指 shell 所使用的简化了的正则表达式。具体如下：

- 星号（*）匹配零个或多个任意字符；
- [abc] 匹配任何一个列在方括号中的字符（这个例子要么匹配一个 a，要么匹配一个 b，要么匹配一个 c）；
- 问号（?）只匹配一个任意字符；
- 如果在方括号中使用短划线分隔两个字符，表示所有在这两个字符范围内的都可以匹配（比如 [0-9] 表示匹配所有 0 到 9 的数字）；
- 使用两个星号（*) 表示匹配任意中间目录，比如`a/**/z` 可以匹配 `a/z`, `a/b/z` 或 `a/b/c/z`等。

示例 [`example.gitignore`](example.gitignore) 。

## 4.6 查看已暂存和未暂存的修改

如果 `git status` 命令的输出对于你来说过于模糊，你想知道具体修改了什么地方，可以用 `git diff` 命令。

`git diff`将通过文件补丁的格式显示具体哪些行发生了改变，即它本身只显示尚未暂存的改动，而不是自上次提交以来所做的所有改动。此命令比较的是工作目录中当前文件和暂存区域快照之间的差异，也就是修改之后还没有暂存起来的变化内容。  
`git diff --cached` 查看已暂存的将要添加到下次提交里的内容。（Git 1.6.1 及更高版本还允许使用 `git diff --staged`，效果是相同的，但更好记些。）

## 4.7 提交更新

暂存区域已经准备妥当之后，就可以提交了。在此之前，请一定要确认还有什么修改过的或新建的文件还没有 `git add` 过，否则提交的时候不会记录这些还没暂存起来的变化。这些修改过的文件只保留在本地磁盘。所以，每次准备提交前，先用 `git status` 看下，是不是都已暂存起来了，然后再运行提交命令 `git commit`。

```command
$ git commit
```

编辑器会显示类似下面的文本信息（本例选用 Vim 的屏显方式展示）：

```command
# Please enter the commit message for your changes. Lines starting
# with '#' will be ignored, and an empty message aborts the commit.
# On branch master
# Changes to be committed:
#	new file:   README
#	modified:   CONTRIBUTING.md
#
~
~
~
".git/COMMIT_EDITMSG" 9L, 283C
```

可以看到，默认的提交消息包含最后一次运行 `git status` 的输出，放在注释行里，另外开头还有一空行，供你输入提交说明。你完全可以去掉这些注释行，不过留着也没关系，多少能帮你回想起这次更新的内容有哪些。 (如果想要更详细的对修改了哪些内容的提示，可以用 `-v` 选项，这会将你所做的改变的 `diff` 输出放到编辑器中从而使你知道本次提交具体做了哪些修改。）退出编辑器时，Git 会丢掉注释行，用你输入提交附带信息生成一次提交。

另外，你也可以在 `commit` 命令后添加 `-m` 选项，将提交信息与命令放在同一行，如下所示：

```command
$ git commit -m "Story 182: Fix benchmarks for speed"
[master 463dc4f] Story 182: Fix benchmarks for speed
 2 files changed, 2 insertions(+)
 create mode 100644 README
```

可以看到，提交后它会告诉你，当前是在哪个分支（master）提交的，本次提交的完整 `SHA-1` 校验和是什么（463dc4f），以及在本次提交中，有多少文件修订过，多少行添加和删改过。

请记住，提交时记录的是放在暂存区域的快照。任何还未暂存的仍然保持已修改状态，可以在下次提交时纳入版本管理。每一次运行提交操作，都是对你项目作一次快照，以后可以回到这个状态，或者进行比较。

## 4.8 跳过使用暂存区域

Git 提供了一个跳过使用暂存区域的方式， 只要在提交的时候，给 `git commit` 加上 `-a` 选项，Git 就会自动把所有已经跟踪过的文件暂存起来一并提交，从而跳过 `git add` 步骤：

```command
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

    modified:   CONTRIBUTING.md

no changes added to commit (use "git add" and/or "git commit -a")
$ git commit -a -m 'added new benchmarks'
[master 83e38c7] added new benchmarks
 1 file changed, 5 insertions(+), 0 deletions(-)
```

## 4.9 移除文件

要从 Git 中移除某个文件，就必须要**从已跟踪文件清单中移除**（确切地说，是**从暂存区域移除**），然后提交。可以用 `git rm` 命令完成此项工作，并连带从工作目录中删除指定的文件，这样以后就不会出现在未跟踪文件清单中了。

如果只是简单地从工作目录中手工删除文件，运行 `git status` 时就会在 “Changes not staged for commit” 部分（也就是 *未暂存清单*）看到：

```command
$ rm PROJECTS.md
$ git status
On branch master
Your branch is up-to-date with 'origin/master'.
Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

        deleted:    PROJECTS.md

no changes added to commit (use "git add" and/or "git commit -a")
```

然后再运行 git rm 记录此次移除文件的操作：

```command
$ git rm PROJECTS.md
rm 'PROJECTS.md'
$ git status
On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

    deleted:    PROJECTS.md
```

下一次提交时，该文件就**不再纳入版本管理**了。如果删除之前修改过并且已经放到暂存区域的话，则必须要用强制删除选项 `-f`（译注：即 `force` 的首字母）。 这是一种安全特性，用于防止误删还没有添加到快照的数据，这样的数据不能被 Git 恢复。

另外一种情况是，我们想把文件从 Git 仓库中删除（亦即从暂存区域移除），但仍然希望保留在当前工作目录中。 换句话说，你想让文件保留在磁盘，但是并不想让 Git 继续跟踪。当你忘记添加 `.gitignore` 文件，不小心把一个很大的日志文件或一堆 `.a` 这样的编译生成文件添加到暂存区时，这一做法尤其有用。为达到这一目的，使用 `--cached` 选项：

```command
$ git rm --cached README
...
```

`git rm` 命令后面可以列出文件或者目录的名字，也可以使用 `glob` 模式。 比方说：

```command
$ git rm log/\*.log
...
```

注意到星号 `*` 之前的反斜杠 `\`， 因为 Git 有它自己的文件模式扩展匹配方式，所以我们不用 `shell` 来帮忙展开。此命令删除 `log/` 目录下扩展名为 `.log` 的所有文件。 类似的比如：

```command
$ git rm \*~
```

该命令为删除以 `~` 结尾的所有文件。

## 4.10 移动文件

不像其它的 VCS 系统，Git 并不显式跟踪文件移动操作。 如果在 Git 中重命名了某个文件，仓库中存储的元数据并不会体现出这是一次改名操作。不过 Git 非常聪明，它会推断出究竟发生了什么，至于具体是如何做到的，我们稍后再谈。

既然如此，当你看到 Git 的 `mv` 命令时一定会困惑不已。 要在 Git 中对文件改名，可以这么做：

```command
$ git mv file_from file_to
...
```

它会恰如预期般正常工作。 实际上，即便此时查看状态信息，也会明白无误地看到关于重命名操作的说明：

```command
$ git mv README.md README
$ git status
On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

    renamed:    README.md -> README
```

其实，运行 `git mv` 就相当于运行了下面三条命令：

```command
$ mv README.md README
$ git rm README.md
$ git add README
```

如此分开操作，Git 也会意识到这是一次改名，所以不管何种方式结果都一样。 两者唯一的区别是，`mv` 是一条命令而另一种方式需要三条命令，直接用 `git mv` 轻便得多。 不过有时候用其他工具批处理改名的话，要记得在提交前删除老的文件名，再添加新的文件名。

## 4.11 查看提交历史

在提交了若干更新，又或者克隆了某个项目之后，你也许想回顾下提交历史。 完成这个任务最简单而又有效的工具是 `git log` 命令。

默认不用任何参数的话，`git log` 会按提交时间列出所有更新，最近的更新排在最上面。这个命令会列出每个提交的 `SHA-1` 校验和、作者的名字和电子邮件地址、提交时间以及提交说明。

`git log` 有许多选项可以帮助你搜寻你所要找的提交， 接下来我们介绍些最常用的。

- `-p` 选项  
  显示每次提交的内容差异。 你也可以加上 `-2` 来仅显示最近两次提交：`$ git log -p -2` 。
  该选项除了显示基本信息之外，还附带了每次 `commit` 的变化。当进行代码审查，或者快速浏览某个搭档提交的 `commit` 所带来的变化的时候，这个参数就非常有用了。
- `--stat` 选项  
  使用 `$ git log --stat` 查看每次提交的简略统计信息。
    ```command
    $ git log --stat
    commit ca82a6dff817ec66f44342007202690a93763949
    Author: Scott Chacon <schacon@gee-mail.com>
    Date:   Mon Mar 17 21:52:11 2008 -0700

        changed the version number

    Rakefile | 2 +-
    1 file changed, 1 insertion(+), 1 deletion(-)

    commit 085bb3bcb608e1e8451d4b2432f8ecbe6306e7e7
    Author: Scott Chacon <schacon@gee-mail.com>
    Date:   Sat Mar 15 16:40:33 2008 -0700

        removed unnecessary test

    lib/simplegit.rb | 5 -----
    1 file changed, 5 deletions(-)

    commit a11bef06a3f659402fe7563abf99ad00de2209e6
    Author: Scott Chacon <schacon@gee-mail.com>
    Date:   Sat Mar 15 10:31:28 2008 -0700

        first commit

    README           |  6 ++++++
    Rakefile         | 23 +++++++++++++++++++++++
    lib/simplegit.rb | 25 +++++++++++++++++++++++++
    3 files changed, 54 insertions(+)
    ```  
  在每次提交的下面列出所有被修改过的文件、有多少文件被修改了以及被修改过的文件的哪些行被移除或是添加了。在每次提交的最后还有一个总结。
- `--pretty` 选项  
  指定使用不同于默认格式的方式展示提交历史。这个选项有一些内建的子选项供你使用。 比如用 `oneline` 将每个提交放在一行显示，查看的提交数很大时非常有用。另外还有 `short`，`full` 和 `fuller` 可以用，展示的信息或多或少有些不同
    ```command
    $ git log --pretty=oneline
    ca82a6dff817ec66f44342007202690a93763949 changed the version number
    085bb3bcb608e1e8451d4b2432f8ecbe6306e7e7 removed unnecessary test
    a11bef06a3f659402fe7563abf99ad00de2209e6 first commit
    ```
  子选项 `format` ，允许自定义显示的格式。
    ```command
    $ git log --pretty=format:"%h - %an, %ar : %s"
    ca82a6d - Scott Chacon, 6 years ago : changed the version number
    085bb3b - Scott Chacon, 6 years ago : removed unnecessary test
    a11bef0 - Scott Chacon, 6 years ago : first commit
    ```
  `git log --pretty=format` [常用的选项](https://git-scm.com/book/zh/v2/ch00/rpretty_format) 列出了常用的格式占位符写法及其代表的意义。

- `--graph` 选项  
  当 `oneline` 或 `format` 与另一个 `log` 选项 `--graph` 结合使用时尤其有用。这个选项添加了一些ASCII字符串来形象地展示你的分支、合并历史：
    ```command
    $ git log --pretty=format:"%h %s" --graph
    * 2d3acf9 ignore errors from SIGCHLD on trap
    *  5e3ee11 Merge branch 'master' of git://github.com/dustin/grit
    |\
    | * 420eac9 Added a method for getting the current branch.
    * | 30e367c timeout code and tests
    * | 5a09431 add timeout protection to grit
    * | e1193f8 support for heads with slashes in them
    |/
    * d6016bc require time for xmlschema
    *  11d191e Merge branch 'defunkt' into local
    ```
- `git log` 的其它常用选项  
  列出了我们目前涉及到的和没涉及到的选项，以及它们是如何影响 log 命令的输出的：
    选项 |	说明
    --- | --- 
    -p      |按补丁格式显示每个更新之间的差异。
    --stat  |   显示每次更新的文件修改统计信息。
    --shortstat |   只显示 --stat 中最后的行数修改添加移除统计。
    --name-only |   仅在提交信息后显示已修改的文件清单。
    --name-status   |   显示新增、修改、删除的文件清单。
    --abbrev-commit |   仅显示 SHA-1 的前几个字符，而非所有的 40 个字符。
    --relative-date |   使用较短的相对时间显示（比如，“2 weeks ago”）。
    --graph     |	显示 ASCII 图形表示的分支合并历史。
    --pretty    |   使用其他格式显示历史提交信息。可用的选项包括 oneline，short，full，fuller 和 format（后跟指定格式）。
- 限制输出长度的选项  
  - `-<n>` 选项  
    之前你已经看到过 `-2` 了，它只显示最近的两条提交， 实际上，这是 `-<n>` 选项的写法，其中的 `n` 可以是任何整数，表示仅显示最近的若干条提交。
    不过实践中我们是不太用这个选项的，Git 在输出所有提交时会自动调用分页程序，所以你一次只会看到一页的内容。
  - `--since` 选项  
    列出所有最近两周内的提交：`$ git log --since=2.weeks`。
    具体的某一天 "2008-01-15"
    相对地多久以前 "2 years 1 day 3 minutes ago"。
  - `--author` 选项  
    显示指定作者的提交
  - `--grep` 选项  
    搜索提交说明中的关键字
  - `--all-match` 选项
    请注意，如果要得到同时满足这两个选项（比如`--author`和`--grep`）搜索条件的提交，就必须用 `--all-match` 选项。否则，满足任意一个条件的提交都会被匹配出来
  - `-S` 选项  
    列出那些添加或移除了某些字符串的提交。比如说，你想找出添加或移除了某一个特定函数的引用的提交，你可以这样使用：`$ git log -Sfunction_name`
  - (path) 选项
     如果只关心某些文件或者目录的历史提交，可以在 `git log` 选项的最后指定它们的路径。因为是放在最后位置上的选项，所以用两个短划线（--）隔开之前的选项和后面限定的路径名。
  - 常用选项  
    选项 |	说明
    --- | ---
    -(n)  | 仅显示最近的 n 条提交
    --since, --after  | 仅显示指定时间之后的提交。
    --until, --before | 仅显示指定时间之前的提交。
    --author  | 仅显示指定作者相关的提交。
    --committer | 仅显示指定提交者相关的提交。
    --grep  | 仅显示含指定关键字的提交
    -S  | 仅显示添加或移除了某个关键字的提交
  - 示例 —— 查看Git仓库中，2008年10月期间，Junio Hamano提交但未合并的测试文件。
    ```command
    $ git log --pretty="%h - %s" --author=gitster --since="2008-10-01" --before="2008-11-01" --no-merges -- t/
    5610e3b - Fix testcase failure when extended attributes are in use
    acd3b9e - Enhance hold_lock_file_for_{update,append}() API
    f563754 - demonstrate breakage of detached checkout with symbolic link HEAD
    d1a43f2 - reset --hard/read-tree --reset -u: remove unmerged new paths
    51a94af - Fix "checkout --track -b newbranch" on detached HEAD
    b0ad11e - pull: allow "git pull origin $something:$current_branch" into an unborn branch
    ```
    在近 40000 条提交中，上面的输出仅列出了符合条件的 6 条记录。

## 4.12 撤销操作

在任何一个阶段，你都有可能想要撤销某些操作。注意，有些撤销操作是不可逆的。这是在使用 Git 的过程中，会因为操作失误而导致之前的工作丢失的少有的几个地方之一。

1. 撤销操作 —— `git commit` 的 `--amend` 选项  
   有时候我们提交完了才发现漏掉了几个文件没有添加，或者提交信息写错了。
   此时，可以运行带有 `--amend` 选项的提交命令尝试重新提交：`$ git commit --amend`。这个命令会将暂存区中的文件提交。
   如果自上次提交以来你还未做任何修改（例如，在上次提交后马上执行了此命令），那么快照会保持不变，而你所修改的只是提交信息。
   文本编辑器启动后，可以看到之前的提交信息。 编辑后保存会覆盖原来的提交信息。
   例如，你提交后发现忘记了暂存某些需要的修改，可以像下面这样操作：
    ```command
    $ git commit -m 'initial commit'
    $ git add forgotten_file
    $ git commit --amend
    ```
   最终你只会有一个提交 - 第二次提交将代替第一次提交的结果。
2. 取消暂存 —— `git reset` 的 `HEAD <file> ...` 选项  
   假如你已经修改了两个文件并且想要将它们作为两次独立的修改提交，但是意外地输入了`git add *`暂存了它们两个。如何只取消暂存两个中的一个呢？
   `git status` 命令提示了你：使用`git reset HEAD <file>...`来取消暂存。所以，我们可以这样来取消暂存 `CONTRIBUTING.md` 文件：
    ```command
    $ git add *
    $ git status
    On branch master
    Changes to be committed:
      (use "git reset HEAD <file>..." to unstage)

        renamed:    README.md -> README
        modified:   CONTRIBUTING.md
    $ git reset HEAD CONTRIBUTING.md
    Unstaged changes after reset:
    M	CONTRIBUTING.md
    $ git status
    On branch master
    Changes to be committed:
      (use "git reset HEAD <file>..." to unstage)

        renamed:    README.md -> README

    Changes not staged for commit:
      (use "git add <file>..." to update what will be committed)
      (use "git checkout -- <file>..." to discard changes in working directory)

        modified:   CONTRIBUTING.md
    ```
3. 撤销对文件的修改 —— `git checkout` 命令  
   不想保留对 `CONTRIBUTING.md` 文件的修改，将它还原成上次提交时的样子。
    ```command
    $ git status
    Changes not staged for commit:
      (use "git add <file>..." to update what will be committed)
      (use "git checkout -- <file>..." to discard changes in working directory)

        modified:   CONTRIBUTING.md

    $ git checkout -- CONTRIBUTING.md
    $ git status
    On branch master
    Changes to be committed:
      (use "git reset HEAD <file>..." to unstage)

        renamed:    README.md -> README
    ```

## 4.13 远程仓库的使用

在任意Git项目上协作，需要使用**远程仓库**。远程仓库是指托管在因特网或其他网络中的你的项目的版本库。你可以有好几个远程仓库，通常有些仓库对你只读，有些则可以读写。与他人协作涉及管理远程仓库以及根据需要推送或拉取数据。  
管理远程仓库包括了解如何添加远程仓库、移除无效的远程仓库、管理不同的远程分支并定义它们是否被跟踪等等。

1. 查看远程仓库 —— `git remote` 命令和 `-v` 选项  
   `git remote` 命令：列出指定的每一个远程服务器的简写。
   `git remote -v` 命令：显示需要读写远程仓库使用的 Git 保存的简写与其对应的 URL。
   如果你的远程仓库不止一个，该命令会将它们全部列出。
2. 添加远程仓库 —— `git remote` 命令和 `add <shortname> <url>` 选项  
   运行 `git remote add <shortname> <url>` 添加一个新的远程 Git 仓库，同时指定一个你可以轻松引用的简写：
    ```command
    $ git remote
    origin
    $ git remote add pb https://github.com/paulboone/ticgit
    $ git remote -v
    origin	https://github.com/schacon/ticgit (fetch)
    origin	https://github.com/schacon/ticgit (push)
    pb	https://github.com/paulboone/ticgit (fetch)
    pb	https://github.com/paulboone/ticgit (push)
    ```
3. 从远程仓库中抓取与拉取 —— `git fetch [remote-name]` 命令  
   从远程仓库中获取数据，可以执行：`$ git fetch [remote-name]`。这个命令会访问远程仓库，从中拉取所有你还没有的数据。执行完成后，你将会拥有那个远程仓库中所有分支的引用，可以随时合并或查看。
   如果你使用 `clone` 命令克隆了一个仓库，命令会自动将其添加为远程仓库并默认以 “origin” 为简写。所以，`git fetch origin` 会抓取克隆（或上一次抓取）后新推送的所有工作。必须注意 `git fetch` 命令会将数据拉取到你的本地仓库 —— 它并不会自动合并或修改你当前的工作。 当准备好时你必须手动将其合并入你的工作。
4. 推送到远程仓库 —— `git push` 命令  
   使用 `git push [remote-name] [branch-name]` 将想要分享的仓库推送到上游。
   当你想要将 `master` 分支推送到 `origin` 服务器时（再次说明，克隆时通常会自动帮你设置好那两个名字），那么运行这个命令就可以将你所做的备份到服务器：`$ git push origin master` 。只有当你有所克隆服务器的写入权限，并且之前没有人推送过时，这条命令才能生效。当你和其他人在同一时间克隆，他们先推送到上游然后你再推送到上游，你的推送就会毫无疑问地被拒绝。你必须先将他们的工作拉取下来并将其合并进你的工作后才能推送。
5. 查看远程仓库 —— `git remote` 命令和 `show` 选项  
   使用 `git remote show [remote-name]` 命令，查看某一个远程仓库的更多信息。会列出远程仓库的 URL 与跟踪分支的信息，还列出当你在特定的分支上执行 git push 会自动地推送到哪一个远程分支。 它也同样地列出了哪些远程分支不在你的本地，哪些远程分支已经从服务器上移除了，还有当你执行 git pull 时哪些分支会自动合并。
6. 远程仓库的重命名 —— `git remote` 命令和 `rename` 选项  
   运行 `git remote rename` 去修改一个远程仓库的简写名。例如，想要将 `pb` 重命名为 `paul`，可以用 `git remote rename` 这样做：`$ git remote rename pb paul` 。
   值得注意的是这同样也会修改你的远程分支名字。 那些过去引用 `pb/master` 的现在会引用 `paul/master`。
7. 远程仓库的移除 —— `git remote` 命令和 `rm` 选项  
   如果因为一些原因想要移除一个远程仓库 - 你已经从服务器上搬走了或不再想使用某一个特定的镜像了，又或者某一个贡献者不再贡献了 - 可以使用 `git remote rm` ：删除 `paul` 远程仓库 `$ git remote rm paul`。

## 4.14 打标签

像其他版本控制系统（VCS）一样，Git 可以给历史中的某一个提交打上标签，以示重要。 比较有代表性的是人们会使用这个功能来标记发布结点（v1.0 等等）。

1. 列出标签 —— `git tag` 命令和 `-l` 选项  
   在 Git 中列出已有的标签是非常简单直观的。 只需要输入 `git tag`：
    ```command
    $ git tag
    v0.1
    v1.3
    ```
   这个命令以字母顺序列出标签；但是它们出现的顺序并不重要。你也可以使用特定的模式查找标签。 例如，Git 自身的源代码仓库包含标签的数量超过 `500` 个。 如果只对 `1.8.5` 系列感兴趣，可以运行：
    ```command
    $ git tag -l 'v1.8.5*'
    v1.8.5
    v1.8.5-rc0
    v1.8.5-rc1
    v1.8.5-rc2
    v1.8.5-rc3
    v1.8.5.1
    v1.8.5.2
    v1.8.5.3
    v1.8.5.4
    v1.8.5.5
    ```
2. 创建标签 —— 轻量标签和附注标签
   Git 使用两种主要类型的标签：**轻量标签（lightweight）** 与 **附注标签（annotated）**。
   一个轻量标签很像一个不会改变的分支 - 它只是一个特定提交的引用。
   附注标签是存储在 Git 数据库中的一个完整对象。
   它们是可以被校验的；其中包含打标签者的名字、电子邮件地址、日期时间；还有一个标签信息；并且可以使用 GNU Privacy Guard （GPG）签名与验证。通常建议创建附注标签，这样你可以拥有以上所有信息；但是如果你只是想用一个临时的标签，或者因为某些原因不想要保存那些信息，轻量标签也是可用的。
   - 附注标签 —— `-a` `-m` 选项  
      ```command
      $ git tag -a v1.4 -m 'my version 1.4'
      $ git tag
      v0.1
      v1.3
      v1.4
      ```
     使用`-a`选项创建一个附注标签，`-m`选项指定了一条将会存储在标签中的信息。如果没有为附注标签指定一条信息，Git 会运行编辑器要求你输入信息。
     使用`git show`命令查看标签信息与对应的提交信息。
   - 轻量标签  
     轻量标签本质上是将提交校验和存储到一个文件中 —— 没有保存任何其他信息。创建轻量标签，不需要使用 `-a`、`-s` 或 `-m` 选项，只需要提供标签名字：`$ git tag v1.4-lw`。这时，如果在标签上运行 `git show`，你不会看到额外的标签信息。 命令只会显示出提交信息。
   - 后期打标签  
     在命令的末尾指定提交的校验和（或部分校验和）: `$ git tag -a v1.2 9fceb02` 。
3. 共享标签  
   默认情况下，`git push` 命令并不会传送标签到远程仓库服务器上。 在创建完标签后你必须显式地推送标签到共享服务器上。
   这个过程就像共享远程分支一样 - 你可以运行 `git push origin [tagname]`。
   如果想要一次性推送很多标签，也可以使用带有 `--tags` 选项的 `git push` 命令。这将会把所有不在远程仓库服务器上的标签全部传送到那里。
4. 检出标签  
   在 Git 中你并不能真的检出一个标签，因为它们并不能像分支一样来回移动。 如果你想要工作目录与仓库中特定的标签版本完全一样，可以使用 `git checkout -b [branchname] [tagname]` 在特定的标签上创建一个新分支：
    ```command
    $ git checkout -b version2 v2.0.0
    Switched to a new branch 'version2'
    ```
   当然，如果在这之后又进行了一次提交，version2 分支会因为改动向前移动了，那么 version2 分支就会和 v2.0.0 标签稍微有些不同，这时就应该当心了。

## 4.15 Git别名

Git 并不会在你输入部分命令时自动推断出你想要的命令。如果不想每次都输入完整的 Git 命令，可以通过 `git config` 文件来轻松地为每一个命令设置一个别名。

这里有一些例子你可以试试：

```command
$ git config --global alias.co checkout
$ git config --global alias.br branch
$ git config --global alias.ci commit
$ git config --global alias.st status
```

这意味着，当要输入 `git commit` 时，只需要输入 `git ci`。 随着你继续不断地使用 Git，可能也会经常使用其他命令，所以创建别名时不要犹豫。

在创建你认为应该存在的命令时这个技术会很有用。 例如，为了解决取消暂存文件的易用性问题，可以向 Git 中添加你自己的取消暂存别名：

```command
$ git config --global alias.unstage 'reset HEAD --'
```

这会使下面的两个命令等价：

```command
$ git unstage fileA
$ git reset HEAD -- fileA
```

这样看起来更清楚一些。 通常也会添加一个 `last` 命令，像这样：

```command
$ git config --global alias.last 'log -1 HEAD'
```

这样，可以轻松地看到最后一次提交：

```command
$ git last
commit 66938dae3329c7aebe598c2246a8e6af90d04646
Author: Josh Goebel <dreamer3@example.com>
Date:   Tue Aug 26 19:48:51 2008 +0800

    test for current head

    Signed-off-by: Scott Chacon <schacon@example.com>
```

可以看出，Git 只是简单地将别名替换为对应的命令。 然而，你可能想要执行外部命令，而不是一个 Git 子命令。 如果是那样的话，可以在命令前面加入 `!` 符号。 如果你自己要写一些与 Git 仓库协作的工具的话，那会很有用。 我们现在演示将 `git visual` 定义为 `gitk` 的别名：

```command
$ git config --global alias.visual '!gitk'
```

# 5. Git 分支

Git 保存的不是文件的变化或者差异，而是一系列不同时刻的文件快照。

在进行提交操作时，Git 会保存一个提交对象（commit object）。知道了 Git 保存数据的方式，我们可以很自然的想到——该提交对象会包含一个指向暂存内容快照的指针。 但不仅仅是这样，该提交对象还包含了作者的姓名和邮箱、提交时输入的信息以及指向它的父对象的指针。

首次提交产生的提交对象没有父对象，普通提交操作产生的提交对象有一个父对象，而由多个分支合并产生的提交对象有多个父对象。为了更加形象地说明，我们假设现在有一个工作目录，里面包含了三个将要被暂存和提交的文件。 暂存操作会为每一个文件计算校验和（SHA-1 哈希算法），然后会把当前版本的文件快照保存到 Git 仓库中（Git 使用 blob 对象来保存它们），最终将校验和加入到暂存区域等待提交。

当使用 `git commit` 进行提交操作时，Git 会先计算每一个子目录（本例中只有项目根目录）的校验和，然后在 Git 仓库中这些校验和保存为树对象。 随后，Git 便会创建一个提交对象，它除了包含上面提到的那些信息外，还包含指向这个树对象（项目根目录）的指针。如此一来，Git 就可以在需要的时候重现此次保存的快照。

现在，Git 仓库中有五个对象：三个 blob 对象（保存着文件快照）、一个树对象（记录着目录结构和 blob 对象索引）以及一个提交对象（包含着指向前述树对象的指针和所有提交信息）。
![commit-and-tree](images/topic5/commit-and-tree.png '首次提交对象及其树结构')

做些修改后再次提交，那么这次产生的提交对象会包含一个指向上次提交对象（父对象）的指针。
![commits-and-parents](images/topic5/commits-and-parents.png '提交对象及其父对象')

Git 的分支，其实本质上仅仅是指向提交对象的可变指针。 Git 的默认分支名字是 master。 在多次提交操作之后，你其实已经有一个指向最后那个提交对象的 master 分支。它会在每次的提交操作中自动向前移动。
![branch-and-history](images/topic5/branch-and-history.png '分支及其提交历史')

- 分支创建  
  Git 是怎么创建新分支的呢？ 很简单，它只是为你创建了一个可以移动的新的指针。比如，创建一个 `testing` 分支， 你需要使用 `git branch` 命令：

   `$ git branch testing`

  这会在当前所在的提交对象上创建一个指针。
   ![two-branches](images/topic5/two-branches.png '两个指向相同提交历史的分支')

  那么，Git 又是怎么知道当前在哪一个分支上呢？也很简单，它有一个名为 `HEAD` 的特殊指针。在 Git 中，它是一个指针，指向当前所在的本地分支（译注：将 HEAD 想象为当前分支的别名）。在本例中，你仍然在 master 分支上。 因为 `git branch` 命令仅仅 创建 一个新分支，并不会自动切换到新分支中去。
   ![head-to-master](images/topic5/head-to-master.png 'HEAD 指向当前所在的分支')

- 分支切换  
  要切换到一个已存在的分支，你需要使用 `git checkout` 命令。 我们现在切换到新创建的 `testing` 分支去：

  `$ git checkout testing`

  这样 HEAD 就指向 testing 分支了。
   ![head-to-testing](images/topic5/head-to-testing.png 'HEAD 指向当前所在的分支')

  那么，这样的实现方式会给我们带来什么好处呢？ 现在不妨再提交一次。
   ![advance-testing](images/topic5/advance-testing.png 'HEAD 分支随着提交操作自动向前移动')

  如图所示，你的 `testing` 分支向前移动了，但是 `master` 分支却没有，它仍然指向运行 `git checkout` 时所指的对象。 这就有意思了，现在我们切换回 `master` 分支看看：`$ git checkout master`。
   ![checkout-master](images/topic5/checkout-master.png '检出时 HEAD 随之移动')

  这条命令做了两件事。 一是使 HEAD 指回 master 分支，二是将工作目录恢复成 master 分支所指向的快照内容。 也就是说，你现在做修改的话，项目将始于一个较旧的版本。 本质上来讲，这就是忽略 testing 分支所做的修改，以便于向另一个方向进行开发。

  **注意**： 分支切换会改变你工作目录中的文件
  在切换分支时，一定要注意你工作目录里的文件会被改变。 如果是切换到一个较旧的分支，你的工作目录会恢复到该分支最后一次提交时的样子。
  
  我们不妨再稍微做些修改并提交。现在，这个项目的提交历史已经产生了分叉。因为刚才你创建了一个新分支，并切换过去进行了一些工作，随后又切换回 master 分支进行了另外一些工作。 上述两次改动针对的是不同分支：你可以在不同分支间不断地来回切换和工作，并在时机成熟时将它们合并起来。 而所有这些工作，你需要的命令只有 `branch`、`checkout` 和 `commit`。
   ![advance-master](images/topic5/advance-master.png '项目分叉历史')
- 查看分支  
  你可以简单地使用 `git log` 命令查看分叉历史。 
  运行 `git log --oneline --decorate --graph --all` ，它会输出你的提交历史、各个分支的指向以及项目的分支分叉情况。

## 5.1 分支的新建与合并

一个简单的分支新建与分支合并的例子，实际工作中可能会用到类似的工作流。类似工作步骤如下：

1. 开发某个网站
2. 为实现某个新的需求，创建一个分支
3. 在这个分支上展开工作。

正在此时，你突然接到一个电话说有个很严重的问题需要紧急修补。类似工作步骤如下：

1. 切换到你的线上分支（production branch）
2. 为这个紧急任务新建一个分支，并在其中修复它
3. 在测试通过之后，切换回线上分支，然后合并这个修补分支，最后将改动推送到线上分支
4. 切换回你最初工作的分支上，继续工作

### 5.1.1 新建分支

假设你正在你的项目上工作，并且有了一些提交。类似下图所示：
![basic-branching-1](images/topic5/basic-branching-1.png '一个简单提交历史')

现在需要解决问题跟踪系统中的 `#53` 问题。想要新建一个分支并同时切换到那个分支上，可以使用带有`-b`参数的`git branch`命令:

```command
$ git checkout -b iss53
Switched to a new branch "iss53"
```

它是下面两条命令的简写，且分支情况如下图所示：

```command
$ vim index.html
$ git commit -a -m 'added a new footer [issue 53]'
```

![basic-branching-2](images/topic5/basic-branching-2.png '创建一个新分支指针')

继续工作并做了一些提交，操作如下。在此过程中`iss53`分支不断向前推进，因为你已经检出到该分支（也就是说，你的 `HEAD` 指针指向了 `iss53` 分支），分支情况如下图所示：

```command
$ vim index.html
$ git commit -a -m 'added a new footer [issue 53]'
```

![basic-branching-3](images/topic5/basic-branching-3.png 'iss53 分支随着工作的进展向前推进')

现在接到那个电话，有个紧急问题需要处理。有了 Git 的帮助，你不必把这个紧急问题和 `iss53` 的修改混在一起，你也不需要花大力气来还原关于 `53#` 问题的修改，然后再添加关于这个紧急问题的修改，最后将这个修改提交到线上分支。你所要做的仅仅是切换回 master 分支。  
但是，在你这么做之前，要留意你的工作目录和暂存区里那些还没有被提交的修改，它可能会和你即将检出的分支产生冲突从而阻止 Git 切换到该分支。  
最好的方法是，在你切换分支之前，保持好一个 **干净** 的状态。 有一些方法可以绕过这个问题（即，**保存进度（stashing）** 和 **修补提交（commit amending）**），我们会在 [储藏与清理](https://git-scm.com/book/zh/v2/ch00/r_git_stashing) 中看到关于这两个命令的介绍。 现在，我们假设你已经把你的修改全部提交了，这时你可以切换回 master 分支了：

```command
$ git checkout master
Switched to branch 'master'
```

这时，工作目录与处理`#53`问题之前一模一样，现在可以修复紧急问题了。切换分支时，Git 会重置工作目录，使其回到这个分支上一次提交的时候。  
**注意**： Git 会自动添加、删除、修改文件以确保此时你的工作目录和这个分支最后一次提交时的样子一模一样。

接下来新建该紧急问题的分支（hotfix branch）来解决问题，直到问题解决，分支情况如下图所示：

```command
$ git checkout -b hotfix
Switched to a new branch 'hotfix'
$ vim index.html
$ git commit -a -m 'fixed the broken email address'
[hotfix 1fb7853] fixed the broken email address
1 file changed, 2 insertions(+)
```

![basic-branching-4](images/topic5/basic-branching-4.png '基于 master 分支的紧急问题分支 hotfix branch')

运行测试，确保修改正确，然后将其合并回到 master 分支上，并部署到线上。使用 `git merge` 命令：

```command
$ git checkout master
$ git merge hotfix
Updating f42c576..3a0874c
Fast-forward
  index.html | 2 ++
  1 file changed, 2 insertions(+)
```

在合并的时候，你应该注意到了 **"快进（fast-forward）"** 这个词。由于当前 master 分支所指向的提交是你当前提交（有关 hotfix 的提交）的直接上游，所以 Git 只是简单的将指针向前移动。换句话说，当你试图合并两个分支时，如果顺着一个分支走下去能够到达另一个分支，那么 Git 在合并两者的时候，只会简单的将指针向前推进（指针右移），因为这种情况下的合并操作没有需要解决的分歧——这就叫做 “快进（fast-forward）”。  
现在，最新的修改已经在 master 分支所指向的提交快照中，你可以着手发布该修复了。
![basic-branching-5](images/topic5/basic-branching-5.png 'master 被快进到 hotfix')

### 5.1.2 删除分支

关于这个紧急问题的解决方案发布之后，你准备回到被打断之前时的工作中。 然而，你应该先删除 `hotfix` 分支，因为你已经不再需要它了 —— `master` 分支已经指向了同一个位置。你可以使用带 `-d` 选项的 `git branch` 命令来删除分支：

```command
$ git branch -d hotfix
Deleted branch hotfix (3a0874c).
```
现在你可以切换回你正在工作的分支继续你的工作，也就是针对 `#53` 问题的那个分支（iss53 分支）。

```command
$ git checkout iss53
Switched to branch "iss53"
$ vim index.html
$ git commit -a -m 'finished the new footer [issue 53]'
[iss53 ad82d7a] finished the new footer [issue 53]
1 file changed, 1 insertion(+)
```

![basic-branching-6](images/topic5/basic-branching-6.png '继续在 iss53 分支上的工作')
你在 `hotfix` 分支上所做的工作并没有包含到 `iss53` 分支中。如果你需要拉取 `hotfix` 所做的修改，你可以使用 `git merge master` 命令将 `master` 分支合并入 `iss53` 分支，或者你也可以等到 `iss53` 分支完成其使命，再将其合并回 master 分支。

### 5.1.3 合并分支

假设你已经修正了 `#53` 问题，并且打算将你的工作合并入 `master` 分支。为此，你需要合并 `iss53` 分支到 `master` 分支，这和之前你合并 `hotfix` 分支所做的工作差不多。 你只需要检出到你想合并入的分支，然后运行 `git merge` 命令：

```command
$ git checkout master
Switched to branch 'master'
$ git merge iss53
Merge made by the 'recursive' strategy.
index.html |    1 +
1 file changed, 1 insertion(+)
```

这和你之前合并 `hotfix` 分支的时候看起来有一点不一样。在这种情况下，你的开发历史从一个更早的地方开始分叉开来（**diverged**）。因为，`master` 分支所在提交并不是 `iss53` 分支所在提交的直接祖先，Git 不得不做一些额外的工作。  
出现这种情况的时候，Git 会使用两个分支的末端所指的快照（`C4` 和 `C5`）以及这两个分支的工作祖先（`C2`），做一个简单的三方合并。合并情况如下图所示：
![basic-merging-1](images/topic5/basic-merging-1.png '一次典型合并中所用到的三个快照')

和之前将分支指针向前推进所不同的是，Git 将此次三方合并的结果做了一个 **新的快照** 并且自动创建一个 **新的提交** 指向它。这个被称作一次 **合并提交**，它的特别之处在于他有不止一个父提交。
![basic-merging-2](images/topic5/basic-merging-2.png '一个合并提交')

需要指出的是，Git 会自行决定选取哪一个提交作为最优的共同祖先，并以此作为合并的基础；这和更加古老的 CVS 系统或者 Subversion （1.5 版本之前）不同，在这些古老的版本管理系统中，用户需要自己选择最佳的合并基础。Git 的这个优势使其在合并操作上比其他系统要简单很多。  
既然你的修改已经合并进来了，你已经不再需要 `iss53` 分支了。 现在你可以在任务追踪系统中关闭此项任务，并删除这个分支。

```command
$ git branch -d iss53
```

### 5.1.4 遇到冲突时的分支合并

有时候合并操作不会如此顺利。如果你在两个不同分支中，对同一个文件的同一部分进行了不同的修改，Git 就没法干净的合并它们。  
如果你对 `#53` 问题的修改和有关 `hotfix` 的修改都涉及到同一个文件的同一处，在合并它们的时候就会产生合并冲突：

```command
$ git merge iss53
Auto-merging index.html
CONFLICT (content): Merge conflict in index.html
Automatic merge failed; fix conflicts and then commit the result.
```

此时 Git 做了合并，但是没有自动地创建一个新的合并提交。 Git 会暂停下来，等待你去解决合并产生的冲突。  
你可以在合并冲突后的任意时刻使用 `git status` 命令来查看那些因包含合并冲突而处于未合并（**unmerged**）状态的文件：

```command
$ git status
On branch master
You have unmerged paths.
  (fix conflicts and run "git commit")

Unmerged paths:
  (use "git add <file>..." to mark resolution)

    both modified:      index.html

no changes added to commit (use "git add" and/or "git commit -a")
```

任何因包含合并冲突而有待解决的文件，都会以未合并状态标识出来。Git 会在有冲突的文件中加入标准的冲突解决标记，这样你可以打开这些包含冲突的文件然后手动解决冲突。现冲突的文件会包含一些特殊区段，看起来像下面这个样子：

```html
<<<<<<< HEAD:index.html
<div id="footer">contact : email.support@github.com</div>
=======
<div id="footer">
 please contact us at support@github.com
</div>
>>>>>>> iss53:index.html
```

这表示 `HEAD` 所指示的版本（也就是你的 `master` 分支所在的位置，因为你在运行 `merge` 命令的时候已经检出到了这个分支）在这个区段的上半部分（ `=======` 的上半部分），而 `iss53` 分支所指示的版本在 `=======` 的下半部分。 为了解决冲突，你必须选择使用由 `=======` 分割的两部分中的一个，或者你也可以自行合并这些内容。例如，你可以通过把这段内容换成下面的样子来解决冲突：

```html
<div id="footer">
please contact us at email.support@github.com
</div>
```

上述的冲突解决方案仅保留了其中一个分支的修改，并且 `<<<<<<<` , `=======` , 和 `>>>>>>>` 这些行被完全删除了。在你解决了所有文件里的冲突之后，对每个文件使用 `git add` 命令来将其标记为冲突已解决。一旦暂存这些原本有冲突的文件，Git 就会将它们标记为冲突已解决。

如果你想使用 **图形化工具** 来解决冲突，你可以运行 `git mergetool`，该命令会为你启动一个合适的可视化合并工具，并带领你一步一步解决这些冲突：

```command
$ git mergetool

This message is displayed because 'merge.tool' is not configured.
See 'git mergetool --tool-help' or 'git help config' for more details.
'git mergetool' will now attempt to use one of the following tools:
opendiff kdiff3 tkdiff xxdiff meld tortoisemerge gvimdiff diffuse diffmerge ecmerge p4merge araxis bc3 codecompare vimdiff emerge
Merging:
index.html

Normal merge conflict for 'index.html':
  {local}: modified file
  {remote}: modified file
Hit return to start merge resolution tool (opendiff):
```

如果你想使用除默认工具（在这里 Git 使用 `opendiff` 做为默认的合并工具，因为作者在 Mac 上运行该程序）外的其他合并工具，你可以在 “下列工具中（one of the following tools）” 这句后面看到所有支持的合并工具。 然后输入你喜欢的工具名字就可以了。  
Note：如果你需要更加高级的工具来解决复杂的合并冲突，我们会在 [高级合并](https://git-scm.com/book/zh/v2/ch00/r_advanced_merging) 介绍更多关于分支合并的内容。

等你退出合并工具之后，Git 会询问刚才的合并是否成功。如果你回答是，Git 会暂存那些文件以表明冲突已解决： 你可以再次运行 `git status` 来确认所有的合并冲突都已被解决：

```command
$ git status
On branch master
All conflicts fixed but you are still merging.
  (use "git commit" to conclude merge)

Changes to be committed:

    modified:   index.html
```

如果你对结果感到满意，并且确定之前有冲突的的文件都已经暂存了，这时你可以输入 `git commit` 来完成合并提交。 默认情况下提交信息看起来像下面这个样子：

```command
Merge branch 'iss53'

Conflicts:
    index.html
#
# It looks like you may be committing a merge.
# If this is not correct, please remove the file
#	.git/MERGE_HEAD
# and try again.


# Please enter the commit message for your changes. Lines starting
# with '#' will be ignored, and an empty message aborts the commit.
# On branch master
# All conflicts fixed but you are still merging.
#
# Changes to be committed:
#	modified:   index.html
#
```

如果你觉得上述的信息不够充分，不能完全体现分支合并的过程，你可以修改上述信息，添加一些细节给未来检视这个合并的读者一些帮助，告诉他们你是如何解决合并冲突的，以及理由是什么。

## 5.2 分支管理

分支管理 `git branch`：它不只是可以创建与删除分支。 如果不加任何参数运行它，会得到当前所有分支的一个列表：

```command
$ git branch
  iss53
* master
  testing
```

注意 master 分支前的 `*` 字符：它代表现在检出的那一个分支（即当前 `HEAD` 指针所指向的分支）。这意味着如果在这时候提交，master 分支将会随着新的工作向前移动。

运行 `git branch -v` 命令查看每一个分支的最后一次提交:

```command
$ git branch -v
  iss53   93b412c fix javascript issue
* master  7a98805 Merge branch 'iss53'
  testing 782fd34 add scott to the author list in the readmes
```

`--merged` 与 `--no-merged` 这两个有用的选项可以过滤这个列表中已经合并或尚未合并到当前分支的分支。  
运行 `git branch --merged` 查看哪些分支已经合并到当前分支：

```command
$ git branch --merged
  iss53
* master
```

因为之前已经合并了 `iss53` 分支，所以现在看到它在列表中。在这个列表中分支名字前没有 `*` 号的分支通常可以使用 `git branch -d` 删除掉；你已经将它们的工作整合到了另一个分支，所以并不会失去任何东西。

运行 `git branch --no-merged`查看所有包含未合并工作的分支：

```command
$ git branch --no-merged
  testing
```

这里显示了其他分支。因为它包含了还未合并的工作，尝试使用 `git branch -d` 命令删除它时会失败：

```command
$ git branch -d testing
error: The branch 'testing' is not fully merged.
If you are sure you want to delete it, run 'git branch -D testing'.
```

如果真的想要删除分支并丢掉那些工作，如同帮助信息里所指出的，可以使用 `-D` 选项强制删除它。

## 5.3 分支开发工作流

### 5.3.1 长期分支

因为 Git 使用简单的三方合并，所以就算在一段较长的时间内，反复把一个分支合并入另一个分支，也不是什么难事。 也就是说，在整个项目开发周期的不同阶段，你可以同时拥有多个开放的分支；你可以定期地把某些特性分支合并入其他分支中。

许多使用 Git 的开发者都喜欢使用这种方式来工作，比如只在 `master` 分支上保留完全稳定的代码——有可能仅仅是已经发布或即将发布的代码。他们还有一些名为 `develop` 或者 `next` 的平行分支，被用来做后续开发或者测试稳定性——这些分支不必保持绝对稳定，但是一旦达到稳定状态，它们就可以被合并入 `master` 分支了。 这样，在确保这些已完成的特性分支（短期分支，比如之前的 `iss53` 分支）能够通过所有测试，并且不会引入更多 `bug` 之后，就可以合并入主干分支中，等待下一次的发布。

稳定分支的指针总是在提交历史中落后一大截，而前沿分支的指针往往比较靠前。
![lr-branches-1](images/topic5/lr-branches-1.png '渐进稳定分支的线性图')

通常把他们想象成流水线（work silos）可能更好理解一点，那些经过测试考验的提交会被遴选到更加稳定的流水线上去。
![lr-branches-2](images/topic5/lr-branches-2.png '渐进稳定分支的流水线（“silo”）视图')

你可以用这种方法维护不同层次的稳定性。一些大型项目还有一个 `proposed`（建议） 或 `pu`: `proposed updates`（建议更新）分支，它可能因包含一些不成熟的内容而不能进入 `next` 或者 `master` 分支。这么做的目的是使你的分支具有不同级别的稳定性；当它们具有一定程度的稳定性后，再把它们合并入具有更高级别稳定性的分支中。再次强调一下，使用多个长期分支的方法并非必要，但是这么做通常很有帮助，尤其是当你在一个非常庞大或者复杂的项目中工作时。

### 5.3.2 特性分支

特性分支对任何规模的项目都适用。特性分支是一种短期分支，它被用来 **实现单一特性或其相关工作**。

你已经在上一节中你创建的 `iss53` 和 `hotfix` 特性分支中看到过这种用法。 你在上一节用到的特性分支（`iss53` 和 `hotfix` 分支）中提交了一些更新，并且在它们合并入主干分支之后，你又删除了它们。  
这项技术能使你快速并且完整地进行上下文切换（context-switch）——因为你的工作被分散到不同的流水线中，在不同的流水线中每个分支都仅与其目标特性相关，因此，在做代码审查之类的工作的时候就能更加容易地看出你做了哪些改动。你可以把做出的改动在特性分支中保留几分钟、几天甚至几个月，等它们成熟之后再合并，而不用在乎它们建立的顺序或工作进度。

考虑这样一个例子，你在 master 分支上工作到 `C1`，这时为了解决一个问题而新建 `iss91` 分支，在 `iss91` 分支上工作到 `C4`，然而对于那个问题你又有了新的想法，于是你再新建一个 `iss91v2` 分支试图用另一种方法解决那个问题，接着你回到 master 分支工作了一会儿，你又冒出了一个不太确定的想法，你便在 `C10` 的时候新建一个 `dumbidea` 分支，并在上面做些实验。 你的提交历史看起来像下面这个样子：
![topic-branches-1](images/topic5/topic-branches-1.png '拥有多个特性分支的提交历史')

现在，我们假设两件事情：你决定使用第二个方案来解决那个问题，即使用在 `iss91v2` 分支中方案；另外，你将 `dumbidea` 分支拿给你的同事看过之后，结果发现这是个惊人之举。这时你可以抛弃 `iss91` 分支（即丢弃 `C5` 和 `C6` 提交），然后把另外两个分支合并入主干分支。最终你的提交历史看起来像下面这个样子：
![topic-branches-2](images/topic5/topic-branches-2.png '合并了 dumbidea 和 iss91v2 分支之后的提交历史')

请牢记，当你做这么多操作的时候，这些分支全部都存于本地。 当你新建和合并分支的时候，所有这一切都只发生在你本地的 Git 版本库中 —— 没有与服务器发生交互。

## 5.4 远程分支

远程引用是对远程仓库的引用（指针），包括分支、标签等等。查看远程分支的方式如下所示。然而，一个更常见的做法是利用远程跟踪分支。

- 通过 `git ls-remote (remote)` 来显式地获得远程引用的完整列表。  
- 通过 `git remote show (remote)` 获得远程分支的更多信息。

**远程跟踪分支** 是远程分支状态的引用。它们是你不能移动的本地引用，当你做任何网络通信操作时，它们会自动移动。远程跟踪分支像是你上次连接到远程仓库时，那些分支所处状态的书签。  
它们以 `(remote)/(branch)` 形式命名。 例如，如果你想要看你最后一次与远程仓库 `origin` 通信时 `master` 分支的状态，你可以查看 `origin/master` 分支。你与同事合作解决一个问题并且他们推送了一个 `iss53` 分支，你可能有自己的本地 `iss53` 分支；但是在服务器上的分支会指向 `origin/iss53` 的提交。  
这可能有一点儿难以理解，让我们来看一个例子。 假设你的网络里有一个在 `git.ourcompany.com` 的 Git 服务器。 如果你从这里克隆，Git 的 `clone` 命令会为你自动将其命名为 `origin`，拉取它的所有数据，创建一个指向它的 `master` 分支的指针，并且在本地将其命名为 `origin/master`。 Git 也会给你一个与 `origin` 的 `master` 分支在指向同一个地方的本地 `master` 分支，这样你就有工作的基础。
![remote-branches-1](images/topic5/remote-branches-1.png '克隆之后的服务器与本地仓库')

如果你在本地的 `master` 分支做了一些工作，然而在同一时间，其他人推送提交到 `git.ourcompany.com` 并更新了它的 `master` 分支，那么你的提交历史将向不同的方向前进。也许，只要你不与 `origin` 服务器连接，你的 `origin/master` 指针就不会移动。
![remote-branches-2](images/topic5/remote-branches-2.png '本地与远程的工作可以分叉')

### 5.4.1 同步

运行 `git fetch origin` 命令来同步你的工作。  
这个命令查找 “origin” 是哪一个服务器（在本例中，它是 `git.ourcompany.com`），从中抓取本地没有的数据，并且更新本地数据库，移动 `origin/master` 指针指向新的、更新后的位置。
![remote-branches-3](images/topic5/remote-branches-3.png 'git fetch 更新你的远程仓库引用')

为了演示有多个远程仓库与远程分支的情况，我们假定你有另一个内部 Git 服务器，仅用于你的 `sprint` 小组的开发工作。这个服务器位于 `git.team1.ourcompany.com`。你可以运行 `git remote add` 命令添加一个新的远程仓库引用到当前的项目，这个命令我们会在 [Git 基础](https://git-scm.com/book/zh/v2/ch00/ch02-git-basics) 中详细说明。将这个远程仓库命名为 `teamone`，将其作为整个 URL 的缩写。
![remote-branches-4](images/topic5/remote-branches-4.png '添加另一个远程仓库')

运行 `git fetch teamone` 来抓取远程仓库 `teamone` 有而本地没有的数据。因为那台服务器上现有的数据是 `origin` 服务器上的一个子集，所以 Git 并不会抓取数据而是会设置远程跟踪分支 `teamone/master` 指向 `teamone` 的 `master` 分支。
![remote-branches-5](images/topic5/remote-branches-5.png '远程跟踪分支 teamone/master')

### 5.4.2 推送

当你想要公开分享一个分支时，需要将其推送到有写入权限的远程仓库上。 本地的分支并不会自动与远程仓库同步 - 你必须显式地推送想要分享的分支。 这样，你就可以把不愿意分享的内容放到私人分支上，而将需要和别人协作的内容推送到公开分支。

如果希望和别人一起在名为 `serverfix` 的分支上工作，你可以像推送第一个分支那样推送它。 运行 `git push (remote) (branch)`:

```command
$ git push origin serverfix
Counting objects: 24, done.
Delta compression using up to 8 threads.
Compressing objects: 100% (15/15), done.
Writing objects: 100% (24/24), 1.91 KiB | 0 bytes/s, done.
Total 24 (delta 2), reused 0 (delta 0)
To https://github.com/schacon/simplegit
 * [new branch]      serverfix -> serverfix
```

这里有些工作被简化了。 Git 自动将 `serverfix` 分支名字展开为 `refs/heads/serverfix:refs/heads/serverfix`，那意味着，“推送本地的 serverfix 分支来更新远程仓库上的 serverfix 分支。  
你也可以运行 `git push origin serverfix:serverfix`，它会做同样的事 - 相当于它说，“推送本地的 serverfix 分支，将其作为远程仓库的 serverfix 分支” 可以通过这种格式来推送本地分支到一个命名不相同的远程分支。  
如果并不想让远程仓库上的分支叫做 `serverfix`，可以运行 `git push origin serverfix:awesomebranch` 来将本地的 `serverfix` 分支推送到远程仓库上的 awesomebranch 分支。

下一次其他协作者从服务器上抓取数据时，他们会在本地生成一个远程分支 `origin/serverfix`，指向服务器的 `serverfix` 分支的引用：

```command
$ git fetch origin
remote: Counting objects: 7, done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 0), reused 3 (delta 0)
Unpacking objects: 100% (3/3), done.
From https://github.com/schacon/simplegit
 * [new branch]      serverfix    -> origin/serverfix
```

要特别注意的一点是当抓取到新的远程跟踪分支时，本地不会自动生成一份可编辑的副本（拷贝）。 换一句话说，这种情况下，不会有一个新的 `serverfix` 分支 - 只有一个不可以修改的 `origin/serverfix` 指针。  
可以运行 `git merge origin/serverfix` 将这些工作合并到当前所在的分支。 如果想要在自己的 `serverfix` 分支上工作，可以将其建立在远程跟踪分支之上：

```command
$ git checkout -b serverfix origin/serverfix
Branch serverfix set up to track remote branch serverfix from origin.
Switched to a new branch 'serverfix'
```

这会给你一个用于工作的本地分支，并且起点位于 `origin/serverfix`。

### 5.4.3 跟踪分支

从一个远程跟踪分支检出一个本地分支会自动创建一个叫做 “跟踪分支”（有时候也叫做 “上游分支”）。跟踪分支是与远程分支有直接关系的本地分支。如果在一个跟踪分支上输入 `git pull`，Git 能自动地识别去哪个服务器上抓取、合并到哪个分支。

当克隆一个仓库时，它通常会自动地创建一个跟踪 `origin/master` 的 `master` 分支。 然而，如果你愿意的话可以设置其他的跟踪分支 - 其他远程仓库上的跟踪分支，或者不跟踪 `master` 分支。最简单的就是之前看到的例子，运行 `git checkout -b [branch] [remotename]/[branch]`。  
这是一个十分常用的操作所以 Git 提供了 `--track` 快捷方式：

```command
$ git checkout --track origin/serverfix
Branch serverfix set up to track remote branch serverfix from origin.
Switched to a new branch 'serverfix'
```

如果想要将本地分支与远程分支设置为不同名字，你可以轻松地增加一个不同名字的本地分支的上一个命令：

```command
$ git checkout -b sf origin/serverfix
Branch sf set up to track remote branch serverfix from origin.
Switched to a new branch 'sf'
```

现在，本地分支 `sf` 会自动从 `origin/serverfix` 拉取。  
设置已有的本地分支跟踪一个刚刚拉取下来的远程分支，或者想要修改正在跟踪的上游分支，你可以在任意时间使用 `-u` 或 `--set-upstream-to` 选项运行 `git branch` 来显式地设置。

```command
$ git branch -u origin/serverfix
Branch serverfix set up to track remote branch serverfix from origin.
```

如果想要查看设置的所有跟踪分支，可以使用 `git branch` 的 `-vv` 选项。 这会将所有的本地分支列出来并且包含更多的信息，如每一个分支正在跟踪哪个远程分支与本地分支是否是领先、落后或是都有。

```command
$ git branch -vv
  iss53     7e424c3 [origin/iss53: ahead 2] forgot the brackets
  master    1ae2a45 [origin/master] deploying index fix
* serverfix f8674d9 [teamone/server-fix-good: ahead 3, behind 1] this should do it
  testing   5ea463a trying something new
```

这里可以看到 `iss53` 分支正在跟踪 `origin/iss53` 并且 “ahead” 是 2，意味着本地有两个提交还没有推送到服务器上。 也能看到 `master` 分支正在跟踪 `origin/master` 分支并且是最新的。 接下来可以看到 `serverfix` 分支正在跟踪 `teamone` 服务器上的 `server-fix-good` 分支并且领先 3 落后 1，意味着服务器上有一次提交还没有合并入同时本地有三次提交还没有推送。 最后看到 `testing` 分支并没有跟踪任何远程分支。

需要重点注意的一点是这些数字的值来自于你从每个服务器上最后一次抓取的数据。这个命令并没有连接服务器，它只会告诉你关于本地缓存的服务器数据。如果想要统计最新的领先与落后数字，需要在运行此命令前抓取所有的远程仓库。可以像这样做：`$ git fetch --all; git branch -vv`。

### 5.4.4 拉取

当 `git fetch` 命令从服务器上抓取本地没有的数据时，它并不会修改工作目录中的内容。它只会获取数据然后让你自己合并。然而，有一个命令叫作 `git pull` 在大多数情况下它的含义是一个 `git fetch` 紧接着一个 `git merge` 命令。

如果有一个像之前章节中演示的设置好的跟踪分支，不管它是显式地设置还是通过 `clone` 或 `checkout` 命令为你创建的，`git pull` 都会查找当前分支所跟踪的服务器与分支，从服务器上抓取数据然后尝试合并入那个远程分支。

由于 `git pull` 的魔法经常令人困惑所以通常单独显式地使用 `fetch` 与 `merge` 命令会更好一些。

### 5.4.5 删除远程分支

假设你已经通过远程分支做完所有的工作了 - 也就是说你和你的协作者已经完成了一个特性并且将其合并到了远程仓库的 `master` 分支（或任何其他稳定代码分支）。可以运行带有 `--delete` 选项的 `git push` 命令来删除一个远程分支。 如果想要从服务器上删除 `serverfix` 分支，运行下面的命令：

```command
$ git push origin --delete serverfix
To https://github.com/schacon/simplegit
 - [deleted]         serverfix
```

基本上这个命令做的只是从服务器上移除这个指针。Git 服务器通常会保留数据一段时间直到垃圾回收运行，所以如果不小心删除掉了，通常是很容易恢复的。

## 5.5 变基

在 Git 中整合来自不同分支的修改主要有两种方法：merge 以及 rebase。

### 5.5.1 变基的基本操作

前面我们看到开发任务分叉到两个不同分支，又各自提交了更新。
![basic-rebase-1](images/topic5/basic-rebase-1.png '分叉的提交历史')
之后整合分支，最容易的方法是 `merge` 命令。它会把两个分支的最新快照（C3 和 C4）以及二者最近的共同祖先（C2）进行三方合并，合并的结果是生成一个新的快照（并提交）。
![basic-rebase-2](images/topic5/basic-rebase-2.png '通过合并操作来整合分叉了的历史')
其实还有一种方式，你可以提取在 `C4` 中引入的补丁和修改，然后在 `C3` 的基础上应用一次。在 Git 中，这种操作就叫做 *变基*。你可以使用 `rebase` 命令将提交到某一分支上的所有修改都移至另一分支上，就好像“重新播放”一样。在上面这个例子中，运行：

```command
$ git checkout experiment
$ git rebase master
First, rewinding head to replay your work on top of it...
Applying: added staged command
```

它的原理是首先找到这两个分支（即当前分支 `experiment`、变基操作的目标基底分支 `master`）的最近共同祖先 `C2`，然后对比当前分支相对于该祖先的历次提交，提取相应的修改并存为临时文件，然后将当前分支指向目标基底 C3, 最后以此将之前另存为临时文件的修改依序应用。
![basic-rebase-3](images/topic5/basic-rebase-3.png '将 C4 中的修改变基到 C3 上')

现在回到 master 分支，进行一次快进合并。

```command
$ git checkout master
$ git merge experiment
```

![basic-rebase-4](images/topic5/basic-rebase-4.png 'master 分支的快进合并')
此时，`C4'` 指向的快照就和上面使用 `merge` 命令的例子中 `C5` 指向的快照一模一样了。这两种整合方法的最终结果没有任何区别，但是变基使得提交历史更加整洁。你在查看一个经过变基的分支的历史记录时会发现，尽管实际的开发工作是并行的，但它们看上去就像是串行的一样，提交历史是一条直线没有分叉。  
一般我们这样做的目的是为了确保在向远程分支推送时能 **保持提交历史的整洁**——例如向某个其他人维护的项目贡献代码时。在这种情况下，你首先在自己的分支里进行开发，当开发完成时你需要先将你的代码变基到 `origin/master` 上，然后再向主项目提交修改。这样的话，该项目的维护者就不再需要进行整合工作，只需要快进合并便可。

请注意，无论是通过变基，还是通过三方合并，整合的最终结果所指向的快照始终是一样的，只不过提交历史不同罢了。变基是将一系列提交按照原有次序依次应用到另一分支上，而合并是把最终结果合在一起。

### 5.5.2 更有趣的变基例子

在对两个分支进行变基时，所生成的“重放”并不一定要在目标分支上应用，你也可以指定另外的一个分支进行应用。就像从一个特性分支里再分出一个特性分支那样，你创建了一个特性分支 `server`，为服务端添加了一些功能，提交了 `C3` 和 `C4`。然后从 `C3` 上创建了特性分支 `client`，为客户端添加了一些功能，提交了 `C8` 和 `C9`。 最后，你回到 server 分支，又提交了 `C10`。
![interesting-rebase-1](images/topic5/interesting-rebase-1.png '从一个特性分支里再分出一个特性分支的提交历史')

假设你希望将 `client` 中的修改合并到主分支并发布，但暂时并不想合并 `server` 中的修改，因为它们还需要经过更全面的测试。 这时，你就可以使用 `git rebase` 命令的 `--onto` 选项，选中在 `client` 分支里但不在 `server` 分支里的修改（即 `C8` 和 `C9`），将它们在 master 分支上重放：

```command
$ git rebase --onto master server client
```

以上命令的意思是：“取出 `client` 分支，找出处于 `client` 分支和 `server` 分支的共同祖先之后的修改，然后把它们在 `master` 分支上重放一遍”。
![interesting-rebase-2](images/topic5/interesting-rebase-2.png '截取特性分支上的另一个特性分支，然后变基到其他分支')

现在可以快进合并 `master` 分支了。操作命令与分支情况如下所示：

```command
$ git checkout master
$ git merge client
```

![interesting-rebase-3](images/topic5/interesting-rebase-3.png '快进合并 master 分支，使之包含来自 client 分支的修改')

接下来你决定将 `server` 分支中的修改也整合进来。 使用 `git rebase [basebranch] [topicbranch]` 命令可以直接将特性分支（即本例中的 `server`）变基到目标分支（即 `master`）上。这样做能省去你先切换到 `server` 分支，再对其执行变基命令的多个步骤。

```command
$ git rebase master server
```

如图将 `server` 中的修改变基到 `master` 上 所示，`server` 中的代码被“续”到了 `master` 后面。
![interesting-rebase-4](images/topic5/interesting-rebase-4.png '将 server 中的修改变基到 master 上')

然后就可以快进合并主分支 master 了：

```command
$ git checkout master
$ git merge server
```

至此，`client` 和 `server` 分支中的修改都已经整合到主分支里了，你可以删除这两个分支，最终提交历史会变成下图中的样子：

```command
$ git branch -d client
$ git branch -d server
```

![interesting-rebase-5](images/topic5/interesting-rebase-5.png '最终的提交历史')

### 5.5.3 变基的风险

呃，奇妙的变基也并非完美无缺，要用它得遵守一条准则：

> **不要对在你的仓库外有副本的分支执行变基。**

变基操作的实质是丢弃一些现有的提交，然后相应地新建一些内容一样但实际上不同的提交。如果你已经将提交推送至某个仓库，而其他人也已经从该仓库拉取提交并进行了后续工作，此时，如果你用 git rebase 命令重新整理了提交并再次推送，你的同伴因此将不得不再次将他们手头的工作与你的提交进行整合，如果接下来你还要拉取并整合他们修改过的提交，事情就会变得一团糟。

让我们来看一个在公开的仓库上执行变基操作所带来的问题。 假设你从一个中央服务器克隆然后在它的基础上进行了一些开发。 你的提交历史如图所示：
![perils-of-rebasing-1](images/topic5/perils-of-rebasing-1.png '克隆一个仓库，然后在它的基础上进行了一些开发')

然后，某人又向中央服务器提交了一些修改，其中还包括一次合并。你抓取了这些在远程分支上的修改，并将其合并到你本地的开发分支，然后你的提交历史就会变成这样：
![perils-of-rebasing-2](images/topic5/perils-of-rebasing-2.png '抓取别人的提交，合并到自己的开发分支')

接下来，这个人又决定把合并操作回滚，改用变基；继而又用 `git push --force` 命令覆盖了服务器上的提交历史。之后你从服务器抓取更新，会发现多出来一些新的提交。
![perils-of-rebasing-3](images/topic5/perils-of-rebasing-3.png '有人推送了经过变基的提交，并丢弃了你的本地开发所基于的一些提交')

结果就是你们两人的处境都十分尴尬。 如果你执行 `git pull` 命令，你将合并来自两条提交历史的内容，生成一个新的合并提交，最终仓库会如图所示：
![perils-of-rebasing-4](images/topic5/perils-of-rebasing-4.png '你将相同的内容又合并了一次，生成了一个新的提交')

此时如果你执行 `git log` 命令，你会发现有两个提交的作者、日期、日志居然是一样的，这会令人感到混乱。 此外，如果你将这一堆又推送到服务器上，你实际上是将那些已经被变基抛弃的提交又找了回来，这会令人感到更加混乱。 很明显对方并不想在提交历史中看到 `C4` 和 `C6`，因为之前就是他把这两个提交通过变基丢弃的。

### 5.5.4 用变基解决变基

如果你 **真的** 遭遇了类似的处境，Git 还有一些高级魔法可以帮到你。 如果团队中的某人强制推送并覆盖了一些你所基于的提交，你需要做的就是检查你做了哪些修改，以及他们覆盖了哪些修改。

实际上，Git 除了对整个提交计算 `SHA-1` 校验和以外，也对本次提交所引入的修改计算了校验和—— 即 “patch-id”。

如果你拉取被覆盖过的更新并将你手头的工作基于此进行变基的话，一般情况下 Git 都能成功分辨出哪些是你的修改，并把它们应用到新分支上。

![perils-of-rebasing-3](images/topic5/perils-of-rebasing-3.png '有人推送了经过变基的提交，并丢弃了你的本地开发所基于的一些提交')
举个例子，如果遇到前面提到的 [有人推送了经过变基的提交，并丢弃了你的本地开发所基于的一些提交](https://git-scm.com/book/zh/v2/ch00/r_pre_merge_rebase_work) 那种情境，如果我们不是执行合并，而是执行 `git rebase teamone/master`, Git 将会：

- 检查哪些提交是我们的分支上独有的（C2，C3，C4，C6，C7）
- 检查其中哪些提交不是合并操作的结果（C2，C3，C4）
- 检查哪些提交在对方覆盖更新时并没有被纳入目标分支（只有 C2 和 C3，因为 C4 其实就是 C4'）
- 把查到的这些提交应用在 teamone/master 上面

从而我们将得到与 [你将相同的内容又合并了一次，生成了一个新的提交](https://git-scm.com/book/zh/v2/ch00/r_merge_rebase_work) 中不同的结果，如图 [在一个被变基然后强制推送的分支上再次执行变基](https://git-scm.com/book/zh/v2/ch00/r_rebase_rebase_work) 所示。
![perils-of-rebasing-5](images/topic5/perils-of-rebasing-5.png '在一个被变基然后强制推送的分支上再次执行变基')

要想上述方案有效，还需要对方在变基时确保 C4' 和 C4 是几乎一样的。 否则变基操作将无法识别，并新建另一个类似 C4 的补丁（而这个补丁很可能无法整洁的整合入历史，因为补丁中的修改已经存在于某个地方了）。

在本例中另一种简单的方法是使用 `git pull --rebase` 命令而不是直接 `git pull`。 又或者你可以自己手动完成这个过程，先 `git fetch`，再 `git rebase teamone/master`。  
如果你习惯使用 `git pull` ，同时又希望默认使用选项 `--rebase`，你可以执行这条语句 `git config --global pull.rebase true` 来更改 `pull.rebase` 的默认配置。

只要你把变基命令当作是在推送前清理提交使之整洁的工具，并且只在从未推送至共用仓库的提交上执行变基命令，就不会有事。

### 5.5.5 变基 vs. 合并

至此，你已在实战中学习了变基和合并的用法，你一定会想问，到底哪种方式更好。 在回答这个问题之前，让我们退后一步，想讨论一下 **提交历史到底意味着什么**。

有一种观点认为，仓库的提交历史即是 **记录实际发生过什么**。它是针对历史的文档，本身就有价值，不能乱改。 从这个角度看来，改变提交历史是一种亵渎，你使用 *谎言* 掩盖了实际发生过的事情。 如果由合并产生的提交历史是一团糟怎么办？ 既然事实就是如此，那么这些痕迹就应该被保留下来，让后人能够查阅。

另一种观点则正好相反，他们认为提交历史是 **项目过程中发生的事**。 没人会出版一本书的第一版草稿，软件维护手册也是需要反复修订才能方便使用。 持这一观点的人会使用 `rebase` 及 `filter-branch` 等工具来编写故事，怎么方便后来的读者就怎么写。

现在，让我们回到之前的问题上来，到底合并还是变基好？希望你能明白，这并没有一个简单的答案。 Git 是一个非常强大的工具，它允许你对提交历史做许多事情，但每个团队、每个项目对此的需求并不相同。 既然你已经分别学习了两者的用法，相信你能够根据实际情况作出明智的选择。

总的原则是，只对尚未推送或分享给别人的本地修改执行变基操作清理历史，从不对已推送至别处的提交执行变基操作，这样，你才能享受到两种方式带来的便利。

# 6. 服务器上的Git

为了使用 Git 协作功能，你还需要有远程的 Git 仓库。

4.1 协议
4.2 在服务器上搭建 Git
4.3 生成 SSH 公钥
4.4 配置服务器
4.5 Git 守护进程
4.6 Smart HTTP
4.7 GitWeb
4.8 GitLab
4.9 第三方托管的选择
4.10 总结

# 7. 分布式 Git

拥有了一个远程 Git 版本库，能为所有开发者共享代码提供服务，在一个本地工作流程下，你也已经熟悉了基本 Git 命令。你现在可以学习如何利用 Git 提供的一些分布式工作流程了。

## 7.1 分布式工作流程

- 集中式工作流 —— 单点协作模型  
  一个中心集线器，或者说仓库，可以接受代码，所有人将自己的工作与之同步。 若干个开发者则作为节点——也就是中心仓库的消费者——并且与其进行同步。
   ![centralized_workflow](images/topic7/centralized_workflow.png '集中式工作流')
  
  这意味着如果两个开发者从中心仓库克隆代码下来，同时作了一些修改，那么只有第一个开发者可以顺利地把数据推送回共享服务器。 第二个开发者在推送修改之前，必须先将第一个人的工作合并进来，这样才不会覆盖第一个人的修改。
- 集成管理者工作流  
  Git 允许多个远程仓库存在，使得这样一种工作流成为可能：每个开发者拥有自己仓库的写权限和其他所有人仓库的读权限。  
  这种情形下通常会有个代表 “官方” 项目的权威的仓库。 要为这个项目做贡献，你需要从该项目克隆出一个自己的公开仓库，然后将自己的修改推送上去。接着你可以请求官方仓库的维护者拉取更新合并到主项目。维护者可以将你的仓库作为远程仓库添加进来，在本地测试你的变更，将其合并入他们的分支并推送回官方仓库。  
  这一流程的工作方式如下所示：
  1. 项目维护者推送到主仓库。
  2. 贡献者克隆此仓库，做出修改。
  3. 贡献者将数据推送到自己的公开仓库。
  4. 贡献者给维护者发送邮件，请求拉取自己的更新。
  5. 维护者在自己本地的仓库中，将贡献者的仓库加为远程仓库并合并修改。
  6. 维护者将合并后的修改推送到主仓库。

  ![integration-manager](images/topic7/integration-manager.png '集成管理者工作流')

  这是 GitHub 和 GitLab 等集线器式（hub-based）工具最常用的工作流程。
- 司令官与副官工作流
  这其实是多仓库工作流程的变种。 一般拥有数百位协作开发者的超大型项目才会用到这样的工作方式，例如著名的 `Linux` 内核项目。  
  被称为副官（lieutenant）的各个集成管理者分别负责集成项目中的特定部分。  
  所有这些副官头上还有一位称为司令官（dictator）的总集成管理者负责统筹。司令官维护的仓库作为参考仓库，为所有协作者提供他们需要拉取的项目代码。  
  整个流程看起来是这样的：
  1. 普通开发者在自己的特性分支上工作，并根据 master 分支进行变基。 这里是司令官的`master`分支。
  2. 副官将普通开发者的特性分支合并到自己的 master 分支中。
  3. 司令官将所有副官的 master 分支并入自己的 master 分支中。
  4. 司令官将集成后的 master 分支推送到参考仓库中，以便所有其他开发者以此为基础进行变基。

  ![benevolent-dictator.png](images/topic7/benevolent-dictator.png '司令官与副官工作流')

5.2 向一个项目贡献
5.3 维护项目
5.4 总结

# 8. GitHub

6.1 账户的创建和配置
6.2 对项目做出贡献
6.3 维护项目
6.4 管理组织
6.5 脚本 GitHub
6.6 总结

# 9. Git 工具

## 9.1 选择修订版本

通过 Git 给出的 `SHA-1` 值来获取一次提交，不过还有很多更人性化的方式来做同样的事情。

### 9.1.1 简短的 `SHA-1`  
只需要提供 `SHA-1` 的前几个字符就可以获得对应的那次提交，当然你提供的 `SHA-1` 字符数量不得少于 4 个，并且没有歧义——也就是说，当前仓库中只有一个对象以这段 `SHA-1` 开头。  
假设执行 `git log` 命令来查看之前新增一个功能的那次提交，这个提交是 `1c002dd4b536e7479fe34593e72e6c6c1819e53b` ，如果你想 `git show` 这个提交，下面的命令是等价的：

```command
$ git show 1c002dd4b536e7479fe34593e72e6c6c1819e53b
$ git show 1c002dd4b536e7479f
$ git show 1c002d
```

Git 可以为 `SHA-1` 值生成出简短且唯一的缩写。如果你在 `git log` 后加上 `--abbrev-commit` 参数，输出结果里就会显示简短且唯一的值；

```command
$ git log --abbrev-commit --pretty=oneline
ca82a6d changed the version number
085bb3b removed unnecessary test code
a11bef0 first commit
```

### 9.1.2 分支引用  

指明一次提交最直接的方法是有一个指向它的分支引用。这样你就可以在任意一个 Git 命令中使用这个分支名来代替对应的提交对象或者 SHA-1 值。  
例如，你想要查看一个分支的最后一次提交的对象，假设 `topic1` 分支指向 `ca82a6d` ，那么以下的命令是等价的:

```command
$ git show ca82a6dff817ec66f44342007202690a93763949
$ git show topic1
```

如果你想知道某个分支指向哪个特定的 SHA-1，或者想看任何一个例子中被简写的 SHA-1 ，你可以使用一个叫做 `rev-parse` 的 Git 探测工具。 

### 9.1.3 引用日志

当你在工作时， Git 会在后台保存一个引用日志(reflog)，引用日志记录了最近几个月你的 `HEAD` 和分支引用所指向的历史。你可以使用 `git reflog` 来查看引用日志：

```command
$ git reflog
734713b HEAD@{0}: commit: fixed refs handling, added gc auto, updated
d921970 HEAD@{1}: merge phedders/rdocs: Merge made by recursive.
1c002dd HEAD@{2}: commit: added some blame and merge stuff
1c36188 HEAD@{3}: rebase -i (squash): updating HEAD
95df984 HEAD@{4}: commit: # This is a combination of two commits.
1c36188 HEAD@{5}: rebase -i (squash): updating HEAD
7e05da5 HEAD@{6}: rebase -i (pick): updating HEAD
```

每当你的 HEAD 所指向的位置发生了变化，Git 就会将这个信息存储到引用日志这个历史记录里。通过这些数据，你可以很方便地获取之前的提交历史。如果你想查看仓库中 `HEAD` 在五次前的所指向的提交，你可以使用 `@{n}` 来引用 `reflog` 中输出的提交记录，即 `$ git show HEAD@{5}` 。

你同样可以使用这个语法来查看某个分支在一定时间前的位置。 例如，查看你的 master 分支在昨天的时候指向了哪个提交，你可以输入 `$ git show master@{yesterday}` 。就会显示昨天该分支的顶端指向了哪个提交。

可以运行 `git log -g` 来查看类似于 `git log` 输出格式的引用日志信息。

值得注意的是，引用日志只存在于本地仓库，一个记录你在你自己的仓库里做过什么的日志。 其他人拷贝的仓库里的引用日志不会和你的相同；而你新克隆一个仓库的时候，引用日志是空的，因为你在仓库里还没有操作。 `git show HEAD@{2.months.ago}` 这条命令只有在你克隆了一个项目至少两个月时才会有用——如果你是五分钟前克隆的仓库，那么它将不会有结果返回。

### 9.1.3 祖先引用

祖先引用是另一种指明一个提交的方式。如果你在引用的尾部加上一个 `^`， Git 会将其解析为该引用的上一个提交。 假设你的提交历史是：

```command
$ git log --pretty=format:'%h %s' --graph
* 734713b fixed refs handling, added gc auto, updated tests
*   d921970 Merge commit 'phedders/rdocs'
|\
| * 35cfb2b Some rdoc changes
* | 1c002dd added some blame and merge stuff
|/
* 1c36188 ignore *.gem
* 9b29157 add open3_detach to gemspec file list
```

你可以使用 `HEAD^` 来查看上一个提交，也就是 “HEAD 的父提交”：

```command
$ git show HEAD^
commit d921970aadf03b3cf0e71becdaab3147ba71cdef
Merge: 1c002dd... 35cfb2b...
Author: Scott Chacon <schacon@gmail.com>
Date:   Thu Dec 11 15:08:43 2008 -0800

    Merge commit 'phedders/rdocs'
```

你也可以在 `^` 后面添加一个数字——例如 `d921970^2` 代表 “d921970 的第二父提交” 这个语法只适用于合并(merge)的提交，因为合并提交会有多个父提交。第一父提交是你合并时所在分支，而第二父提交是你所合并的分支：

另一种指明祖先提交的方法是 `~`。同样是指向第一父提交，因此 `HEAD~` 和 `HEAD^` 是等价的。而区别在于你在后面加数字的时候。 `HEAD~2` 代表 “第一父提交的第一父提交”，也就是 “祖父提交” —— Git 会根据你指定的次数获取对应的第一父提交。例如，在之前的列出的提交历史中，`HEAD~3` 就是：

```command
$ git show HEAD~3
commit 1c3618887afb5fbcbea25b7c013f4e2114448b8d
Author: Tom Preston-Werner <tom@mojombo.com>
Date:   Fri Nov 7 13:47:59 2008 -0500

    ignore *.gem
```

也可以写成 `HEAD^^^`，也是第一父提交的第一父提交的第一父提交，等同于上面的例子。

### 9.1.4 提交区间

1. 双点  
   让 Git 选出在一个分支中而不在另一个分支中的提交。`$ git log master..experiment` 选出 “在 experiment 分支中而不在 master 分支中的提交”。

2. 多点  
   双点语法很好用，但有时候你可能需要两个以上的分支才能确定你所需要的修订，比如查看哪些提交是被包含在某些分支中的一个，但是不在你当前的分支上。  
   Git 允许你在任意引用前加上 `^` 字符或者 `--not` 来指明你不希望提交被包含其中的分支。下列3个命令是等价的：

    ```command
    $ git log refA..refB
    $ git log ^refA refB
    $ git log refB --not refA
    ```
  
   这个语法很好用，因为你可以在查询中指定超过两个的引用，这是双点语法无法实现的。 比如，你想查看所有被 `refA` 或 `refB` 包含的但是不被 `refC` 包含的提交，你可以输入下面中的任意一个命令：

    ```command
    $ git log refA refB ^refC
    $ git log refA refB --not refC
    ```

3. 三点  
   选择出被两个引用中的一个包含但又不被两者同时包含的提交。`$ git log master...experiment` 选出 “master与experiment中包含但不共有的提交”。

## 9.2 交互式暂存

 如果运行 `git add` 时使用 `-i` 或者 `--interactive` 选项，Git 将会进入一个交互式终端模式，显示类似下面的东西：

## 9.3 储藏与清理

有时，当你在项目的一部分上已经工作一段时间后，所有东西都进入了混乱的状态，而这时你想要切换到另一个分支做一点别的事情。问题是，你不想仅仅因为过会儿回到这一点而为做了一半的工作创建一次提交。 针对这个问题的答案是 `git stash` 命令。

储藏会处理工作目录的脏的状态 - 即，修改的跟踪文件与暂存改动 - 然后将未完成的修改保存到一个栈上，而你可以在任何时候重新应用这些改动。

1. 储藏工作  
   进入项目并改动几个文件，然后可能暂存其中的一个改动。现在想要切换分支，但是还不想要提交之前的工作；所以储藏修改。将新的储藏推送到栈上，运行 `git stash` 或 `git stash save`：
    ```command
    $ git stash
    Saved working directory and index state \
      "WIP on master: 049d078 added the index file"
    HEAD is now at 049d078 added the index file
    (To restore them type "git stash apply")
    ```
   此时，工作目录是干净的了：
    ```command
    $ git status
    # On branch master
    nothing to commit, working directory clean
    ```
   在这时，你能够轻易地切换分支并在其他地方工作；你的修改被存储在栈上。 要查看储藏的东西，可以使用 `git stash list`：
    ```command
    $ git stash list
    stash@{0}: WIP on master: 049d078 added the index file
    stash@{1}: WIP on master: c264051 Revert "added file_size"
    stash@{2}: WIP on master: 21d80a5 added number to log
    ```
   在本例中，有两个之前做的储藏，所以你接触到了三个不同的储藏工作。可以通过原来 `stash` 命令的帮助提示中的命令将你刚刚储藏的工作重新应用：`git stash apply`。 如果想要应用其中一个更旧的储藏，可以通过名字指定它，像这样：`git stash apply stash@{2}`。如果不指定一个储藏，Git 认为指定的是最近的储藏：
    ```command
    $ git stash apply
    # On branch master
    # Changed but not updated:
    #   (use "git add <file>..." to update what will be committed)
    #
    #      modified:   index.html
    #      modified:   lib/simplegit.rb
    #
    ```
   可以看到 Git 重新修改了当你保存储藏时撤消的文件。在本例中，当尝试应用储藏时有一个干净的工作目录，并且尝试将它应用在保存它时所在的分支；但是有一个干净的工作目录与应用在同一分支并不是成功应用储藏的充分必要条件。 可以在一个分支上保存一个储藏，切换到另一个分支，然后尝试重新应用这些修改。 当应用储藏时工作目录中也可以有修改与未提交的文件 - 如果有任何东西不能干净地应用，Git 会产生合并冲突。

   文件的改动被重新应用了，但是之前暂存的文件却没有重新暂存。 想要那样的话，必须使用 `--index` 选项来运行 `git stash apply` 命令，来尝试重新应用暂存的修改。 如果已经那样做了，那么你将回到原来的位置：
    ```command
    $ git stash apply --index
    # On branch master
    # Changes to be committed:
    #   (use "git reset HEAD <file>..." to unstage)
    #
    #      modified:   index.html
    #
    # Changed but not updated:
    #   (use "git add <file>..." to update what will be committed)
    #
    #      modified:   lib/simplegit.rb
    #
    ```
   应用选项只会尝试应用暂存的工作 - 在堆栈上还有它。 可以运行 `git stash drop` 加上将要移除的储藏的名字来移除它：
    ```command
    $ git stash list
    stash@{0}: WIP on master: 049d078 added the index file
    stash@{1}: WIP on master: c264051 Revert "added file_size"
    stash@{2}: WIP on master: 21d80a5 added number to log
    $ git stash drop stash@{0}
    Dropped stash@{0} (364e91f3f268f0900bc3ee613f9f733e82aaed43)
    ```
   也可以运行 `git stash pop` 来应用储藏然后立即从栈上扔掉它。

2. 创造性的储藏
   有几个储藏的变种可能也很有用。第一个非常流行的选项是 `stash save` 命令的 `--keep-index` 选项。它告诉 Git 不要储藏任何你通过 git add 命令已暂存的东西。  
   当你做了几个改动并只想提交其中的一部分，过一会儿再回来处理剩余改动时，这个功能会很有用。
    ```command
    $ git status -s
    M  index.html
    M lib/simplegit.rb

    $ git stash --keep-index
    Saved working directory and index state WIP on master: 1b65b17 added the index file
    HEAD is now at 1b65b17 added the index file

    $ git status -s
    M  index.html
    ```
   另一个经常使用储藏来做的事情是像储藏跟踪文件一样储藏未跟踪文件。默认情况下，`git stash` 只会储藏已经在索引中的文件。如果指定 `--include-untracked` 或 `-u` 标记，Git 也会储藏任何创建的未跟踪文件。
    ```command
    $ git status -s
    M  index.html
    M lib/simplegit.rb
    ?? new-file.txt

    $ git stash -u
    Saved working directory and index state WIP on master: 1b65b17 added the index file
    HEAD is now at 1b65b17 added the index file

    $ git status -s
    $
    ```
   最终，如果指定了 `--patch` 标记，Git 不会储藏所有修改过的任何东西，但是会交互式地提示哪些改动想要储藏、哪些改动需要保存在工作目录中。
    ```command
    $ git stash --patch
    diff --git a/lib/simplegit.rb b/lib/simplegit.rb
    index 66d332e..8bb5674 100644
    --- a/lib/simplegit.rb
    +++ b/lib/simplegit.rb
    @@ -16,6 +16,10 @@ class SimpleGit
            return `#{git_cmd} 2>&1`.chomp
          end
        end
    +
    +    def show(treeish = 'master')
    +      command("git show #{treeish}")
    +    end

    end
    test
    Stash this hunk [y,n,q,a,d,/,e,?]? y

    Saved working directory and index state WIP on master: 1b65b17 added the index file
    ```

3. 从储藏创建一个分支  
   运行 `git stash branch` 创建一个新分支，检出储藏工作时所在的提交，重新在那应用工作，然后在应用成功后扔掉储藏：
    ```command
    $ git stash branch testchanges
    Switched to a new branch "testchanges"
    # On branch testchanges
    # Changes to be committed:
    #   (use "git reset HEAD <file>..." to unstage)
    #
    #      modified:   index.html
    #
    # Changed but not updated:
    #   (use "git add <file>..." to update what will be committed)
    #
    #      modified:   lib/simplegit.rb
    #
    Dropped refs/stash@{0} (f0dfc4d5dc332d1cee34a634182e168c4efc3359)
    ```
   这是在新分支轻松恢复储藏工作并继续工作的一个很不错的途径。

4. 清理工作目录  
   对于工作目录中一些工作或文件，你想做的也许不是储藏而是移除。 `git clean` 命令会帮你做这些事。  
   你需要谨慎地使用这个命令，因为它被设计为从工作目录中移除未被追踪的文件。 如果你改变主意了，你也不一定能找回来那些文件的内容。 一个更安全的选项是运行 `git stash --all` 来移除每一样东西并存放在栈中。  
   你可以使用 `git clean` 命令去除冗余文件或者清理工作目录。使用`git clean -f -d`命令来移除工作目录中所有未追踪的文件以及空的子目录。 `-f` 意味着 强制 或 “确定移除”。  
   如果只是想要看看它会做什么，可以使用 `-n` 选项来运行命令，这意味着 “做一次演习然后告诉你 将要 移除什么”。
    ```command
    $ git clean -d -n
    Would remove test.o
    Would remove tmp/
    ```
   默认情况下，git clean 命令只会移除没有忽略的未跟踪文件。任何与 `.gitiignore` 或其他忽略文件中的模式匹配的文件都不会被移除。 如果你也想要移除那些文件，例如为了做一次完全干净的构建而移除所有由构建生成的 `.o` 文件，可以给 `clean` 命令增加一个 `-x` 选项。
    ```command
    $ git status -s
    M lib/simplegit.rb
    ?? build.TMP
    ?? tmp/

    $ git clean -n -d
    Would remove build.TMP
    Would remove tmp/

    $ git clean -n -d -x
    Would remove build.TMP
    Would remove test.o
    Would remove tmp/
    ```
   如果不知道 `git clean` 命令将会做什么，在将 `-n` 改为 `-f` 来真正做之前总是先用 `-n` 来运行它做双重检查。 另一个小心处理过程的方式是使用 `-i` 或 “interactive” 标记来运行它。这将会以交互模式运行 `clean` 命令。

## 9.4 签署工作

Git 虽然是密码级安全的，但它不是万无一失的。 如果你从因特网上的其他人那里拿取工作，并且想要 **验证提交是不是真正地来自于可信来源** ，Git 提供了几种通过 `GPG` 来签署和验证工作的方式。

1. GPG 介绍
2. 签署标签
3. 验证标签
4. 签署提交

## 9.5 搜索

无论仓库里的代码量有多少，你经常需要查找一个函数是在哪里调用或者定义的，或者一个方法的变更历史。 Git 提供了两个有用的工具来快速地从它的数据库中浏览代码和提交。

1. Git Grep 
2. Git 日志搜索

## 9.6 重写历史

1. 修改最后一次提交
2. 修改多个提交信息
3. 重新排序提交
4. 压缩提交
5. 拆分提交
6. 核武器级选项：filter-branch

## 9.7 重置揭密

### 9.7.1 三棵树

树 |	用途
--- | ---
HEAD  | 上一次提交的快照，下一次提交的父结点
Index | 预期的下一次提交的快照
Working Directory | 沙盒

- HEAD  
  `HEAD` 是当前分支引用的指针，它总是指向该分支上的最后一次提交。这表示 `HEAD` 将是下一次提交的父结点。 通常，理解 `HEAD` 的最简方式，就是将它看做你的上一次提交的快照。
- 索引  
  索引是你的 **预期的下一次提交**。 我们也会将这个概念引用为 Git 的 “暂存区域”，这就是当你运行 `git commit` 时 Git 看起来的样子。
- 工作目录  
  以把工作目录当做 沙盒。在你将修改提交到暂存区并记录到历史之前，可以随意更改。

### 9.7.2 工作流程

Git 主要的目的是通过操纵这三棵树来以更加连续的状态记录项目的快照。
![reset-workflow](images/topic9/reset-workflow.png '工作流程')

让我们来可视化这个过程：

#### 1. v1

假设我们进入到一个新目录，其中有一个文件。 我们称其为该文件的 `v1` 版本，将它标记为蓝色。
![reset-ex1](images/topic9/reset-ex1.png '初始化仓库')

现在运行 `git init`，这会创建一个 Git 仓库，其中的 `HEAD` 引用指向未创建的分支（master 还不存在）。此时，只有工作目录有内容。  
现在我们想要提交这个文件，所以用 `git add` 来获取工作目录中的内容，并将其复制到索引中。
![reset-ex2](images/topic9/reset-ex2.png '暂存 v1 版本文件')

接着运行 `git commit`，它会取得索引中的内容并将它保存为一个永久的快照，然后创建一个指向该快照的提交对象，最后更新 `master` 来指向本次提交。
![reset-ex3](images/topic9/reset-ex3.png '提交 v1 文件快照')

此时如果我们运行 `git status`，会发现没有任何改动，因为现在 **三棵树完全相同**。

#### 2. v2

现在我们想要对文件进行修改然后提交它。 我们将会经历同样的过程；首先在工作目录中修改文件。 我们称其为该文件的 `v2` 版本，并将它标记为红色。
![reset-ex4](images/topic9/reset-ex4.png '修改 v1 文件为 v2 文件')

如果现在运行 `git status`，我们会看到文件显示在 “Changes not staged for commit,” 下面并被标记为红色，因为该条目在索引与工作目录之间存在不同。 接着我们运行 `git add` 来将它暂存到索引中。
![reset-ex5](images/topic9/reset-ex5.png '暂存 v2 版本文件')

此时，由于索引和 `HEAD` 不同，若运行 `git status` 的话就会看到 “Changes to be committed” 下的该文件变为绿色 —— 也就是说，现在预期的下一次提交与上一次提交不同。 最后，我们运行 `git commit` 来完成提交。
![reset-ex6](images/topic9/reset-ex6.png '提交 v2 文件快照')

现在运行 `git status` 会没有输出，因为三棵树又变得相同了。

**切换分支** 或 **克隆** 的过程也类似。 当检出一个分支时，它会修改 `HEAD` 指向新的分支引用，将 `索引` 填充为该次提交的快照，然后将 `索引` 的内容复制到 `工作目录` 中。

### 9.7.3 重置的作用

在以下情景中观察 `reset` 命令会更有意义。

#### 3. v3

为了演示这些例子，假设我们再次修改了 `file.txt` 文件并第三次提交它。 现在的历史看起来是这样的：
![reset-start](images/topic9/reset-start.png '修改 v2 文件，并暂存提交')

#### 4. reset

让我们跟着 `reset` 看看它都做了什么。 它以一种简单可预见的方式直接操纵这三棵树。 它做了三个基本操作。

1. 第 1 步：移动 HEAD  
   `reset` 做的第一件事是移动 `HEAD` 的指向。 这与改变 `HEAD` 自身不同（`checkout` 所做的）；`reset` 移动 `HEAD` 指向的分支。 这意味着如果 `HEAD` 设置为 `master` 分支（例如，你正在 `master` 分支上），运行 `git reset 9e5e64a` 将会使 `master` 指向 `9e5e64a`。
   ![reset-soft](images/topic9/reset-soft.png '移动 HEAD')
  
   无论你调用了何种形式的带有一个提交的 `reset`，它首先都会尝试这样做。 使用 `reset --soft`，它将仅仅停在那儿。  
   现在看一眼上图，理解一下发生的事情：它本质上是撤销了上一次 `git commit` 命令。 当你在运行 `git commit` 时，Git 会创建一个新的提交，并移动 HEAD 所指向的分支来使其指向该提交。 当你将它 `reset` 回 `HEAD~`（HEAD 的父结点）时，其实就是把该分支移动回原来的位置，而不会改变索引和工作目录。 现在你可以更新索引并再次运行 `git commit` 来完成 `git commit --amend` 所要做的事情了（见 [修改最后一次提交](https://git-scm.com/book/zh/v2/ch00/r_git_amend)）。
2. 第 2 步：更新索引（`--mixed`）  
   注意，如果你现在运行 `git status` 的话，就会看到新的 `HEAD` 和以绿色标出的它和索引之间的区别。  
   接下来，reset 会用 HEAD 指向的当前快照的内容来更新索引。  
   ![reset-mixed](images/topic9/reset-mixed.png '更新索引')

   如果指定 `--mixed` 选项，`rese`t 将会在这时停止。这也是默认行为，所以如果没有指定任何选项（在本例中只是 `git reset HEAD~`），这就是命令将会停止的地方。  
   现在再看一眼上图，理解一下发生的事情：它依然会撤销一上次 `提交`，但还会 `取消暂存` 所有的东西。 于是，我们回滚到了所有 `git add` 和 `git commit` 的命令执行之前。
3. 第 3 步：更新工作目录（`--hard`）
   `reset` 要做的的第三件事情就是让工作目录看起来像索引。如果使用 `--hard` 选项，它将会继续这一步。
   ![reset-hard](images/topic9/reset-hard.png '更新工作目录')

   现在让我们回想一下刚才发生的事情。 你撤销了最后的提交、`git add` 和 `git commit` 命令以及工作目录中的所有工作。  
   必须注意，`--hard` 标记是 `reset` 命令唯一的危险用法，它也是 Git 会真正地销毁数据的仅有的几个操作之一。其他任何形式的 `reset` 调用都可以轻松撤消，但是 `--hard` 选项不能，因为它 **强制覆盖了工作目录中的文件**。在这种特殊情况下，我们的 Git 数据库中的一个提交内还留有该文件的 v3 版本，我们可以通过 `reflog` 来找回它。但是若该文件还未提交，Git 仍会覆盖它从而导致无法恢复。

**回顾** `reset` 命令会以特定的顺序重写这三棵树，在你指定以下选项时停止：

1. 移动 HEAD 分支的指向 （若指定了 --soft，则到此停止）
2. 使索引看起来像 HEAD （若未指定 --hard，则到此停止）
3. 使工作目录看起来像索引

#### 5. 通过路径来重置

前面讲述了 reset 基本形式的行为，不过你还可以给它提供一个作用路径。 若指定了一个路径，`reset` 将会跳过第 1 步，并且将它的作用范围限定为指定的文件或文件集合。这样做自然有它的道理，因为 `HEAD` 只是一个指针，你无法让它同时指向两个提交中各自的一部分。不过索引和工作目录 *可以部分更新*，所以重置会继续进行第 2、3 步。
  
现在，假如我们运行 `git reset file.txt` （这其实是 `git reset --mixed HEAD file.txt` 的简写形式，因为你既没有指定一个提交的 SHA-1 或分支，也没有指定 `--soft` 或 `--hard`），它会：

1. 移动 HEAD 分支的指向 （已跳过）
2. 让索引看起来像 HEAD （到此处停止）

所以它本质上只是将 `file.txt` 从 `HEAD` 复制到索引中。
![reset-path1](iamges/topic9/reset-path1.png 'git reset file.txt')

它还有 *取消暂存文件* 的实际效果。 如果我们查看该命令的示意图，然后再想想 `git add` 所做的事，就会发现它们正好相反。
![reset-path2](iamges/topic9/reset-path2.png 'git add file.txt')

这就是为什么 `git status` 命令的输出会建议运行此命令来取消暂存一个文件。 （查看 [取消暂存的文件](https://git-scm.com/book/zh/v2/ch00/r_unstaging) 来了解更多。）

我们可以不让 Git 从 `HEAD` 拉取数据，而是通过具体指定一个提交来拉取该文件的对应版本。 我们只需运行类似于 `git reset eb43bf file.txt` 的命令即可。
![reset-path3](iamges/topic9/reset-path3.png 'git reset eb43 -- file.txt')

它其实做了同样的事情，也就是把工作目录中的文件恢复到 `v1` 版本，运行 `git add` 添加它，然后再将它恢复到 `v3` 版本（只是不用真的过一遍这些步骤）。如果我们现在运行 `git commit`，它就会记录一条“将该文件恢复到 v1 版本”的更改，尽管我们并未在工作目录中真正地再次拥有它。

还有一点同 `git add` 一样，就是 `reset` 命令也可以接受一个 `--patch` 选项来一块一块地取消暂存的内容。 这样你就可以根据选择来取消暂存或恢复内容了。

#### 6. 压缩

我们来看看如何利用这种新的功能来做一些有趣的事情 - **压缩提交**。

假设你的一系列提交信息中有 “oops.”、“WIP” 和 “forgot this file”， 聪明的你就能使用 `reset` 来轻松快速地将它们压缩成单个提交，也显出你的聪明。（[压缩提交](https://git-scm.com/book/zh/v2/ch00/r_squashing) 展示了另一种方式，不过在本例中用 reset 更简单。）

假设你有一个项目，第一次提交中有一个文件，第二次提交增加了一个新的文件并修改了第一个文件，第三次提交再次修改了第一个文件。 由于第二次提交是一个未完成的工作，因此你想要压缩它。
![reset-squash-r1](iamges/topic9/reset-squash-r1.png '初始分支情况')

那么可以运行 `git reset --soft HEAD~2` 来将 `HEAD` 分支移动到一个旧一点的提交上（即你想要保留的第一个提交）：
![reset-squash-r2](iamges/topic9/reset-squash-r2.png '移动 HEAD')

然后只需再次运行 `git commit`：
![reset-squash-r3](iamges/topic9/reset-squash-r3.png '压缩提交')

现在你可以查看可到达的历史，即将会推送的历史，现在看起来有个 `v1` 版 file-a.txt 的提交，接着第二个提交将 `file-a.txt` 修改成了 `v3` 版并增加了 `file-b.txt`。 包含 `v2` 版本的文件已经不在历史中了。

#### 7. 检出

`checkout` 和 `reset` 之间的区别： 和 `reset` 一样，`checkout` 也操纵三棵树，不过它有一点不同，这取决于你是否传给该命令一个文件路径。

- 不带路径  
  运行 `git checkout [branch]` 与运行 `git reset --hard [branch]` 非常相似，它会更新所有三棵树使其看起来像 `[branch]`，不过有两点重要的区别。

  首先不同于 `reset --hard`，`checkout` 对工作目录是安全的，它会通过检查来确保不会将已更改的文件弄丢。其实它还更聪明一些。它会在工作目录中先试着简单合并一下，这样所有 *还未修改过的* 文件都会被更新。 而 `reset --hard` 则会不做检查就全面地替换所有东西。

  第二个重要的区别是如何更新 `HEAD`。 `reset` 会移动 `HEAD` 分支的指向，而 `checkout` 只会移动 `HEAD` 自身来指向另一个分支。 例如，假设我们有 `master` 和 `develop` 分支，它们分别指向不同的提交；我们现在在 `develop` 上（所以 `HEAD` 指向它）。 如果我们运行 `git reset master`，那么 `develop` 自身现在会和 `master` 指向同一个提交。而如果我们运行 `git checkout master` 的话，`develop` 不会移动，`HEAD` 自身会移动。 现在 HEAD 将会指向 `master`。

  所以，虽然在这两种情况下我们都移动 `HEAD` 使其指向了提交 `A`，但 *做法* 是非常不同的。 `reset` 会移动 `HEAD` 分支的指向，而 `checkout` 则移动 HEAD 自身。
  ![reset-checkout](images/topic9/reset-checkout.png 'checkout 与 reset 区别')
- 带路径  
  运行 `checkout` 的另一种方式就是指定一个文件路径，这会像 `reset` 一样不会移动 `HEAD`。它就像 `git reset [branch] file` 那样用该次提交中的那个文件来更新索引，但是它也会覆盖工作目录中对应的文件。 它就像是 `git reset --hard [branch] file`（如果 `reset` 允许你这样运行的话）- 这样对工作目录并不安全，它也不会移动 `HEAD`。

  此外，同 `git reset` 和 `git add` 一样，`checkout` 也接受一个 `--patch` 选项，允许你根据选择一块一块地恢复文件内容。

#### 8. 总结

下面的速查表列出了命令对树的影响。 “HEAD” 一列中的 “REF” 表示该命令移动了 HEAD 指向的分支引用，而 “HEAD” 则表示只移动了 `HEAD` 自身。 特别注意 *WD Safe?* 一列 - 如果它标记为 *NO*，那么运行该命令之前请考虑一下。

  Level               | HEAD | Index | Workdir | WD Safe?
-----                 |  -   |   -   |    -    |    -
Commit Level          |      |       |         |
reset --soft [commit] | REF  | NO    | NO      | YES
reset [commit]        | REF  | YES   | NO      | YES
reset --hard [commit] | REF  | YES   | YES     | NO
checkout [commit]     | HEAD | YES   | YES     | YES
Commit Level          |      |       |         |
reset (commit) [file] | NO   | YES   | NO      | YES
checkout (commit) [file] | NO| YES   | YES     | YES

## 9.8 高级合并

首先，在做一次可能有冲突的合并前尽可能保证工作目录是 **干净** 的。如果你有正在做的工作，要么提交到一个临时分支要么储藏它。这使你可以撤消在这里尝试做的*任何事情*。 如果在你尝试一次合并时工作目录中有未保存的改动，下面的这些技巧可能会使你丢失那些工作。

### 9.8.1 合并冲突

让我们通过一个非常简单的例子来了解一下。 我们有一个超级简单的打印 `hello world` 的 `Ruby` 文件。

```ruby
#! /usr/bin/env ruby

def hello
  puts 'hello world'
end

hello()
```

在我们的仓库中，创建一个名为 `whitespace` 的新分支并将所有 Unix 换行符修改为 DOS 换行符，实质上虽然改变了文件的每一行，但改变的都只是空白字符。 然后我们修改行 “hello world” 为 “hello mundo”。

```command
$ git checkout -b whitespace
Switched to a new branch 'whitespace'

$ unix2dos hello.rb
unix2dos: converting file hello.rb to DOS format ...
$ git commit -am 'converted hello.rb to DOS'
[whitespace 3270f76] converted hello.rb to DOS
 1 file changed, 7 insertions(+), 7 deletions(-)

$ vim hello.rb
$ git diff -b
diff --git a/hello.rb b/hello.rb
index ac51efd..e85207e 100755
--- a/hello.rb
+++ b/hello.rb
@@ -1,7 +1,7 @@
 #! /usr/bin/env ruby

 def hello
-  puts 'hello world'
+  puts 'hello mundo'^M
 end

 hello()

$ git commit -am 'hello mundo change'
[whitespace 6d338d2] hello mundo change
 1 file changed, 1 insertion(+), 1 deletion(-)
```

现在我们切换回我们的 `master` 分支并为函数增加一些注释。

```command
$ git checkout master
Switched to branch 'master'

$ vim hello.rb
$ git diff
diff --git a/hello.rb b/hello.rb
index ac51efd..36c06c8 100755
--- a/hello.rb
+++ b/hello.rb
@@ -1,5 +1,6 @@
 #! /usr/bin/env ruby

+# prints out a greeting
 def hello
   puts 'hello world'
 end

$ git commit -am 'document the function'
[master bec6336] document the function
 1 file changed, 1 insertion(+)
```

现在我们尝试合并入我们的 `whitespace` 分支，因为修改了空白字符，所以合并会出现冲突。

```command
$ git merge whitespace
Auto-merging hello.rb
CONFLICT (content): Merge conflict in hello.rb
Automatic merge failed; fix conflicts and then commit the result.
```

### 9.8.2 中断一次合并

合并发生冲突，如何摆脱这个情况？

你可能不想处理冲突这种情况，完全可以通过 `git merge --abort` 来简单地退出合并。  
`git merge --abort` 选项会尝试恢复到你运行合并前的状态。但当运行命令前，在工作目录中有未储藏、未提交的修改时它不能完美处理，除此之外它都工作地很好。

```command
$ git status -sb
## master
UU hello.rb

$ git merge --abort

$ git status -sb
## master
```

如果因为某些原因你发现自己处在一个混乱的状态中然后只是想要重来一次，也可以运行 `git reset --hard HEAD` 回到之前的状态或其他你想要恢复的状态。 请牢记这会将清除工作目录中的所有内容，所以确保你不需要保存这里的任意改动。

### 9.8.3 忽略空白

在这个特定的例子中，冲突与空白有关。我们知道这点是因为这个例子很简单，但是在实际的例子中发现这样的冲突也很容易，因为每一行都被移除而在另一边每一行又被加回来了。 默认情况下，Git 认为所有这些行都改动了，所以它不会合并文件。  
默认合并策略可以带有参数，其中的几个正好是关于忽略空白改动的。如果你看到在一次合并中有大量的空白问题，你可以简单地中止它并重做一次。  
这次使用 `-Xignore-all-space` 或 `-Xignore-space-change` 选项。第一个选项忽略任意数量的已有空白的修改，第二个选项忽略所有空白修改。

```command
$ git merge -Xignore-space-change whitespace
Auto-merging hello.rb
Merge made by the 'recursive' strategy.
hello.rb | 2 +-
1 file changed, 1 insertion(+), 1 deletion(-)
```

### 9.8.4 手动文件再合并

当发生合并冲突时，我们可以选择手动处理。这时，需要比对合并时的三个版本，即我的版本的文件，他们的版本的文件（从我们将要合并入的分支）和共同的版本的文件（从分支叉开时的位置）的拷贝。然后我们想要修复任何一边的文件，并且为这个单独的文件重试一次合并。

如何获得这三个文件版本？  
Git 在索引中存储了所有这些版本，在 “stages” 下每一个都有一个数字与它们关联。`Stage 1` 是它们共同的祖先版本，`stage 2` 是你的版本，`stage 3` 来自于 `MERGE_HEAD`，即你将要合并入的版本（“theirs”）。通过 `git show` 命令与一个特别的语法，你可以将冲突文件的这些版本释放出一份拷贝。

```command
$ git show :1:hello.rb > hello.common.rb
$ git show :2:hello.rb > hello.ours.rb
$ git show :3:hello.rb > hello.theirs.rb
```

`:1:hello.rb` 只是查找那个 `blob` 对象 `SHA-1` 值的简写。既然在我们的工作目录中已经有这所有三个阶段的内容，我们可以手工修复它们来修复空白问题，然后使用鲜为人知的 `git merge-file` 命令来重新合并那个文件。

```command
$ dos2unix hello.theirs.rb
dos2unix: converting file hello.theirs.rb to Unix format ...

$ git merge-file -p \
    hello.ours.rb hello.common.rb hello.theirs.rb > hello.rb

$ git diff -b
diff --cc hello.rb
index 36c06c8,e85207e..0000000
--- a/hello.rb
+++ b/hello.rb
@@@ -1,8 -1,7 +1,8 @@@
  #! /usr/bin/env ruby

 +# prints out a greeting
  def hello
-   puts 'hello world'
+   puts 'hello mundo'
  end

  hello()
```

在这时我们已经漂亮地合并了那个文件。 实际上，这比使用 `ignore-space-change` 选项要更好，因为在合并前真正地修复了空白修改而不是简单地忽略它们。 在使用 `ignore-space-change` 进行合并操作后，我们最终得到了有几行是 DOS 行尾的文件，从而使提交内容混乱了。

如果你想要在最终提交前看一下我们这边与另一边之间实际的修改，你可以使用 `git diff` 来比较将要提交作为合并结果的工作目录与其中任意一个阶段的文件差异。 让我们看看它们。

要在合并前比较结果与在你的分支上的内容，换一句话说，看看合并引入了什么，可以运行 `git diff --ours`：

```command
$ git diff --ours
* Unmerged path hello.rb
diff --git a/hello.rb b/hello.rb
index 36c06c8..44d0a25 100755
--- a/hello.rb
+++ b/hello.rb
@@ -2,7 +2,7 @@

 # prints out a greeting
 def hello
-  puts 'hello world'
+  puts 'hello mundo'
 end

 hello()
```

这里我们可以很容易地看到在我们的分支上发生了什么，在这次合并中我们实际引入到这个文件的改动，是修改了其中一行。

如果我们想要查看合并的结果与他们那边有什么不同，可以运行 `git diff --theirs`。 在本例及后续的例子中，我们会使用 `-b` 来去除空白，因为我们将它与 Git 中的，而不是我们清理过的 `hello.theirs.rb` 文件比较。

```command
$ git diff --theirs -b
* Unmerged path hello.rb
diff --git a/hello.rb b/hello.rb
index e85207e..44d0a25 100755
--- a/hello.rb
+++ b/hello.rb
@@ -1,5 +1,6 @@
 #! /usr/bin/env ruby

+# prints out a greeting
 def hello
   puts 'hello mundo'
 end
```

最终，你可以通过 `git diff --base` 来查看文件在两边是如何改动的。

```command
$ git diff --base -b
* Unmerged path hello.rb
diff --git a/hello.rb b/hello.rb
index ac51efd..44d0a25 100755
--- a/hello.rb
+++ b/hello.rb
@@ -1,7 +1,8 @@
 #! /usr/bin/env ruby

+# prints out a greeting
 def hello
-  puts 'hello world'
+  puts 'hello mundo'
 end

 hello()
```

在这时我们可以使用 `git clean` 命令来清理我们为手动合并而创建但不再有用的额外文件。

```command
$ git clean -f
Removing hello.common.rb
Removing hello.ours.rb
Removing hello.theirs.rb
```

### 9.8.5 检出冲突

也许有时我们并不满意这样的解决方案，或许有时还要手动编辑一边或者两边的冲突，但还是依旧无法正常工作，这时我们需要更多的 **上下文关联** 来解决这些冲突。  
让我们来稍微改动下例子。 对于本例，我们有两个长期分支，每一个分支都有几个提交，但是在合并时却创建了一个合理的冲突。

```command
$ git log --graph --oneline --decorate --all
* f1270f7 (HEAD, master) update README
* 9af9d3b add a README
* 694971d update phrase to hola world
| * e3eb223 (mundo) add more tests
| * 7cff591 add testing script
| * c3ffff1 changed text to hello mundo
|/
* b7dcc89 initial hello world code
```

现在有只在 `master` 分支上的三次单独提交，还有其他三次提交在 `mundo` 分支上。 如果我们尝试将 `mundo` 分支合并入 `master` 分支，我们得到一个冲突。

```command
$ git merge mundo
Auto-merging hello.rb
CONFLICT (content): Merge conflict in hello.rb
Automatic merge failed; fix conflicts and then commit the result.
```

我们想要看一下合并冲突是什么。 如果我们打开这个文件，我们将会看到类似下面的内容：

```command
#! /usr/bin/env ruby

def hello
<<<<<<< HEAD
  puts 'hola world'
=======
  puts 'hello mundo'
>>>>>>> mundo
end

hello()
```

合并的两边都向这个文件增加了内容，但是导致冲突的原因是其中一些提交修改了文件的同一个地方。  
一个很有用的工具是带 `--conflict` 选项的 `git checkout`。 这会重新检出文件并替换合并冲突标记。如果想要重置标记并尝试再次解决它们的话这会很有用。  
可以传递给 `--conflict` 参数 `diff3` 或 `merge`（默认选项）。 如果传给它 `diff3`，Git 会使用一个略微不同版本的冲突标记：不仅仅只给你 “ours” 和 “theirs” 版本，同时也会有 “base” 版本在中间来给你更多的上下文。

```command
$ git checkout --conflict=diff3 hello.rb
```
一旦我们运行它，文件看起来会像下面这样：
```command
#! /usr/bin/env ruby

def hello
<<<<<<< ours
  puts 'hola world'
||||||| base
  puts 'hello world'
=======
  puts 'hello mundo'
>>>>>>> theirs
end

hello()
```

如果你喜欢这种格式，可以通过设置 `merge.conflictstyle` 选项为 `diff3` 来做为以后合并冲突的默认选项。

```command
$ git config --global merge.conflictstyle diff3
```

`git checkout` 命令也可以使用 `--ours` 和 `--theirs` 选项，这是一种无需合并的快速方式，你可以选择留下一边的修改而丢弃掉另一边修改。  
当有二进制文件冲突时这可能会特别有用，因为可以简单地选择一边，或者可以只合并另一个分支的特定文件 - 可以做一次合并然后在提交前检出一边或另一边的特定文件。

### 9.8.6 合并日志

另一个解决合并冲突有用的工具是 `git log`。 这可以帮助你得到那些对冲突有影响的上下文。 回顾一点历史来记起为什么两条线上的开发会触碰同一片代码有时会很有用。

为了得到此次合并中包含的每一个分支的所有独立提交的列表，我们可以使用之前在 [三点](https://git-scm.com/book/zh/v2/ch00/r_triple_dot) 学习的 “三点” 语法。

```command
$ git log --oneline --left-right HEAD...MERGE_HEAD
< f1270f7 update README
< 9af9d3b add a README
< 694971d update phrase to hola world
> e3eb223 add more tests
> 7cff591 add testing script
> c3ffff1 changed text to hello mundo
```

这个漂亮的列表包含 6 个提交和每一个提交所在的不同开发路径。

我们可以通过更加特定的上下文来进一步简化这个列表。 如果我们添加 `--merge` 选项到 `git log` 中，它会只显示任何一边接触了合并冲突文件的提交。

```command
$ git log --oneline --left-right --merge
< 694971d update phrase to hola world
> c3ffff1 changed text to hello mundo
```

如果你运行命令时用 `-p` 选项代替，你会得到所有冲突文件的区别。快速获得你需要帮助理解为什么发生冲突的上下文，以及如何聪明地解决它，这会非常有用。

### 9.8.7 组合式差异格式

因为 Git **暂存** 合并成功的结果，当你在合并冲突状态下运行 `git diff` 时，只会得到现在还在冲突状态的区别。 当需要查看你还需要解决哪些冲突时这很有用。

在合并冲突后直接运行的 `git diff` 会给你一个相当独特的输出格式。

```command
$ git diff
diff --cc hello.rb
index 0399cd5,59727f0..0000000
--- a/hello.rb
+++ b/hello.rb
@@@ -1,7 -1,7 +1,11 @@@
  #! /usr/bin/env ruby

  def hello
++<<<<<<< HEAD
 +  puts 'hola world'
++=======
+   puts 'hello mundo'
++>>>>>>> mundo
  end

  hello()
```

这种叫作 “组合式差异” 的格式会在每一行给你两列数据。 第一列为你显示 “ours” 分支与工作目录的文件区别（添加或删除），第二列显示 “theirs” 分支与工作目录的拷贝区别。

所以在上面的例子中可以看到 `<<<<<<<` 与 `>>>>>>>` 行在工作拷贝中但是并不在合并的任意一边中。 这很有意义，合并工具因为我们的上下文被困住了，它期望我们去移除它们。

如果我们解决冲突再次运行 `git diff`，我们将会看到同样的事情，但是它有一点帮助。

```command
$ vim hello.rb
$ git diff
diff --cc hello.rb
index 0399cd5,59727f0..0000000
--- a/hello.rb
+++ b/hello.rb
@@@ -1,7 -1,7 +1,7 @@@
  #! /usr/bin/env ruby

  def hello
-   puts 'hola world'
 -  puts 'hello mundo'
++  puts 'hola mundo'
  end

  hello()
```

这里显示出 “hola world” 在我们这边但不在工作拷贝中，那个 “hello mundo” 在他们那边但不在工作拷贝中，最终 “hola mundo” 不在任何一边但是现在在工作拷贝中。 在提交解决方案前这对审核很有用。

也可以在合并后通过 `git log` 来获取相同信息，并查看冲突是如何解决的。 如果你对一个合并提交运行 `git show` 命令 Git 将会输出这种格式，或者你也可以在 `git log -p`（默认情况下该命令只会展示还没有合并的补丁）命令之后加上 `--cc` 选项。

```command
$ git log --cc -p -1
commit 14f41939956d80b9e17bb8721354c33f8d5b5a79
Merge: f1270f7 e3eb223
Author: Scott Chacon <schacon@gmail.com>
Date:   Fri Sep 19 18:14:49 2014 +0200

    Merge branch 'mundo'

    Conflicts:
        hello.rb

diff --cc hello.rb
index 0399cd5,59727f0..e1d0799
--- a/hello.rb
+++ b/hello.rb
@@@ -1,7 -1,7 +1,7 @@@
  #! /usr/bin/env ruby

  def hello
-   puts 'hola world'
 -  puts 'hello mundo'
++  puts 'hola mundo'
  end

  hello()
```

### 9.8.8 撤消合并

假设现在在一个特性分支上工作，不小心将其合并到 `master` 中，现在提交历史看起来是这样：
![undomerge-start](images/topic9/undomerge-start.png '意外的合并提交')

有两种方法来解决这个问题，这取决于你想要的结果是什么。

1. 修复引用  
   如果这个不想要的合并提交只存在于你的本地仓库中，最简单且最好的解决方案是 **移动分支到你想要它指向的地方**。 大多数情况下，如果你在错误的 `git merge` 后运行 `git reset --hard HEAD~`，这会重置分支指向所以它们看起来像这样：
   ![undomerge-reset](images/topic9/undomerge-reset.png '在 git reset --hard HEAD~ 之后的历史')

   这个方法的缺点是它会重写历史，在一个共享的仓库中这会造成问题的。 查阅 [变基的风险](https://git-scm.com/book/zh/v2/ch00/r_rebase_peril) 来了解更多可能发生的事情；用简单的话说就是如果其他人已经有你将要重写的提交，你应当避免使用 `reset`。 如果有任何其他提交在合并之后创建了，那么这个方法也会无效；移动引用实际上会丢失那些改动。
2. 还原提交  
   如果移动分支指针并不适合你，Git 给你一个生成一个新提交的选项，提交将会撤消一个已存在提交的所有修改。 Git 称这个操作为 “还原”，在这个特定的场景下，你可以像这样调用它：
    ```command
    $ git revert -m 1 HEAD
    [master b1d8379] Revert "Merge branch 'topic'"
    ```
   `-m 1` 标记指出 “mainline” 需要被保留下来的父结点。  
   当你引入一个合并到 `HEAD（git merge topic）`，新提交有两个父结点：第一个是 `HEAD（C6）`，第二个是将要合并入分支的最新提交`（C4）`。  
   在本例中，我们想要撤消所有由父结点 `#2（C4）` 合并引入的修改，同时保留从父结点 `#1（C4）` 开始的所有内容。

   有还原提交的历史看起来像这样：  
   ![undomerge-revert](images/topic9/undomerge-revert.png '在 git revert -m 1 后的历史')

   新的提交 `^M` 与 `C6` 有完全一样的内容，所以从这儿开始就像合并从未发生过，除了“现在还没合并”的提交依然在 `HEAD` 的历史中。 如果你尝试再次合并 topic 到 master Git 会感到困惑：
    ```command
    $ git merge topic
    Already up-to-date.
    ```
  
   `topic` 中并没有东西不能从 `master` 中追踪到达。 更糟的是，如果你在 `topic` 中增加工作然后再次合并，Git 只会引入被还原的合并 *之后* 的修改。  
   ![undomerge-revert2](images/topic9/undomerge-revert2.png '含有坏掉合并的历史')

   解决这个最好的方式是 **撤消还原原始的合并**，因为现在你想要引入被还原出去的修改，然后创建一个新的合并提交：
    ```command
    $ git revert ^M
    [master 09f0126] Revert "Revert "Merge branch 'topic'""
    $ git merge topic
    ```
   ![undomerge-revert3](images/topic9/undomerge-revert3.png '在重新合并一个还原合并后的历史')

   在本例中，`M` 与 `^M` 抵消了。 `^^M` 事实上合并入了 `C3` 与 `C4` 的修改，`C8` 合并了 `C7` 的修改，所以现在 `topic` 已经完全被合并了。

### 9.8.9 其他类型的合并

到目前为止我们介绍的都是通过一个叫作 “recursive” 的合并策略来正常处理的两个分支的正常合并。然而还有其他方式来合并两个分支到一起。 让我们来快速介绍其中的几个。

1. 我们的或他们的偏好  
   告诉 Git 当它看见一个冲突时 **直接选择一边**。默认情况下，当 Git 看到两个分支合并中的冲突时，它会将合并冲突标记添加到你的代码中并标记文件为冲突状态来让你解决。  如果你希望 Git 简单地 **选择特定的一边并忽略另外一边** 而不是让你 **手动合并冲突**，你可以传递给 `merge` 命令一个 `-Xours` 或 `-Xtheirs` 参数。  
   如果 Git 看到这个，它并不会增加冲突标记。 任何可以合并的区别，它会直接合并。 任何有冲突的区别，它会简单地选择你全局指定的一边，包括二进制文件。

   如果我们回到之前我们使用的 “hello world” 例子中，我们可以看到合并入我们的分支时引发了冲突。然而如果我们运行时增加 `-Xours` 或 `-Xtheirs` 参数就不会有冲突。
    ```command
    $ git merge -Xours mundo
    Auto-merging hello.rb
    Merge made by the 'recursive' strategy.
    hello.rb | 2 +-
    test.sh  | 2 ++
    2 files changed, 3 insertions(+), 1 deletion(-)
    create mode 100644 test.sh
    ```
   在上例中，它并不会为 “hello mundo” 与 “hola world” 标记合并冲突，它只会简单地选取 “hola world”。 然而，在那个分支上所有其他非冲突的改动都可以被成功地合并入。

   这个选项也可以传递给我们之前看到的 `git merge-file` 命令，通过运行类似 `git merge-file --ours` 的命令来合并单个文件。  
   如果想要做类似的事情但是甚至并不想让 Git 尝试合并另外一边的修改，有一个更严格的选项，它是 “ours” 合并策略。 这与 “ours” recursive 合并选项(`-Xours`)不同。

   这本质上会做一次假的合并。 它会记录一个以两边分支作为父结点的新合并提交，但是它甚至根本不关注你正合并入的分支。 它只会简单地把当前分支的代码当作合并结果记录下来。
    ```command
    $ git merge -s ours mundo
    Merge made by the 'ours' strategy.
    $ git diff HEAD HEAD~
    $
    ```
  
   你可以看到合并后与合并前我们的分支并没有任何区别。

   当再次合并时从本质上欺骗 Git 认为那个分支已经合并过经常是很有用的。  
   例如，假设你有一个分叉的 `release` 分支并且在上面做了一些你想要在未来某个时候合并回 `master` 的工作。 与此同时 `master` 分支上的某些 `bugfix` 需要向后移植回 `release` 分支。 你可以合并 `bugfix` 分支进入 `release` 分支同时也 `merge -s ours` 合并进入你的 `master` 分支（即使那个修复已经在那儿了）这样当你之后再次合并 `release` 分支时，就不会有来自 `bugfix` 的冲突。
2. 子树合并  
   子树合并的思想是你有两个项目，并且其中一个映射到另一个项目的一个子目录，或者反过来也行。当你执行一个子树合并时，Git 通常可以自动计算出其中一个是另外一个的子树从而实现正确的合并。

   我们来看一个例子如何将一个项目加入到一个已存在的项目中，然后将第二个项目的代码合并到第一个项目的子目录中。  
   首先，我们将 `Rack` 应用添加到你的项目里。 我们把 `Rack` 项目作为一个远程的引用添加到我们的项目里，然后检出到它自己的分支。
    ```command
    $ git remote add rack_remote https://github.com/rack/rack
    $ git fetch rack_remote
    warning: no common commits
    remote: Counting objects: 3184, done.
    remote: Compressing objects: 100% (1465/1465), done.
    remote: Total 3184 (delta 1952), reused 2770 (delta 1675)
    Receiving objects: 100% (3184/3184), 677.42 KiB | 4 KiB/s, done.
    Resolving deltas: 100% (1952/1952), done.
    From https://github.com/rack/rack
    * [new branch]      build      -> rack_remote/build
    * [new branch]      master     -> rack_remote/master
    * [new branch]      rack-0.4   -> rack_remote/rack-0.4
    * [new branch]      rack-0.9   -> rack_remote/rack-0.9
    $ git checkout -b rack_branch rack_remote/master
    Branch rack_branch set up to track remote branch refs/remotes/rack_remote/master.
    Switched to a new branch "rack_branch"
    ```

   现在在我们的 `rack_branch` 分支里就有 `Rack` 项目的根目录，而我们的项目则在 `master` 分支里。 如果你从一个分支切换到另一个分支，你可以看到它们的项目根目录是不同的：
    ```command
    $ ls
    AUTHORS         KNOWN-ISSUES   Rakefile      contrib         lib
    COPYING         README         bin           example         test
    $ git checkout master
    Switched to branch "master"
    $ ls
    README
    ```

   这个是一个比较奇怪的概念。 并不是仓库中的所有分支都是必须属于同一个项目的分支. 这并不常见，因为没啥用，但是却是在不同分支里包含两条完全不同提交历史的最简单的方法。

   在这个例子中，我们希望将 `Rack` 项目拉到 `master` 项目中作为一个子目录。 我们可以在 Git 中执行 `git read-tree` 来实现。 你可以在 [Git 内部原理](https://git-scm.com/book/zh/v2/ch00/ch10-git-internals) 中查看更多 `read-tree` 的相关信息，现在你只需要知道它会读取一个分支的根目录树到当前的暂存区和工作目录里。 先切回你的 `master` 分支，将 `rack_back` 分支拉取到我们项目的 `master` 分支中的 `rack` 子目录。
    ```command
    $ git read-tree --prefix=rack/ -u rack_branch
    ```
   当我们提交时，那个子目录中拥有所有 `Rack` 项目的文件 —— 就像我们直接从压缩包里复制出来的一样。 有趣的是你可以很容易地将一个分支的变更合并到另一个分支里。所以，当 `Rack` 项目有更新时，我们可以切换到那个分支来拉取上游的变更。
    ```command
    $ git checkout rack_branch
    $ git pull
    ```
   接着，我们可以将这些变更合并回我们的 `master` 分支。 使用 `--squash` 选项和使用 `-Xsubtree` 选项（它采用递归合并策略），都可以用来可以拉取变更并且预填充提交信息。 （递归策略在这里是默认的，提到它是为了让读者有个清晰的概念。）
    ```command
    $ git checkout master
    $ git merge --squash -s recursive -Xsubtree=rack rack_branch
    Squash commit -- not updating HEAD
    Automatic merge went well; stopped before committing as requested
    ```
   `Rack` 项目中所有的改动都被合并了，等待被提交到本地。 你也可以用相反的方法——在 `master` 分支上的 `rack` 子目录中做改动然后将它们合并入你的 `rack_branch` 分支中，之后你可能将其提交给项目维护着或者将它们推送到上游。

   这给我们提供了一种类似 **子模块工作流** 的工作方式，但是它并不需要用到子模块（有关子模块的内容我们会在 [子模块](https://git-scm.com/book/zh/v2/ch00/r_git_submodules) 中介绍）。我们可以在自己的仓库中保持一些和其他项目相关的分支，偶尔使用子树合并将它们合并到我们的项目中。 某些时候这种方式很有用，例如当所有的代码都提交到一个地方的时候。然而，它同时也有缺点，它更加复杂且更容易让人犯错，例如重复合并改动或者不小心将分支提交到一个无关的仓库上去。

   另外一个有点奇怪的地方是，当你想查看 `rack` 子目录和 `rack_branch` 分支的差异 —— 来确定你是否需要合并它们——你不能使用普通的 `diff` 命令。 取而代之的是，你必须使用 `git diff-tree` 来和你的目标分支做比较：
    ```command
    $ git diff-tree -p rack_branch
    ```
   或者，将你的 `rack` 子目和最近一次从服务器上抓取的 `master` 分支进行比较，你可以运行：
    ```command
    $ git diff-tree -p rack_remote/master
    ```

## 9.9 Rerere

`git rerere` 功能是一个隐藏的功能。 正如它的名字 “reuse recorded resolution” 所指，它允许你让 Git 记住解决一个块冲突的方法，这样在下一次看到相同冲突时，Git 可以为你自动地解决它。

## 9.10 使用 Git 调试

Git 也提供了两个工具来辅助你调试项目中的问题。 由于 Git 被设计成适用于几乎所有类型的项目，这些工具是比较通用的，但它们可以在出现问题的时候帮助你找到 bug 或者错误。

1. 文件标注
2. 二分查找

## 9.11 子模块

有种情况我们经常会遇到：某个工作中的项目需要包含并使用另一个项目。也许是第三方库，或者你独立开发的，用于多个父项目的库。现在问题来了：你想要把它们当做两个独立的项目，同时又想在一个项目中使用另一个。

## 9.12 打包

## 9.13 替换

## 9.14 凭证存储

# 10. 自定义 Git

8.1 配置 Git
8.2 Git 属性
8.3 Git 钩子
8.4 使用强制策略的一个例子
8.5 总结

# 11. Git 与其他系统

9.1 作为客户端的 Git
9.2 迁移到 Git
9.3 总结

# 12. Git 内部原理

10.1 底层命令和高层命令
10.2 Git 对象
10.3 Git 引用
10.4 包文件
10.5 引用规格
10.6 传输协议
10.7 维护与数据恢复
10.8 环境变量
10.9 总结

# A1. 附录 A: 其它环境中的 Git

A1.1 图形界面
A1.2 Visual Studio 中的 Git
A1.3 Eclipse 中的 Git
A1.4 Bash 中的 Git
A1.5 Zsh 中的 Git
A1.6 Powershell 中的 Git
A1.7 总结

# A2. 附录 B: 将 Git 嵌入你的应用

A2.1 命令行 Git 方式
A2.2 Libgit2
A2.3 JGit

# A3. 附录 C: Git 命令

A3.1 设置与配置
A3.2 获取与创建项目
A3.3 快照基础
A3.4 分支与合并
A3.5 项目分享与更新
A3.6 检查与比较
A3.7 调试
A3.8 补丁
A3.9 邮件
A3.10 外部系统
A3.11 管理
A3.12 底层命令

