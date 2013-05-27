Automating your TV downloads with SABnzbd+ and Sick Beard
#########################################################
:date: 2010-08-18 23:57
:category: Tutorials
:slug: automating-your-tv-downloads-with-sabnzbd-and-sick-beard

Why bother with a DVR when you can get your computer to automatically
download TV shows soon after they air? By using a few open-source tools
and a Usenet account (yeah, I know, don't talk about Usenet), you can
build such a system quite easily. Naturally, it works best in a home
server environment, but you can run it on your desktop or notebook as
well.

*Standard Disclaimer:* Your use of this software and configuration is at
your own risk. Check the legality of downloading TV shows in your area.
This post is purely for the sake of information.

This tutorial is for Ubuntu 10.04, but it should, with a little
tweaking, work on any major operating system. To get started, you will
need a few things:

Note: For some advice on getting this running on a Mac, see the
`followup post`_.

#. A computer - I would use a cheap, headless desktop that is always on
   and has lots of storage (colloquially known as a "home server").
   Again, this tutorial assumes that you're running Ubuntu, so adjust
   accordingly.
#. A Usenet provider - I won't go into this, given the rule about not
   talking about Usenet.
#. A few bits of open-source software: `SABnzbd+`_ and `Sick Beard`_

So, let's get started. I assume at this point that you have Ubuntu
installed, are somehow interfacing with it (whether that's directly over
SSH does not matter), and have a terminal open. I also assume you have
root access.

Step 1: Setting up SABnzbd+
~~~~~~~~~~~~~~~~~~~~~~~~~~~

First, we'll need to install a few packages. This command installs
SABnzbd+, a theme and the git version control system (we'll need this
later):

``$ sudo apt-get install sabnzbdplus sabnzbdplus-theme-smpl git-core``

From here, we will need to configure SABnzbd+. To do this, run
``$ sabnzbdplus`` and open http://<server IP>:8080 in your web browser.
If you're running this on your local machine, it will automatically open
the page for you.

Now follow the directions on the setup wizard. For more information on
the wizard options, visit the `SABnzbd+ Wiki`_.

Once you finish the wizard and SABnzbd+ restarts, you can go back to
your terminal and press Ctrl-C to close SABnzbd+. Now, as root, edit
*/etc/default/sabnzbdplus*, changing the options as appropriate. Here is
a cut-down version:

.. code-block:: none

	USER=chris
	CONFIG=/home/chris/.sabnzbd/sabnzbd.ini
	HOST=0.0.0.0
	PORT=8080
	EXTRAOPTS=


Now you can start SABnzbd+ as a daemon by running
``sudo invoke-rc.d sabnzbdplus start``. Let's open it up again in the
web browser and configure it a little more.

First, let's change the download directories. Click on "Config" and then
"General". The default setting for completed downloads is
~/downloads/complete, and the default for in-progress downloads is
~/downloads/incomplete. This looks messy to me, so I would change the
completed download folder to "Downloads/Usenet" and the temporary folder
to something like "Downloads/Usenet/.incomplete". This way, I wouldn't
have to see incomplete downloads, but I would have to remember to clear
it out every once in awhile.

On the same page, set the post-processing scripts folder. I would use
"/home/chris/.sabnzbd/scripts". This folder contains (or, will contain,
once you create it) scripts that are run when downloads are completed.
We'll use this later to have Sick Beard organize our episodes for us.
You may want to ``$ mkdir`` now so that you don't forget.

Step 2: Setting up Sick Beard
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

First, we're going to use git (which we installed at the beginning of
the tutorial) to download Sick Beard. So, let's download the latest code
from the repository:

``$ git clone http://github.com/midgetspy/Sick-Beard.git``

Once this command finishes, there will be a directory called Sick-Beard
which contains everything you need. Inside that directory, run:

``$ python SickBeard.py``

Much like SABnzbd+, Sick Beard is configured within the browser, so open
http://<server's IP>:8081 and then click "Config" and "General".
Configure this as you see fit. When you're done, move onto the "Episode
Downloads" subtab.

Again, configure this as you see fit. You will have to play around with
the search frequency until you find a balance between performance and
fast downloads. You will definitely want to change "NZB Action" to
"SABnzbd" so that Sick Beard uses the SABnzbd+ API to queue downloads
instead of dumping NZB files into a folder. Of course, fill in your
SABnzbd+ information in the lower-left pane of the page. You can find
the API key in the SABnzbd+ configuration on the General page. For the
category, enter "tv" and for the IP and port, "127.0.0.1:8080". I would
leave "Keep folder" checked for now and disable it later. "Rename
episodes" should remain checked. "Scan & Process TV Download Dir" should
*not* be checked.

Next up, search providers. This is how Sick Beard will find NZBs, so you
want to make sure to get this right. I would start by picking one or two
of the supported search providers and creating an account with them. You
can get your UID and hash from the RSS feed URLs at the search provider.
You can safely ignore the "Notifications" subtab for now.

While we're at it, let's make Sick Beard run as a daemon as well. Go
back to your terminal and press Ctrl-C to close Sick Beard. In the
Sick-Beard directory:

``$ sudo cp initscript /etc/init.d/sickbeard``

Now edit */etc/init.d/sickbeard* (as root). It should look something
like this:

.. code-block:: none

	APP_PATH=/home/chris/Sick-Beard/
	DAEMON=/usr/bin/python
	DAEMON_OPTS=" SickBeard.py -q"
	NAME=sickbeard
	DESC=SickBeard
	RUN_AS=chris
	PID_FILE=/var/run/sickbeard.pid 
	# Lots of other stuff that you don't need to worry about


Now set it to run at boot and start the daemon:

`` $ sudo update-rc.d sickbeard defaults $ sudo invoke-rc.d sickbeard start``

Sick Beard should now be fully set-up!

Putting it all together
~~~~~~~~~~~~~~~~~~~~~~~

Now we'll integrate Sick Beard with SABnzbd+. First, we'll copy the
post-processing scripts into the right location (which we set up
earlier). In the Sick-Beard directory:

.. code-block:: none


	$ cp autoProcessTV/* /home/chris/.sabnzbd/scripts/
	$ cd /home/chris/.sabnzbd/scripts/
	$ rm hellaToSickBeard.py
	$ mv autoProcessTV.cfg.sample autoProcessTV.cfg


We copied all of the scripts into SABnzbd+'s scripts directory (which we
created earlier), removed one that is for a different Usenet downloader
and renamed the configuration sample. Now edit autoProcessTV.cfg, which
should look like this:

.. code-block:: none

	[SickBeard]
	host=localhost
	port=8081
	username=
	password=


Now we have just one configuration step remaining: telling SABnzbd+ to
use the sabToSickBeard.py script for downloads in the TV category. So,
open up SABnzbd+, go to "Config" and then "Categories". For the "tv"
category, change the script dropdown to "sabToSickBeard.py" and the
processing dropdown to "D" (this tells SABnzbd+ to repair broken files,
then extract, then delete the RAR files). Now click the "Save" button
next to the "tv" category.

Adding a show to Sick Beard
~~~~~~~~~~~~~~~~~~~~~~~~~~~

We can finally start using the system! Adding a new show to the system
is a little more unwieldy than I'd like, but it isn't *too* complicated.
The first step is to add a directory somewhere on your hard drive, and
the next step is to tell Sick Beard where to find it. So, let's pick a
show (say, Burn Notice) and create a directory for it:

``$ mkdir ~/Videos/TV\ Shows/Burn\ Notice/``

Now, on Sick Beard's home page, click "Add Shows" and then under "Add
Single Show", click Browse. Find the directory you just created and
click "Add Show". It'll search by name and give you a list of shows.
Pick the correct one and click Continue. The show will now appear in
your Show List and information will show up within a few minutes. When
an episode is posted to Usenet, Sick Beard will automatically download
it.

Now you have your own Usenet-powered DVR! For more information on
SABnzbd+ or Sick Beard, visit their websites at `sabnzbd.org`_ and
`sickbeard.com`_.

`Part Two: Getting it working on a Mac`_

Next: `Automating Your Movie Downloads with SABnzbd+ and CouchPotato`_

.. _followup post: automating-your-tv-show-downloads-with-sabnzbd-and-sick-beard-part-2-mac-os-x.html
.. _SABnzbd+: http://sabnzbd.org/
.. _Sick Beard: http://github.com/midgetspy/Sick-Beard
.. _SABnzbd+ Wiki: http://wiki.sabnzbd.org/quick-setup#toc9
.. _sabnzbd.org: http://sabnzbd.org/
.. _sickbeard.com: http://www.sickbeard.com/
.. _`Part Two: Getting it working on a Mac`: automating-your-tv-show-downloads-with-sabnzbd-and-sick-beard-part-2-mac-os-x.html
.. _Automating Your Movie Downloads with SABnzbd+ and CouchPotato: automating-your-movie-downloads-with-sabnzbd-and-couchpotato.html

