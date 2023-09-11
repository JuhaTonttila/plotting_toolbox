#! /usr/bin/env python

# Holds an Axes instance and related plots instances
# ---------------------------------------------------
class AxesAndPlots():

    def __init__(self,n,ax):
        self.ax = ax      # Axes instance
        self.pic = []     # List for plot instances within the axes 
        self.N = n        # Index for the instance

    # Add new plot instance for the axes
    def addPlot(self,plot):
        self.pic.append(plot)

