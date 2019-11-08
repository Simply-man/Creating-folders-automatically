# Creating Folders Automatically
Simply Python script that creating as many folders and one file with text in it, as we want.

## Why I wrote it?
I wrote it, because I needed create bunch of folders with file for course on Udemy. So it's creating folder one by one with "special name". In that case it is number of folder. Also it's create one-line text in file. Text: <b>"# LAB {number of file}"</b>. 

## Installation

First you have to clone or download repository to your local computer by running command like that in console:

```git 
git clone https://github.com/Simply-man/Creating-folders-automatically.git 
```

If we cloned/downloaded repositry it's time to set out our path for folders. Fill "YOUR PATH" with path where you wan't your folders:
```python
path = r"YOUR PATH\#{} LAB".format(i+1)
```

Same for file in that folders:
```python
path_for_file = r"YOUR PATH\#{} LAB\lab {}.py".format(i+1, i+1)
```

That's it. You have corretly configurated script. Let's run it. 

## Usage

Go to folder with your script by typing in commad-line:
```
cd "YOUR PATH TO FILE SCRIPT"
```
then write:
```
python mkdir.py
``` 
When script is running, specify number of folders to create.
Once you run it, it create as many folers as you want.

## Examples

##### Correctly working script:
![wroking script](https://user-images.githubusercontent.com/38534681/67718046-40aae980-f9cf-11e9-873f-3ee0bffec321.png)

##### Here is an example structure of folder, file and the text in it:

  - ##### Structure:
    ![structure folder](https://user-images.githubusercontent.com/38534681/67717814-bb273980-f9ce-11e9-8de6-c69752aa9fff.png)

  - ##### Filled file:
    ![lab1](https://user-images.githubusercontent.com/38534681/67718236-a008f980-f9cf-11e9-90fe-7df61310a4d9.png)
