Title: Deploy a pelican project on Ubuntu/Debian development environment
Date: 2017-01-21 16:00
Category: web,Programming
Tags: Python, Pelican
Author: Jianming

I just switched the template of this blog site, changed the url, made the changes on url of vfxware.com, will online a whole new home page, so that this blog will be only a part of the new site system.

As a note, I put how to setup pelican here, after 2 years using this static blog system, I still think it is one of the best option.

To setup the pelican project,

1. Install openssl

	:::sh
	sudo apt-get install libssl-dev

2. Update pip

	:::sh
	sudo pip install --upgrade pip

3. Install fabric and bs4

	:::sh
	sudo pip install fabric bs4

4. Install pelican and other dependencies
	
	:::sh
	sudo pip install pelican Markdown typogrify

5. Check out or git clone the pelican themes and plugins

	:::sh
	git clone <the custom theme>

for plugins:
	:::sh
	git clone https://github.com/getpelican/pelican-plugins.git

6. install theme like

	:::sh
	sudo pelican-themes -i <the custom theme path>

7. Checkout your pelican website code, and use fab build to check if the pelican code can run

	:::sh
	git clone <your pelican website repo>
	cd <your pelican website repo folder>
	fab build

Tips:

# `fab publish` to send it remotely to the web server, the configuration is in the publishconf.py file.
# To check the detail installation instruction, please refer to the [official doc](http://docs.getpelican.com/en/stable/)

Note: 
### `Markdown` must be installed to properly scan the md files.
