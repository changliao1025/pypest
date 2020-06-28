# PyPEST

This is a Python package for the PEST [(http://www.pesthomepage.org/)](http://www.pesthomepage.org/) tool.

It extends the capacity of current PEST that it can be applied to almost any computational numerical model.


# Abstarct

Model calibration can be tedious and computationally expensive, especially when the models are spatially distributed. We developed a Python software package based on the Parameter ESTimation (PEST) code to automate and speed up the calibration process. This package is model independent and can be customized for any computational models. To speed up the calibration, it uses a parent-child structure to conduct model calibration in a parallel computing environment. The software package can be used to (1) automate input data preparation for model simulation; (2) automate input data preparation for PEST calibration; and (3) analyze/visualize the model outputs. 

# Illustration 

1. Model concept

![Model concept](https://github.com/changliao1025/pypest/blob/master/pypest/pypest.png?raw=true)


2. Code template structure
   
![Code structure](https://github.com/changliao1025/pypest/blob/master/pypest/instruction.png?raw=true)

# Citation
Chang Liao, Teklu Tesfa, Zeli Tan, Chao Chen, & L. Ruby Leung. (2020). 



# Acknowledgement
The research described in this paper was primarily funded by a Laboratory Directed Research and Development (LDRD) Program project at Pacific Northwest National Laboratory. CL and LRL were also partly supported by U.S. Department of Energy Office of Science Biological and Environmental Research through the Earth and Environmental System Modeling program as part of the Energy Exascale Earth System Model (E3SM) project. 

# Usage
In order to run the program, you need:
1. git clone git@github.com:changliao1025/pypest.git
2. compile PEST/BeoPEST and place it under the system path
3. use exisitng supported models, or
4. add new models based on the template files

# Contact
Please contact Chang Liao (chang.liao@pnnl.gov) if you have any questions.



