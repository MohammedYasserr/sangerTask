# sangerTask
Software Engineer Sanger Task

This Project is meant to perform analysis and manipulate Compressed FASTQ format files using python scripts that can run on unix and linux operating systems.

# Dependencies and requirements : 

1 - Python version 3.9 

2 - Docker and Docker Desktop. 

3 - VsCode ( or IDE/Code Editor of your choice ) . 

# Installation instructions:

1 - clone the repo on your local machine using ```git clone https://github.com/MohammedYasserr/sangerTask.git ``` and then create a python virtual environment using the following command ``` py -m venv env ``` for windows and ``` python3 -m venv env ``` for Unix/macOs, and finally activate it by the following command ``` source env/Scripts/activate``` 

2 - You can fine the test.fastq.gz in data folder ( This folder is the path to your data files ), you can also replace the test.fastq.gz file in the folder.

3 - you can simply run from your integrated terminal or any other terminal (after navigating to the project folder) the command " python main.py"

# How to run the project ? 

1- If you are using windows operating system, 1 - clone the repo on your local machine using ```git clone https://github.com/MohammedYasserr/sangerTask.git ``` and then create a python virtual environment using the following command ``` py -m venv env ``` for windows and ``` python3 -m venv env ``` for Unix/macOs, and finally activate it by the following command ``` source env/Scripts/activate``` 

2 - You can also run the project by building the docker image by using the following command ```docker build -t fastq-python ``` then run the following command ``` docker run fastq-python ```, you can find the repo for the image on my dockerhub and pull it using the following command ``` docker pull 2981998/fastq-python:latest ```

3 - If you are using unix or linux, I added the ``` #!user/bin/env python3 ```  line at the top of the script and this shebang to make the script excutable on unix-like operating systems.

4 - To excute the script from your linux/unix system follow the instructions : First you need to navigate to the project directory from your termial then hit the following command ``` chmod +x main.py ``` and finally hit the following command ``` ./main.py```

# To contribute to the project : 
- You want to contribute to the project and you don't have access to it, I strongly recommend you to refer to this documentation from github.com that outlines the steps to do so. The documentation can be found at https://docs.github.com/en/get-started/quickstart/contributing-to-projects 

# license : 

MIT License

# Contact : 

Email : bmbmyasser@gmail.com

Linkedin profile : https://www.linkedin.com/in/mohammed-yasser-3700541a4/ 

# Further improvement currently working on : 

- I added automation to this project through github actions by addning ```release-fastq-python.yml ``` at the ```.github``` folder, this pipeline will enable me to publish the software as PyPi package as well as leverging the CI/CD utilities.
