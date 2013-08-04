import sys
sys.argv.append("-b")  # Enable batch mode
import ROOT

import tempfile
from IPython.core import display


def default_canvas(name="icanvas", size=(800, 600)):
    canvas = ROOT.gROOT.FindObject(name)
    assert len(size) == 2
    if canvas:
        return canvas
    else:
        return ROOT.TCanvas(name, name, size[0], size[1])


def display_canvas(canvas):
    file = tempfile.NamedTemporaryFile(suffix=".png")
    canvas.SaveAs(file.name)
    ip_img = display.Image(filename=file.name, format='png', embed=True)
    return ip_img._repr_png_()


def display_any(obj):
    file = tempfile.NamedTemporaryFile(suffix=".png")
    obj.Draw()
    ROOT.gPad.SaveAs(file.name)
    ip_img = display.Image(filename=file.name, format='png', embed=True)
    return ip_img._repr_png_()

# register display func with PNG formatter:
png_formatter = get_ipython().display_formatter.formatters['image/png']  # noqa

png_formatter.for_type(ROOT.TCanvas, display_canvas)
png_formatter.for_type(ROOT.TF1, display_any)
