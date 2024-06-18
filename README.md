# COMPUTER VISION MODEL APIS

A machine learning program that classifies correctly sick patient's chest xray reports to be either pneumonia infected or normal. This program uses a **neural network algorithm** to detect sick patient.

## Description  

This API service contains several packages built and hosted independently and finally imported into this project. There are three endpoints

### Service endpoint 1 (Chest xray classifier)

- returns **prediction** for condition(either normal or pneumonia) of a patient's chest health status

### Service endpoint 2 (Kitchen ware classifier)

- object identification - returns the name of the image of any of the trained objects as seen during development (glass, cup, spoon, plate, knife, fork)

### Service endpoint 3 (Brain Scan image classifier)

- returns **prediction** for condition(either glioma, meningioma, no tumor, or pituitary) of a patient's brain scan outcome

## Dependencies and packages  

1. numpy>=1.20.0,<1.21.0
2. python = 3.10
3. pandas = 2.2.2
4. scikit-learn = 1.4.2
5. pydantic = 2.7.0
6. strictyaml = 1.7.3
7. tensorflow = 2.16.1
8. scikeras = 0.13.0
9. tensorflow-datasets = 4.9.4
10. pillow = 10.3.0
11. pydantic-settings = 2.2.1
12. fastapi = 0.110.3
13. uvicorn = 0.29.0
14. loguru = 0.7.2
15. python-multipart = 0.0.9
16. kitchenware-model-package = 0.0.3
17. braintumor-model-package = 0.1.0
18. pneumonia_model_package = 0.2.0

## Source code link  

Source code link:
[Github link](https://github.com/chibuikeeugene/computer_vision_model_apis.git)

Python index package:
[Pypi link](https://pypi.org/project/pneumonia_model_package/)
[Pypi link](https://pypi.org/project/braintumor-model-package/)
[Pypi link](https://pypi.org/project/kitchenware_model_package/)


## Snapshots
![Api documentation 1](<Screenshot 2024-06-18 at 10.09.18 pm.png>)

![Api documentation 2](<Screenshot 2024-06-18 at 10.10.04 pm.png>)