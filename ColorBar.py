#! /usr/bin/env python

import matplotlib.pyplot as plt

class ColorBar():

    def __init__(self,icolp,ipic,iax,icax=None,tickformat=None,orientation="horizontal"):

        print(icax)
        # Arguments:
        # icolp = ColorParams instance
        # ipic = contourf etc instance
        # iax = axes instance
        # icax = optional coloraxes instance

        pad = 0.05
        if orientation == "horizontal":
            pad = 0.4

        self.cb = plt.colorbar(ipic,ax=iax,cax=icax,ticks=icolp.getTicks(),orientation=orientation,format=tickformat,pad=pad)
