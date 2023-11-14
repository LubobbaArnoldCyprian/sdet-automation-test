# sdet-automation-test

# How to run project:


 ### **Initial Setup:**

To test the project locally:
* Clone the project on your local machine:


      git clone git@github.com:LubobbaArnoldCyprian/sdet-automation-test.git

* open IDE >File >Open(directory of the project).


 ### **Packages Installation:**
* Install the requirements.txt file, open terminal and run command:


	  pip install -r requirements.txt


* Install additional packages, open terminal and run these commands: 


	  pip install selenium

      pip install allure-pytest




 ### **Allure Report Installation:** 

* Run the following command:


      npm install -g allure-commandline


 ### **Running Tests:**
 To run the test use the command below.

      pytest --alluredir="./reports"

 ### **View Allure Report:**
To view the generated report, Navigate to project directory in your terminal use command below.

      allure serve "./reports" 



## What is Expected?
This is a code challenge to test your skills related to the development of automated tests. We use pytest with python, 
and allure for the reports, but feel free to use any framework you are familiar with, as long as you develop it using 
Python. 

The test consists in some steps to interact with a web page and assert some conditions, generating a report with the test result after the execution.

## Test Scenario - Front End test
For this test you should follow the steps:
1. Go to https://www.amazon.com and expand the 'All' hamburger menu

![](./imgs/img_1.jpg)
2. Under 'Shop By Department' open 'Arts & Craft'

![](./imgs/img_2.jpg)
3. Open 'Beading & Jewelry Making'

![](./imgs/img_3.jpg)
4. Open 'Engraving Machines & Tools'

![](./imgs/img_4.jpg)
5. Sort by Price: High to Low

![](./imgs/img_5.jpg)
6. For the products that are currently available, open the third one.
7. Check the review score. If it's less than 4, fail the test, otherwise pass it.
8. Check the price for the opened item. If it's more than $4000, fail the test, otherwise pass it.
9. Generate a report with the test result. In case of failure, attach a screenshot of the current page in the report.

## Repository
You will need to fork the repository and build the solution in Github publicly. Once you are finished, share your
repository with us. We expect this to be finished in one week, but if anything happens and this deadline cannot be met, 
reach out, so we know what is happening instead of think that you are not interested in this position anymore. 

## Deliverables:
* Code in a public Github repository
* README file with the notes, documentation, and instructions related to the code developed
* The test execution should do the above steps and generate a report with the tests results. In case of a test failure, it should also attach a screenshot of the current page when the test failed.
* Have the test parametrized so we can choose if we want to run it in headless mode or not.
