                __                      __                                          
         _____ / /_ _____ __  __ _____ / /_ __  __ _____ ___         ____ ___   ___ 
        / ___// __// ___// / / // ___// __// / / // ___// _ \       / __ `__ \ / _ \
       (__  )/ /_ / /   / /_/ // /__ / /_ / /_/ // /   /  __/      / / / / / //  __/
      /____/ \__//_/    \__,_/ \___/ \__/ \__,_//_/    \___/______/_/ /_/ /_/ \___/ 
                                                           /_____/                 
### Helping newbies and pros in creating a starting structure for projects involving python, following some of the general guidelines and principles widely used.  
  

## Table of Contents
- [Quick start](#quick-start)
- [Examples](#examples)
- [Author](#author)
- [Inspiration and background](#inspiration-and-background)
- [Copyright and license](#copyright-and-license)

## Quick start
Instalation:
- pip:  
    `pip install structure_me`
- github:  
    `git clone https://github.com/the-marcos/structure_me.git`



## Examples
1. Descriptive files: create folder/file structures with **django** like comments
on the files making it easier for new users to create their first programs.
  
`python structure_me <project_name>`

TODO: include tree s/s and files with description

2. Simple: create a simple folder/file structure. No comments.

`python structure_me --simple <project_name>`


## Author

**Marcos Paterson**
- <https://github.com/the-marcos>


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
- <https://dev.to/codemouse92/dead-simple-python-project-structure-and-imports-38c6>
- <https://github.com/yngvem/python-project-structure>


## Copyright and license

Code and documentation copyright 2020 [the-marcos](https://github.com/the-marcos). Code released under the [MIT License](https://github.com/the-marcos/structure_me/blob/master/LICENSE).