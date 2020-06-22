                __                      __                                          
         _____ / /_ _____ __  __ _____ / /_ __  __ _____ ___         ____ ___   ___ 
        / ___// __// ___// / / // ___// __// / / // ___// _ \       / __ `__ \ / _ \
       (__  )/ /_ / /   / /_/ // /__ / /_ / /_/ // /   /  __/      / / / / / //  __/
      /____/ \__//_/    \__,_/ \___/ \__/ \__,_//_/    \___/______/_/ /_/ /_/ \___/ 
                                                           /_____/                 
### Helping newbies and pros in creating a starting structure for python projects, following some of the general guidelines and principles widely used.  
  
  
## Table of Contents
- [Quick start](#quick-start)
- [Examples](#examples)
- [Author](#author)
- [Inspiration and background](#inspiration-and-background)
- [Copyright and license](#copyright-and-license)

## Quick start
### Instalation:
- pip:  
    `pip install structure_me`

### General Guidance
The usage should be rather straight forward. Following Django's default approach
and using setuptools to package your software, with the intent to hosting it in
pypi.
These are the steps I recommend:
1. Create a folder where you want to save your app or navigate to where you want it
to be saved. See the [Examples](#examples) section below for a sample tree of how 
your folder structure should look like after running the program.

2. run the script following the recipe described in the [Examples](#examples) 
section below.

3. I recommend using the --expressive argument as it will create files with descriptions
that are easy to follow along. If you know what you are doing, or feeling adventurous
be my guest to generate empty files and populating them yourselves.

4. start a local repo:
`$ git init`

4. Create a repository in github, with a .gitignore and LICENSE files. When you do
so, local and remote repos will be out of synch. Do the following to bring them
back to the same thread. In your command line:
`$ git add *`
`$ git commit -m 'initial commit message'`
`$ git remote add origin https://github.com/your-username/your-repo.git`
`$ git pull --allow-unrelated-histories origin master`
`$ git push origin master`

Your local and remote should now be in synch.

5. GO DEVELOP YOUR IDEAS!

6. Once you are ready to ship your software, ensure you have setuptools installed 
and follow along the instructions [here](https://packaging.python.org/guides/distributing-packages-using-setuptools/).

## Examples
Example usage can be checked by running:  
`$ structure_me -h`

There are two predefined ways of running this program:
  
1. Expressive files: create folder/file structures with **django** like comments
on the files making it easier for new users to create their first programs.
  
`$ structure_me -n <project_name> -e`

NOTE: as of version 1.7 the comments provided are not super comprehensive, 
but give a decent number of pointers on setup.py and README.md. Most of the work 
is still in your hands.

2. Simple: create a simple folder/file structure. No comments.

`$ structure_me -n <project_name>`

The resulting folder structure given a succesful execution will look like the 
following folder tree:  
```
project_name/ 
    ├── project_name/   
    │   ├── data/  
    │   ├── __init__.py  
    │   └── project_name.py  
    ├── tests/  
    │   └── tests.py    
    ├── README.MD  
    ├── setup.cfg
    └── setup.py  
```

## Author

**Marcos Paterson**
- <https://github.com/marcospaterson>


## Inspiration and background

In May 2020, while in the initial steps of learning django, I was amazed to
see how easy it was to create a new project/app, and that django had a functionality
that would create an entire folder structure and the baseline files with helpful
tips along the way.

Then started the search to find a similar package that would do just that. Create
a baseline/boiler plate folder and file structure, so I could dig into the core 
of the development, without worrying about having the structure around it.

I found none. That would fit my needs. Simple. Straight Forward. So here we go!
If by any chance you know of other more fitted alternatives, I'd love to hear about it.

Inspirations:
- <https://packaging.python.org/guides/distributing-packages-using-setuptools/>
- <https://github.com/yngvem/python-project-structure>
- <https://the-hitchhikers-guide-to-packaging.readthedocs.io>
- <https://python-packaging.readthedocs.io/en/latest/minimal.html>


## Copyright and license

Code and documentation copyright 2020 [Marcos Paterson](https://github.com/marcospaterson). 
Code released under the [MIT License](https://github.com/marcospaterson/structure_me/blob/master/LICENSE).
