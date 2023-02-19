# sangerTask
Software Engineer Sanger Task

This Project is meant to perform analysis and manipulate Compressed FASTQ format files using python scripts that can run on unix and linux operating systems.

# Dependencies : 

1 - Python version 3.9 

2 - Docker and Docker Desktop. 

3 - VsCode ( or IDE/Code Editor of your choice ) . 

# Installation instructions:

1 - clone the repo on your local machine using ```git clone https://github.com/MohammedYasserr/sangerTask.git ``` and then create a python virtual environment using the following command ``` py -m venv env ``` for windows and ``` python3 -m venv env ``` for Unix/macOs, and finally activate it by the following command ``` cd/env/Scripts/activate``` 

2 - You can fine the test.fastq.gz in data folder ( This folder is the path to your data files ), you can also replace the test.fastq.gz file in the folder.

3 - you can simply run from your integrated terminal or any other terminal (after navigating to the project folder) the command " python main.py"

# How to run the project ? 

1- If you are using windows operating system, simply clone the repo, create a virtual environment and run from your integrated terminal or any other terminal (after navigating to the project directory" the following command python main.py. 

2 - You can also run the project by building the docker image by using the following command ```docker build -t fastq-python ``` then run the following command ``` docker run fastq-python ```, you can find the repo for the image on my dockerhub and pull it using the following command ``` docker pull 2981998/fastq-python:latest ```

3 - If you are using unix or linux, I added the ``` #!user/bin/env python3 ```  line at the top of the script and this shebang to make the script excutable on unix-like operating systems.
