litecoind version 0.4.3 is now available for download at:
http://luke.dashjr.org/programs/litecoin/files/litecoind-0.4.3/ (until Gavin uploads to SourceForge)

This is a bugfix-only release based on 0.4.0.

Please note that the wxLitecoin GUI client is no longer maintained nor supported. If someone would like to step up to maintain this, they should contact Luke-Jr.

Please report bugs for the daemon only using the issue tracker at github:
https://github.com/litecoin/litecoin/issues

Stable source code is hosted at Gitorious:
http://gitorious.org/litecoin/litecoind-stable/archive-tarball/v0.4.3#.tar.gz

BUG FIXES

Cease locking memory used by non-sensitive information (this caused a huge performance hit on some platforms, especially noticable during initial blockchain download).
Fixed some address-handling deadlocks (client freezes).
No longer accept inbound connections over the internet when Litecoin is being used with Tor (identity leak).
Use the correct base transaction fee of 0.0005 LTC for accepting transactions into mined blocks (since 0.4.0, it was incorrectly accepting 0.0001 LTC which was only meant to be relayed).
Add new DNS seeds (maintained by Pieter Wuille and Luke Dashjr).

