# Interacting with the operacting system fns using python
# %%
# os.system() function generaly used to execute the command in the shell
# due to security reasons and the control over the execution it is not a recommanded fn
# use subprocess module
import subprocess
from subprocess import CompletedProcess

p: CompletedProcess = subprocess.run('dir', shell=True, check=True, capture_output=True, encoding='utf-8')
# print(p)
print(p.args) # print the arguments used.
print(p.returncode) # the return code 
print(p.stdout) # output stream.




# %%
# code to search a purticular package in pip installed or not 
# using dual subprocess run
# command : pip freeze | grep pandas
# following code only works in linux
import subprocess
import typing

# getting the search input
keyword:str = 'pandas'

pip_process = subprocess.run('pip freeze', check=False, shell=True, capture_output=True)
if pip_process.returncode != 0:
    print("Can not process the pip freeze, output stream:\n")
    print(pip_process.stderr)
    exit()
grep_search = subprocess.run(f'grep {keyword}', input= pip_process.stdout, check=False, shell=True, capture_output=True )
if grep_search.returncode != 0:
    print("unable to perform the search on the output of pip freeze")
    print(grep_search.stderr)
    exit()
print(f"what we found for the search {keyword}: \n")
print(grep_search.stdout)



# %%
