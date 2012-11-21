####################
Dependencies
####################

* django-timezones
* pytz (used by django-timezones).

####################
Installation
####################

These instructions assume you have a Django project set up using `virtualenv
<http://www.virtualenv.org>`_ and `pip <http://www.pip-installer.org>`_

install::

    pip install -e git://github.com/tomscytale/django-jqchat.git#egg=django-jqchat
  
* add ``jqchat`` and ``timezones`` to the project's list of applications.
* include jqchat's ``urls.py`` to your main ``urls.py`` file.
* run a ``syncdb`` to add new tables.

test it. By default the urls.py file supplied adds 2 types of chat
test rooms, you will have to manually create one in the admin before
you can test it.

####################
Design philosophy
####################
Jqchat is built on the assumption that a chat room is an extra feature
on top of an existing object. Hence jqchat is kept very basic and
extensible.

####################
Integration
####################
The easiest way to add a jqchat room to an existing model is to create
a OneToOne field on the existing model. For example::
  
            from myapp.models import Room
            chat_room = models.OneToOneField(Room, help_text='Chat
            room to be used for this lobby.')

In the jqchat templates folder you will find
chat_test.html; you will have to pull out some code and
add it to your own templates:

* the header code which initialises the javascript code.
* the chatwindow div and the chatform form. If you decide to rename these elements, you will have to adjust the javascript code accordingly.

This should be enough to use the supplied chat client; to extend it, please see below.

There's no chat room members list?
===================================

No, not at present; as stated above, jqchat is designed
to be an extension to an existing object.
Patches with a neat and generic way of adding
this to jqchat are welcome


####################
Extending jqchat
####################
The big feature of jqchat is that it can be extended to
piggyback extra information in the Ajax payloads.
Within the source is an example of
using this to add and change descriptions for the chat
rooms. Things to look at are:

* template chat_test_with_desc.html: note how the call to the javascript includes a different url for handling the AJAX calls.
* views.py: the normal handler for the Ajax calls has been overridden. The view WindowWithDescriptionAjaxHandler is an instance of the view class DescriptionAjax. This class has its own custom handler - 'ExtraHandling' - that knows what to do with custom actions from the client, and also knows what extra fields to pass back.
            
