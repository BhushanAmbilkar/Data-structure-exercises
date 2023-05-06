# Exercise 3: Slice list into 3 equal chunks and reverse each chunk

# Given:
#
# sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]

# Show Hint
# Divide the length of a list by 3 to get the each chunk size
# Run loop three times and use the slice() function to get the chunk and reverse it

# Show Solution
# Get the length of a list using a len() function
# Divide the length by 3 to get the chunk size
# Run loop three times
# In each iteration, get a chunk using a slice(start, end, step) function and reverse it using the reversed() function
# In each iteration, start and end value will change

sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
print("Original list ", sample_list)

length = len(sample_list)
chunk_size = int(length / 3)
start = 0
end = chunk_size

# run loop 3 times
for i in range(3):
    # get indexes
    indexes = slice(start, end)

    # get chunk
    list_chunk = sample_list[indexes]
    print("Chunk ", i, list_chunk)

    # reverse chunk
    print("After reversing it ", list(reversed(list_chunk)))

    start = end
    end += chunk_size


