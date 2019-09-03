Litecoin Core integration/staging tree
=====================================

<<<<<<< HEAD
[![Build Status](https://travis-ci.org/litecoin/litecoin.svg?branch=master)](https://travis-ci.org/litecoin/litecoin)

https://litecoincore.org
=======
[![Build Status](https://travis-ci.org/litecoin-project/litecoin.svg?branch=master)](https://travis-ci.org/litecoin-project/litecoin)

https://litecoin.org
>>>>>>> 28c3cad38365b51883be89e7a306ac7eae1d9ba5

What is Litecoin?
----------------

Litecoin is an experimental digital currency that enables instant payments to
anyone, anywhere in the world. Litecoin uses peer-to-peer technology to operate
with no central authority: managing transactions and issuing money are carried
out collectively by the network. Litecoin Core is the name of open source
software which enables the use of this currency.

For more information, as well as an immediately useable, binary version of
<<<<<<< HEAD
the Litecoin Core software, see https://litecoincore.org/en/download/, or read the
[original whitepaper](https://litecoincore.org/litecoin.pdf).
=======
the Litecoin Core software, see [https://litecoin.org](https://litecoin.org).
>>>>>>> 28c3cad38365b51883be89e7a306ac7eae1d9ba5

License
-------

Litecoin Core is released under the terms of the MIT license. See [COPYING](COPYING) for more
information or see https://opensource.org/licenses/MIT.

Development Process
-------------------

The `master` branch is regularly built and tested, but is not guaranteed to be
<<<<<<< HEAD
completely stable. [Tags](https://github.com/litecoin/litecoin/tags) are created
=======
completely stable. [Tags](https://github.com/litecoin-project/litecoin/tags) are created
>>>>>>> 28c3cad38365b51883be89e7a306ac7eae1d9ba5
regularly to indicate new official, stable release versions of Litecoin Core.

The contribution workflow is described in [CONTRIBUTING.md](CONTRIBUTING.md)
and useful hints for developers can be found in [doc/developer-notes.md](doc/developer-notes.md).

The developer [mailing list](https://groups.google.com/forum/#!forum/litecoin-dev)
should be used to discuss complicated or controversial changes before working
on a patch set.

Developer IRC can be found on Freenode at #litecoin-dev.

Testing
-------

Testing and code review is the bottleneck for development; we get more pull
requests than we can review and test on short notice. Please be patient and help out by testing
other people's pull requests, and remember this is a security-critical project where any mistake might cost people
lots of money.

### Automated Testing

Developers are strongly encouraged to write [unit tests](src/test/README.md) for new code, and to
submit new unit tests for old code. Unit tests can be compiled and run
(assuming they weren't disabled in configure) with: `make check`. Further details on running
and extending unit tests can be found in [/src/test/README.md](/src/test/README.md).

There are also [regression and integration tests](/test), written
in Python, that are run automatically on the build server.
These tests can be run (if the [test dependencies](/test) are installed) with: `test/functional/test_runner.py`

The Travis CI system makes sure that every pull request is built for Windows, Linux, and macOS, and that unit/sanity tests are run automatically.

### Manual Quality Assurance (QA) Testing

Changes should be tested by somebody other than the developer who wrote the
code. This is especially important for large or high-risk changes. It is useful
to add a test plan to the pull request description if testing the changes is
not straightforward.

Translations
------------

<<<<<<< HEAD
Changes to translations as well as new translations can be submitted to
[Litecoin Core's Transifex page](https://www.transifex.com/projects/p/litecoin/).
=======
We only accept translation fixes that are submitted through [Bitcoin Core's Transifex page](https://www.transifex.com/projects/p/bitcoin/).
Translations are converted to Litecoin periodically.
>>>>>>> 28c3cad38365b51883be89e7a306ac7eae1d9ba5

Translations are periodically pulled from Transifex and merged into the git repository. See the
[translation process](doc/translation_process.md) for details on how this works.

**Important**: We do not accept translation changes as GitHub pull requests because the next
pull from Transifex would automatically overwrite them again.
<<<<<<< HEAD

Translators should also subscribe to the [mailing list](https://groups.google.com/forum/#!forum/litecoin-translators).
=======
>>>>>>> 28c3cad38365b51883be89e7a306ac7eae1d9ba5
