import os
import pylint.lint
# Define a function to find all Python files in a directory
def find_py_files(directory):
    py_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                py_files.append(os.path.join(root, file))
    return py_files

# Find all Python files in the current working directory and its subdirectories
diretories=['/home/cloud/54/ld-cora-cll-api','/home/cloud/54/ld-cora-mwaa-s3']
all_py_files = []
#print(all_py_files)
for i in diretories:
    py_files=find_py_files(i)
    all_py_files+=py_files
# Print the list of Python files
for i in all_py_files:
    results=pylint.lint.Run([i],do_exit=False)
