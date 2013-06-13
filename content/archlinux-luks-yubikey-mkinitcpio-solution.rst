Arch Linux Full-disk-encryption with Yubikey
#############################################################
:date: 2013-06-12 22:45
:author: chris
:category: Tutorials
:slug: archlinux-luks-yubikey-mkinitcpio-solution

When using LUKS with Arch Linux, I had some difficulty getting my Yubikey to
work for entering the passphrase. I solved this problem once and then promptly
forgot the solution, so this time I'm writing it down. The key is that the 
*block* and *keyboard* hooks must be before the *autodetect* hook:

*/etc/mkinitcpio.conf*:

.. code-include:: code/archlinux-luks-yubikey-mkinitcpio-solution/mkinitcpio.conf