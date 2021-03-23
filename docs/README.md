# Vair, a bunny resource managment game

To install run

`git clone`

Then run

`$ python3 -m venv venv && source venv/bin/activate`

`$ python3 -m pip install requirements.txt`

Next run
`$ python3 version1/vair.py`


Controls:

`Q W E` - Move upLeft, Up, upRight

`A S D` - Move downLeft, Down, downRight

`Space` - Wait a turn

`1,2,3` - Eat food located in upper right HUD


Ascii tile and food reference list:

  Tiles:
    no_tile = '!'

    # White
    rock = '\u001b[37m@'

    # Black
    barren = '\u001b[30m|'

    # Blue
    prairie = '\u001b[34m-'

    # Cyan
    lush_prairie = '\u001b[36m*'

    # Green
    forest = '\u001b[32m^'

  Foods:
    # red
    'harmful' = '\u001b[31mB' B = bad

    # Magenta
    'normal' = '\u001b[35mN' N = Normal

    # Yellow
    'helpful' = '\u001b[33mG' G = Good


