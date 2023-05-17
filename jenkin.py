import os

product_name = os.environ['ProductName']
application_name = os.environ['ApplicationName']
jira_db = os.environ['JiraDb']
target_url = os.environ['TargetURL']

repo_name = product_name + ".git"
os.system("git clone --bare https://github.com/smartdev0218/Jenkins_Python.git " + repo_name)

os.system("git clone --mirror https://github.com/smartdev0218/Jenkins_Python.git")
os.chdir("Jenkins_Python.git")
os.system("git push --mirror ../" + repo_name)
os.chdir("..")

config_file_path = os.path.join(repo_name, "API", "Config.YAML")
with open(config_file_path, "r") as config_file:
  config_data = config_file.read()
  
config_data = config_data.replace("ProductNamePlaceholder", product_name)
config_data = config_data.replace("ApplicationNamePlaceholder", application_name)
config_data = config_data.replace("TargetUrlPlaceholder", target_url)

with open(config_file_path, "w") as config_file:
  config_file.write(config_data)

key = product_name + "_" + application_name
encrypted_key = "thisisademooauthkey"

key_folder_path = os.path.join(repo_name, "key")
os.makedirs(key_folder_path)

key_file_path = os.path.join(key_folder_path, "encrypted_key")
with open(key_file_path, "w") as key_file:
  key_file.write(encrypted_key)

os.chdir(repo_name)
os.system("git add .")
os.system("git commit -m 'Adding updated Config.YAML and encrypted key'")
os.system("git push")