Simple chat client that sends PGP encrypted messages.

To use this service you must have a GPG key set up.
A good tutorial on GPG is available here: http://www.dewinter.com/gnupg_howto/english/GPGMiniHowto.html

Note that the configuration is currently baked into the source and will not work much.
This will be fixed eventually if this does not go to project heaven.

Requires zeromq and python-gnupg

    $ sudo apt-get install libzmq-dev
    $ pip install python-gnupg pyzmq

To run the chat server run

    $ python server.py

To listen to messages

    $ python ear.py

To send messages run

    $ python mouth.py

Messages are multiline and must end in `^D` on a newline.
