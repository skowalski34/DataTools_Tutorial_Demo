# Auto-sklearn AutoML Installation instructions

Due to the nature of Auto-SKlearn, the package is not currently supported on Windows Machienes.
It is 2/18/2022, so it could be possible this has changed if you are viewing this in the future.
This being said, an installation guide for how to get this running on the HPCC is
included. If you are running macOS, you can possible just create the enviroment from
the `auto_sklearn_env.yaml` file in this folder. For Windows machienes, you recommened to run
this on the HPCC. If you have anaconda running on \*uniux on your machiene, you can use
that instead and just create the enviroment from the yaml file.

IF YOU ARE MACOS or LINUX USER:
Run the following in your terminal

```bash
conda env create --prefix ./envs --file auto_sklearn_env.yml
conda activate ./auto_sklearn_env
jupyter notebook
```

WINDOWS MACHIENES CONTINUE BELOW

## ANACONDA SET UP:

In order to run this example easily, it is suggested that Anaconda 3 with python 
is used. With using Anaconda, since many python pacakges are already installed 
and conda is pre-installed, the setup will be less intensive.

If you already have Anaconda 3 with python, you can skip
to Virtual Enviroment Setup.

Below are instructions on how to install Anaconda 3 with python version 3.9 on
the HPCC. We will also set up a new virtual enviroment with the packages we 
will need to install to get our example working. Please note this would probably
work best if you can keep this README.md open and also have access to a terminal
in another window.

### INSTALL Anaconda 3 w/ Python 3.9 on HPCC:

The following was created on 2/18/2022. It is possbile at the time you are reading
this the Anaconda version has updated. If this is the case, visit [Anconda's website](https://www.anaconda.com/products/individual#:~:text=environments%2C%20and%20packages.-,Anaconda%20Installers,-Windows)
and use the link to the newest Anconda version in place of the link below. Note you
can find the download link by going to the Anaconda Website. Finding where you can 
download Anaconda. You will see there is a linux option something like 
"64-Bit (x86) Installer (XXX MB)". Right click on this and copy the link it directs
you to (do not actually follow the link). This will be the link you change in the `curl` command below. Also
make sure to change the `bash` command to run the appropiate script. You can easily
see what this by looking at the end of the link. In this case it is 
`Anaconda3-2021.11-Linux-x86_64.sh`

You will need access to the HPCC. If this is Spring 2022, you will have access to the
HPCC if you apart of CMSE 495. If this is not Spring 2022, check with your Instructor
to see if you have access to the HPCC.

To access HPCC visit [this site](https://icer.msu.edu/web-portal-hpcc-resources) and click on the link to OnDemand.
Once logged in, find the tab on top that says something like "Devleopment Node".
Click on this tab, and select any development node. You now will have access to a shell
and can run the following commands.

1. In your home directory (~), or wherever you would like,
you will want to download the installation script from Anaconda's website. 
This can easily be done with this command.

```bash
curl -O https://repo.anaconda.com/archive/Anaconda3-2021.11-Linux-x86_64.sh
```

2. Next we need to run the installation script. To do this makes sure you are
in the same directory as the file we just downloaded. Then run the following.

```bash
bash Anaconda3-2021.11-Linux-x86_64.sh
```

3. The installation process will ask you a few things

4. Read through the License agreement by pressing/holding `ENTER`

5. Type "yes" to accept the terms

6. You will then be asked where you would like to install anaconda 3. 
Press "Enter" to save it in `~/anaconda3`, or if you have another location 
you would like to save it, you can enter this here. But note this guide 
assumes this is installed in the home directory. You may neeed to modify 
directions later based on where you save anaconda3.

7. Once finished installing, it will ask if you would like the installer to 
initalize Anaconda3. In order to allow for the most future flexibility.
You will type "No". (You can say "yes", however, when you need to run different
versions of anaconda. You will need to comment out the "conda initalize" commands that are
placed in your `~/.bashrc`)

8. Now we will need to activate our Anaconda with running

```bash
module load Anaconda/3
```

9. You can now delete or move the `Anaconda3-2021.11-Linux-x86_64.sh` file to 
wherever you would like.

10. You can test that the installation worked properly if the following command 
returns `conda 4.10.3` or something equivalent.

```bash
conda --version
```

### Virtual Enviroment Setup: 

From the last section, make sure you Anaconda 3 is active (Make sure you have ran `module load Anaconda/3` prior)

```bash
conda --version
```
If a version number was given you are good to go.

We will now create the enviroment, and set ourselves up to launch a Jupyter Notebook.

**Load the Enviroment from the yml file**

Loading the enviroment yaml file allows you to use the same exact enviroment we used to 
run the code

1. In the terminal navigate to the same folder this README.md is in 
(`/Auto-SKLearn_AutoML`).

2. You can create the enviroment from the `auto_sklearn_env.yml` file with
```bash
conda env create -f auto_sklearn_env.yml
```

**Launching Jupyter Notebook with auto_sklearn_env**

We can start a "Jupyter Notebook Interactive App" on OnDemand to access our
Jupyter Notebook and using settings we can tell it to use the appropiate enviroment.

1. Open up Ondemand and find the "Interactive Apps" tab and click on "Jupyter Notebook"

There is a list of setting to change, here is what we put, but you can change hours/cores/memory/advanced
setings as needed.

* Number of hours: 2
* Number of cores per task: 1
* Amount of memory: 5gb
* CHECK: Launch Jupyter Notebook using the Anaconda installation in my home directory
* Anaconda Path: anaconda3
* Conda Environment: auto_sklearn_env

2. Now click launch. Wait for the the job to make it through the "Queued". Then it should say
"Starting". It should take less than 3 min to start. If you are waiting anylonger please make
sure you followed the above steps exactly. If successful, it should now say "Running". There
will be a Blue button that says "Connect to Jupyter". Click that and you will have successfully
launched Jupyter Notebooks with our enviroment that has Auto-sklearn pre-installed!

3. Navigate to this repository and run our examples.

**Notes**

In the future you would like to delete the enviroment you can use
```bash
conda env remove -n auto_sklearn_env
```

Also if you are interest in using Jupyter Notebooks Interactive App on OnDemand in
general and want to use the "base" anaconda. You can change "Conda Environment"
in the settings to be "base".


## (OPTIONAL) GPU Setup

In order to take full advantage of GPU with Auto-SKlean, it is suggested to use a
developer node with GPU access (`dev-intel16-k80`,
`dev-amd20-v100` ---- Note that `dev-intel14-k20` most likely not work with this
example). This can be set with the Jupyter Notebook Interactive App setting in the 
Advanced Options. Set "Node Type" to `intel16` or `intel14` and change 
"Number of GPUs" to 1 or more.

(Optional if GPU does not work, with just the settings above)
We need to load the appropiate modules for use of CUDA. In your `~/.bashrc`
add the following commands to the end of the file.

```bash
module load GCC/8.3.0
module load CUDA/10.2.89
```
