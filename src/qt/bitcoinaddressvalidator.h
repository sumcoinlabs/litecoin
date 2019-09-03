// Copyright (c) 2011-2014 The Litecoin Core developers
// Distributed under the MIT software license, see the accompanying
// file COPYING or http://www.opensource.org/licenses/mit-license.php.

#ifndef BITCOIN_QT_BITCOINADDRESSVALIDATOR_H
#define BITCOIN_QT_BITCOINADDRESSVALIDATOR_H

#include <QValidator>

/** Base58 entry widget validator, checks for valid characters and
 * removes some whitespace.
 */
class LitecoinAddressEntryValidator : public QValidator
{
    Q_OBJECT

public:
    explicit LitecoinAddressEntryValidator(QObject *parent);

    State validate(QString &input, int &pos) const;
};

/** Litecoin address widget validator, checks for a valid litecoin address.
 */
class LitecoinAddressCheckValidator : public QValidator
{
    Q_OBJECT

public:
    explicit LitecoinAddressCheckValidator(QObject *parent);

    State validate(QString &input, int &pos) const;
};

#endif // BITCOIN_QT_BITCOINADDRESSVALIDATOR_H
