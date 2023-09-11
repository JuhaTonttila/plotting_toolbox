from MyFigure import MyFigure

# Subclass for MyFigure including plot and colorbar methods for contour plots
# ----------------------------------------------------------------------------
class Contourf(MyFigure):
    def __init__(self,rows,cols,figsize,cp=None,extend="neither"):
        super().__init__(rows,cols,figsize,cp=cp) 

        self.extend = extend

    def plot(self,X,Y,Z,ipanel):
        #cp = self.cp

        panel = self.axes[ipanel]
        ax = panel.ax

        #levels=self.cp.getClevs(), vmin=self.cp.getMinv(),vmax=self.cp.getMaxv(),
        if self.cp != None:
            pp = ax.contourf(X,Y,Z, norm=self.cp.norm, \
                             levels=self.cp.getClevs(),extend=self.extend,cmap=self.cp.getCmap())
        else:
            pp = ax.contourf(X,Y,Z,)

        panel.addPlot(pp)

    def set_colorbar(self,label=None): 
        import matplotlib.cm as cm
        import matplotlib.pyplot as plt

        # Sets a common colorbar for all the subplots.
        # The first panel is used as the mappable, and 
        # assumed to be valid for all others.
        cax = plt.axes([0.93, 0.1, 0.01, 0.8])
        bar = plt.colorbar(self.axes[0].pic[0],cax=cax,ticks=self.cp.getTicks())
        bar.ax.set_ylabel(label,fontsize=16)
 
