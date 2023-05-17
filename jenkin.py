import os

product_name = os.environ['ProductName']
application_name = os.environ['ApplicationName']
jira_db = os.environ['JiraDb']
target_url = os.environ['TargetURL']

keyArr = ['ProductName', 'ApplicationName', 'TargetURL']
valueArr = []
valueArr.append(product_name)
valueArr.append(application_name)
valueArr.append(target_url)

repo_name = product_name

os.system("git clone https://github.com/smartdev0218/Jenkins_Python.git " + repo_name)
os.chdir(repo_name)
os.system("git push --mirror https://github.com/smartdev0218/" + repo_name)
os.chdir("..")

config_file_path = os.path.join(repo_name, "API", "Config.yaml")

file_path = open(config_file_path, "rt")

config_file = file_path.read()
lines = config_file.split('\n')

for i in range(len(lines)):
    for j in range(len(keyArr)):
        if keyArr[j] in lines[i]:
            lines[i] = keyArr[j] + ": " + valueArr[j]
            break

file_path = open(config_file_path, "wt")
file_path.write('\n'.join(lines))
file_path.close()

key = product_name + "_" + application_name
encrypted_key = key + "_" + "thisisademooauthkey"

key_folder_path = os.path.join(repo_name, "key")
os.makedirs(key_folder_path)

key_file_path = os.path.join(key_folder_path, "encrypted_key")

key_file = open(key_file_path, "wt")
key_file.write(encrypted_key)
key_file.close()

os.chdir(repo_name)
os.system("git add .")
os.system("git commit -m 'change'")
os.system("git push --mirror https://github.com/smartdev0218/" + repo_name)