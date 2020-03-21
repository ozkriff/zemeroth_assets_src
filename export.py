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
    'imp_summoner_cast',
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
    'explosion_ground_mark',
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
    'heavy_hammerman',
    'spearman',
    'elite_spearman',
    'heavy_spearman',
    'alchemist',
    'alchemist_throw',
    'alchemist_heal',
    'healer',
    'healer_throw',
    'healer_heal',
    'firer',
    'firer_throw',
    'swordsman',
    'elite_swordsman',
    'elite_swordsman_rage',
    'heavy_swordsman',
    'effect_poison',
    'effect_stun',
    'effect_bloodlust',
    'icon_ability_club',
    'icon_ability_knockback',
    'icon_ability_jump',
    'icon_ability_dash',
    'icon_ability_rage',
    'icon_ability_heal',
    'icon_ability_bomb_push',
    'icon_ability_bomb',
    'icon_ability_bomb_fire',
    'icon_ability_bomb_poison',
    'icon_ability_bomb_demonic',
    'icon_ability_summon',
    'icon_ability_bloodlust',
    'icon_info',
    'icon_end_turn',
    'icon_menu',

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
