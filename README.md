# scientific-calculator

# Index: 

a.Problem statement 

b.Introduction to Devops 

c.Devops Toolchain 

d.Source Code Management 

e.Testing 

f.Build 

g.Containerize 

h.Continuous Integration and Deployment 

i.Conclusion 

Building environment: 
IDE: VS Code 
Language: Python 


# Problem Statement 

Create a scientific calculator program with the following user menu driven operations:  

● Square root function - √x  

● Factorial function - x!  

● Natural logarithm (base е) - ln(x)  

● Power function – x^b 
 
The pipeline includes, 

1. Using a source control management tool - like GitHub, GitLab, BitBucket etc 

2. Testing - test your code using either JUnit, Selenium, PyUnit and many more 

3. Build - build your code using tool like Maven, Gradle, Ant and many more 

4. Continuous Integration - Continuous integrate your code using tool like Jenkins, 

GitLab CLI, Travis CLI, and many more. 

5. Containerize - Containerize your code using Docker. 

6. Push your created Docker image to Docker hub. 

7. Deployment - Do configuration management and deployment using either Chef, 

Puppet, Ansible, Rundeck. Using these do configuration management and pull your 

docker image and run it on the managed hosts. 

8. For Deployment you can either do it on your local machine or on Kubernetes cluster 

or OpenStack cloud. You can also use Amazon AWS or Google Cloud or some other 

3rd party cloud 

# Introduction to Devops 

DevOps combines development and operations to increase the efficiency, speed, and security of software development and delivery compared to traditional processes. A more nimble software development lifecycle results in a competitive advantage for businesses and their customers. 
 
DevOps is a collaboration between development and operation teams, which enables continuous delivery of applications and services to our end users.  

Benefits of DevOps: 

Continuous delivery of software 

Better collaboration between teams 

Easy deployment 

Better efficiency and scalability 

Errors are fixed at the initial stage 

More security 

Less manual intervention (which means fewer chances of error) 

# DevOps Lifecycle: 

Now that you know why DevOps and what is it exactly, we will learn all about the DevOps Lifecycle which will give you a clarit on why devops, that is divided into six different phases which will give a clear idea on why Devops: 

Source Code Management - In this phase, the business owners and software development team discuss project goals and create a plan. Programmers then design and code the application, using tools like Git to store the application code. 

Continuous Build and Test - This phase deals with building tools, like Maven and Gradle, then taking code from different repositories and combining them to build the complete application. The application is then tested using automation testing tools, like Selenium and JUnit, to ensure software quality. 

Continuous Integration - When the testing is complete, new features are integrated automatically to the existing codebase. 

Continuous Deployment - Here, the application is packaged after being released and deployed from the development server to the production server. Once the software is deployed, operations teams perform tasks, such as configuring servers and provisioning them with the required resources. 

Continuous Monitoring - Monitoring allows IT organizations to identify issues of specific releases and understand the impact on end-users. 

Software Released - After all the phases are completed and the software meets the user’s requirement, it is released into the market. 

Devops ToolChain 

The Devops tools used to automate the Devops life cycle are listed as follows: 

GitHub: A web-based platform for version control and collaboration, allowing users to store, manage, and track changes to their code projects using Git. 

Docker: A platform for developing, shipping, and running applications inside lightweight containers, ensuring consistency across multiple development and release cycles. 

Ansible: An open-source automation tool for software provisioning, configuration management, and application deployment, using declarative language to describe system configurations. 

Jenkins: An open-source automation server used for continuous integration and continuous delivery, facilitating the technical aspects of software development by automating builds, tests, and deployments. 

 

# Source Control Management (SCM) 

Tools Used: Github 
Source code Language: Python 
Create a new Repository: 

We create a new Repository in Github for the project and name it (e.g. scientific-calculator). 
Initially you repository must have 2 files – Readme and  .gitinore(if you wish to include it). 

Clone the Repository Locally: 
Open Vs Code and Clone the Repository. 

Set Up Project Structure: 
Navigate to your Project from the bash shell and set the repository as your current    
working directory: 
 				cd scientific-calculator 

Create your python Script: 
Open the text editor and write the script for your Calculator program. 
Save the script as Calculator.py. 

Add the Script to git, commit and push the changes to github. 
Use the git add command to stage your new Python script for commit: 
 				git add calculator.py 
 
Commit the addition of your Python script with a descriptive message: 
 		git commit -m "Calculator with all the Functions" 
 
Push your commit to GitHub to update your repository: 
 				git push origin main 

Verify the Changes on GitHub: 
Go to your repository on the GitHub website and refresh the page. You should see three files (Readme and .gitinore as initial commits and Calculator.py) in your repository. 

 

# Testing 

Tool used: Pytest 

1. Install PyTest: 
    Open bash in vs code and run: 
			                              pip install pytest 

    Next create a test file named test_calculator.py to test the cases 

Write Tests for Each Function: 
Start by importing the functions from your calculator.py script. 
Now, create a function for testing each mathematical operation. Each test function should start with test_ as per PyTest conventions. 
After making the test_calculator.py file, push the file to the github. 

Running Your Tests: 
With your tests written, you can now run them through PyTest. Open bash and execute the following command: 
    					     pytest 
PyTest will automatically discover and run all tests in files prefixed or suffixed with test_, providing a report on which tests passed or failed. 
If all the test cases are executed successfully, you will get a message like this in the terminal. 

# Building  

Tools Used: PyInstaller 

Note: Make sure you have pyinstaller installed in your computer. If not use the following command: 
 					pip insall pyinstaller 
 
1. Run PyInstaller: 
    Open bash in vs code and navigate to your directory. 
    Execute the following command to create the standalone executable. Replace your_script.py        
    with the path to the main Python script of your project (e.g., calculator.py): 
  	 		pyinstaller –onefile scientific-calculator.py 

 
The --onefile option tells PyInstaller to bundle everything into a single executable file for easy distribution. 
 
2. Locate and Run the Executable 

After the build process completes, find your standalone executable in the ‘dist’ directory inside your project folder. The executable will have the same name as your script file but without the .py extension. 

Running the Executable:
Windows: Navigate to the dist directory and double-click on the executable file to run the application. 
macOS/Linux: Open a terminal, navigate to the dist directory, and execute the file by typing ./your_executable_name. 
 
# Containerize 

1. Write a Dockerfile 

You start by defining a Dockerfile that specifies how to build the Docker image for your application. The Dockerfile includes the base image you're building from, any software you need to install, and any commands you run as part of the setup process. 

2. Build the Docker Image 

Next, you use the docker build command to create a Docker image from the Dockerfile. This command reads the Dockerfile in the current directory (denoted by . at the end of the command) and builds an image according to its specifications. 

docker build -t scientific-calculator . 

Tag your image for Docker Hub: 

docker tag scientific-calculator radhika20/scientific-calculator:latest 

3. Push your image to DockerHub: 

docker push radhika20/scientific-calculator:latest 

# Continuous Integration and Deployment 

1. Install Jenkins: Download and install Jenkins on your server.  
Install Java  

sudo apt-get update 

sudo apt install -y openjdk-11-jdk 

To check:  java  - - version 

openjdk version "11.0.11" 2021-04-20 

OpenJDK Runtime Environment (build 11.0.11+9-Ubuntu-0ubuntu2.18.04) 

OpenJDK 64-Bit Server VM (build 11.0.11+9-Ubuntu-0ubuntu2.18.04, mixed mode, sharing) 

Install Jenkins 

wget -q -O - https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo apt-key add - 

sudo sh -c 'echo deb http://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list' 

Install ca-certificates  (man 8 update-ca-certificates) 

sudo apt install ca-certificates 

Install Jenkins 

sudo apt-get update 

sudo apt-get install jenkins 

To check Jenkins version:  vim /var/lib/jenkins/config.xml 

To copy admin password: sudo cat /var/lib/jenkins/secrets/initialAdminPassword 

2. Configure Jenkins: After installation, access Jenkins through your web browser (usually at http://yourserver:8080) . Enter the username as ‘admin’ and admin password. Complete the initial setup, including the installation of suggested plugins. 

3. Install Necessary Plugins: Install plugins for Docker and Ansible integration in Jenkins. You can find these plugins in the "Manage Jenkins" > "Manage Plugins" section. 

4. Add Global Configuration tool: Go to “Manage Jenkins” > “Tools”
   
5. Add Github and Docker Hub Credentials: Go to “Manage Jenkins” > “Configure” 

6. Add Github server: Go to “Manage Jenkins” > “System” 

7. For the deployment, let's focus on using Ansible: 

Step 1: Install Ansible 

First, you need to have Ansible installed on your machine (the control node). For installation of ansible in Ubuntu: 

sudo apt update 

sudo apt install ansible 

Step 2: Write an Ansible Playbook 

An Ansible playbook defines the tasks to be executed on the managed hosts. Create a YAML file named deploy.yml to pull and run your Docker image on your managed hosts. 

Step 3: Run Your Ansible Playbook: 

Execute your playbook with the following command, specifying your inventory file: 

ansible-playbook -i hosts deploy.yml 

8. Set Up a Project: Create a new job in Jenkins for your project, configuring it to pull from your source control repository. It must be a pipeline project.  

9. Create a Jenkins Pipeline: Define your build, test, and deployment stages in a Jenkinsfile and add it to your project repository. 

10. Click on build now to build the project. The following figure shows the stage view for the pipeline stages: 

11. Following the successful completion of the pipeline job, the newly created Docker image can be verified by the command: 

docker images 

12. Immediately after the pipeline job successfully builds, the Docker image can be executed directly. This is visible in the following section using containers with the command  

 docker run -it --name myHostContainer <Image-Id/Name>  

# Conclusion 

The project effectively demonstrates the application of DevOps practices, showcasing the seamless integration of tools like Git, GitHub, VS Code, Docker, Ansible, and Jenkins. This integration facilitates a robust CI/CD pipeline, automating the software development lifecycle from code changes to deployment. Insights gained emphasize the importance of automation in achieving efficiency, consistency, and scalability. The experience underscores the critical role of collaboration and toolchain synergy in modern software development, paving the way for future enhancements and more complex implementations. 
