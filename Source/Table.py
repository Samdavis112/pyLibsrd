import re
import tabulate
 
class Table:
	"""
	**Table**
 
	A table class for reading data from a tab seperated variable file.
 
	- Comments are supported, by default they are indicated with ! at the start of a line, but that can be changed.
	"""
 
	def __init__(self) -> None:
		self.Headers:list[str] = []
		self.Data:list[str] = []
	
	def __str__(self) -> str:
		"""Gets the table ready for displaying"""
		return tabulate.tabulate(self.Data, self.Headers, tablefmt="mixed_outline")

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
 
	@staticmethod
	def ConvertTSVLines(lines:list[str]):
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
	
	@staticmethod
	def ParseAndLoadTSV(Lines: str, commentChar="!"):
		"""Parse and load a TSV table into a table object from a string.
		Comments will be removed, settings loaded and TSV loaded."""
	
		table = Table()
	
		# Remove Comments
		Lines = re.sub(f"{commentChar}.*?\n", "", Lines)
	
		# Convert to array of strings
		lines = Lines.split("\n")
	
		# Remove all lines without tabs present
		for i in range(len(lines)-1, -1, -1):
			if "\t" not in lines[i]:
				lines.remove(lines[i])
	
		table.Headers, table.Data =  Table.ConvertTSVLines(lines)
		return table
	
	@staticmethod
	def OpenTSV(path:str, commentChar="!"):
		"""Read, parse and load a TSV table into a table object from a file path.
		Comments will be removed, settings loaded and TSV loaded."""
	
		# Read lines from filepath
		lines = open(path).read()
		table = Table.ParseAndLoadTSV(lines, commentChar)
	
		return table
