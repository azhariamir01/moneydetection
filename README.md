In order to run this application you need the following:
- Python >= 3.9
- PyCharm
- Git

The reason we use PyCharm is that it's an IDE that supports all the programming languages that we use for this 
application.  It supports JavaScript, HTML and CSS within the IDE, without needing additional frameworks or installations
outside the two mentioned above.

Repository link: 

In order to get the repository, please run the following command:
```
git clone
```
Or download the code as a .zip from the repository link and open it within PyCharm.

Then, create a virtual environment by running the following commands in the PyCharm terminal:

```
cd path/to/your/project
python -m venv MyVirtualEnvironment
MyVirtualEnvironment\Scripts\activate
```
Replace *MyVirtualEnvironment* with the desired name for the environment.

To install the requirements for the application run the following command:
```
pip install -r requirements.txt
```
In order to run the application, execute the following command:
```
python app.py
```
And click the link that can be seen in the logs of the terminal within the IDE. Example:
```
* Running on *link*
```
In order to stop the app from running, hit ```Ctrl+C``` in the PyCharm terminal.