# -*- coding: utf-8 -*-
"""Image Generation with Dall-E-mini.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1vKhpdMp-3BShbPYeptWeP61cLLSNUz5x

# **Image Generation using Text Prompts**
"""

! pip install min-dalle -q

from min_dalle import MinDalle

model = MinDalle(is_mega=True, is_reusable=True)

# Commented out IPython magic to ensure Python compatibility.
# %%time
# 
# text = "Womens enjoying sunset in paris"
# seed = 6
# grid_size = 2
# 
# display(model.generate_image(text, seed, grid_size))

# Commented out IPython magic to ensure Python compatibility.
# %%time
# 
# text = "A women sitting on the beach with flowers and watching sunset"
# seed = 6
# grid_size = 2
# 
# display(model.generate_image(text, seed, grid_size))