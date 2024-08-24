# backupall
Backup old versions of Windows required by manufacturing devices (requiring only Python and modules able to be patched offline).

Wow, Windows 2000 is really old, but some manufacturing devices still require it.

There are many good backup programs, but supporting Windows 2000 is the reason backupall exists.

For Windows 2000, you will need Python 3.2 (also very old, but apparently the latest to support Windows 2000).

Installing dependencies can be done on a computer with Python (x86 not x86_64) on a recent version of Windows then transferred to the Windows 2000 computer.
- Why? Because you shouldn't connect Windows 2000 to the internet! It is too old. Microsoft said it had over 20,000 unresolved issues when support ended.
- How: See [doc/pip_on_win2k.md](doc/pip_on_win2k.md).
