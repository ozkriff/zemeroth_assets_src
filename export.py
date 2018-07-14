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
    'imp_bomber',
    'grass',
    'shadow',
    'fire',
    'boulder',
    'bomb',
    'blood',
    'spike_trap',
    'dot',
    'selection',
    'white_hex',

    # 'swordsman',  # TODO: actually, it's a "axeman" or something atm

    # TODO:
    'hammerman',
    'spearman',
    'alchemist',
    'swordsman',
    #
    #
    # 'bomb_fire',
    # 'bomb_poison',
    #
    # 'test_button_bg',

    # new sprites
    'eye',
    'snake',
    'grave_stone',
    'axeman',
    # 'human',
]
out_dir_name = 'png'
input_file_name = 'atlas.svg'  # TODO: make configurable


# cp png/{imp,imp_toxic,boulder,grass,shadow}.png ~/zemeroth/main/assets

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
