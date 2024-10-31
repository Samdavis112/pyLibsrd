"""
# LibSrd 

## Modules
image_convert.py  
merge_pdf.py  
table.py  

## Commands
1. ```mergepdfs```  
Will merge all pdf's found in the current directory, and save the result at: ./Output/Output.pdf  
  
2. ```imgconvert {InitalFormat} {FinalFormat}```  
Will convert all images of InitalFormat in current directory to FinalFormat in ./Output/
"""

from libsrd.image_convert import convert_images
from libsrd.merge_pdf import merge_pdfs
from libsrd.table import Table
from libsrd.__version__ import __version__

def _script():
	print(f"LibSrd v{__version__} - Sam Davis")