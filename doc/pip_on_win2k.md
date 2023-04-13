# PIP on Win2k
(without the internet)

Why these steps are necessary:
- Later versions of Python dropped support for Win2k, but the Python 3 versions that support it don't come with pip (nor setuptools which pip requires).
- Avoid connecting Win2k to the internet since it has many known vulnerabilities and is no longer supported by Microsoft.

The Python versions necessary can be downloaded from the list of Python releases (only some releases have downloads):
<https://www.python.org/downloads/windows/>

During install of Python 2.7.10, a warning appears saying that 3.3.0 will be the last version of Python released with Python support.

These notes explain what was tried, including Python 3.3.5 even though that is above 3.3.0.
- 3.3.5 doesn't run ("not a valid win32 application") on Win2k though it installs (I ensured that I used the 32-bit version).

The files were created using a Windows computer using the same (32-bit) version of Python connected to the internet (So that the Win2k machine doesn't have to be).

The following was created using the manually downloaded dirsync repo and the quoted answer further down and diffnames.py by Jake Gustafson:
- pip+six+dirsync-patch_for_Python3.3.5.zip
- (unusable since 3.3.0 doesn't run) pip+six+dirsync-patch_for_Python3.3.5.zip

The following was created manually using downloaded repo and pip:
- six+dirsync-patch_for_Python2.7.10.zip


## Quoted answer
<https://stackoverflow.com/questions/56798617/how-to-install-pip-for-python-3-3-on-windows>
`pip` dropped support for Python 3.3 at version [18.0](https://pip.pypa.io/en/stable/news/#id109). `setuptools` (required by `pip`) dropped support for Python 3.3 at version [40.0](https://github.com/pypa/setuptools/blob/master/CHANGES.rst#v4000). So you need to download [`pip 10.0.1`](https://pypi.org/project/pip/10.0.1/#files) and [`setuptools 39.2.0`](https://pypi.org/project/setuptools/39.2.0/#files) (source distributions, `*.tar.gz`). Extract the archives and run `python setup.py install` first for `setuptools`, then for `pip`.

As for the latest versions of numpy and scipy, let's us see.

Numpy: [https://pypi.org/project/numpy/](https://pypi.org/project/numpy/)
Requires: Python >=2.7, !=3.0.\*, !=3.1.\*, !=3.2.\*, **!=3.3.\***

scipy: [https://pypi.org/project/scipy/](https://pypi.org/project/scipy/)
Requires: Python **\>=3.5**

See? You will need to do research to find out versions compatible with Python 3.3.

[Share](https://stackoverflow.com/a/56798945 "Short permalink to this answer")

Share a link to this answer

Copy link[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/ "The current license for this post: CC BY-SA 4.0")

[Improve this answer](https://stackoverflow.com/posts/56798945/edit)

Follow

Follow this answer to receive notifications

answered Jun 27, 2019 at 22:02

[

![phd's user avatar](https://www.gravatar.com/avatar/512cfbaf98d63ca4acd57b2df792aec6?s=64&d=identicon&r=PG)

](https://stackoverflow.com/users/7976758/phd)

[phd](https://stackoverflow.com/users/7976758/phd)phd

79.3k1212 gold badges115115 silver badges153
