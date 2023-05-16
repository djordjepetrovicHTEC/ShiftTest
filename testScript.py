import os
import difflib

current_directory = os.getcwd()

workflow_file_path = os.path.join(current_directory, ".github", "workflows", "testWorkflow1.yaml")

readme_file_path = os.path.join(current_directory, ".github", "workflows", "mockReadme.txt")

with open(workflow_file_path, 'r') as workflow_file:
    workflow_contents = workflow_file.readlines()

prev_version_command = f"git diff {workflow_file_path}"

print(prev_version_command)

prev_version_output = os.popen(prev_version_command).read().splitlines()

new_lines = difflib.unified_diff(prev_version_output, workflow_contents, lineterm='', n=0)
new_lines = [line for line in new_lines if line.startswith('+')]

print(new_lines)

#with open(readme_file_path, 'a') as readme_file:
#    readme_file.write('\n'.join(new_lines))
