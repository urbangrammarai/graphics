# graphics
Visual style for Urban Grammar AI research project

Available visual presets:

- `RGB` - 256 RGB codes
- `COLORS` - 0-1 RGB codes
- `DIVERGING` - diverging seaborn palette
- `CMAP` - matplotlib colormap (6 primary colors)
- `get_colormap(n=18, randomize=True)` - Get expanded colormap
- `get_tiles(tiles, token)` - Get links to Mapbox tiles. `tiles` can be `"roads"`, `"labels"` or `"background"`

- `north_arrow(f, ax, rotation=0, loc="upper left", size=0.02, linewidth=3, color="k", pad=0, alpha=1,)` - Create north arrow

```rst
north_arrow parameters
----------------------

f : figure

ax: axis

rotation : float
    rotation of an arrow (in case map is rotated)

loc : string
    location of an arrow

size : float
    float denoting the length/width of the a in terms
    of a fraction of the axis.

linewidth : float
    linewidth

color : string
    color of an arrow

pad : float
    additional padding

alpha : float
    alpha
```