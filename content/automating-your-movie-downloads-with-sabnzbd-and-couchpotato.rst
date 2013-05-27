Automating Your Movie Downloads with SABnzbd+ and CouchPotato
#############################################################
:date: 2011-02-16 20:37
:author: chris
:category: Tutorials
:slug: automating-your-movie-downloads-with-sabnzbd-and-couchpotato

Now that you're set up to automatically download TV shows with `SABnzbd+
and Sick Beard`_ (and if you're not, you should go back to that post and
set that up), it is time to upgrade a bit and automatically download
movies as well. `CouchPotato`_ is a relatively new web application that
is essentially Sick Beard for movies. In my opinion, the combination of
SABnzbd+, Sick Beard and CouchPotato is pretty close to perfect.

*Standard Disclaimer:* Your use of this software and configuration is at
your own risk. Check the legality of downloading movies in your area.
This post is purely for the sake of information.

Once again, this tutorial is for Ubuntu 10.04. It should work with any
major operating system. I assume you have followed the Sick Beard
tutorial, and consequently you should have Python, git, and SABnzbd+
installed and working at the very least.

Installing CouchPotato
~~~~~~~~~~~~~~~~~~~~~~

Let's start by downloading CouchPotato:

``$ git clone https://github.com/RuudBurger/CouchPotato.git``

Now, we simply run it:

``$ cd CouchPotato && python CouchPotato.py -d``

That's it, really. In your web browser, go to http://<server IP>:5000.
If you're running this on your local machine, it will automatically open
the page for you.

Configuration
~~~~~~~~~~~~~

Configuring CouchPotato is fairly straightforward and pretty similar to
that of Sick Beard. Start by clicking the little gear icon on the top
bar and then clicking "General." Everything in this tab is relatively
self-explanatory and can be left alone or customized to your liking.

Next up are the "NZBs/Torrents" and "Providers" tabs. Fill these in just
like the equivalent in Sick Beard, but make sure the category field is
not set to "tvshows" (of course, I recommend "movies").

You can leave "Qualities" alone for now. I'd suggest playing around with
it at some point to fit your preferences. I do recommend eventually
creating a custom quality. I would have two separate qualities set to go
through, in order, R5, DVDrip, and then either 720p or 1080p. This means
that it will look for each of these and download the best one available
at the time. It will then continue to look for the other qualities as
well. When it reaches 720p or 1080p, it will stop.

The "Renaming" tab is like Sick Beard's SABnzbd+ script, except it works
by watching the download directory instead of having SABnzbd+ execute a
script upon completion. Set the Download field to wherever SABnzbd+
places completed downloads (by default, *~/Downloads/Usenet/movies*) and
the destination field to wherever you keep your movies. It is important
that these *not* be the same location. This will not rename in place, so
if you're looking for that, you need a different solution. I would also
check the cleanup box.

The "Extras" tab contains a few optional features that could be
interesting. If you're not using XBMC, I don't see much point to
enabling these options. Of course, if you want subtitles in your
language, you should enable that option.

The "Userscript" tab installs a Chrome or Firefox script that allows you
to add movies to CouchPotato while browsing IMDb and the like with the
click of a button. CouchPotato is now fully configured!

Running CouchPotato at boot
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Much like Sick Beard, CouchPotato comes with an init script. So, copy
that to */etc/init.d/couchpotato*:

``$ sudo cp initd /etc/init.d/couchpotato``

And edit it so it looks something like this:

.. code-block:: initd

	*snip* 
	############### EDIT ME ################## 
	# path to app 
	APP_PATH=/home/chris/CouchPotato 
	# path to python bin 
	DAEMON=/usr/bin/python 
	# startup args
	DAEMON_OPTS=" CouchPotato.py -q" 
	# script name 
	NAME=couchpotato 
	# app name 
	DESC=CouchPotato 
	# user 
	RUN_AS=chris 
	PID_FILE=/var/run/couchpotato.pid 
	############### END EDIT ME ################## 
	*snip*

Now mark it as executable and run it:

.. code-block:: none

	$ sudo chown root.root /etc/init.d/couchpotato 
	$ sudo chmod 755 /etc/init.d/couchpotato 
	$ sudo update-rc.d couchpotato defaults 
	$ sudo invoke-rc.d couchpotato start


LaunchDaemon for Mac OS
~~~~~~~~~~~~~~~~~~~~~~~

A commenter posted this LaunchDaemon file for Mac OS users as an
adaptation of the one from Sick Beard. The file content has been moved
here so it can be formatted properly. To use this, place the file in
your user account's "Library/LaunchAgents" folder:

.. code-block:: launchd

	<?xml version="1.0" encoding="UTF-8"?>
	<!DOCTYPE plist PUBLIC "-//Apple Computer//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
	<plist version="1.0">
		<dict>
			<key>Label</key>
			<string>com.couchpotato.agent</string>
			<key>OnDemand</key>
			<false/>
			<key>ProgramArguments</key>
			<array>
				<string>python</string>
				<string>/Users/yourusername/CouchPotato/CouchPotato.py</string>
			</array>
			<key>RunAtLoad</key>
			<true/>
			<key>WorkingDirectory</key>
			<string>/Users/yourusername/CouchPotato/</string>
			<key>ServiceDescription</key>
			<string>CouchPotato</string>
		</dict>
	</plist>

.. _SABnzbd+ and Sick Beard: automating-your-tv-downloads-with-sabnzbd-and-sick-beard.html
.. _CouchPotato: http://couchpotatoapp.com/
