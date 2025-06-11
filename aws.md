sudo apt-get update -y
sudo apt-get upgrde
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
(This command adds the ubuntu user to the docker group so that you can run Docker commands without needing to use sudo every time)

newgrp docker

----
#from github actution runners
# Create a folder
$ mkdir actions-runner && cd actions-runnerCopied!# Download the latest runner package
$ curl -o actions-runner-linux-x64-2.325.0.tar.gz -L https://github.com/actions/runner/releases/download/v2.325.0/actions-runner-linux-x64-2.325.0.tar.gzCopied!# Optional: Validate the hash
$ echo "5020da7139d85c776059f351e0de8fdec753affc9c558e892472d43ebeb518f4  actions-runner-linux-x64-2.325.0.tar.gz" | shasum -a 256 -cCopied!# Extract the installer
$ tar xzf ./actions-runner-linux-x64-2.325.0.tar.gz

# Create the runner and start the configuration experience
$ ./config.sh --url https://github.com/TarunSaxena1996/datascience_p3 --token AGIRZZ5TI6UMM45WXJQEFXDIIOGWE
--

command line inputs-

Enter the name of the runner group to add this runner to: [press Enter for Default] (press enter)
Enter the name of runner: [press Enter for ip-172-31-80-157] self-hosted
Enter any additional labels (ex. label-1,label-2): [press Enter to skip] (press enter)
Enter name of work folder: [press Enter for _work] (press enter)

# Last step, run it!
$ ./run.sh

<img width="798" alt="image" src="https://github.com/user-attachments/assets/4aef6f9c-6e7d-41a6-aca1-30855f979591" />
<img width="740" alt="image" src="https://github.com/user-attachments/assets/f5398025-b162-4998-ba4d-b2113db26130" />
<img width="1443" alt="image" src="https://github.com/user-attachments/assets/92a5fba2-8f98-4f42-90a7-711bf9e48b9d" />
<img width="1190" alt="image" src="https://github.com/user-attachments/assets/aa190137-a37b-4c83-a06b-bb0fc624bbdc" />


ECR-
<img width="1456" alt="image" src="https://github.com/user-attachments/assets/8b5ba25a-28cd-469d-b276-9d8e1f9f14b1" />

