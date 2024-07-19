__author__ = "Lukas Mahler"
__version__ = "0.0.1"
__date__ = "20.07.2024"
__email__ = "m@hler.eu"
__status__ = "Development"


import re
from typing import Optional, Union

from cs2inspect._hex import bytes_to_float, to_hex
from cs2inspect.econ_pb2 import CEconItemPreviewDataBlock

INSPECT_BASE = "steam://rungame/730/76561202255233023/+csgo_econ_action_preview%20"


def link(data: Union[dict, CEconItemPreviewDataBlock]) -> Optional[str]:
    if isinstance(data, dict):
        required_keys = {"asset_id", "class_id"}
        if not required_keys.issubset(data.keys()):
            return None
        if 'market_id' not in data and 'owner_id' not in data:
            return None
        return link_unmasked(
            asset_id=data['asset_id'],
            class_id=data['class_id'],
            market_id=data.get('market_id'),
            owner_id=data.get('owner_id')
        )
    elif isinstance(data, CEconItemPreviewDataBlock):
        return link_masked(data)

    return None


def gen(data: Union[dict, CEconItemPreviewDataBlock]) -> Optional[str]:
    stickers = []
    if isinstance(data, dict):
        required_keys = {"defindex", "paintindex", "paintseed", "paintwear"}
        if not required_keys.issubset(data.keys()):
            return None
        stickers = data.get('stickers', [])
    elif isinstance(data, CEconItemPreviewDataBlock):
        data = {
            'defindex': data.defindex,
            'paintindex': data.paintindex,
            'paintseed': data.paintseed,
            'paintwear': bytes_to_float(data.paintwear),
            'stickers': [{'slot': s.slot, 'sticker_id': s.sticker_id, 'wear': s.wear} for s in data.stickers]
        }
        stickers = data['stickers']

    str_gen = f"!gen {data['defindex']} {data['paintindex']} {data['paintseed']} {data['paintwear']}"

    if not stickers:
        return str_gen

    sticker_slots = [CEconItemPreviewDataBlock.Sticker(slot=i) for i in range(5)]

    for sticker in stickers:
        sticker_slots[sticker['slot']].sticker_id = sticker['sticker_id']
        if 'wear' in sticker:
            sticker_slots[sticker['slot']].wear = sticker['wear']

    for sticker in sticker_slots:
        str_gen += f" {sticker.sticker_id} {sticker.wear}"

    return str_gen


def link_masked(data_block: CEconItemPreviewDataBlock) -> Optional[str]:
    hex_string = to_hex(data_block)
    inspect_link = f"{INSPECT_BASE}{hex_string}"

    # Verify inspection link being valid
    if is_valid_inspection_link(inspect_link, link_type="masked"):
        return inspect_link

    return None


def link_unmasked(asset_id: str, class_id: str,
                  market_id: Optional[str] = None, owner_id: Optional[str] = None) -> Optional[str]:
    if not market_id and not owner_id:
        return None

    location = f"M{market_id}" if market_id else f"S{owner_id}"
    inspect_link = f"{INSPECT_BASE}{location}A{asset_id}D{class_id}"

    # Verify inspection link being valid
    if is_valid_inspection_link(inspect_link):
        return inspect_link

    return None


def is_valid_inspection_link(inspect: str, link_type: str = "unmasked") -> bool:
    if link_type == "unmasked":
        pattern = re.compile(r"^steam://rungame/730/\d+/[+ ]csgo_econ_action_preview%20([SM])(\d+)A(\d+)D(\d+)$")
    elif link_type == "masked":
        pattern = re.compile(r"^steam://rungame/730/\d+/[+ ]csgo_econ_action_preview%20[0-9a-fA-F]+$")
    else:
        return False

    if pattern.search(inspect):
        return True
    else:
        return False


if __name__ == '__main__':
    exit(1)
