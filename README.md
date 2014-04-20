# gpgchat

Simple chat service that sends PGP encrypted messages.

gpgchat encrypts message data end-to-end using the clients' system version of gpg.
Note that while message data is encrypted, the intended recipients and sender
of messages are NOT secret.
The channel is susceptible to all sorts of traffic analysis.
But it's one step closer to secure communication than a cleartext or
"trusted server" messaging service.

gpgchat proudly sports an archaic and laughable user interface.
As a user, you will probably want to run two terminal side
by side. One running the ear, and the other the mouth.

To use this service you must have a GPG key set up.
A good [tutorial on GPG is available here](http://www.dewinter.com/gnupg_howto/english/GPGMiniHowto.html).

## Requirements & Installation

gpgchat requires zeromq, python-gnupg, and gpg-agent

### Ubuntu

To install the requirements on Ubuntu:

    $ sudo apt-get install libzmq-dev gnupg-agent
    $ pip install python-gnupg pyzmq

If you just installed gpg-agent, you may need to log out and back in for it to start the daemon properly.

### OSX

To install the requirements on OSX:

First install [gpgtools](https://gpgtools.org/).

    $ brew install zeromq
    $ pip install python-gnupg pyzmq

If you just installed gpg-agent, you may need to log out and back in for it to start the daemon properly.

## Running gpgchat

You will need to set up a private key and know get some friends public keys
and mark them as trusted.
Setting up keys is not covered here,
but there is a thorough and fairly quick
tutorial on GPG that I recommend [available here](http://www.dewinter.com/gnupg_howto/english/GPGMiniHowto.html).

First, create and edit your configuration file.
The config file determines what server to connect
and which keys to use for encrypting and signing.

    $ cp config_example.py config.py

To start a chat server run

    $ python server.py

To listen to messages run

    $ python ear.py

To send messages run

    $ python mouth.py

Messages are multiline and must end in `^D` on a newline.
