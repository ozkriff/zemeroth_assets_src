#!/usr/bin/env python3
"""Convert one `.svg` file to many `png`s.

TODO: document it.
"""

import subprocess
import os
import hashlib


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
    'bomb_fire',
    'bomb_poison',
    'bomb_demonic',
    'blood',
    'spike_trap',
    'dot',
    'selection',
    'white_hex',
    'hammerman',
    'spearman',
    'alchemist',
    'swordsman',

    # TODO:
    # 'test_button_bg',

    # new sprites
    'eye',  # TODO: rename to 'beholder'
    'snake',
    'grave_stone',
    'axeman',
]
out_dir_name = 'png'
input_file_name = 'atlas.svg'  # TODO: make configurable


def _file_hash(filename: str) -> str:
    with open(filename, mode='rb') as f:
        data = f.read()
        return hashlib.md5(data).hexdigest()


def _write_str_to_file(filename: str, hash: str) -> None:
    with open(filename, mode='w') as f:
        f.write(hash + '\n')


def _update_hash_file(input_file_name: str, out_dir_name: str) -> None:
    hash = _file_hash(input_file_name)
    _write_str_to_file(f'{out_dir_name}/hash', hash)


# ./export.py && cp png/* ~/zemeroth/main/assets


def _main() -> None:
    os.makedirs(out_dir_name, exist_ok=True)
    _update_hash_file(input_file_name, out_dir_name)
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
