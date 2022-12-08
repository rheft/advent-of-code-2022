# Notes

### Solution 1
Remember: Two different directories can contain other directors of the same name! This doesn't show up in the test case, and it wasn't obvious to me until I saw a helpful reddit post regarding a similar problem I was seeing.  
Example:  
```
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
------------------------ Consider the instructions below were added to the test case:
dir e
$ cd e
$ ls
123 foo.foo
456 bar.bar
```

directory `e` now exists in two different paths, this wasn't something that I considered and I spent a good hour trying to figure out why my test case was passing but the true input was not!