import unittest

def suite():
    return unittest.TestLoader().discover("pathfinder.tests", pattern="*.py")
