class MyFigure():

    # Creates and holds a Figure instance and axes instances.
    # --------------------------------------------------------
    def __init__(self,rows,cols,figsize,cp=None):
        from matplotlib import pyplot as plt
        
        self.fig = plt.figure(figsize=figsize)  # Figure instance
        self.axes = []                          # List of AxesAndPlots instances
        self.n = 0                              # Total number of axes instances
        self.rows = 0                           # Number of panel rows
        self.cols = 0                           # Number of panel columns
        self.cp = cp                            # ColorParams or LineColors instance, assumed to hold for entire figure
        
        self.add_panels(rows,cols)

    def add_panels(self,rows,cols):
        from itertools import chain
        from AxesAndPlots import AxesAndPlots
        import numpy as np
        from matplotlib.pyplot import subplots_adjust

        sp = self.fig.subplots(rows,cols) 
        self.rows=rows
        self.cols=cols
        if rows==1 and cols==1:
            self.axes.append(AxesAndPlots(1,sp))
            sp.grid()
        else:
            for i in sp.flatten():
                self.axes.append(AxesAndPlots(self.n,i))
                self.n+=1
                i.grid()

        subplots_adjust(left=0.1,bottom=0.1,right=0.9,top=0.9,wspace=0.4,hspace=0.24)

    # Set labels, titles etc
    def setAttributes(self,ipanel,title=None,xlabel=None,ylabel=None,grid=True):
        # ipanel can be an integer (i.e. set labels for single panel )or list of integers
        # (for  several panels). In case of the latter, provided labels must be single
        # strings (apply same for all) or a list of strings with len(label) == len(ipanel)

        if type(ipanel) == list:
            # check if labels are suitable lists or single strings

            for i in ipanel:
                panel = self.axes[i]
                ax = panel.ax

                self.__setAtt(ax,title,"title",ind=i)
                self.__setAtt(ax,xlabel,"xlabel",ind=i)            
                self.__setAtt(ax,ylabel,"ylabel",ind=i)
                ax.grid(visible=grid)

        elif type(ipanel) == int:
            panel = self.axes[ipanel]
            ax = panel.ax
            self.__setAtt(ax,title,"title")
            self.__setAtt(ax,xlabel,"xlabel")
            self.__setAtt(ax,ylabel,"ylabel")
            ax.grid(visible=grid)

        else:
            print("MyFigure:setAttributes: ipanel must be int or list of ints")

    def __setAtt(self,ax_,entry_,which,ind=0):
        if type(entry_) == list:
            entry = entry_[ind]
        else:
            entry = entry_

        if which == "title":
            if self.__requireType(entry,str,"setAttributes:title"):
                ax_.set_title(entry,fontsize=16)
        elif which == "xlabel":
            if self.__requireType(entry,str,"setAttributes:xlabel"):
                ax_.set_xlabel(entry,fontsize=16)
        elif which == "ylabel":
            if self.__requireType(entry,str,"setAttributes:ylabel"):
                ax_.set_ylabel(entry,fontsize=16)
        # else ERROR HANDLING

    def __requireType(self,entry,reqtype,source):
        if entry != None:
            if type(entry) == reqtype:
                return True
            else:
                raise TypeError("MyFigure:"+source+": required",reqtype)
        else:
            return False

    # Get indices for edge panels in multipanel plots
    def getLeftPanels(self):
        out = []
        for i in range(0,self.rows):
            out.append(i*self.cols)
        return out

    def getRightPanels(self):
        out = []
        for i in range(0,self.rows):
            out.append(i*self.cols + self.cols-1)
        return out

    def getTopPanels(self):
        out = []
        for i in range(0,self.cols):
            out.append(i)
        return out

    def getBottomPanels(self):
        out = []
        start = (self.rows-1)*self.cols
        for i in range(0,self.cols):
            out.append(start + i)
        return out

