# face-recognition
Program to detect the person's face after taking 500 samples of the same
-
The program will take inputs(500 samples) for two people in the first file and will be able to detect their faces after training the module in the second file through the third.

Steps
-
1. Create a folder named 'samples' and subfolders inside it named '0' and '1'.
2. Run the first file : '1_firstFileToRun.py'
3. Now your face samples should be saved in the 0 and 1 folder. If you wanna add another person just make a subfolder '2' in samples add the line - 
  ```python
  print('Taking second person samples')
  collect_samples(2)
  ```
  after adding these lines, go to the 3rd file i.e. '3_finalFileToRun.py' and edit from the fourth line to - 
  ```python
  n1=input('Enter name of the first person: ')
  n2=input('Enter name of the second person: ')
  n3=input('Enter name of the third person: ')
  names = {

      0 : n1,
      1 : n2,
      2 : n3
  }
  ```
  if there are more people, follow the process with subfolders named 3,4,5 and so on accordingly.
  
 4. Now run the second file i.e. '2_secondFileToRun.py' so it trains the module according to your face(s).
 
 5. Finally run the 3rd file and test the code. It will also be displaying the confidence percentage of the module in identifying you correctly.
 
 


**Written By: Arshiya Sharma**
 
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
