# imgconvert
An open source tool for image format conversion based on Python 3 

## Requirements
* Python 3.8.5 or later
* Pillow Library 7.2.0 or later

## Installation
Obtain the latest version of Python 3 (version 3.8.5 at the time of this writing) from official [website](https://www.python.org). Once downloaded, install Python on your machine.

### macOS and GNU/Linux
macOS and GNU/Linux users must verify the successful installation of Python 3.8.5 by running the following command in terminal.
```
$ python3 --version
```
<p align="center"> <img width="572px" height="auto" src="https://github.com/randomsdeveloper/imgconvert/blob/master/macOS-python-version.png"> </p>

After verifying Python 3 installation, **_upgrade pip_** and **_install Pillow_** using following commands.
```bash
$ python3 -m pip install --upgrade pip

$ python3 -m pip install Pillow
```
<p align="center"> <img width="572px" height="auto" src="https://github.com/randomsdeveloper/imgconvert/blob/master/macOS-pip-install.png"> </p>

### Windows
Microsoft Windows users must edit the Path Environment Variable with a new entry to their Python 3 install directory. This directory is generally ```C:\Users\<Username>\AppData\Local\Programs\Python```

<p align="center"> <img width="572px" height="auto" src="https://github.com/randomsdeveloper/imgconvert/blob/master/windows-env-variable.png"> </p>

For step by step instructions on **How to edit path environment variable**, follow this [article](https://www.architectryan.com/2018/08/31/how-to-change-environment-variables-on-windows-10/).

Once the environment variables are updated, check Python version using **Command Prompt** or **PowerShell**, by executing 
```
> python --version
```
Also, upgrade PIP with 
```
> python -m pip install --upgrade pip
``` 
and install Pillow by executing 
```
> python -m pip install Pillow
```
<p align="center"> <img width="572px" height="auto" src="https://github.com/randomsdeveloper/imgconvert/blob/master/win-py-ver-pip-pillow.png"> </p>

## Usage
Download the [imgconvert.py](https://github.com/randomsdeveloper/imgconvert/blob/master/imgconvert.py) file and place in the directory of choice, where it is easy to access the contents of directory in which image files are stored for conversion.

### macOS and GNU/Linux
Using **Terminal** or any other console, navigate to the directory containing [imgconvert.py](https://github.com/randomsdeveloper/imgconvert/blob/master/imgconvert.py) and invoke using python3 as following
```
$ python3 imgconvert.py
```
<p align="center"> <img width="572px" height="auto" src="https://github.com/randomsdeveloper/imgconvert/blob/master/macOS-file-convert.png"> </p>

To convert all the files of same type in a directory instead of a single file, pass the **directory name** when Path is asked. Options to choose the output file type and input file type will be prompted.

<p align="center"> <img width="572px" height="auto" src="https://github.com/randomsdeveloper/imgconvert/blob/master/macOS-directory-convert.png"> </p>

_**Note:** If single file is choosen to convert, the prompt only asks about output file type as it knows input file type already. However, in case of directory, it needs to know the output file type as well as input file type to select multiple files for conversion_

### Windows
Using **Command Prompt** or **PowerShell** or any other console, navigate to the directory containing [imgconvert.py](https://github.com/randomsdeveloper/imgconvert/blob/master/imgconvert.py) and invoke using python as following
```
> python imgconvert.py
```
<p align="center"> <img width="572px" height="auto" src="https://github.com/randomsdeveloper/imgconvert/blob/master/windows-img-convert.png"> </p>

To convert all the files of same type in a directory instead of a single file, pass the **directory name** when Path is asked. Options to choose the output file type and input file type will be prompted.

<p align="center"> <img width="572px" height="auto" src="https://github.com/randomsdeveloper/imgconvert/blob/master/windows-dir-convert.png"> </p>

_**Note:** If single file is choosen to convert, the prompt only asks about output file type as it knows input file type already. However, in case of directory, it needs to know the output file type as well as input file type to select multiple files for conversion_

# License
Contents of this repository are published under GNU General Public License version 2.0. You may copy and distribute verbatim copies of the Program's source code as you receive it.
