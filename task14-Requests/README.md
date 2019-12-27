## Introduction

> McSkidy has been going keeping inventory of all the infrastructure but he finds a random web server running on port 3000. All he receives when accessing '/' is

`{"value":"s","next":"f"}`

> McSkidy needs to access the next page at /f(which is the value received from the data above) and keep track of the value at each step(in this case 's'). McSkidy needs to do this until the 'value' and 'next' data have the value equal to 'end'.

> You can access the machines at the following IP:

>    10.10.241.214  
>    10.10.112.87

> Things to note about this challenge:

+	The JSON object retrieved will need to be converted from unicode to ASCII(as shown in the supporting material)
+	All the values retrieved until the 'end' will be the flag(end is not included in the flag)

> [Read the supporting materials here](./Supporting_Doc.pdf).

## Questions

> 1) What is the value of the flag?

td:lr Answer: **sCrIPtKiDd**


===============================================================================

We can either do :  
1. manual traversing of the URL to get the value of the flag, OR  
2. trying a Python script which is the focus of the exercise here.

[Python3 script](./findflag.py) here.



