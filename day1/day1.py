def resultingFrequency(file):
    
    # Initialize current frequency 
    currentFrequency = 0

    # Open input file
    f = open(file, 'r')

    # Read in each line of input file
    for line in f:
        i = int(line)

        # Update current frequency
        currentFrequency = currentFrequency + i
        
    # Close file
    f.close()

    # Print and return current frequency
    print(currentFrequency)
    return currentFrequency



def twiceFrequency(file):

    # Initialize current frequency 
    currentFrequency = 0

    # Initialize a list of all frequencies
    # allFrequencies = [currentFrequency]

    # Intialize a SET of all frequencies
    # lists are slow (maintain order); sets are fast (but lose order)
    allFrequencies = {currentFrequency}

    # Initialize variable to hold first frequency reached twice
    twice = None

    while twice is None:
   
        with open(file, 'r') as f: 
            
            # Read in each line of input file
            for line in f:
                i = int(line)

                # Update current frequency
                currentFrequency = currentFrequency + i
                
                if currentFrequency in allFrequencies:
                    twice = currentFrequency
                    break

                # Add current frequency to list
                allFrequencies.add(currentFrequency)    

    # Print and return current frequency
    print(twice)
    return twice

resultingFrequency('day1input.txt')
# resultingFrequency('test1.txt')

twiceFrequency('day1input.txt')