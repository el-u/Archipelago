import struct
from struct import pack

kirby_flavor_presets = {
    3: {
        "1": "a6a6ed",
        "2": "e6e6fa",
        "3": "bcbcf2",
        "4": "8484e6",
        "5": "2929ec",
        "6": "b5b5f0",
        "7": "847bd6",
        "8": "3232d6",
        "9": "d6d6ef",
        "10": "4a52ef",
        "11": "c6c6e6",
        "12": "4343ad",
        "13": "9494ea",
        "14": "f6f6fd",
        "15": "3139b6",
    }
}

kirby_target_palettes = {
    0x1E007E: (["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"], 0),
    0x1E00F6: (["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"], 0),
    0x1E0216: (["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"], 0),
}


def get_kirby_palette(multiworld, player):
    palette = multiworld.kirby_flavor_preset[player].value
    if palette in kirby_flavor_presets:
        return kirby_flavor_presets[palette]
    elif palette == 14:
        return multiworld.kirby_flavor[player].value
    else:
        return None


def rgb888_to_bgr555(color: str) -> bytes:
    col = int(color, 16)
    red = (col & 0xFF0000) >> 19
    green = (col & 0x00FF00) >> 11
    blue = (col & 0x0000FF) >> 3
    outcol = (blue << 10) + (green << 5) + red
    return struct.pack("H", outcol)


def get_palette_bytes(palette, target, offset):
    output_data = bytearray()
    for color in target:
        byte_data = rgb888_to_bgr555(str(hex(int(palette[color], 16) + offset)))
        output_data.extend(bytearray(byte_data))
    return output_data