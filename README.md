# rasa_nlu-chatbot
This is a chatbot for controlling iot devices by rasa_nlu and python integration 
I am using Python 3.7.7 installed in a virtual environment of a MAC operating system. It is recommended to install it in a clean virtual environment as the there are quite a number of python modules to be installed.

### step 1
__installing rasa__

$pip install rasa

### step 2
__make a directory__

$mkdir rasa_chatbot

**change into that directory**

$cd rasa_chatbot

 ### Step 3
 **initializing rasa project in the directory** 
 
 $rasa init --no-prompt


**You will be able to see training process for both nlu and core using the default data. The following files will be created:**

__init__.py: An empty file that helps python find your actions. 

 actions.py: Code for your custom actions
 
config.yml: Configuration of your NLU and Core models

credentials.yml: Details for connecting to other services data/nlu.md: Your NLU training data

data/stories.md: Your stories

domain.yml: Your assistant’s domain

endpoints.yml: Details for connecting to endpoint channels

models/<timestamp>.tar.gz: Your initial model. Timestamp is in the format of YYYYMMDD-hhmmss. NLU-only models will have nlu prefix at the front.

### Step 4
**Data Preparation**

If you would like to train it using your own custom data, you can prepare it in either markdown or json format.

[I'm a relative reference to a repository file](data/nlu.json)





