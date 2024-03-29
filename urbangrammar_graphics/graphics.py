import seaborn as sns
from matplotlib.colors import ListedColormap, to_hex
import matplotlib.pyplot as plt
from random import shuffle
import numpy as np
from xyzservices import TileProvider

# 256 RGB codes
RGB = [
    (51, 52, 50),
    (59, 110, 141),
    (189, 91, 79),
    (144, 164, 126),
    (240, 200, 88),
    (149, 102, 110),
]

# 0-1 RGB codes
COLORS = [tuple(x / 256 for x in c) for c in RGB]

# HEX codes
HEX = [to_hex(c) for c in COLORS]

# diverging palette
DIVERGING = sns.diverging_palette(235, 16, 60, 44)

# diverging palette
DIVERGING_MPL = sns.diverging_palette(235, 16, 60, 44, as_cmap=True)

# matplotlib colormap
palette = sns.color_palette(COLORS)
CMAP = ListedColormap(palette)


def get_colormap(n=18, randomize=True):
    """ "Get expanded colormap"""
    n_colors = np.ceil(n / 6) + 1

    cols = []
    for col in COLORS:
        pal = sns.light_palette(col, n_colors=n_colors)
        for rgb in pal[1:]:
            cols.append(rgb)
    if randomize:
        shuffle(cols)  # shuffle to break grouping
    return ListedColormap(cols)


def get_tiles(tiles, token):
    """Get links to Mapbox tiles"""
    if tiles == "roads":
        return TileProvider(
            url="https://api.mapbox.com/styles/v1/martinfleis/ckl6jkuwe3uxa17mrhnp78e62/tiles/256/{z}/{x}/{y}@2x?access_token={accessToken}",
            attribution="(C) Mapbox (C) OpenStreetMap contributors",
            accessToken=token,
            name="MapBox Roads",
        )

    if tiles == "labels":
        return TileProvider(
            url="https://api.mapbox.com/styles/v1/martinfleis/ckl6n87ha0tol17o61wxhfnbo/tiles/256/{z}/{x}/{y}@2x?access_token={accessToken}",
            attribution="(C) Mapbox (C) OpenStreetMap contributors",
            accessToken=token,
            name="MapBox Labels",
        )
    if tiles == "background":
        return TileProvider(
            url="https://api.mapbox.com/styles/v1/martinfleis/ckl6okytj5fg317mvpgc9tc6k/tiles/256/{z}/{x}/{y}@2x?access_token={accessToken}",
            attribution="(C) Mapbox (C) OpenStreetMap contributors",
            accessToken=token,
            name="MapBox Background",
        )


def _make_location(ax, loc, legend_size=0.02, pad=0):
    """
    Construct the location bounds of a north arrow.

    Adapted from legendram, licensed under BSD-3-Clause License.


    Parameters:
    ----------
    ax          :   matplotlib.AxesSubplot
                    axis on which to add an arrow
    loc         :   string
                    valid legend location like that used in matplotlib.pyplot.legend
                    only string is supported
    legend_size :   float
                    float denoting the length/width of the a in terms
                    of a fraction of the axis.
    pad         :   float
                    additional padding
    Returns
    -------
    a list [left_anchor, bottom_anchor, width, height] in terms of plot units
    that defines the location and extent of the arrow.
    """
    position = ax.get_position()
    legend_width = position.width * legend_size
    legend_height = position.height * legend_size
    right_offset = position.width - legend_width
    top_offset = position.height - legend_height
    if loc.lower() == "lower left" or loc.lower() == "best":
        anchor_x, anchor_y = position.x0 + pad, position.y0 + pad
    elif loc.lower() == "lower center":
        anchor_x, anchor_y = position.x0 + position.width * 0.5, position.y0 + pad
    elif loc.lower() == "lower right":
        anchor_x, anchor_y = position.x0 + right_offset - pad, position.y0 + pad
    elif loc.lower() == "center left":
        anchor_x, anchor_y = position.x0 + pad, position.y0 + position.height * 0.5
    elif loc.lower() == "center":
        anchor_x, anchor_y = (
            position.x0 + position.width * 0.5,
            position.y0 + position.height * 0.5,
        )
    elif loc.lower() == "center right" or loc.lower() == "right":
        anchor_x, anchor_y = (
            position.x0 + right_offset - pad,
            position.y0 + position.height * 0.5,
        )
    elif loc.lower() == "upper left":
        anchor_x, anchor_y = position.x0 + pad, position.y0 + top_offset - pad
    elif loc.lower() == "upper center":
        anchor_x, anchor_y = (
            position.x0 + position.width * 0.5,
            position.y0 + top_offset - pad,
        )
    elif loc.lower() == "upper right":
        anchor_x, anchor_y = (
            position.x0 + right_offset - pad,
            position.y0 + top_offset - pad,
        )
    return [anchor_x, anchor_y, legend_width, legend_height]


def north_arrow(
    f,
    ax,
    rotation=0,
    loc="upper left",
    size=0.02,
    linewidth=3,
    color="k",
    pad=0,
    alpha=1,
):
    """
    Create north arrow

    Parameters
    ----------

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

    """
    from matplotlib.transforms import Affine2D

    arrpos = _make_location(ax, loc, legend_size=size, pad=pad)
    arrax = f.add_axes(arrpos)

    face = plt.Polygon([(0, 0), (0, 3), (-1.5, -0.5)], facecolor=color, alpha=alpha)
    edge = plt.Polygon(
        [(0, 0), (1.5, -0.5), (0, 3), (-1.5, -0.5)],
        edgecolor=color,
        facecolor="none",
        linewidth=linewidth,
        alpha=alpha,
    )

    t = Affine2D().rotate_deg(rotation) + arrax.transData
    face.set_transform(t)
    arrax.add_patch(face)
    edge.set_transform(t)
    arrax.add_patch(edge)
    arrax.axis("scaled")
    arrax.set_frame_on(False)
    arrax.get_yaxis().set_visible(False)
    arrax.get_xaxis().set_visible(False)
    return arrax


def get_signature_colors(name=True):
    """
    Get a dictionary of colors mapped to signatures classes of Great Britain

    Parameters
    ----------

    name : bool
        `True` maps to names, `False` maps to string keys (e.g. `'2_1'`)

    Returns
    -------
    dict
    """
    cols = get_colormap(20, randomize=False).colors

    key = {
        "0_0": cols[16],
        "1_0": cols[15],
        "3_0": cols[9],
        "4_0": cols[12],
        "5_0": cols[21],
        "6_0": cols[8],
        "7_0": cols[4],
        "8_0": cols[18],
        "2_0": cols[6],
        "2_1": cols[23],
        "2_2": cols[19],
        "9_0": cols[7],
        "9_1": cols[3],
        "9_2": cols[22],
        "9_3": cols[0],  # outlier
        "9_4": cols[11],
        "9_5": cols[14],
        "9_6": cols[0],  # outlier
        "9_7": cols[0],  # outlier
        "9_8": cols[0],  # outlier
    }

    if name:
        types = {
            "0_0": "Countryside agriculture",
            "1_0": "Accessible suburbia",
            "3_0": "Open sprawl",
            "4_0": "Wild countryside",
            "5_0": "Warehouse/Park land",
            "6_0": "Gridded residential quarters",
            "7_0": "Urban buffer",
            "8_0": "Disconnected suburbia",
            "2_0": "Dense residential neighbourhoods",
            "2_1": "Connected residential neighbourhoods",
            "2_2": "Dense urban neighbourhoods",
            "9_0": "Local urbanity",
            "9_1": "Concentrated urbanity",
            "9_2": "Regional urbanity",
            "9_4": "Metropolitan urbanity",
            "9_5": "Hyper concentrated urbanity",
            "9_3": "outlier",
            "9_6": "outlier",
            "9_7": "outlier",
            "9_8": "outlier",
        }

        return {v: key[k] for k, v in types.items()}

    return key
