# Programs creating as many folders as we wish with file in it
import os


# Answering function about numbers of folders and files. Function will keep asking until we set number not text
def question():
    run = True
    while run:
        try:
            question = int(input("How many folders would you like create?"))
        except ValueError:
            print("Please set the number not text.")
        except Exception as e:
            print("ERROR!\nDetails:{}".format(e))
        else:
            return question


# Function creating number of folders and files in it defined by user
def mkdir(end):
    count = 0
    rest = 0

    for i in range(end):
        # Path for create folder with special name
        path = r"YOUR PATH\#{} LAB".format(i+1)
        # Path for create file in folder also with special name
        path_for_file = r"YOUR PATH\#{} LAB\lab {}.py".format(i+1, i+1)
        try:
            os.mkdir(path)
            with open(path_for_file, "w") as f:
                f.write("# LAB {} -".format(i+1))
            count += 1
            print(path_for_file, "--> Created successfully!")
        except FileExistsError:
            print(path_for_file, "--> Exists! Remove directory or ignore this message.")
            rest += 1
        except Exception as e:
            print("ERROR!\nDetails: {}".format(e))

    return count, rest


# Running ours functions and checking how many folders were created and not created
if __name__ == '__main__':
    num = question()
    counted = mkdir(num)
    # counted[0] --> reference to first returning object from mkdir function
    if counted[0] == num:
        print("All directory and files created successfully!")
    else:
        print("INFO: {} directories exists and {} were created correctly.".format(counted[1], counted[0]))
