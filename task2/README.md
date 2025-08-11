Docker Installation and Running a Hello-World 

Introduction
In this task, I installed Docker on the machine and verified that the installation was successful by running the Hello-World image.

Then I documented the steps, including time and results.
Steps I followed:

1. Install Docker
Downloaded Docker Desktop from the official website https://www.docker.com/products/docker-desktop.
Followed the installation instructions for macOS.
After installation, I ran Docker Desktop and waited until it was in "Running" mode or the whale icon appeared in the system tray..
2. Verify Docker Installation
Opened Terminal and typed the following command to check the Docker version:
docker --version
Docker version 20.10.22
3. Run the Hello-World Image
In Terminal, I executed the command:
docker run --rm hello-world
When it is run, a welcome message appears.

4. Documenting the execution time and results
The first i create filed and show :
mkdir docker-proof
cd docker-proof

I Saved the execution date and current time to a text file:
(date > TIMESTAMP.txt)
I saved a copy of the Docker version:
(docker --version > docker_version.txt)
I saved the output of running hello-world:
(docker run --rm hello-world > hello_output.txt 2>&1)

Result
Proves execution time and system state.

5- Upload to GitHub
I wrote these comments in the terminal inside the project folder.
git init
git add .
git commit -m "Step 1: Install Docker & proof (timestamp)"
git branch -M main
git remote add origin https://github.com/r0ry2/DevOps.git
git push -u origin main



