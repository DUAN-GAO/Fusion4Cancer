# Machine Learning-Driven Data Fusion in Cancer Research: A Review of Methodologies and Trends
-----------------------------------------------------------------

## 1. Introduction
**Fusion4Cancer** is a tool that integrates algorithms from 15 academic papers referenced in review articles. It provides 15 corresponding Docker images and Dockerfiles, eliminating the need for users to manually install complex dependencies in Python, R, or other programming languages. Users can simply pull the pre-built images from Docker Hub or build them locally from the provided Dockerfiles. All original project bugs have been fixed, and the APIs of all 15 algorithms have been fully rewritten, enabling researchers to easily and efficiently reproduce and apply the methods described in the literature.


## 2. Usage
**NIHGCN** 
The Docker image can be directly pulled from Docker Hub using the following command:
```docker pull duangao/fusion4cancer:NIHGCN```

Alternatively, the image can be built locally from the provided Dockerfile by executing:
```sudo docker build -t NIHGCN:v1 .```

After the image has been downloaded or built, enter the container and run the following command:
```python /home/main.py```

Please modify the command-line arguments in main.py as needed. If no modifications are made, the program will run with the default parameters.

**TransCDR** 

**RedCDR** 

### 3. Data


All datasets used in the project are located at [https://zenodo.org/records/15907235?token=eyJhbGciOiJIUzUxMiJ9.eyJpZCI6IjczZmE3YjIxLTA3MWUtNGI2YS1hNDA5LTg3Y2Q0NzAyYjFlMCIsImRhdGEiOnt9LCJyYW5kb20iOiI1ZjdkMmFhYzg4NmEyYWFlNTFiYWJiN2FmOWJkYWVjNCJ9.y15D4lrWkWwBcmM86sMX19k-ovBo9WL2jlzQn7a0GnRlA3ygpiGnSRmz-ErDoJGH9teKyHwWbP1WPlIiltzxQQ](https://zenodo.org/records/15907235?token=eyJhbGciOiJIUzUxMiJ9.eyJpZCI6IjczZmE3YjIxLTA3MWUtNGI2YS1hNDA5LTg3Y2Q0NzAyYjFlMCIsImRhdGEiOnt9LCJyYW5kb20iOiI1ZjdkMmFhYzg4NmEyYWFlNTFiYWJiN2FmOWJkYWVjNCJ9.y15D4lrWkWwBcmM86sMX19k-ovBo9WL2jlzQn7a0GnRlA3ygpiGnSRmz-ErDoJGH9teKyHwWbP1WPlIiltzxQQ). 

## 4. Contact  

**DUAN GAO** < gaoduan666@gmail.com >  



