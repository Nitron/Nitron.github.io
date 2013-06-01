Automating your TV show downloads with SABnzbd+ and Sick Beard Part 2: Mac OS X
###############################################################################
:date: 2010-09-02 13:21
:category: Tutorials
:slug: automating-your-tv-show-downloads-with-sabnzbd-and-sick-beard-part-2-mac-os-x
:alias: /2010/09/automating-your-tv-show-downloads-with-sabnzbd-and-sick-beard-part-2-mac-os-x/

In my previous post, `Automating your TV downloads with SABnzbd+ and
Sick Beard`_, we installed a system for automatically downloading TV
shows from Usenet. The post was written specifically for Ubuntu, so now
we will modify it for Mac OS X. The differences are fairly minor: we
can't use apt-get nor the rc.d system. So instead, we'll install the OS
X binaries and use Apple's `launchd`_ to run as a daemon.

Installing SABnzbd+ and git
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Instead of using aptitude to install SABnzbd+ and git, we'll use
pre-built binaries. So, download:

#. `SABnzbd+ Mac OS X Binary`_
#. `git-osx-installer`_

*Note:* These links go directly to the latest versions as of this
writing. I would advise checking the `SABnzbd+`_ and
`git-osx-installer <http://code.google.com/p/git-osx-installer/>`__
homepages for the latest versions.

Once those are downloaded, install them like any other Mac application.
Now you can run and configure SABnzbd+ just like in the previous post,
and use git to obtain Sick Beard.

Daemonizing SABnzbd+ and Sick Beard
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

With Ubuntu, we use the rc.d system to run at boot and daemonize. Mac OS
X does not have that system, but Apple did design a new system that they
have proposed as a standard. As far as I know, it is only used on OS X
for now, though. launchd is actually a replacement for init, xinet.d and
a few other related systems.

To set launchd to run SABnzbd+ and Sick Beard at boot, you place a file
for each daemon in *~/Library/LaunchAgents*, */Library/LaunchAgents* or
*/Library/LaunchDaemons*. The files are in an XML document whose rules
are defined by Apple. They tell launchd how to find your application and
how it should be daemonized and managed. You can find more information
on the files within the `launchd.plist man page`_.

First, a small decision must be made: where to place the plist files.
There are three options and two of them are very similar. The first
decision is whether or not to start the daemon when a user logs in or as
part of the system boot. Since I use a headless server, I prefer to
place the files in */Library/LaunchDaemons* so that I don't have to use
VNC to log in after boot. If you don't have root access then you really
only have one option: *~/Library/LaunchAgents*. The final option,
*/Library/LaunchAgents* does not seem terribly practical to me, as it
could easily lead to problems with multiple instances running at once.

So, here is an example launchd plist file for running SABnzbd+ as a
daemon:

.. code-block:: none

	<?xml version="1.0" encoding="UTF-8"?>
	<!DOCTYPE plist PUBLIC "-//Apple Computer//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
	<plist version="1.0">
		<dict>
			<key>Label</key>
			<string>net.christopher-williams.sabnzbd</string>
			<key>OnDemand</key>
			<false/>
			<key>ProgramArguments</key>
			<array>
				<string>/Applications/SABnzbd.app/Contents/MacOS/SABnzbd</string>
			</array>
			<key>RunAtLoad</key>
			<true/>
			<key>UserName</key>
			<string>chris</string>
			<key>WorkingDirectory</key>
			<string>/Users/chris/</string>
			<key>ServiceDescription</key>
			<string>SABnzbd+</string>
		</dict>
	</plist>


The format of plist files is out of the scope of this post, but you can
find more information in the `plist man page`_. The important bits here
are:

#. *Label*: This should match the filename (minus the *.plist*
   extension) and be in reverse-DNS notation (also known as a `Uniform
   Type Identifier`_). You can keep the label and filename as they are,
   but if you change one, you must change the other.
#. *ProgramArguments*: This tells launchd how to find your application
   and what arguments it should have. In this case, we're opening the
   actual executable within the application bundle. If you installed
   SABnzbd+ into /Applications (like you probably should), the path
   given is correct.
#. *UserName*: This is the username that the daemon will run as. This
   should probably be your username (the short version). If you created
   a dedicated user for SABnzbd+ and Sick Beard, use its username.
#. *WorkingDirectory*: This is the path from which the daemon runs. I
   don't think it's important for SABnzbd+, but it doesn't hurt to
   include it anyway.

And here is an example for Sick Beard:

.. code-block:: none

	<?xml version="1.0" encoding="UTF-8"?>
	<!DOCTYPE plist PUBLIC "-//Apple Computer//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
	<plist version="1.0">
		<dict>
			<key>Label</key>
			<string>net.christopher-williams.sickbeard</string>
			<key>OnDemand</key>
			<false/>
			<key>ProgramArguments</key>
			<array>
				<string>python</string>
				<string>/Users/chris/Sick-Beard/SickBeard.py</string>
			</array>
			<key>RunAtLoad</key>
			<true/>
			<key>WorkingDirectory</key>
			<string>/Users/chris/Sick-Beard/</string>
			<key>ServiceDescription</key>
			<string>Sick-Beard</string>
		</dict>
	</plist>


You will again have to change some paths around (unless your username is
the same as mine and your Sick-Beard directory is in your home
directory, of course).

I recommend putting both of these in */Library/LaunchDaemons* unless you
have a good reason to put them elsewhere. Once they are there, you can
start the daemons with the `launchctl`_ command:

``$ launchctl load /Library/LaunchDaemons/net.christopher-williams.sabnzbd.plist``

and

``$ launchctl load /Library/LaunchDaemons/net.christopher-williams.sickbeard.plist``

Now they should both be running, and probably opened their respective
pages for you automatically. You can tell Sick Beard not to do this in
the General configuration tab. To my knowledge, there is no way to
prevent SABnzbd+ from doing this without patching it.

There is one important note to keep in mind: launchd will keep the
processes alive. If SABnzbd+ crashes, you kill the process or tell it to
shut itself down, launchd will restart it. If you want to terminate it
for some reason, you will have to run:

``$ launchctl unload /Library/LaunchDaemons/net.christhoper-williams.sabnzbd.plist``

Wrapping it up
~~~~~~~~~~~~~~

So now you should have a working system for automatically downloading TV
shows and it should be running on your Mac. Enjoy!

Next: `Automating Your Movie Downloads with SABnzbd+ and CouchPotato`_

.. _Automating your TV downloads with SABnzbd+ and Sick Beard: http://christopher-williams.net/2010/08/automating-your-tv-downloads-with-sabnzbd-and-sick-beard/
.. _launchd: http://developer.apple.com/macosx/launchd.html
.. _SABnzbd+ Mac OS X Binary: http://sourceforge.net/projects/sabnzbdplus/files/sabnzbdplus/sabnzbd-0.5.4/SABnzbd-0.5.4-osx.dmg/download
.. _git-osx-installer: http://code.google.com/p/git-osx-installer/downloads/detail?name=git-1.7.2.2-intel-leopard.dmg&can=3&q=&sort=-uploaded
.. _SABnzbd+: http://sabnzbd.org/
.. _launchd.plist man page: http://developer.apple.com/documentation/Darwin/Reference/ManPages/man5/launchd.plist.5.html
.. _plist man page: http://developer.apple.com/mac/library/documentation/Darwin/Reference/ManPages/man5/plist.5.html#//apple_ref/doc/man/5/plist
.. _Uniform Type Identifier: http://en.wikipedia.org/wiki/Uniform_Type_Identifier
.. _launchctl: http://developer.apple.com/mac/library/documentation/Darwin/Reference/ManPages/man1/launchctl.1.html
.. _Automating Your Movie Downloads with SABnzbd+ and CouchPotato: http://christopher-williams.net/2011/02/automating-your-movie-downloads-with-sabnzbd-and-couchpotato/
