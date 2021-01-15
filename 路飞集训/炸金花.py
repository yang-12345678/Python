# -*- coding: utf-8 -*-
# Date: 2020/12/29

import random

num_ls = [i for i in range(14)]

color_ls = ["黑桃", "红桃", "梅花", "方片"]

total_poke_ls = [[color, num] for num in num_ls for color in color_ls]

random.shuffle(total_poke_ls)



