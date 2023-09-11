import matplotlib.pyplot as plt
import numpy as np

class ColorParams:
    Ncol = 100 

    def __init__(self,minv=0.,maxv=1.,nticks=10,cmap=plt.get_cmap("jet"),color_levels=None,tick_levels=None):
        self.minv = minv
        self.maxv = maxv
        self.n = nticks
        self.cmap=cmap
        self.color_levels = color_levels 
        self.tick_levels = tick_levels
        self.norm = None

        # Add a check: either specify color and tick levels, or minv, max and nticks

    def getMinv(self):
        if self.color_levels == None:
            return self.minv
        else:
            return self.color_levels[0]

    def getMaxv(self):
        if self.color_levels == None:
            return self.maxv
        else:
            return self.color_levels[-1]

    def getTicks(self):
        if self.tick_levels == None:
            interval = (self.maxv-self.minv)/np.float(self.n)
            return np.arange(self.minv,self.maxv+0.01*interval,interval)
        else:
            return self.tick_levels

    def getClevs(self):
        if self.color_levels == None:
            interval = (self.maxv-self.minv)/np.float(self.Ncol)
            return np.arange(self.minv,self.maxv+0.01*interval,interval)
        else:
            return self.color_levels

    def setNormToClevs(self):
        import matplotlib.colors as cl
        self.norm = cl.BoundaryNorm(boundaries=self.getClevs(), ncolors=256)

    def getCmap(self):
        return self.cmap



class LineColors:

    import matplotlib.cm as cmx
    import matplotlib.colors as colors
    import matplotlib.pyplot as plt
    import numpy as np

    # Gets parameteres to specify colors in line plots according to a given colormap
    
    def __init__(self,colmap,values):

        # Specify colormap
        ccmap = LineColors.plt.get_cmap(colmap)
        # Normalize the color range to the given set of values
        cNorm = LineColors.colors.Normalize(vmin=LineColors.np.min(values),vmax=LineColors.np.max(values))
        # Get the RGB map
        self.__rgbmap = LineColors.cmx.ScalarMappable(norm=cNorm,cmap=ccmap)

        
    def getColor(self,val):
        return self.__rgbmap.to_rgba(val)
