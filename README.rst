Introduction
============

If you use separate skins for the administration and publication of
content, you can use this package to block anonymous access on your
administration url.

Simply add this package as an egg to your buildout and:

1. Add a 'privateurls' lines property to your Plone site on the 'Properties' tab.
Add the URL of your admin URL to the privateurls lines property: eg.
http://admin.plone.org

2. Add a 'publicurls' lines property to your Plone site on the 'Properties' tab.
Add the URLs of anonymously accessible pages to lines property: eg.
http://admin.plone.org/contact-info
http://admin.plone.org/sitemap

