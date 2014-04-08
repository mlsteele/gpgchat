Simple chat service that sends PGP encrypted messages.

To use this service you must have a GPG key set up.
A good tutorial on GPG is available here: http://www.dewinter.com/gnupg_howto/english/GPGMiniHowto.html

Requires zeromq and python-gnupg

    $ sudo apt-get install libzmq-dev
    $ pip install python-gnupg pyzmq

First, create and edit your configuration file.

    $ cp config_example.py config.py

To start a chat server run

    $ python server.py

To listen to messages run

    $ python ear.py

To send messages run

    $ python mouth.py

Messages are multiline and must end in `^D` on a newline.
