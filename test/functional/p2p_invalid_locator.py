#!/usr/bin/env python3
<<<<<<< HEAD
# Copyright (c) 2015-2018 The Litecoin Core developers
=======
# Copyright (c) 2015-2018 The Bitcoin Core developers
>>>>>>> 28c3cad38365b51883be89e7a306ac7eae1d9ba5
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.
"""Test node responses to invalid locators.
"""

from test_framework.messages import msg_getheaders, msg_getblocks, MAX_LOCATOR_SZ
from test_framework.mininode import P2PInterface
from test_framework.test_framework import LitecoinTestFramework


class InvalidLocatorTest(LitecoinTestFramework):
    def set_test_params(self):
        self.num_nodes = 1
        self.setup_clean_chain = False

    def skip_test_if_missing_module(self):
        self.skip_if_no_wallet()

    def run_test(self):
        node = self.nodes[0]  # convenience reference to the node
        node.generatetoaddress(1, node.get_deterministic_priv_key().address)  # Get node out of IBD

        self.log.info('Test max locator size')
        block_count = node.getblockcount()
        for msg in [msg_getheaders(), msg_getblocks()]:
            self.log.info('Wait for disconnect when sending {} hashes in locator'.format(MAX_LOCATOR_SZ + 1))
            node.add_p2p_connection(P2PInterface())
            msg.locator.vHave = [int(node.getblockhash(i - 1), 16) for i in range(block_count, block_count - (MAX_LOCATOR_SZ + 1), -1)]
            node.p2p.send_message(msg)
            node.p2p.wait_for_disconnect()
            node.disconnect_p2ps()

            self.log.info('Wait for response when sending {} hashes in locator'.format(MAX_LOCATOR_SZ))
            node.add_p2p_connection(P2PInterface())
            msg.locator.vHave = [int(node.getblockhash(i - 1), 16) for i in range(block_count, block_count - (MAX_LOCATOR_SZ), -1)]
            node.p2p.send_message(msg)
            if type(msg) == msg_getheaders:
                node.p2p.wait_for_header(int(node.getbestblockhash(), 16))
            else:
                node.p2p.wait_for_block(int(node.getbestblockhash(), 16))


if __name__ == '__main__':
    InvalidLocatorTest().main()
