#! /usr/bin/env python

import netCDF4 as nc

class NCFile(object):

    def __init__(self,ifile,mode="r"):
        self.ncid = nc.Dataset(ifile,mode)

    def NcClose(self):
        self.ncid.close()


class NcInput(NCFile,object):

    def __init__(self,ifile,dimNames,varNames,ranges=dict()):
        super(NcInput,self).__init__(ifile,mode="r")
        
        # Inputs: ifile - input filename (full path)
        #         varnames - List of variable names to be read
        #         dimnames - List of dimension names to be read (as vectors?)
        #         ranges - Dict of tuples specifying subranges for the input data, i.e.
        #                  [(xmin:xmax),(ymin:ymax),(zmin:zmax),...]. Can have any number
        #                  of dimensions (limited by the dimensions of the data of course).
        #                  Empty dict says to discard this and just read in full arrays.
        #                  The keys should be the same as dimnames
        
        self.dimensions = self._readData(dimNames,ranges)

        self.data = self._readData(varNames,ranges)
        
        
    def _readData(self,names,ranges):

        values = dict()

        for nn in names:

            # Tuple of dimension names for current variable
            varDims = self.ncid.variables[nn].dimensions

            # Get the lengths of each of the dimensions for current variable
            varLengths = self.ncid.variables[nn].shape
            
            # Get a tuple of booleans telling weather a subrange is specified for
            # each of the dimensions of the current variable
            useRanges = self._checkBooleanRanges(varDims,ranges)
            
            # Construct a list of tuples for the dimension indices
            indices = self._getVarIndices(varDims,varLengths,useRanges,ranges)
            
            # Fetch the data
            values.update(self._fetchData(nn,indices))

        return values

    def _checkBooleanRanges(self,vardims,ranges):

        # Check for current list of dimension names whether a subrange 
        # is defined for each of them and return a corresponding boolean tuple

        useRanges = []
        for vd in vardims:
            useRanges.append( vd in ranges.keys() )

        return tuple(useRanges)

    def _getVarIndices(self,varDims,varLengths,useRanges,ranges):
        
        # Gets a list of tuples containing min and max indices for each
        # dimension to be used for the input

        indices = []
        ii = 0
        for vv in zip(varDims,useRanges):

            if vv[1]:
                # User specified range available
                indices.append(ranges[vv[0]])
            else:
                # User specified range not available => use the full length
                indices.append((0,varLengths[ii]+1))

            ii+=1

        return indices


    def _fetchData(self,var,indices):

        # Fetch the actual data with given attributes (indexing etc.)
        # For now the max number of dimensions shall be 4
        

        ndims = len(indices)
        
        if ndims == 1:
            tmp = self.ncid.variables[var][indices[0][0]:indices[0][1]]

        elif ndims == 2:
            tmp = self.ncid.variables[var][indices[0][0]:indices[0][1],   \
                                           indices[1][0]:indices[1][1]]
        elif ndims == 3:
            tmp = self.ncid.variables[var][indices[0][0]:indices[0][1],   \
                                           indices[1][0]:indices[1][1],   \
                                           indices[2][0]:indices[2][1]]
        elif ndims == 4:
            tmp = self.ncid.variables[var][indices[0][0]:indices[0][1],   \
                                           indices[1][0]:indices[1][1],   \
                                           indices[2][0]:indices[2][1],   \
                                           indices[3][0]:indices[3][1]]   
        elif ndims == 5:
            tmp = self.ncid.variables[var][indices[0][0]:indices[0][1],   \
                                           indices[1][0]:indices[1][1],   \
                                           indices[2][0]:indices[2][1],   \
                                           indices[3][0]:indices[3][1],   \
                                           indices[4][0]:indices[4][1]]

            
        # In case some dimension subranges define a slice (dimension length == 1), use numpy.squeeze to get rid of 
        # the truncated dimensions
        return {var:tmp.squeeze()}
 
