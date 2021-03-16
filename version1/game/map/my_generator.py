import numpy as np
from enum import Enum
from perlin_noise import generate_perlin_noise_2d


"""
weighted probability map generation:

generate_from_probability(0, (20, 20))

        -----------#
         -- --------
          #---------
       -  ##--------
  ---    ###- #-----
   -----  ######----
    ----  ---####-##
    ----------##### 
    ----------####  
     ----#----      
   -   -------     -
   -  -#-------    -
   --##--  - ---    
  - ----    -       
    --             -
             - ## # 
  #      -----#-##  
   #    -------#-#- 
-     -   -   -#--  
--   -         -    

***************************************************************

generate_from_probability(0, (20, 40), passed_map=map)
We can pass a map into it to extent it, the left half should be the same as above.

        -----------################### #
         -- --------#####-########### # 
          #-----------##-######## ##   #
       -  ##-------------#######-#      
  ---    ###- #------------###--###     
   -----  ######------------##-###-     
    ----  ---####-##------   ####-#     
    ----------##### ##------ ------     
    ----------####  ##--------------  --
     ----#----       ---##-#---#---  ---
   -   -------     -- -#-##-#-#--#-- -- 
   -  -#-------    -----####--  -#---   
   --##--  - ---    --##-#--- - --#     
  - ----    -       -- ##--- -  -#      
    --             -   --#----  - -     
             - ## #       -----  -     -
  #      -----#-##         ----  -      
   #    -------#-#-         -    ---  - 
-     -   -   -#--   -          --###   
--   -         -     -           -####  

***************************************************************

generate_from_probability(0, (20, 40))
If we don't pass a smaller map in it does not extend it just generates a new map.

        -----------#######----##########
         -- --------###-#----------#####
          #--------------##------ ---###
       -  ##------------- ####--------#-
  ---    ###- #------------####-#--- ---
   -----  ######-----------#####--- - -#
    ----  ---####-## --- # -#####--   -#
    ----------#####     - -  -##---  ---
    ----------####     - - ---#-## ---- 
     ----#----      ----  ------  # ----
   -   -------     -----##    --     ---
   -  -#-------    ------#-#         -  
   --##--  - ---    ------##       #    
  - ----    -       ------ ####   ### ##
    --             - -----##############
             - ## #  ---################
  #      -----#-##       #--# #######-# 
   #    -------#-#-     ------########-#
-     -   -   -#--   --  ------#######-#
--   -         -    ---------  ########-

***************************************************************

generate_perlin_noise_2d(0, (20, 40), (4, 4))
We can make a perlin noise map,

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


***************************************************************

generate_from_probability(0, (20, 40), passed_map=p_map, tamper=True)
Then pass it in while turning on tapmer to make it look a little less flat.

 -------#--------- --  --- ---####--  --
----------- -----  -- -       -       -#
----------#-------- -     -    -     ---
-------#---------- --      ---  -    ---
--#------#-#- #----- ----- ---- -    ---
---#---- -#---###--- -----------    - -#
--     - ----####### -#--# ----#-     --
     -  -----######- ---#--------    -  
    ----------####-----#-#--------    - 
     ----#----  -------- -------  -     
-- - ------- -----------##-   --  ------
-- -  ---   --- ------ ----#  - - - ----
--- ---    - - - -- -   ----  - -- -----
--# -     - -   -- --  --- #---- --#----
------   - - ------- -----#-----#-##----
--- ---------#-##-#-----####----###-----
--#--#-####---####  #-- -#--# ----#-- - 
---#-- -###----###------####-------- - -
#-----# ---- --#-----##--###----- - -  -
-#---#- --------  --########-  ----  #- 

***************************************************************

generate_from_probability(0, (20, 40), passed_map=p_map, tamper=True, d_con=(2, 2))
If we pass in a d_con we can veiw a larger area when stocasticaly sampling, this
may or may not be desireable.

 -------#------- - --   --  - -###--  --
----------- -----  -  -       -    - --#
----#-----#-- ----- -    --    -  -  ---
-- ----#---------# --     -#-- --    -- 
--#------#-#- #--### ----- ---- -    ---
---#---- ----#####   ------#-#--    - -#
-- -  -------####### -#- # ----#-     --
    --- -----######  ---#------      -  
 -------------####- ---# #--------  - - 
  -- - --#----  ----##-- ------   -     
-- # - ----- ---# -#- #-##-   --  - ----
-  -  ---   -------#-- - --# -- - - ----
-----#-    - --- -----  --#-  - -- #----
--- -  -  - - ---- --- - - #---- -##---#
------   - - ---- -- #----#-----#-##-#--
--- ------   # ##-#--##-####------------
--#----####---#-## -#-- -#--# ----#-- - 
---#-- -#-#----#-#------##-#-------- - #
#-----#-- -----#-----##- ##------ - -  -
-#---#- - ------ ---##-#####-  ----  #- 

"""


class TileType(Enum):
    prob_given_neighbor = {
        0: np.array([0.0, 0.0, 0.0]),
        1: np.array([0.94, 0.05, 0.01]),
        2: np.array([0.05, 0.9, 0.05]),
        3: np.array([0.01, 0.05, 0.94])
    }
    no_tile = 0
    barren = 1
    prarry = 2
    lush = 3


def generate_from_probability(random_seed, shape, d_con=(1, 1), passed_map=None, tamper=False):
    np.random.seed(random_seed)
    map = np.zeros(shape)
    if passed_map is not None:
        map[0:passed_map.shape[0], 0: passed_map.shape[1]] = passed_map
    for j in range(shape[1]):
        for i in range(shape[0]):
            if map[i, j] == 0 or tamper == True:
                if i == 0 and j == 0:
                    map[0, 0] = np.random.randint(3) + 1
                else:
                    sum_probs = np.array([0., 0., 0.])
                    count_added_probs = 0
                    for in_i in range(i - d_con[0], i + d_con[0] + 1):
                        for in_j in range(j - d_con[1], j + d_con[1] + 1):
                            if in_i >= 0 and in_i < shape[0] and in_j >= 0 and in_j < shape[1]:
                                # print(f'i: {i} in_i: {in_i} j: {j} in_j: {in_j}')
                                if map[in_i, in_j] != 0:
                                    sum_probs += TileType.prob_given_neighbor.value[map[in_i, in_j]]
                                    count_added_probs += 1
                    count_added_probs = 1 if count_added_probs == 0 else count_added_probs
                    # print(sum_probs)
                    actual_probs = sum_probs/count_added_probs
                    # print(actual_probs)
                    # print(sum(actual_probs))
                    map[i, j] = np.random.choice([1, 2, 3], p=actual_probs)
            # print('-----------')
        # print('-----------*******-----------')
    return map


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
    seed = 0
    print('Small map')
    map = generate_from_probability(seed, (20, 20))
    print_map(map)
    print('')
    print('***************************************************************')
    print('Print small map extended')
    map = generate_from_probability(seed, (20, 40), passed_map=map)
    print_map(map)
    print('')
    print('***************************************************************')
    print('Large Map')
    map = generate_from_probability(seed, (20, 40))
    print_map(map)
    print('')
    print('***************************************************************')
    print('Perlin noise map')
    p_map = generate_perlin_noise_2d(seed, (20, 40), (4, 4))
    p_map = (p_map / 2 + 0.5) * 3 + 1
    p_map = np.floor(p_map)
    print_map(p_map)
    print('')
    print('***************************************************************')
    print('Perlin noise map thats been passed over with stocastic sample')
    map = generate_from_probability(
        seed, (20, 40), passed_map=p_map, tamper=True)
    print_map(map)
    print('')
    print('***************************************************************')
    print('Perlin noise map thats been passed over with stocastic sample with larger view')
    map = generate_from_probability(
        seed, (20, 40), passed_map=p_map, d_con=(2, 2), tamper=True)
    print_map(map)
