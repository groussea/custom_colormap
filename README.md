# Custom colormaps with or without transparency

This code has originaly be developped by Chris Slocum and modified during my PhD (2014-2019) since it is sometimes desirable to build transparency colormaps for vizualisations


A small routine to generate custom colormaps for [Matplotlib](https://matplotlib.org/).
The function allows you to create a list of tuples with 8-bit (0 to 255) or arithmetic (0.0 to 1.0)
RGBA values to create linear colormaps by taking your list and converting it into a dictionary (A:Alpha correspond to the level of transparency)
that can work with [LinearSegmentedColormap](https://matplotlib.org/api/_as_gen/matplotlib.colors.LinearSegmentedColormap.html).

## Example
```python
from custom_colormaps import create_colormap
import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure()
colors = [(255, 0, 0,10), (255, 255, 0,70), (255, 255, 255,80), (0, 157, 0,255), (0, 0, 255,255)] # This example uses the 8-bit RGBA
my_cmap = create_colormap(colors, bit=True)
plt.plot([0,50],[0,25],color='k',zorder=0)
plt.text(25,12.5,'colormaps with transparency',zorder=0,horizontalalignment='center',verticalalignment='center',fontsize=20)
plt.pcolormesh(np.random.rand(25, 50), cmap=my_cmap)
plt.colorbar()
plt.show()
```

## Saving custom colormaps
If you do not want to use the create_colormap function everytime you need to use your custom colormap, it would be ideal to register the colormap with matplotlib. Outside of a single piece of code, I do not believe there is a simple solution to this. My suggestion is to save the colormap as an ASCII file and read in this file when you want to reuse your custom colormap.

The code below output an RGBA dictionary of segment data from the colormap object. We then save this dictionary as a JSON file.

### In your script that generates your colormap:
```python
import json
with open('my_cmap.json', 'w') as f:
    json.dump(my_cmap._segmentdata, f)
```

### In your plotting script:
```python
import json
from matplotlib.colors import LinearSegmentedColormap
with open('my_cmap.json', 'r') as f:
    my_cmap = LinearSegmentedColormap("my_cmap", json.load(f))
```

You could save the object as a pickle. But, pickles are not safe and reading in the segment data is fairly quick.

*Original post and tutorial is located at [Custom Colormaps](http://schubert.atmos.colostate.edu/~cslocum/custom_cmap.html).*
Exemples can be found in [Turbulent flows over rough permeable beds](https://infoscience.epfl.ch/record/264790/files/EPFL_TH9327.pdf)
