Cara Install
# $ pip install setup.py

Atau:

# $ python3 setup.py install

#---------------




import loading
total_file_size = 1000
# Create a loading bar object with total_file_size in bytes
lb = loadingbar.LoadingBar(total_file_size)

# For every piece of file
for chunk in file:
  # Update the loading bar with the len of new data
  lg.update(len(chunk))

# When finished, display a 100% loading bar
lg.done()
