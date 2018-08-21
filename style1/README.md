Quick Considerations (to be updated)

1. userSetup.py file needs to be created in a default maya directory (for now, can be changed to network location or better place later)
2. userSetup file appends the rush python directory to the system path. 
3. The directory where userSetup.mel lives must be appended to the PYTHONPATH of the system in order for maya to find the rush tools directory. I put a script in /etc/profile.d/ directory that runs on startup. 
4. Scripts called in the shelfButton function can't have () at the end (have no idea why yet) 

ISSUE: 
1. Program builds and executes fine when copied and pasted into the built in maya interpreter. When put in maya's designated location for autoload on startup the shelf and buttons build, but return "syntax error" when clicked. 
