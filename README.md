# plotter-blockchain


Plotter is a modern cryptocurrency built from the hard work of the Chia devs, designed to be efficient, decentralized, and secure without the pre-mine. Here are some of the features and benefits:
* [Proof of space and time](https://docs.google.com/document/d/1tmRIb7lgi4QfKkNaxuKOBHRmwbVlGL4f7EsBDr_5xZE/edit) based consensus which allows anyone to farm with commodity hardware
* Very easy to use full node and farmer GUI and cli (thousands of nodes active on mainnet)
* Simplified UTXO based transaction model, with small on-chain state
* Lisp-style Turing-complete functional [programming language](https://chialisp.com/) for money related use cases
* BLS keys and aggregate signatures (only one signature per block)
* Support for light clients with fast, objective syncing
* A growing community of farmers and developers around the world

Please check out the [wiki](https://github.com/chia-Network/chia-blockchain/wiki)
and [FAQ](https://github.com/chia-Network/chia-blockchain/wiki/FAQ) for
information on this project.

Python 3.7+ is required. Make sure your default python version is >=3.7
by typing `python3`.

If you are behind a NAT, it can be difficult for peers outside your subnet to
reach you when they start up. You can enable
[UPnP](https://www.homenethowto.com/ports-and-nat/upnp-automatic-port-forward/)
on your router or add a NAT (for IPv4 but not IPv6) and firewall rules to allow
TCP port 4242 access to your peer.
These methods tend to be router make/model specific.

Most users should only install harvesters, farmers, plotter, full nodes, and wallets.
Building Timelords and VDFs is for sophisticated users, in most environments.
Plotter Network and additional volunteers are running sufficient Timelords
for consensus.

## Installing

Install instructions are available in the
[INSTALL](https://github.com/chia-Network/chia-blockchain/wiki/INSTALL)
section of the
[plotter-blockchain repository wiki](https://github.com/chia-Network/chia-blockchain/wiki).

## Running

Once installed, a
[Quick Start Guide](https://github.com/chia-Network/chia-blockchain/wiki/Quick-Start-Guide)
is available from the repository
[wiki](https://github.com/chia-Network/chia-blockchain/wiki).
