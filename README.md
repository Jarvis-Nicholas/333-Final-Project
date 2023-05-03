# 333-Final-Project (Pokemon)

## Introduction
This is a scaled down version of Pokemon. It operates mostly in part to user defined classes. These classes contain the attributes and methods that impact the pokemon, pokemon trainer, poke center, etc. Additionally, the files for "battle_stadium" and "research_lab" serve as utility files to further handle these class objects. All pokemon are grabbed from the pokemon_list.txt file.

## Automatic Testing:
The testing for this application is automated through "pytest". Within the application, there are multiple files that perform unit tests and integration tests. When a push is made to this github repository, a worflow is initiated. Due to github Actions, the application is built in different version of python (3.7, 3.8, 3.9, 3.10, 3.11). Pytest is then ran in each build, checking the assert statements contained within the body of the application.

### Documenation for Replication:
This automatic testing was made possible through github workflows and github actions laid out within a yml file
* Create the github-actions.yml file
  * On Github, click "Add file", "Create new file", and name the file ".github/workflow/github-actions.yml"
  * Create actions within github-actions.yml
  * "on : [push]" makes the workflow execute whenever code is pushed to the repository
  * "steps" is where the desired executables are outlined
  * "Install dependencies" installs python and pytest so that tests may be ran
  * "Lint with ruff" checks the application files for proper code formatting and syntax
  * "Test with pytest" runs the actual tests

## Automatic Deployment:
The deployment for this application is automated through github Actions and Docker Hub. After the tests sucessfully run, an image is built for the application. This image is then pushed to Docker Hub after the correct Docker login credentials are provided. These credentials are hidden as "secret" variables, as provided by Github for this repository. Now, the image resides within a Docker Hub repository named "njarvis1/333_final_project". This is a public repository, so anyone with the link may pull the image from the repository to their own machine. Then, they may "run" the image, which in turn creates a container that runs. The container allows anyone to run the Pokemon application without having to had accessed my Github repository or download the files to their own IDE.

Link to Docker Hub Repository: https://hub.docker.com/r/njarvis1/333_final_project

### Documenation for Replication:
This automatic deployment was made possible through a github workflow. Github actions written in the github-actions.yml file are what deployed the application as an image to Docker Hub. Additionally, a Dockerfile is needed within one's own application so that the image may be built. This Dockerfile should lay out the files included in the image and their programming language type.
* Open up "github-actions.yml"
* Add a new job named "Deploy-Image-To-DockerHub:"
* "needs: build"
  * This makes it so that "Deploy-Image-To-DockerHub:" only executes if the automated testing is sucessful
* "Checkout code" , "set up Qemo", and "Set up Docker Buildx" are all pre-checks to make a Docker image
* "Login to Docker Hub" provides the username and token needed to log in
  * It is best practice to make these "secret" variables. Othwerise, anyone can see the login information
* "Build and push to Docker Hub" takes the Dockerfile within the application and pushes it to the Docker Hub respository
  * The name of the repository is provided by "tags"
#### *Note:*
* Pull from Docker Hub terminal command
  * docker pull njarvis1/333_final_project:lastest
* Run
  * docker run -i -t njarvis1/333_final_project:lastest 
