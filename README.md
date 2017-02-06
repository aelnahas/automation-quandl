# automation-quandl
Python automation framework 

## Selenium Setup
    In order to be able to run the web automation, we would need to install the drivers for the browsers needed
    
    * Firefox :
        Need to download the geckodriver:
            1. go to https://github.com/mozilla/geckodriver/releases
            2. Find your platform ( windows, linux ... etc) and download the relevant zip file
            3. extract the zip file
            4. copy the geckodriver to a different folder. Ensure that folder is in the path so that windows, 
                linux, OSX can find and execute it
        
        

## Installation
    * [Linux](###Linux)
    * [Windows](###Windows)
    
    ###Linux
    
        * Requirements:
            * Python 3 installed
            * Pip package managed installed (for debian : sudo apt install python3-pip )
            
        *Steps:     
            1. Clone git: git clone https://github.com/aelnahas/automation-quandl.git
            2. cd ./automation-quandl
            3. install packages :
                a. Globally: sudo pip3 install -r ./requirements
                b. Make a virtual env using python 3, then pip3 install -r ./requirements
            4. add path to the PYTHONPATH: export PYTHONPATH=$(pwd)
            5. run the test pytest ./tests
        
    ###Windows
        * Requirements:
            * Python 3 installed
            * Python 3 added to path
            * Pip package installed for python 3
            
        * Steps:
            1. Clone git: git clone https://github.com/aelnahas/automation-quandl.git
                alternatively download the zip file and extract it to a folder
            2. Open a command prompt
            3. change into the folder with the automation
            4. pip3 install -r ./requirements.txt
            5. Add folder to the PYTHONPATH, set PYTHONPATH=
            
        
            
    
## running the tests
    1. From the root folder of the automation directory:
        pytest ./tests
