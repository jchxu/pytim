# vim: set expandtab:
# vim: set tabstop=4:
""" Module: testsuite1
    ==================
"""

class testsuite1():

    """
    This is a collection of basic tests to check
    that code is running -- no test on the correctness
    of the output is performed here.
    
    
    >>> # TEST:1 basic functionality
    >>> import MDAnalysis as mda
    >>> import pytim 
    >>> from pytim.datafiles import *
    >>> u         = mda.Universe(WATER_GRO)
    >>> oxygens   = u.select_atoms("name OW") 
    >>> interface = pytim.ITIM(u, alpha=2.0, max_layers=4)
    >>> interface.assign_layers()
    >>> del interface
     
    >>> # TEST:2 large probe sphere radius 
    >>> interface = pytim.ITIM(u, alpha=100000.0, max_layers=1,multiproc=False)
    Traceback (most recent call last):
    	...
    AssertionError: parameter alpha in pytim.itim.ITIM must be smaller than the smaller box side
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()
