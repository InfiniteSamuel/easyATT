from subprocess import Popen, PIPE

p = Popen(['pdf2txt.py', '-p 1,1','test.pdf'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
output, err = p.communicate(b"input data that is passed to subprocess' stdin")
rc = p.returncode
