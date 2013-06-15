Building a "Secure" Dedicated Privacy Laptop
############################################
:date: 2013-06-15 14:45
:author: chris
:category: Tutorials
:slug: dedicated-privacy-laptop

Given the recent news of NSA collection of call and email (meta)data, it might
not be a bad idea to have a dedicated "secure communications" machine. I originally
built the machine several months ago for monitoring "hacker" forums on the Tor network
so that exposure of my primary machine (and thus, identity) wouldn't be a problem 
while exploring the deeper parts of the Internet. 

It's important to note that the technology is only one tiny piece of online privacy. 
All of the cryptography in the world won't protect you if you tell someone untrustworthy
all about your secret activities. `The Grugq`_ has posted a number of excellent essays on
the topic of operational security (OpSec), as well as a must-watch conference talk on 
`OpSec for Hackers`_. In short: Be smart and keep your mouth shut.

That said, having some technology can help out quite a bit. The Tor network provides some
element of anonymity, and end-to-end message-level encryption such as `GPG`_ and `OTR`_ allow
for secure communications against *most* adversaries. So, the technology won't save you from
the NSA, but that doesn't mean it isn't useful, as long as you know the limitations.

So, let's get started. Our goals are as follows:

#. Connect anonymously to the Internet via Tor using The Grugq's `PORTAL`_ modification for `OpenWRT`_.
#. If the host machine is compromised, it should not be possible to determine a physical location
   or an identity.
#. Utilize full-disk-encryption (FDE) with two-factor authentication.
#. Have some combination of GPG/Torchat/Jabber+OTR/Bitmessage ready to go.

And an equipment list:

#. Clean laptop -- Preferably brand new and never been connected to your network.
#. `TP-LINK WR703N`_ -- Pre-modded with additional Flash ROM and RAM.
#. A supported USB wireless adapter -- I like the `Alfa AWUSO36NH`_ (Disclosure: Referral link).
#. A `Yubikey`_ -- I'm using the standard model, but the other models allow for other configurations
   that could be better.
#. A flash drive for installing Linux.

PORTAL Installation
~~~~~~~~~~~~~~~~~~~

Arch Linux Installation
~~~~~~~~~~~~~~~~~~~~~~~

Setting Up The Environment
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _The Grugq: http://grugq.github.io
.. _OpSec for Hackers: http://www.youtube.com/watch?v=9XaYdCdwiWU
.. _GPG: http://gnupg.org/
.. _OTR: http://www.cypherpunks.ca/otr/
.. _PORTAL: https://github.com/grugq/portal
.. _OpenWRT: https://openwrt.org/
.. _TP-LINK WR703N: http://www.ebay.com/itm/SLBoat-The-TL-WR703N-Mod-64Mbyte-RAM-16Mbyte-Flash-And-TTLout-Inside-MicroUSB-/181078954797?pt=COMP_EN_Routers&hash=item2a2925932d
.. _Alfa AWUSO36NH: http://www.amazon.com/gp/product/B0035APGP6/ref=as_li_ss_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=B0035APGP6&linkCode=as2&tag=cfs0f-20
.. _Yubikey: https://www.yubico.com