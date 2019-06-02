#!/usr/bin/env python3
"""Convert one `.svg` file to many `png`s.

TODO: document it.
"""

import subprocess
import os


# TODO: extract to some json (?) config
ids = [
    'tile',
    'tile_rocks',
    'poison_cloud',
    'imp',
    'imp_toxic',
    'imp_summoner',
    'imp_summoner_summon',
    'imp_bomber',
    'imp_bomber_throw',
    'grass',
    'shadow',
    'fire',
    'boulder',
    'bomb',
    'bomb_fire',
    'bomb_poison',
    'bomb_demonic',
    'blood',
    'slash',
    'smash',
    'pierce',
    'claw',
    'spike_trap',
    'dot',
    'selection',
    'white_hex',
    'hammerman',
    'spearman',
    'alchemist',
    'alchemist_throw',
    'alchemist_heal',
    'swordsman',
    'swordsman_rage',

    # # new sprites
    # 'eye',
    # 'snake',
    # 'grave_stone',
    # 'axeman',
]
out_dir_name = 'png'
input_file_name = 'atlas.svg'  # TODO: make configurable


# ./export.py && cp png/* ~/zemeroth/main/assets


def _main() -> None:
    os.makedirs(out_dir_name, exist_ok=True)
    for id in ids:
        cmd = [
            'inkscape',
            input_file_name,
            f'--export-id={id}',
            f'--export-png={out_dir_name}/{id}.png',
            # f'--export-dpi={96 * 4}',
        ]
        print(cmd)
        # TODO: check resulting image size. I'm expecting 256x256, right?
        subprocess.run(cmd, check=True)


_main()
