#!/usr/bin/env bash

export LC_ALL=C
TOPDIR=${TOPDIR:-$(git rev-parse --show-toplevel)}
BUILDDIR=${BUILDDIR:-$TOPDIR}

BINDIR=${BINDIR:-$BUILDDIR/src}
MANDIR=${MANDIR:-$TOPDIR/doc/man}

<<<<<<< HEAD
BITCOIND=${BITCOIND:-$BINDIR/litecoind}
BITCOINCLI=${BITCOINCLI:-$BINDIR/litecoin-cli}
BITCOINTX=${BITCOINTX:-$BINDIR/litecoin-tx}
WALLET_TOOL=${WALLET_TOOL:-$BINDIR/litecoin-wallet}
BITCOINQT=${BITCOINQT:-$BINDIR/qt/litecoin-qt}
=======
LITECOIND=${BITCOIND:-$BINDIR/litecoind}
LITECOINCLI=${BITCOINCLI:-$BINDIR/litecoin-cli}
LITECOINTX=${BITCOINTX:-$BINDIR/litecoin-tx}
LITECOINQT=${BITCOINQT:-$BINDIR/qt/litecoin-qt}
>>>>>>> 28c3cad38365b51883be89e7a306ac7eae1d9ba5

[ ! -x $LITECOIND ] && echo "$LITECOIND not found or not executable." && exit 1

# The autodetected version git tag can screw up manpage output a little bit
<<<<<<< HEAD
LTCVER=($($BITCOINCLI --version | head -n1 | awk -F'[ -]' '{ print $6, $7 }'))
=======
LTCVER=($($LITECOINCLI --version | head -n1 | awk -F'[ -]' '{ print $6, $7 }'))
>>>>>>> 28c3cad38365b51883be89e7a306ac7eae1d9ba5

# Create a footer file with copyright content.
# This gets autodetected fine for litecoind if --version-string is not set,
# but has different outcomes for litecoin-qt and litecoin-cli.
echo "[COPYRIGHT]" > footer.h2m
$LITECOIND --version | sed -n '1!p' >> footer.h2m

<<<<<<< HEAD
for cmd in $BITCOIND $BITCOINCLI $BITCOINTX $WALLET_TOOL $BITCOINQT; do
=======
for cmd in $LITECOIND $LITECOINCLI $LITECOINTX $LITECOINQT; do
>>>>>>> 28c3cad38365b51883be89e7a306ac7eae1d9ba5
  cmdname="${cmd##*/}"
  help2man -N --version-string=${LTCVER[0]} --include=footer.h2m -o ${MANDIR}/${cmdname}.1 ${cmd}
  sed -i "s/\\\-${LTCVER[1]}//g" ${MANDIR}/${cmdname}.1
done

rm -f footer.h2m
