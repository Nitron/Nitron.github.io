Django Subdomain Middleware with CNAME Support
##############################################
:date: 2012-07-16 19:19
:category: Computer Science
:slug: django-subdomain-middleware-with-cname-support
:alias: /2012/07/django-subdomain-middleware-with-cname-support/

For a personal project (details forthcoming), I've been trying to have
separate subdomains for accounts and allow some of these accounts to
have CNAME support. So, if I have an account *cwilliams*, my data should
be available at *cwilliams.myproject.com*. I could also add
*myproject.christopher-williams.net* as a CNAME and get the same view.

The implementation is fairly straightforward. I ended up taking
`django-subdomains`_, removing some functionality that I didn't need and
adding the CNAME handling.

To use this middleware:

#. Put *middleware.py* (see below) somewhere in your project. I have a
   Django app called *core* for things like this.
#. Add a CNAME field to a model of your choosing (a user profile might
   be appropriate), preferably as a CharField. URLField will not work.
#. Add a SlugField to the same model and wire that up like you would any
   other slug.
#. Add a new *subdomain\_urls.py* and put the URLconf that should be
   used for your subdomains/CNAMEs.
#. Add *SUBDOMAIN\_URLCONF='yourproject.subdomain\_urls'* to
   *settings.py*.
#. Add *core.middleware.SubdomainMiddleware* to *MIDDLEWARE\_CLASSES* in
   *settings.py* (bottom of the list should work for most usages).
#. Create some fake DNS entries in your *hosts* file (see below).
#. Set up your slug/CNAME entries created in your model (i.e. for slugs,
   *test1*, *test2*. For CNAMEs, *djangotest.christopher-williams.net*,
   etc.)
#. Open your fake subdomains in your browser.

Any hostname that doesn't have a corresponding slug/CNAME will be routed
through your *ROOT\_URLCONF*. Otherwise, you should see what's in your
*SUBDOMAIN\_URLCONF*.

The Code
~~~~~~~~

*/etc/hosts*:

.. code-include:: code/hosts

*middleware.py*:

.. code-include:: code/middleware.py
	:lexer: python
	:tab-width: 4

.. _django-subdomains: https://github.com/tkaemming/django-subdomains/
