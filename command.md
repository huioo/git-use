
# git add —— 暂存

- `-i` 或 `--interactive`  
  `$ git add -i` 之后，Git 将会进入一个交互式终端模式。

# git clean —— 清除

- `-f` 和 `-d`  
  你可以使用 `git clean` 命令去除冗余文件或者清理工作目录。 默认情况下，`git clean` 命令只会移除没有忽略的未跟踪文件。
  使用`git clean -f -d`命令来移除工作目录中所有未追踪的文件以及空的子目录。 `-f` 意味着 强制 或 “确定移除”。

- `-n`  
  如果只是想要看看它会做什么，可以使用 `-n` 选项来运行命令，这意味着 “做一次演习然后告诉你 将要 移除什么”。
    ```command
    $ git clean -d -n
    Would remove test.o
    Would remove tmp/
    ```
    如果不知道 `git clean` 命令将会做什么，在将 `-n` 改为 `-f` 来真正做之前总是先用 `-n` 来运行它做双重检查。 另一个小心处理过程的方式是使用 `-i` 或 “interactive” 标记来运行它。这将会以交互模式运行 `clean` 命令。

- `-x`  
  任何与 `.gitiignore` 或其他忽略文件中的模式匹配的文件都不会被移除。 如果你也想要移除那些文件，例如为了做一次完全干净的构建而移除所有由构建生成的 `.o` 文件，可以给 `clean` 命令增加一个 `-x` 选项。
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

# git diff —— 差异

- `--ours`  
  `$ git diff --ours` 查看合并引入了什么，即在合并前比较结果与在你的分支上的内容。

- `--theirs`  
  `$ git diff --theirs` 查看合并的结果与他们那边有什么不同。通过 `$ git diff --theirs -b` 中的 `-b` 取出空白

- `--base`  
  `git diff --base` 查看文件两边是如何修改的。

# git log —— 提交历史

- `..`  
  `$ git log master..experiment` 选出 “在 experiment 分支中而不在 master 分支中的提交”。

- `...`  
  `$ git log master...experiment` 选出 “master 与 experiment中包含但不共有的提交”。

- `--not` 或 `^`  
  查看被多个分支包含，但不在某个分支中的提交。比如，你想查看所有被 `refA` 或 `refB` 包含的但是不被 `refC` 包含的提交，你可以输入下面中的任意一个命令：

    ```command
    $ git log refA refB ^refC
    ...
    $ git log refA refB --not refC
    ```

- `--left-right`  
  查看不同分支中的所有独立提交的列表，比如：`$ git log --oneline --left-right HEAD...MERGE_HEAD`

- `--merge`  
  显示多个不同分支之间任何一边接触了合并冲突文件的提交

- `--graph`  
  显示提交的图线结构。

- `--pretty=format:'%h %s'`  
  格式化显示，自定义模板形式显示。比如 `$ git log --pretty=format:'%h %s' --graph`。
  
- `--pretty=oneline`  
  格式化显示，`oneline`指以行形式显示。

- `--abbrev-commit`  
  在 `git log` 后加上 `--abbrev-commit` 参数，输出结果里就会显示简短且唯一的值；默认使用七个字符，不过有时为了避免 `SHA-1` 的歧义，会增加字符数。通常 8 到 10 个字符就已经足够在一个项目中避免 `SHA-1` 的歧义。
    ```command
    $ git log --abbrev-commit --pretty=oneline
    ca82a6d changed the version number
    085bb3b removed unnecessary test code
    a11bef0 first commit
    ```

- `-g`  
  运行 `git log -g` 来查看类似于 `git log` 输出格式的引用日志信息：
    ```command
    $ git log -g master
    commit 734713bc047d87bf7eac9674765ae793478c50d3
    Reflog: master@{0} (Scott Chacon <schacon@gmail.com>)
    Reflog message: commit: fixed refs handling, added gc auto, updated
    Author: Scott Chacon <schacon@gmail.com>
    Date:   Fri Jan 2 18:32:33 2009 -0800

        fixed refs handling, added gc auto, updated tests
    ... ...
    ```

# git merge —— 合并

- `git merge-file` 合并文件

# git reset —— 重置

三棵树：HEAD、index 和 working directory。

`reset` 以一种简单可预见的方式直接操纵这三棵树。 它做了三个基本操作：移动 HEAD、更新索引、更新工作目录。

## 提供一个提交的 SHA-1值或分支

- `git reset --soft`  
  使用 `--soft` 选项来仅仅移动 `HEAD` 的指向。  
  比如：`$ git reset --soft HEAD~`，只会移动 `HEAD` 指向当前分支的父节点提交上。

- `git reset [--mixed]`  
  使用 `--mixed` 选项或没有指定任何选项，`reset` 将会仅仅移动 `HEAD` 和更新索引。
  比如：`$ git reset HEAD~`（等同于`$ git reset --mixed HEAD~`）。此时， `reset` 做的第一件事是移动 `HEAD` 的指向，将它 `reset` 回 `HEAD~`（HEAD 的父结点），而不会改变索引和工作目录。接着，`reset` 会用 `HEAD` 指向的当前快照的内容来更新索引。

  如果指定 `--mixed` 选项，`reset` 将会在这时停止。这也是默认行为，所以如果没有指定任何选项（在本例中只是 `git reset HEAD~`），这就是命令将会停止的地方。

- `git reset --hard`  
  使用 `--hard` 选项，`reset` 将会移动 HEAD、更新索引和更新工作目录。
  比如：`$ git reset --hard HEAD~`。该命令将会先执行等同于 `$ git reset HEAD~` 的操作，最后更新工作目录，让工作目录看起来像索引。

## 提供文件路径

若指定了一个路径，reset 将会跳过第 1 步，并且将它的 **作用范围** 限定为指定的文件或文件集合。这样做自然有它的道理，因为 `HEAD` 只是一个指针，你无法让它同时指向两个提交中各自的一部分。 不过索引和工作目录 *可以部分更新*，所以重置会继续进行第 2、3 步。

比如：`$ git reset file.txt`（等同于`$ git reset --mixed HEAD file.txt`），该指令会更新该文件的索引，让索引看起来像 `HEAD` 指向的情况，而不会更新工作目录。该命令与 `$ git add file.txt` 的效果正好相反。

比如：`$ git reset eb43bf file.txt`，更新该文件的索引，让索引看起来像之前某个提交时的情况，但工作目录没变，之后重新 `git commit` ，这样做整合了该提交之后做的所有提交的内容。

# git checkout —— 检出

# git show —— 提交

- 合并冲突时的三个版本展示  
  获得这三个文件版本实际上相当容易。 Git 在索引中存储了所有这些版本，在 “stages” 下每一个都有一个数字与它们关联。 `Stage 1` 是它们共同的祖先版本，`stage 2` 是你的版本，`stage 3` 来自于 `MERGE_HEAD`，即你将要合并入的版本（“theirs”）。
    ```command
    $ git show :1:hello.rb > hello.common.rb
    $ git show :2:hello.rb > hello.ours.rb
    $ git show :3:hello.rb > hello.theirs.rb
    ```

# git stash —— 储藏

- 目的  
  工作到一半时，需要到另一个分支做点事情。问题是，你不想仅仅因为过会儿回到这一点而为做了一半的工作创建一次提交。所以需要将工作目录的脏的状态储藏起来。 即，修改的跟踪文件与暂存改动 - 然后将未完成的修改保存到一个栈上，而你可以在任何时候重新应用这些改动。

- 储藏  
  储藏修改。 将新的储藏推送到栈上，运行 `git stash` 或 `git stash save`。  
  `--keep-index` 选项：储藏时忽略任何通过 `git add` 命令已暂存的东西。比如：`$ git stash --keep-index` 。  
  `--include-untracked` 或 `-u` 选项：Git 也会储藏任何创建的未跟踪文件。比如：`$ git stash -u` 。  
  `--patch` 选项：Git 不会储藏所有修改过的任何东西，但是会交互式地提示哪些改动想要储藏、哪些改动需要保存在工作目录中。比如：`$ git stash --patch`。

- 查看储藏的东西  
  使用 `git stash list` 查看储藏的东西。修改的工作被储藏在栈上。栈上可能存在多个储藏的工作。
    ```command
    $ git stash list
    stash@{0}: WIP on master: 049d078 added the index file
    stash@{1}: WIP on master: c264051 Revert "added file_size"
    stash@{2}: WIP on master: 21d80a5 added number to log
    ```

- 应用储藏  
  使用 `git stash apply stash@{n}` 样式指令重新应用一个指定的储藏，通过名字指定它。比如：应用一个更旧的储藏，使用`git stash apply stash@{2}` 。  
  使用 `git stash apply` 重新应用刚刚储藏的工作，即栈顶上储藏的工作。即没有指定一个储藏，Git 认为指定的是最近的储藏。  
  使用 `git stash apply --index` 重新应用包含已经暂存的修改的储藏。
  使用 `git stash branch` 创建一个新分支，检出储藏工作时所在的提交，重新在那应用工作，然后在应用成功后扔掉储藏。
  使用 `git stash --all` 移除每一样东西并存放在栈中，类似 `git clean`。

- 删除储藏的东西  
  使用 `git stash drop` 加上将要移除的储藏的名字来移除它：
    ```command
    $ git stash list
    stash@{0}: WIP on master: 049d078 added the index file
    stash@{1}: WIP on master: c264051 Revert "added file_size"
    stash@{2}: WIP on master: 21d80a5 added number to log
    $ git stash drop stash@{0}
    Dropped stash@{0} (364e91f3f268f0900bc3ee613f9f733e82aaed43)
    ```
  也可以运行 `git stash pop` 来应用储藏然后立即从栈上扔掉它。

# git reflog —— 引用历史