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

[my training data](data/nlu.json)

Markdown is arguably the safest choice for beginner to create the data. 
if your data is in markdown format ,you have to convert it into json format

$rasa data convert nlu --data data/nlu.md --out data/nlu.json -f json

--data is the path to the file or directory containing Rasa NLU data.

--out is the name of the file to save training data in Rasa format.

-f is the output format the training data should be converted into. Accepts either json or md.

### Step 5

**Training model**

To train the nlu model, you can just run the following command:

$rasa train nlu

**Testing model**

$rasa shell nlu

If you have multiple nlu models and would like to test a specific model, use the following command instead.

$rasa shell -m models/nlu-2020433___.tar.gz

### Step 6
**Running server**

Rasa also provides a way for you to start a nlu server which you can call via HTTP API. Run the following command (modify the name of the model accordingly):

$rasa run --enable-api -m models/nlu-2020___.tar.gz


### Step 7
**testing**
curl localhost:5005/model/parse -d '{"text":"turn on light"}'

**testing using python**
$ python reqtest.py

### Reference

[rasa](https://rasa.com/docs/rasa)



















