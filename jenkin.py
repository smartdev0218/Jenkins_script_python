import os

product_name = os.environ['ProductName']
application_name = os.environ['ApplicationName']
jira_db = os.environ['JiraDb']
target_url = os.environ['TargetURL']

# repo_name = product_name + ".git"
repo_name = product_name
# os.system("git clone --bare https://github.com/smartdev0218/Jenkins_Python.git " + repo_name)

os.system("git clone https://github.com/smartdev0218/Jenkins_Python.git " + repo_name)
os.chdir("Jenkins_Python")
os.system("git push --mirror https://github.com/smartdev0218/" + repo_name)
os.chdir("..")

config_file_path = os.path.join(repo_name, "API", "Conig.yaml")
# with open(config_file_path, "r") as config_file:
#   config_data = config_file.read()

file = open(config_file_path, "rt")

config_file = file.read()

config_data = config_data.replace(product_name, "ProductNamePlaceholder")
config_data = config_data.replace(application_name, "ApplicationNamePlaceholder")
config_data = config_data.replace(target_url, "TargetUrlPlaceholder")

# with open(config_file_path, "w") as config_file:
#   config_file.write(config_data)

file = open('config.yaml', "wt")
file.write(config_file)
file.close()

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
os.system("git push --mirror https://github.com/smartdev0218/" + repo_name)