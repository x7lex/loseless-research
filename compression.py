"""
Goal: Create a simple compression algorithm. 
Objective: If duplicated_data is equal to 1 or 2 don't include it in COMPRESSED_DATA
    Because it either makes the data larger or adds more CPU work during decompression, or both.

Problems:
1. It still adds '2' to compressed data
    it shouldn't do that because during decompression it will waste time turning '2x' into 'xx'.

2. What if we had numbers in the data? 
    When we make our decompression algorithm this will be tricky to solve. 
    One of my proposals includes adding special characters around generated numbers.
        for example: ||3n|| so it wont be confused if there was an organic '3n' in the data.
"""

DATA = 'ann'
COMPRESSED_DATA = ""
duplicate_data = 1

# iterate through data.
# compare everything to eachother to find duplicates.

for i in range(1, len(DATA)):
    if DATA[i] == DATA[i - 1]:
        duplicate_data += 1

    # when it no longer meets the previous requirement:
    # add value to COMPRESSED_DATA of the previous sequence.
    # heads up: DATA i - 1 is the previous item we just compared.
    else:
        # safeguarding to prevent bloat.
        if duplicate_data >= 3:
            # include duplicate_data
            COMPRESSED_DATA += str(duplicate_data) + DATA[i - 1]
        else:
            COMPRESSED_DATA += DATA[i - 1]

        duplicate_data = 1 # Reset value back to 1


# Add the last group
COMPRESSED_DATA += str(duplicate_data) + DATA[-1]

print(COMPRESSED_DATA)
