# ArcSight Integration with TheHive
And now, for the first time, you can send alerts via action from ArcSight ESM Console to the TheHive when Correlation Rules are triggered.


All actions taken on a SIEM to enhance its functionalities are in line with the goal of being able to send the alerts and results of all detected incidents centrally to an Incident Response platform. One of the best Incident Response platforms is the TheHive. As you know, Some Add-ons have already been developed to integrate TheHive with Splunk Enterprise, but there was no way to integrate TheHive with ArcSight ESM.
Here you can find a general and extensible script that can be used as an execution command in ArcSight ESM, you can send the results of the triggered correlation rules  to the TheHive platform in the form of an Alert.

--------------------



# Quick Start
In this section, a brief explanation of how to use and function of this script is provided.


## Pre-Requirements

#### Knowledge 
For using this python script you must be completely proficient in the functionality of the [ArcSight ESM](https://www.microfocus.com/en-us/cyberres/secops/arcsight-esm) Execution Command Resource and the structure of the CEF log format. 
Also, you must be familiar with the functionalities of the [TheHive](https://github.com/TheHive-Project) and [TheHive4Py](https://github.com/TheHive-Project/TheHive4py).

#### Creating Custom Fields
At the first, login to the ArcSight Console and Find the Rule resource that you want to add an action with the type of Command Execution. 
Related to the all fields of correlation events, you must add the Custom Fields in the Thehive.
All types of fields(string, boolean, integer, date) must be defined in the custom fields. 

#### Configuration the script file
Edit the sample-makealert.py file and put the IP address or Hostname of Thehive server. 
Also, put the API key
Insert all fields name of correlation events in the custom fields helper section.
Save and exit. 
Place the script file in the appropriate path on the ArcSight server. 

#### Add command execution as action
In the ArcSight Console, add an action as a command execution. 
Add below command
/usr/bin/python3 <Path_of_script_file>/makealert.py 
Add all fields name as a variable type in the parameter section. 
Save and Apply. 
