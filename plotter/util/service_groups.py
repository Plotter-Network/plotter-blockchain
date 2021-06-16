from typing import KeysView, Generator

SERVICES_FOR_GROUP = {
    "all": "plotter_harvester plotter_timelord_launcher plotter_timelord plotter_farmer plotter_full_node plotter_wallet".split(),
    "node": "plotter_full_node".split(),
    "harvester": "plotter_harvester".split(),
    "farmer": "plotter_harvester plotter_farmer plotter_full_node plotter_wallet".split(),
    "farmer-no-wallet": "plotter_harvester plotter_farmer plotter_full_node".split(),
    "farmer-only": "plotter_farmer".split(),
    "timelord": "plotter_timelord_launcher plotter_timelord plotter_full_node".split(),
    "timelord-only": "plotter_timelord".split(),
    "timelord-launcher-only": "plotter_timelord_launcher".split(),
    "wallet": "plotter_wallet plotter_full_node".split(),
    "wallet-only": "plotter_wallet".split(),
    "introducer": "plotter_introducer".split(),
    "simulator": "plotter_full_node_simulator".split(),
}


def all_groups() -> KeysView[str]:
    return SERVICES_FOR_GROUP.keys()


def services_for_groups(groups) -> Generator[str, None, None]:
    for group in groups:
        for service in SERVICES_FOR_GROUP[group]:
            yield service


def validate_service(service: str) -> bool:
    return any(service in _ for _ in SERVICES_FOR_GROUP.values())
