# Creating Folders Automatically
--------
##### Simply Python script that creating as many folders and one file with text in it, as we want.

I wrote it, because I need create bunch of folder with same file for course on Udemy. So it's creating folder one by one with "special name". In that case is number of folder. You can change and modify code like you want for your purpose. 
Also it's create one-line text in file. In that case is it "# LAB {} -". 
It happend, thanks to this line:
    f.write("# LAB {} -".format(i+1))

Here is an example structure of folder, file and the text in it:
![alt text][logo]
[logo]:

To run this script use command-line, powerShell etc. Run your command-line, go to folder with script then write:
python mkdir.py

Ofcourse before first of all you need to clone or download repository to you local computer. You can do it by typing in console:
git clone ...
