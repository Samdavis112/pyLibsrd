import re
import tabulate
 
class Table:
    """
    **Table**
 
    A table class for reading data from a tab seperated variable file.
 
    - Comments are supported, by default they are indicated with ! at the start of a line, but that can be changed.
    - Table settings are supported. By default they are indicated with # at the start of a line, but that can be changed. They will be loaded into a dict named TableSettings and then can be accessed like regular settings. They must take the format -> settingName=setting
    """
 
    def __init__(self) -> None:
        self.Headers:list[str] = []
        self.Data:list[str] = []
        self.TableSettings:dict = dict()
 
    def GetColIndex(self, colname: str) -> None | int:
        """Finds the index of a certain column in a table from its name. Will return None if column isn't found."""
        colindex = None
       
        for header in self.Headers:
            if header.lower() == colname.lower():
                colindex = self.Headers.index(header)
 
        return colindex
 
    def ReadColumn(self, colname: str) -> list[str] | None:
        """Will return a 1D list representing all the data within a certain column, from its name. Will return None if column not found."""
        colindex = self.GetColIndex(colname)
 
        # return nothing if column not found.
        if colindex == None:
            return None
 
        data = []
 
        # Add data from each row that is in the requested col to a list.
        for row in self.Data:
            data.append(row[colindex].strip())
 
        return data
   
    def ReadColumnIndex(self, colindex: int) -> list[str] | None:
        """Will return a 1D list representing all the data within a certain column, from its index. Will return None if column not found."""
 
        # return nothing if column not found.
        if colindex > len(self.Headers):
            return None
 
        data = []
 
        # Add data from each row that is in the requested col to a list.
        for row in self.Data:
            data.append(row[colindex].strip())
 
        return data
 
    def __str__(self) -> str:
        """Gets the table ready for displaying"""
        string = f"Settings:\n{self.TableSettings.__str__()}\n\n"
        string += tabulate.tabulate(self.Data, self.Headers, tablefmt="simple_grid")
        return string
 
def ConvertTSVLines(lines:list[str]) -> tuple[list, list]:
    """Just get headers and data from a TSV string list. No comment or settings handling."""
    headers = []
    data = []
    NumHeaders = 0
 
    for i in range(len(lines)):
        lines[i] = lines[i].replace("\n", "")  # Remove newline chars
        temp = lines[i].split("\t")  # Split by tabs
 
        if i == 0:  # If header
            NumHeaders = len(temp)
            headers = temp
        else:
            # Append blank cols, until column count the same as header
            while len(temp) < NumHeaders:
                temp.append("")
            data.append(temp)
 
    return headers, data
 
def ParseAndLoadTSV(Lines: str, commentChar="!", settingChar="#") -> list[list[str]]:
    """Parse and load a TSV table into a table object from a string.
    Comments will be removed, settings loaded and TSV loaded."""
 
    table = Table()
 
    # Remove Comments
    Lines = re.sub(f"{commentChar}.*?\n", "", Lines)
 
    # Convert to array of strings
    lines = Lines.split("\n")
 
    # Read settings from lines
    for i in range(len(lines)):    
        if len(lines[i]) > 0 and lines[i][0] == settingChar:
            lines[i] = lines[i].removeprefix(settingChar) # Remove the settings character
            lines[i] = lines[i].removesuffix("\n")
            array = lines[i].split("=")
 
            if(len(array) == 2):
                array[0] = array[0].strip()
                array[1] = array[1].strip()
                table.TableSettings.update({array[0]:array[1]}) # Add settings to dict
 
    # Remove all lines without tabs present
    for i in range(len(lines)-1, -1, -1):
        if "\t" not in lines[i]:
            lines.remove(lines[i])
 
    table.Headers, table.Data =  ConvertTSVLines(lines)
    return table
 
def OpenTSV(path:str, commentChar="!", settingChar="#") -> Table:
    """Read, parse and load a TSV table into a table object from a file path.
    Comments will be removed, settings loaded and TSV loaded."""
 
    # Read lines from filepath
    lines = open(path).read()
    table = ParseAndLoadTSV(lines, commentChar, settingChar)
 
    return table
