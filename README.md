# Urban Grammar AI graphics
Visual style for Urban Grammar AI research project

See the Jupyter notebook in `examples` for an illustration of usage.

Available visual presets:

- `RGB` - 0-256 RGB codes
- `COLORS` - 0-1 RGB codes
- `HEX` - HEX codes
- `DIVERGING` - diverging seaborn palette
- `CMAP` - matplotlib colormap (6 primary colors)
- `get_colormap(n=18, randomize=True)` - Get expanded colormap
- `get_tiles(tiles, token)` - Get links to Mapbox tiles. `tiles` can be `"roads"`, `"labels"` or `"background"`

- `north_arrow(f, ax, rotation=0, loc="upper left", size=0.02, linewidth=3, color="k", pad=0, alpha=1,)` - Create north arrow

```
north_arrow parameters
----------------------

f : figure

ax: axis

rotation : float
    rotation of an arrow (in case map is rotated)

loc : string
    location of an arrow

size : float
    float denoting the length/width in terms
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