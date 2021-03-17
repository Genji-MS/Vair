import numpy as np
"""
Using perlin noise generator from:
https://github.com/pvigier/perlin-numpy/blob/master/perlin_numpy/perlin2d.py
as a reference.
Sample output from generate_perlin_noise_2d(0, (20, 20), (4, 4))
random seed 0
--------------------
-----------   --    
---------          -
----------         -
-------#---   --  --
--  ----#-----------
-   ----##--------  
-   ---#####-----   
-  ----#####-----   
-  -----##-------   
--------------------
--  -- -------------
--          --#-----
--      --  --------
----------- --------
--------#-----------
--#----###----------
---##--#######------
---------#####---  -
-----------###--    

Sample output from generate_perlin_noise_2d(0, (20, 40), (4, 4))
When you re generate it to make it longer it just makes it streched out???

----------------------------------------
---------------------      ----        -
------------------                    --
-------------------                  ---
-------------##------      ----     ----
---    --------##-----------------------
--      -------#####---------------     
-       ------#########-----------      
-     --------##########---------       
--   ----------#####-------------       
----------------------------------------
----    ---  ---------------------------
---              -      ----##----------
----           ----     ----------------
--------- ------------ -----------------
---------------##-----------------------
---###-------######---------------------
-----####-----##############------------
-----------------###########-----    ---
----------------------######----       -

"""


def interpolant(t):
    return t*t*t*(t*(t*6 - 15) + 10)


def generate_perlin_noise_2d(
        random_seed, shape, res, tileable=(False, False), interpolant=interpolant
):
    """Generate a 2D numpy array of perlin noise.
    Args:
        shape: The shape of the generated array (tuple of two ints).
            This must be a multple of res.
        res: The number of periods of noise to generate along each
            axis (tuple of two ints). Note shape must be a multiple of
            res.
        tileable: If the noise should be tileable along each axis
            (tuple of two bools). Defaults to (False, False).
        interpolant: The interpolation function, defaults to
            t*t*t*(t*(t*6 - 15) + 10).
    Returns:
        A numpy array of shape shape with the generated noise.
    Raises:
        ValueError: If shape is not a multiple of res.
    """
    np.random.seed(random_seed)
    delta = (res[0] / shape[0], res[1] / shape[1])
    d = (shape[0] // res[0], shape[1] // res[1])
    grid = np.mgrid[0:res[0]:delta[0], 0:res[1]:delta[1]]\
             .transpose(1, 2, 0) % 1
    # Gradients
    angles = 2*np.pi*np.random.rand(res[0]+1, res[1]+1)
    gradients = np.dstack((np.cos(angles), np.sin(angles)))
    if tileable[0]:
        gradients[-1, :] = gradients[0, :]
    if tileable[1]:
        gradients[:, -1] = gradients[:, 0]
    gradients = gradients.repeat(d[0], 0).repeat(d[1], 1)
    g00 = gradients[:-d[0], :-d[1]]
    g10 = gradients[d[0]:, :-d[1]]
    g01 = gradients[:-d[0], d[1]:]
    g11 = gradients[d[0]:, d[1]:]
    # Ramps
    n00 = np.sum(np.dstack((grid[:, :, 0], grid[:, :, 1])) * g00, 2)
    n10 = np.sum(np.dstack((grid[:, :, 0]-1, grid[:, :, 1])) * g10, 2)
    n01 = np.sum(np.dstack((grid[:, :, 0], grid[:, :, 1]-1)) * g01, 2)
    n11 = np.sum(np.dstack((grid[:, :, 0]-1, grid[:, :, 1]-1)) * g11, 2)
    # Interpolation
    t = interpolant(grid)
    n0 = n00*(1-t[:, :, 0]) + t[:, :, 0]*n10
    n1 = n01*(1-t[:, :, 0]) + t[:, :, 0]*n11
    return np.sqrt(2)*((1-t[:, :, 1])*n0 + t[:, :, 1]*n1)


def print_map(map):
    for row in map:
        str_row = ''
        for i in row:
            if i == 3:
                str_row += '#'
            elif i == 2:
                str_row += '-'
            else:
                str_row += ' '
        print(str_row)


if __name__ == '__main__':
    map = generate_perlin_noise_2d(0, (20, 20), (4, 4))
    map = (map / 2 + 0.5) * 3 + 1
    map = np.floor(map)
    print_map(map)
    print('')
    print('***************************************************************')
    print('')
    map = generate_perlin_noise_2d(0, (20, 40), (4, 4))
    map = (map / 2 + 0.5) * 3 + 1
    map = np.floor(map)
    print_map(map)
