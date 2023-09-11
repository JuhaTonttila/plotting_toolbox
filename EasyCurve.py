#! /usr/bin/env python
from MyFigure import MyFigure
class Curve(MyFigure):
    
    def __init__(self,rows,cols,figsize,lc=None):
        super().__init__(rows,cols,figsize,lc)
        
    def plot(self,X,Y,ipanel,label=None,ls="-"):        
        panel = self.axes[ipanel]
        ax = panel.ax  # Just make it shorter...

        pl = ax.plot(X,Y,label=label,linewidth=3.0,ls=ls)
        panel.addPlot(pl)

    def setLegend(self,ipanel):
        panel = self.axes[ipanel]
        panel.ax.legend(fontsize=16)

    def setAxisScale(self,ipanel,xscale='linear',yscale='linear'):
            ax = self.axes[ipanel].ax
            ax.set_xscale(xscale)
            ax.set_yscale(yscale)