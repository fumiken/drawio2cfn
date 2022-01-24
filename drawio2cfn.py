'''
Notes on use
  To generate the input file, you need to select [Extras] > [Configuration]
  from the menu on drawio and enter the following information.
  
{
  "compressXml": false
}
'''
from lib import main
import os

baseDir = os.path.dirname(os.path.abspath(__file__))
if __name__ == "__main__":
  main.main(baseDir)

