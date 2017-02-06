# automation-quandl
Python automation framework 

## Selenium Setup
    In order to be able to run the web automation, we would need to install the drivers for the browsers needed
    
    * Firefox :
        Need to download the geckodriver:
            1. go to https://github.com/mozilla/geckodriver/releases
            2. On the latest release , find your platform ( windows, linux ... etc) and download the relevant zip file
            3. extract the zip file
            4. copy the geckodriver to a different folder. Ensure that folder is in the path so that windows, 
                linux, OSX can find and execute it
        
        

## Automation Setup
    # Linux
    
        * Requirements:
            * Python 3 installed
            * Pip package manager installed (for debian : sudo apt install python3-pip )
            
        *Steps:     
            1. Clone git: git clone https://github.com/aelnahas/automation-quandl.git
            2. cd ./automation-quandl
            3. install packages sudo pip3 install -r ./requirements.txt
            4. add path to the PYTHONPATH: export PYTHONPATH=$(pwd)
        
    # Windows
        * Requirements:
            * Python 3 installed:
                1. go to : https://www.python.org/downloads/release/python-360/
                2. Scroll to the bottom where there is a list of files
                3. For windows download: Windows x86-64 executable installer   for 64 bit version   
                4. Run the executable file.
                5. On the screen asking you to Install Now or Customize installation, make sure
                    to check the box next to "Add Python 3.6 to PATH"
            * Click on Install Now, Allow the process to finish
            
        * Steps:
            1. Clone git: git clone https://github.com/aelnahas/automation-quandl.git
            2. Open a command prompt
            3. cd into automation-quandl
            4. pip3 install -r ./requirements.txt ( if it complain because of administration rights,
                  then you need to open the command prompt in admin mode )
            5. Add folder to the PYTHONPATH, set PYTHONPATH=%cd%
            
    
## running the tests
    1. From the root folder of the automation directory:
        pytest ./tests --html=report.html --self-contained-html
        
    2. The above command should generate an html log the can be viewed on a browser.
