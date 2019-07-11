"""
NAME
    Custom Colormaps for Matplotlib
PURPOSE
    This program shows how to implement make_cmap which is a function that
    generates a colorbar
PROGRAMMER(S)
    Chris Slocum
    Gauthier Rousseau
REVISION HISTORY
    20130411 -- Initial version created
    20140313 -- Small changes made and code posted online
    20140320 -- Added the ability to set the position of each color
    20150724 -- Attempted to make this more Pythonic
    20180307 -- Changed license to BSD 3-clause
    20190711 -- Added transprency (Alpha component) + different customized color maps + resolution of the colormap as an argument
"""
import numpy as np


def create_colormap(colors, position=None, bit=False, reverse=False, res=256, name='custom_colormap'):
    """
    returns a linear custom colormap

    Parameters
    ----------
    colors : array-like
        contain RGBA values. The RGBA values may either be in 8-bit [0 to 255]
        or arithmetic [0 to 1] (default).
        Arrange your tuples so that the first color is the lowest value for the
        colorbar and the last is the highest.
    position : array like
        contains values from 0 to 1 to dictate the location of each color.
    bit : Boolean
        8-bit [0 to 255] (in which bit must be set to
        True when called) or arithmetic [0 to 1] (default)
    reverse : Boolean
        If you want to flip the scheme
    res : integer
        Resolution of the colormap
    name : string
        name of the scheme if you plan to save it

    Returns
    -------
    cmap : matplotlib.colors.LinearSegmentedColormap
        cmap with equally spaced colors
    """
    from matplotlib.colors import LinearSegmentedColormap
    if not isinstance(colors, np.ndarray):
        colors = np.array(colors, dtype='f')
    if reverse:
        colors = colors[::-1]
    if position is not None and not isinstance(position, np.ndarray):
        position = np.array(position)
    elif position is None:
        position = np.linspace(0, 1, colors.shape[0])
    else:
        if position.size != colors.shape[0]:
            raise ValueError("position length must be the same as colors")
        elif not np.isclose(position[0], 0) and not np.isclose(position[-1], 1):
            raise ValueError("position must start with 0 and end with 1")
    if bit:
        colors[:] = [tuple(map(lambda x: x / 255., color)) for color in colors]
    cdict = {'red':[], 'green':[], 'blue':[], 'alpha':[]}
    for pos, color in zip(position, colors):
        cdict['red'].append((pos, color[0], color[0]))
        cdict['green'].append((pos, color[1], color[1]))
        cdict['blue'].append((pos, color[2], color[2]))
        cdict['alpha'].append((pos, color[3], color[3]))
    return LinearSegmentedColormap(name, cdict,res)

def make_cmap_customized(Palette='mountain',position=[0.0, 0.16, 0.2, 0.24, 0.4, 0.7, 0.8, 1],reverse=False,alpha=255):
    if Palette=='sunrise':
        couleur7=(0,0,0,alpha)
        couleur6=(64,50,79,alpha)
        couleur5=(107,64,110,alpha)
        couleur4=(141,76,125,alpha)
        couleur3=(172,85,122,alpha)
        couleur2=(210,124,124,alpha)
        couleur1=(240,206,125,alpha) 
        couleur0=(255,255,255,alpha)
    elif Palette=='green':
        couleur7=(0,0,0,alpha)
        couleur6=(6,49,50,alpha)
        couleur5=(28,78,78,alpha)
        couleur4=(55,140,129,alpha)
        couleur3=(172,185,153,alpha)
        couleur2=(199,205,181,alpha)
        couleur1=(232,219,194,alpha) 
        couleur0=(255,255,255,alpha)
    elif Palette=='mountain':
        couleur7=(0,0,0,alpha)
        couleur6=(45,52,70,alpha)
        couleur5=(89,76,96,alpha)
        couleur4=(145,101,118,alpha)
        couleur3=(212,119,127,alpha)
        couleur2=(212,153,154,alpha)
        couleur1=(238,189,184,alpha) 
        couleur0=(255,255,255,alpha)        
    elif Palette=='prune':
        couleur7=(0,0,0,alpha)
        couleur6=(66,37,67,alpha)
        couleur5=(125,58,91,alpha)
        couleur4=(107,77,131,alpha)
        couleur3=(205,179,214,alpha)
        couleur2=(164,173,154,alpha)
        couleur1=(207,213,199,alpha) 
        couleur0=(255,255,255,alpha)
    elif Palette=='asym_mountain5':
        couleur7=(45,52,70,alpha)
        couleur6=(110,86,96,alpha)
        couleur5=(135,90,115,alpha)
        couleur4=(145,101,118,alpha)   
        couleur3=(212,119,127,alpha)
        couleur2=(232,219,194,alpha) 
        couleur1=(167,213,229,alpha)    
        couleur0=(121,175,204,alpha)
        
    colors = [couleur0,couleur1,couleur2,couleur3,couleur4,couleur5,couleur6,couleur7]

    return create_colormap(colors, bit=True ,position=position,reverse=reverse,res=1000) 




if __name__ == "__main__":
    # An example of how to use make_cmap
    import matplotlib.pyplot as plt
    fig = plt.figure()
    ax = fig.add_subplot(311)
    # Create a list of RGB tuples
    colors = [(255, 0, 0,10), (255, 255, 0,70), (255, 255, 255,80), (0, 157, 0,255), (0, 0, 255,255)] # This example uses the 8-bit RGB
    # Call the function make_cmap which returns your colormap
    my_cmap = create_colormap(colors, bit=True)
    # Use your colormap
    plt.plot([0,50],[0,25],color='k',zorder=0)

    plt.text(25,12.5,'colormaps',zorder=0,horizontalalignment='center',verticalalignment='center',fontsize=30)
    plt.pcolor(np.random.rand(25, 50), cmap=my_cmap)

    plt.colorbar()
    ax = fig.add_subplot(312)

    plt.plot([0,50],[0,25],color='k',zorder=0)
    plt.text(25,12.5,'with',zorder=0,horizontalalignment='center',verticalalignment='center',fontsize=30)
    plt.pcolor(np.random.rand(25, 50), cmap=make_cmap_customized(Palette='green',alpha=255/4))
    plt.colorbar()

    ax = fig.add_subplot(313)
    colors = [(0.4, 0.2, 0.0,0.5), (1, 1, 1,0.2), (0, 0.3, 0.4,0.8)]
    # Create an array or list of positions from 0 to 1.
    position = [0, 0.3, 1]
    plt.plot([0,50],[0,25],color='k',zorder=0)
    plt.text(25,12.5,'transparency',zorder=0,horizontalalignment='center',verticalalignment='center',fontsize=30)
    plt.pcolor(np.random.rand(25, 50), cmap=make_cmap_customized(Palette='mountain',alpha=255/2))
    plt.colorbar()
    plt.savefig("example_custom_colormap.png")
    plt.show()
