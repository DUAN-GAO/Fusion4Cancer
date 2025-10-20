# Machine Learning-Driven Data Fusion in Cancer Research: A Review of Methodologies and Trends
-----------------------------------------------------------------

## 1. Introduction
**Fusion4Cancer** is a tool that integrates algorithms from 15 academic papers referenced in review articles. It provides 18 corresponding Docker images and Dockerfiles, eliminating the need for users to manually install complex dependencies in Python, R, or other programming languages. Users can simply pull the pre-built images from Docker Hub or build them locally from the provided Dockerfiles. All original project bugs have been fixed, and the APIs of all 18 algorithms have been fully rewritten, enabling researchers to easily and efficiently reproduce and apply the methods described in the literature.


## 2. Usage
**NIHGCN** 
The Docker image can be directly pulled from Docker Hub using the following command:
```docker pull duangao/fusion4cancer:NIHGCN```

Alternatively, the image can be built locally from the provided Dockerfile by executing:
```sudo docker build -t NIHGCN:v1 .```

After the image has been downloaded or built, enter the container and run the following command:
```python /home/main.py```

Please modify the command-line arguments in main.py as needed. If no modifications are made, the program will run with the default hyperparameters.

**TransCDR** 
The Docker image can be directly pulled from Docker Hub using the following command:
```docker pull duangao/fusion4cancer:TransCDR```

Alternatively, the image can be built locally from the provided Dockerfile by executing:
```sudo docker build -t TransCDR:v1 .```

After the image has been downloaded or built, enter the container and run the following command:
```python /home/main.py```

Please modify the command-line arguments in main.py as needed. If no modifications are made, the program will run with the default hyperparameters.

**RedCDR** 
The Docker image can be directly pulled from Docker Hub using the following command:
```docker pull duangao/fusion4cancer:RedCDR```

Alternatively, the image can be built locally from the provided Dockerfile by executing:
```sudo docker build -t RedCDR:v1 .```

After the image has been downloaded or built, enter the container and run the following command:
```python /home/main.py```

Please modify the command-line arguments in main.py as needed. If no modifications are made, the program will run with the default hyperparameters.

**MSDRP** 
The Docker image can be directly pulled from Docker Hub using the following command:
```docker pull duangao/fusion4cancer:MSDRP```

Alternatively, the image can be built locally from the provided Dockerfile by executing:
```sudo docker build -t MSDRP:v1 .```

After the image has been downloaded or built, enter the container and run the following command:
```python /home/main.py```

Please modify the command-line arguments in main.py as needed. If no modifications are made, the program will run with the default hyperparameters.

**MOMLIN** 
The Docker image can be directly pulled from Docker Hub using the following command:
```docker pull duangao/fusion4cancer:MOMLIN```

Alternatively, the image can be built locally from the provided Dockerfile by executing:
```sudo docker build -t MOMLIN:v1 .```

After the image has been downloaded or built, enter the container and run the following command:

Modify the parameter value from 'start_momlin.m' to 'MOMLIN_example.m' in the main.py configuration.
```python /home/main.py```

Please modify the command-line arguments in main.py as needed. If no modifications are made, the program will run with the default hyperparameters.

**MMPROLN** 
The Docker image can be directly pulled from Docker Hub using the following command:
```docker pull duangao/fusion4cancer:MMPROLN```

Alternatively, the image can be built locally from the provided Dockerfile by executing:
```sudo docker build -t MMPROLN:v1 .```

After the image has been downloaded or built, enter the container and run the following command:

```python /home/main.py```

Please modify the command-line arguments in main.py as needed. If no modifications are made, the program will run with the default hyperparameters.

**MetaCancer** 
The Docker image can be directly pulled from Docker Hub using the following command:
```docker pull duangao/fusion4cancer:MetaCancer```

Alternatively, the image can be built locally from the provided Dockerfile by executing:
```sudo docker build -t MetaCancer:v1 .```

After the image has been downloaded or built, enter the container and run the following command:

```python /home/main.py```

Please modify the command-line arguments in main.py as needed. If no modifications are made, the program will run with the default hyperparameters.

**MMPROLN** 
The Docker image can be directly pulled from Docker Hub using the following command:
```docker pull duangao/fusion4cancer:MMproln```

Alternatively, the image can be built locally from the provided Dockerfile by executing:
```sudo docker build -t MMproln:v1 .```

After the image has been downloaded or built, enter the container and run the following command:

```python /home/main.py```

Please modify the command-line arguments in main.py as needed. If no modifications are made, the program will run with the default hyperparameters.

Warning:
    GPU is a must and running on CPU is not possible. You have to delete certain code block in the utils.py when you are using real world data. The images in the Data folder are only for testing purposes.

**OLMN** 
The Docker image can be directly pulled from Docker Hub using the following command:
```docker pull duangao/fusion4cancer:OLNM```

Alternatively, the image can be built locally from the provided Dockerfile by executing:
```sudo docker build -t OLNM:v1 .```

After the image has been downloaded or built, enter the container and run the following command:

```python /home/main.py```

Please modify the command-line arguments in main.py as needed. If no modifications are made, the program will run with the default hyperparameters.

Warning:
    GPU is a must and running on CPU is not possible. You have to modify json files when you are using real world data since some values is fixed in the files whereas it should be calculated by using preprocessing.py. The images in the Data folder are only for testing purposes. The metric printed is like ---Best_AUC_Epoch:-1  Best_Acc:-1.0000  Best_AUC:-1.0000, since there are insufficient data. You have to provide more data to make it fully functional.

**HE_breast_recurrence** 
The Docker image can be directly pulled from Docker Hub using the following command:
```docker pull duangao/fusion4cancer:HE_breast_recurrence```

Alternatively, the image can be built locally from the provided Dockerfile by executing:
```sudo docker build -t HE_breast_recurrence:v1 .```

After the image has been downloaded or built, enter the container and run the following command:

```python /home/main.py```

Please modify the command-line arguments in main.py as needed. If no modifications are made, the program will run with the default hyperparameters.

Warning:
    GPU is a not must but running on GPU is faster, simply add .cuda() function to certain part of the neural network. You have to modify json files when you are using real world data since some values is fixed in the files. The images in the database_c2 folder are only for testing purposes. You have to provide more data to make it fully functional.

**AutoRDL** 
The Docker image can be directly pulled from Docker Hub using the following command:
```docker pull duangao/fusion4cancer:AutoRDL```

Alternatively, the image can be built locally from the provided Dockerfile by executing:
```sudo docker build -t AutoRDL:v1 .```

After the image has been downloaded or built, enter the container and run the following command:

```python /home/main.py```

Please modify the command-line arguments in main.py as needed. If no modifications are made, the program will run with the default hyperparameters.

Warning:
    GPU is a must and running on CPU is not possible. You have to modify json files when you are using real world data since some values is fixed in the files whereas it should be calculated. The images in the Data folder are only for testing purposes. You have to provide more data to make it fully functional.

**DeepProg** 
The Docker image can be directly pulled from Docker Hub using the following command:
```docker pull duangao/fusion4cancer:DeepProg```

Alternatively, the image can be built locally from the provided Dockerfile by executing:
```sudo docker build -t DeepProg:v1 .```

After the image has been downloaded or built, enter the container and run the following command:

```python /home/main.py```

Please modify the command-line arguments in main.py as needed. If no modifications are made, the program will run with the default hyperparameters.

**deep-multipit** 
The Docker image can be directly pulled from Docker Hub using the following command:
```docker pull duangao/fusion4cancer:deep-multipit```

Alternatively, the image can be built locally from the provided Dockerfile by executing:
```sudo docker build -t deep-multipit:v1 .```

After the image has been downloaded or built, enter the container and run the following command:

```python /home/scripts/main.py```

Please modify the command-line arguments in main.py as needed. If no modifications are made, the program will run with the default hyperparameters.

**DTLCDR** 
The Docker image can be directly pulled from Docker Hub using the following command:
```docker pull duangao/fusion4cancer:DTLCDR```

Alternatively, the image can be built locally from the provided Dockerfile by executing:
```sudo docker build -t DTLCDR:v1 .```

After the image has been downloaded or built, enter the container and run the following command:

```python /home/main.py```

Please modify the command-line arguments in main.py as needed. If no modifications are made, the program will run with the default hyperparameters.

**DeepKEGG** 
The Docker image can be directly pulled from Docker Hub using the following command:
```docker pull duangao/fusion4cancer:DeepKEGG```

Alternatively, the image can be built locally from the provided Dockerfile by executing:
```sudo docker build -t DeepKEGG:v1 .```

After the image has been downloaded or built, enter the container and run the following command:

```python /home/main.py```

Please modify the command-line arguments in main.py as needed. If no modifications are made, the program will run with the default hyperparameters.

**multisurv** 
The Docker image can be directly pulled from Docker Hub using the following command:
```docker pull duangao/fusion4cancer:multisurv```

Alternatively, the image can be built locally from the provided Dockerfile by executing:
```sudo docker build -t multisurv:v1 .```

After the image has been downloaded or built, enter the container and run the following command:

```cd  /home/src/```
```python /home/main.py```

Please modify the command-line arguments in main.py as needed. If no modifications are made, the program will run with the default hyperparameters.

### 3. Data


All datasets used in the project are located at [https://zenodo.org/records/15907235?token=eyJhbGciOiJIUzUxMiJ9.eyJpZCI6IjczZmE3YjIxLTA3MWUtNGI2YS1hNDA5LTg3Y2Q0NzAyYjFlMCIsImRhdGEiOnt9LCJyYW5kb20iOiI1ZjdkMmFhYzg4NmEyYWFlNTFiYWJiN2FmOWJkYWVjNCJ9.y15D4lrWkWwBcmM86sMX19k-ovBo9WL2jlzQn7a0GnRlA3ygpiGnSRmz-ErDoJGH9teKyHwWbP1WPlIiltzxQQ](https://zenodo.org/records/15907235?token=eyJhbGciOiJIUzUxMiJ9.eyJpZCI6IjczZmE3YjIxLTA3MWUtNGI2YS1hNDA5LTg3Y2Q0NzAyYjFlMCIsImRhdGEiOnt9LCJyYW5kb20iOiI1ZjdkMmFhYzg4NmEyYWFlNTFiYWJiN2FmOWJkYWVjNCJ9.y15D4lrWkWwBcmM86sMX19k-ovBo9WL2jlzQn7a0GnRlA3ygpiGnSRmz-ErDoJGH9teKyHwWbP1WPlIiltzxQQ). 

To get more image data, you can find by clicking https://github.com/zhaoziheng/SAT-DS.
## 4. Contact  

**DUAN GAO** < gaoduan666@gmail.com >  


