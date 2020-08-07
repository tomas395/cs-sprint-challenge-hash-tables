# Given a list of full paths to files, and a list of filenames to query,
# report all the full paths that match that filename.

# Example input:

# ```python
# paths = [
#     "/usr/local/share/foo.txt",
#     "/usr/bin/ls",
#     "/home/davidlightman/foo.txt",
#     "/bin/su"
# ]

# queries = [
#     "ls",
#     "foo.txt",
#     "nosuchfile.txt"
# ]
# ```

# Example return value:

# ```
# [ "/usr/local/share/foo.txt", "/usr/bin/ls", "/home/davidlightman/foo.txt" ]
# ```

# because that's where the `foo.txt` and `ls` files are. 

# The file `"nosuchfile.txt"` is ignored because it's not in the `paths`.

# Return list can be in any order.

# Limits:

# * Up to approximately 1,000,000 paths.
# * Up to approximately 1,000,000 queries.


def finder(files, queries):
    cache = {}
    results_list = []

# set up cache
    for f in files:
        sections = f.split("/") # splitting every path on the slash so i know all the values 
        file_name = sections[-1] # get the filename after the last slash 
        
        if file_name not in cache: # if the filename isn't in the cache, create an empty list for it
            cache[file_name] = []
        cache[file_name].append(f) # group all the filenames with the paths and add it to the cache

# compare queries to cache
    for q in queries:
        if q in cache: 
            results_list.extend(cache[q]) # iterate through and combine all the paths to the results_list and return it

    return results_list

if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
