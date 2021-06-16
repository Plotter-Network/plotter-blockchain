from setuptools import setup

dependencies = [
    "blspy==1.0.2",  # Signature library
    "plottervdf==1.0.2",  # timelord and vdf verification
    "plotterbip158==1.0",  # bip158-style wallet filters
    "plotterpos==1.0.3",  # proof of space
    "clvm==0.9.6",
    "clvm_rs==0.1.7",
    "clvm_tools==0.4.3",
    "aiohttp==3.7.4",  # HTTP server for full node rpc
    "aiosqlite==0.17.0",  # asyncio wrapper for sqlite, to store blocks
    "bitstring==3.1.7",  # Binary data management library
    "colorlog==5.0.1",  # Adds color to logs
    "concurrent-log-handler==0.9.19",  # Concurrently log and rotate logs
    "cryptography==3.4.7",  # Python cryptography library for TLS - keyring conflict
    "keyring==23.0.1",  # Store keys in MacOS Keychain, Windows Credential Locker
    "keyrings.cryptfile==1.3.4",  # Secure storage for keys on Linux (Will be replaced)
    #  "keyrings.cryptfile==1.3.8",  # Secure storage for keys on Linux (Will be replaced)
    #  See https://github.com/frispete/keyrings.cryptfile/issues/15
    "PyYAML==5.4.1",  # Used for config file format
    "setproctitle==1.2.2",  # Gives the plotter processes readable names
    "sortedcontainers==2.3.0",  # For maintaining sorted mempools
    "websockets==8.1.0",  # For use in wallet RPC and electron UI
    "click==7.1.2",  # For the CLI
    "dnspython==2.1.0",  # Query DNS seeds
]

upnp_dependencies = [
    "miniupnpc==2.2.2",  # Allows users to open ports on their router
]

dev_dependencies = [
    "pytest",
    "pytest-asyncio",
    "flake8",
    "mypy",
    "black",
    "aiohttp_cors",  # For blackd
    "ipython",  # For asyncio debugging
]

kwargs = dict(
    name="plotter-blockchain",
    author="Mariano Sorgente",
    author_email="mariano@plotter.net",
    description="Plotter blockchain full node, farmer, timelord, and wallet.",
    url="https://plotter.net/",
    license="Apache License",
    python_requires=">=3.7, <4",
    keywords="plotter blockchain node",
    install_requires=dependencies,
    setup_requires=["setuptools_scm"],
    extras_require=dict(
        uvloop=["uvloop"],
        dev=dev_dependencies,
        upnp=upnp_dependencies,
    ),
    packages=[
        "build_scripts",
        "plotter",
        "plotter.cmds",
        "plotter.consensus",
        "plotter.daemon",
        "plotter.full_node",
        "plotter.timelord",
        "plotter.farmer",
        "plotter.harvester",
        "plotter.introducer",
        "plotter.plotting",
        "plotter.protocols",
        "plotter.rpc",
        "plotter.server",
        "plotter.simulator",
        "plotter.types.blockchain_format",
        "plotter.types",
        "plotter.util",
        "plotter.wallet",
        "plotter.wallet.puzzles",
        "plotter.wallet.rl_wallet",
        "plotter.wallet.cc_wallet",
        "plotter.wallet.did_wallet",
        "plotter.wallet.settings",
        "plotter.wallet.trading",
        "plotter.wallet.util",
        "plotter.ssl",
        "mozilla-ca",
    ],
    entry_points={
        "console_scripts": [
            "plotter = plotter.cmds.plotter:main",
            "plotter_wallet = plotter.server.start_wallet:main",
            "plotter_full_node = plotter.server.start_full_node:main",
            "plotter_harvester = plotter.server.start_harvester:main",
            "plotter_farmer = plotter.server.start_farmer:main",
            "plotter_introducer = plotter.server.start_introducer:main",
            "plotter_timelord = plotter.server.start_timelord:main",
            "plotter_timelord_launcher = plotter.timelord.timelord_launcher:main",
            "plotter_full_node_simulator = plotter.simulator.start_simulator:main",
        ]
    },
    package_data={
        "plotter": ["pyinstaller.spec"],
        "plotter.wallet.puzzles": ["*.clvm", "*.clvm.hex"],
        "plotter.util": ["initial-*.yaml", "english.txt"],
        "plotter.ssl": ["plotter_ca.crt", "plotter_ca.key", "dst_root_ca.pem"],
        "mozilla-ca": ["cacert.pem"],
    },
    use_scm_version={"fallback_version": "unknown-no-.git-directory"},
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    zip_safe=False,
)


if __name__ == "__main__":
    setup(**kwargs)
