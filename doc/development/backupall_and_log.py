'''
'''
raise NotImplementedError("See backupall.py instead.")
from subprocess import Popen, PIPE, STDOUT

process = Popen(command_line_args, stdout=PIPE, stderr=STDOUT)
with process.stdout:
    log_subprocess_output(process.stdout)
exitcode = process.wait()  # 0 means success
