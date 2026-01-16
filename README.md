Title: GreenGhar
This is a necessary file for our hardware hackathon project on Modern Agriculture theme.
The txt file is an arduino uno and py file is a python file.
Python file is used to add voice control system to out project.
You need python 3.12 version to use this feature.
After installing python 3.12 version, run these commands in Powershell to install necessary modules.
py -3.12 --version (to check if it is installed correctly)
cd D:\GreenGhar (go to your project folder like this)
py -3.12 -m venv .venv (to create a virtual environment)
.venv\Scripts\Activate (to activate the virtual environment)
Your terminal will change to: (.venv) PS C:\Users\...
pip install requests pyttsx3 SpeechRecognition numpy sounddevice (to install all required python modules)
python breakbad.py (to run voice control program)
(Or just run) py -3.12 breakbad.py (after opening powershell in that folder)
use ctrl+c to stop voice control
