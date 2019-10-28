# Creating Folders Automatically

#### Simply Python script that creating as many folders and one file with text in it, as we want.

I wrote it, because I needed create bunch of folders with file for course on Udemy. So it's creating folder one by one with "special name". In that case is number of folder. Also it's create one-line text in file. In that case is it "# LAB {number of file} -". 

-----

## Installation

First you have to clone or download repository to your local computer by running command like that in console:

<b> git clone https://github.com/Simply-man/Creating-folders-automatically.git </b>

If we cloned/downloaded repositry it's time to set out our path for folders. Fill "YOUR PATH" with path when you wan't your folders:
```python
path = r"YOUR PATH\#{} LAB".format(i+1)
```

Same for file in that folders:
```python
path_for_file = r"YOUR PATH\#{} LAB\lab {}.py".format(i+1, i+1)
```

That's it. You have corretly configurated script. Let's run it. Go to folder with your script by typing in commad-line:
<b>cd "YOUR PATH TO SCRIPT"</b>
then write:
<b>python mkdir.py</b>. 
Once you run it, it create as many folers as you want.

## Examples
Here is an example structure of folder, file and the text in it:
![alt text][logo]
[logo]:
