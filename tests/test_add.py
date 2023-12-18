
import sys
 
# setting path
sys.path.append('../jenkinsCourse')

from jenkinsCourse.add import add
def test_add():
    assert add(2,2)==4
