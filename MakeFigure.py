
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib.ticker as mtick
import sys

class Figure():

    def __init__(self,number_of_panels,shape,size=(8,8),colorbar_axes=False):

        x = shape[0]
        y = shape[1]

        if x*y < number_of_panels:
            print("class Figure: init: Error - number of panels > shape")
            sys.exit(0)
            
        self.fig = plt.figure(num=None,figsize=size)  # Figure instance
        self.sp = []                                  # List of Panel instances for subplots
        for i in range(1,number_of_panels+1):
            self.sp.append(Panel(self.fig.add_subplot(y,x,i)))
            
        self.colorbar_axes = colorbar_axes            # Whether to create separate colorbar axes
 
        self.cax = []                                 # List of colorbar axes instances
        if colorbar_axes:
            for s in self.sp:
                divider = make_axes_locatable(s.ax)
                hlp = divider.new_horizontal(size="5%",pad=0.7,pack_start=True)
                self.cax.append(self.fig.add_axes(hlp))

    def adjust(self,left,right,bottom,top,wspace,hspace):

        self.fig.subplots_adjust(left=left,bottom=bottom,      \
                                 right=right, top=top,         \
                                 wspace=wspace, hspace=hspace  )
        
    def clearSubplots(self):
        for s in self.sp:
            s.ax.clear()
            
        if self.colorbar_axes:
            for c in self.cax:
                c.clear()
        
    def getAllAxes(self):
        return [s.ax for s in self.sp]

    def getAxes(self,i_subplot):
        return self.sp[i_subplot].ax

    def storePlot(self,i_subplot,store):
        self.sp[i_subplot].savePlot(store)
        
    def showGrid(self,i=None):
        # if i is not present, show grid for all subplots
        if i != None:
            self.sp[i].ax.grid()
        else:
            for ss in self.sp:
                ss.ax.grid()

    def hideEveryNthTickX(self,i_subplot,N):
        for label in self.sp[i_subplot].ax.xaxis.get_ticklabels()[::N]:
            label.set_visible(False)
    def showEveryNthTickX(self,i_subplot,N):
        for label in self.sp[i_subplot].ax.get_xticklabels():
            label.set_visible(False)
        for label in self.sp[i_subplot].ax.get_xticklabels()[::N]:
            label.set_visible(True)
    def hideEveryNthTickY(self,i_subplot,N):
        for label in self.sp[i_subplot].ax.yaxis.get_ticklabels()[::N]:
            label.set_visible(False)

    def setAttributes(self,i_subplot,fontsize=16,title=None,xlabel=None,ylabel=None,  \
                      x_log=False,y_log=False,sci_x_ticks=False,sci_y_ticks=False):

        if title != None:
            self.sp[i_subplot].ax.set_title(title,fontsize=fontsize)
        if xlabel != None:
            self.sp[i_subplot].ax.set_xlabel(xlabel,fontsize=fontsize)
        if ylabel != None:
            self.sp[i_subplot].ax.set_ylabel(ylabel,fontsize=fontsize)
        if x_log:
            self.sp[i_subplot].ax.set_xscale("log",nonposx="clip")
        if y_log:
            self.sp[i_subplot].ax.set_yscale("log",nonposy="clip")
        if sci_x_ticks:
            self.sp[i_subplot].ax.xaxis.set_major_formatter(mtick.FormatStrFormatter('%.1e'))
        if sci_y_ticks:
            self.sp[i_subplot].ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.1e'))

    def setLimits(self,i_subplot,xlims=None,ylims=None):
        # xlims and ylims should be tuple e.g. (xmin,xmax)

        if xlims != None:
            self.sp[i_subplot].ax.set_xlim(xlims)
        if ylims != None:
            self.sp[i_subplot].ax.set_ylim(ylims)
        
    def getPlots(self,i_subplot,Nth_plot=None):
        # Gets the plots list from Panel instance for subplot i_subplot
        # or the Nth_plot from every cell in plots.
        
        if Nth_plot == None:
            # Return all plot instances for current axes
            ll = [pl.draws[:] for pl in self.sp[i_subplot].plots]
            return [cc for cur in ll for cc in cur]

        elif Nth_plot > 0:
            # return the Nth plot instance from every set for current axes
            return [pl.draws[Nth_plot-1] for pl in self.sp[i_subplot].plots]

        elif Nth_plot < 0:
            # Return the plot instances from Nth set for current axes
            ll = [pl.draws[:] for pl in self.sp[i_subplot].plots]
            return ll[-Nth_plot-1]

class Panel():

    def __init__(self,ax):

        self.ax = ax    # Holds the axes instance
        self.plots = [] # Save plots here

    def savePlot(self,plotInstance):
        self.plots.append(plotInstance)
