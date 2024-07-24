import subprocess

proc = subprocess.Popen(['./micropython','-i'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
proc.stdin.write(b'print(2+2)\n')