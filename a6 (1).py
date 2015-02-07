# a6.py
# YOUR NAME(S) AND NETID(S) HERE
# DATE COMPLETED HERE
"""Classes to perform KMeans Clustering"""

import math
import random
import numpy

# HELPER FUNCTIONS FOR ASSERTS GO HERE
def is_point(thelist):
    """Return: True if thelist is a list of int or float"""
    if (type(thelist) != list):
        return False
    
    # All float
    okay = True
    for x in thelist:
        if (not type(x) in [int,float]):
            okay = False
    
    return okay


# CLASSES
class Dataset(object):
    """Instance is a dataset for k-means clustering.

    The data is stored as a list of list of numbers
    (ints or floats).  Each component list is a data point.

    Instance Attributes:
        _dimension [int > 0. Value never changes after initialization]:
            the point dimension for this dataset
        _contents  [a 2D list of numbers (float or int), possibly empty]:
            the dataset contents
        
    Additional Invariants:
        The number of columns in _contents is equal to _dimension.  That is,
        for every item _contents[i] in the list _contents, 
        len(_contents[i]) == dimension.
    
    None of the attributes should be accessed directly outside of the class
    Dataset (e.g. in the methods of class Cluster or KMeans). Instead, this class 
    has getter and setter style methods (with the appropriate preconditions) for 
    modifying these values.
    """
    
    def __init__(self, dim, contents=None):
        """Initializer: Makes a database for the given point dimension.
    
        The parameter dim is the initial value for attribute _dimension.  
  
        The optional parameter contents is the initial value of the
        attribute _contents. When assigning contents to the attribute
        _contents it COPIES the list contents. If contents is None, the 
        initializer assigns _contents an empty list. The parameter contents 
        is None by default.
    
        Precondition: dim is an int > 0. contents is either None or 
        it is a 2D list of numbers (int or float). If contents is not None, 
        then contents if not empty and the number of columns of contents is 
        equal to dim.
        """
        #assert type(dim) == int and dim > 0
        #assert type(contents) == list or None
        #assert of columns in contents = dim
        #FINISH ASSERT STATEMENTS
        self._dimension = dim
        if contents is None:
            self._contents= []
        
        
        else:
            numrows = len(contents)
            numcols = len(contents[0]) # All rows have same no. cols
            result = [] # Result accumulator 
            for m in range(numrows):
                row = [] # Single row accumulator
                for n in range(numcols):
                    row.append(contents[m][n]) # Build up row
                result.append(row) # Add result to table
            self._contents = result
    

    
    
    def getDimension(self):
        """Return: The point dimension of this data set.
        """
        return self._dimension
    
    
    def getSize(self):
        """Return: the number of elements in this data set.
        """
        return len(self._contents)

    
    def getContents(self):
        """Return: The contents of this data set as a list.
        
        This method returns the attribute _contents directly.  Any changes
        made to this list will modify the data set.  If you want to access
        the data set, but want to protect yourself from modifying the data,
        use getPoint() instead.
        """
        
        return self._contents
        
    
    def getPoint(self, i):
        """Returns: A COPY of the point at index i in this data set.
        
        Often, we want to access a point in the data set, but we want a copy
        to make sure that we do not accidentally modify the data set.  That
        is the purpose of this method.  
        
        If you actually want to modify the data set, use the method getContents().
        That returns the list storing the data set, and any changes to that
        list will alter the data set.
        While it is possible, to access the points of the data set via
        the method getContents(), that method 
        
        Precondition: i is an int that refers to a valid position in the data
        set (e.g. i is between 0 and getSize()).
        """
        numrows = len(self._contents)
        numcols = len(self._contents[0]) # All rows have same no. cols
        result = [] # Result accumulator 
        for m in range(numrows):
            row = [] # Single row accumulator
            for n in range(numcols):
                row.append(self._contents[m][n]) # Build up row
            result.append(row) # Add result to table
        a = result
        return a[i]
    
    
    def addPoint(self,point):
        """Adds a COPY of point at the end of _contents.
        
        This method does not add the point directly. It adds a copy of the point.
    
        Precondition: point is a list of numbers (int or float),  
        len(point) = _dimension.
        """
        a = point[:]
        self._contents.append(a)
       
        
    # PROVIDED METHODS: Do not modify!
    def __str__(self):
        """Returns: String representation of the centroid of this cluster."""
        return str(self._contents)
    
    def __repr__(self):
        """Returns: Unambiguous representation of this cluster. """
        return str(self.__class__) + str(self)


class Cluster(object):
    """An instance is a cluster, a subset of the points in a dataset.

    A cluster is represented as a list of integers that give the indices
    in the dataset of the points contained in the cluster.  For instance,
    a cluster consisting of the points with indices 0, 4, and 5 in the
    dataset's data array would be represented by the index list [0,4,5].

    A cluster instance also contains a centroid that is used as part of
    the k-means algorithm.  This centroid is an n-D point (where n is
    the dimension of the dataset), represented as a list of n numbers,
    not as an index into the dataset.  (This is because the centroid
    is generally not a point in the dataset, but rather is usually in between
    the data points.)

    Instance attributes:
        _dataset [Dataset]: the dataset this cluster is a subset of
        _indices [list of int]: the indices of this cluster's points in the dataset
        _centroid [list of numbers]: the centroid of this cluster
    Extra Invariants:
        len(_centroid) == _dataset.getDimension()
        0 <= _indices[i] < _dataset.getSize(), for all 0 <= i < len(_indices)
    """
    
    # Part A
    def __init__(self, ds, centroid):
        """A new empty cluster whose centroid is a copy of <centroid> for the
        given dataset ds.
    
        Pre: ds is an instance of a subclass of Dataset.
             centroid is a list of ds.getDimension() numbers.
        """
        a = centroid[:]
        self._dataset = ds
        self._centroid = a
        self._indices = []
        

    def getCentroid(self):
        """Returns: the centroid of this cluster.
        
        This getter method is to protect access to the centroid.
        """
        return self._centroid
        
        
    def getIndices(self):
        """Returns: the indices of points in this cluster
        
        This method returns the attribute _indices directly.  Any changes
        made to this list will modify the cluster.
        """
        
        return self._indices
        
    
    def addIndex(self, index):
        """Add the given dataset index to this cluster.
        
        If the index is already in this cluster, this method leaves the
        cluster unchanged.
        
        Precondition: index is a valid index into this cluster's dataset.
        That is, index is an int in the range 0.._dataset.getSize().
        """
        if index not in self._indices:
            self._indices.append(index)
    
    
    def clear(self):
        """Remove all points from this cluster, but leave the centroid unchanged.
        """
        self._indices = []
        
        
    def getContents(self):
        """Return: a new list containing copies of the points in this cluster.
        
        The result is a list of list of numbers.  It has to be computed from
        the indices.
        """
        a = []
        for x in self._indices:
            b = Dataset.getPoint(self._dataset,x)
            a.append(b)
        return a 
    
    
    # Part B
    def distance(self, point):
        """Return: The euclidean distance from point to this cluster's centroid.
    
        Pre: point is a list of numbers (int or float)
             len(point) = _ds.getDimension()
        """
        c=0
        length = len(self._centroid)
        for x in range(length):
            a= self._centroid[x] - point[x]
            b= a*a
            c = c + b
        return math.sqrt(c)
    
    
    def updateCentroid(self):
        """Returns: Trues if the centroid remains the same after recomputation,
        and False otherwise.
        
        This method recomputes the _centroid attribute of this cluster. The
        new _centroid attribute is the average of the points of _contents
        (To average a point, average each coordinate separately).  
    
        Whether the centroid "remained the same" after recomputation is
        determined by numpy.allclose.  The return value should be interpreted
        as an indication of whether the starting centroid was a "stable"
        position or not.
    
        If there are no points in the cluster, the centroid. does not change.
        """
        if self._indices == []:
            return True
        a = self.getContents()
        lengthrows = len(a)
        lengthcols = len(a[0])
        new = []
        for x in range(lengthcols):
            b = 0
            c = 0
            for y in range(lengthrows):
                b = b + a[y][x]
                c = c + 1
            pt = b/c
            new.append(pt)
        newcopy= self._centroid[:]
        self._centroid = new
        return numpy.allclose(newcopy, self._centroid)
            
        
    # PROVIDED METHODS: Do not modify!
    def __str__(self):
        """Returns: String representation of the centroid of this cluster."""
        return str(self._centroid)
    
    def __repr__(self):
        """Returns: Unambiguous representation of this cluster. """
        return str(self.__class__) + str(self)


class ClusterGroup(object):
    """An instance is a set of clusters of the points in a dataset.

    Instance attributes:
        _dataset [Dataset]: the dataset which this is a clustering of
        _clusters [list of Cluster]: the clusters in this clustering (not empty)
    """
    
    # Part A
    def __init__(self, ds, k, seed_inds=None):
        """A clustering of the dataset ds into k clusters.
        
        The clusters are initialized by randomly selecting k different points
        from the database to be the centroids of the clusters.  If seed_inds
        is supplied, it is a list of indices into the dataset that specifies
        which points should be the initial cluster centroids.
        
        Pre: ds is an instance of a subclass of Dataset.
             k is an int, 0 < k <= ds.getSize().
             seed_inds is None, or a list of k valid indices into ds.
        """
 
        self._dataset = ds
        mylist = []
        for x in range(k):
            rnumber = random.randrange(0, k)
            mylist.append(rnumber)
            
        if seed_inds == None:
            self._clusters = mylist
        else:
            self._clusters = seed_inds

    
    def getClusters(self):
        """Return: The list of clusters in this object.
        
        This method returns the attribute _clusters directly.  Any changes
        made to this list will modify the set of clusters.
        """ 
        return self._clusters

    # Part B
    def _nearest_cluster(self, point):
        """Returns: Cluster nearest to point
    
        This method uses the distance method of each Cluster to compute
        the distance between point and the cluster centroid. It returns
        the Cluster that is the closest.
        
        Ties are broken in favor of clusters occurring earlier in the
        list of self._clusters.
        
        Pre: point is a list of numbers (int or float),
             len(point) = self._dataset.getDimension().
        """
        # IMPLEMENT ME
        pass
    
    def _partition(self):
        """Repartition the dataset so each point is in exactly one Cluster.
        """
        # First, clear each cluster of its points.  Then, for each point in the
        # dataset, find the nearest cluster and add the point to that cluster.
        
        # IMPLEMENT ME
        pass
    
    # Part C
    def _update(self):
        """Return:True if all centroids are unchanged after an update; False otherwise.
        
        This method first updates the centroids of all clusters'.  When it is done, it
        checks whether any of them have changed. It then returns the appropriate value.
        """
        # IMPLEMENT ME
        pass
    
    def step(self):
        """Return: True if the algorithm converges after one step; False otherwise.
        
        This method performs one cycle of the k-means algorithm. It then checks if
        the algorithm has converged and returns the appropriate value.
        """
        # In a cycle, we partition the points and then update the means.
        # IMPLEMENT ME
        pass
    
    # Part D
    def run(self, maxstep):
        """Continue clustering until either it converges or maxstep steps 
        (which ever comes first).
        """
        # Call step repeatedly, up to maxstep times, until the algorithm
        # converges.  Stop after maxstep iterations even if the algorithm has not
        # converged.
        
        # IMPLEMENT ME
        pass
    
    # PROVIDED METHODS: Do not modify!
    def __str__(self):
        """Returns: String representation of the centroid of this cluster."""
        return str(self._clusters)
    
    def __repr__(self):
        """Returns: Unambiguous representation of this cluster. """
        return str(self.__class__) + str(self)

