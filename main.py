'''
pascal tree

      1
    1   1
  1   2   1
1   3   3   1

'''
# notes:
# length is first slide= 1
# it get's incremented by 1
# starting of each slide is 1


# taking input for steps
totalSteps= int(input('Enter the steps of triangle--> '))
series= []
firstSlide=[1]
listLen= 1

# creating the required steps with all 1's
for i in range(totalSteps):

    # generating 1's based upon listLen
    tempList= [1]*listLen

    # incrmenting the list length
    listLen += 1

    # adding this to the series list
    series.append(tempList)

# changing elements
for i in range(len(series)):

    # handling rows after second step
    if i > 1:

        # getting the current element
        element= series[i]
        prev_element= series[i - 1]
        
        # iterating through the element
        for i in range(len(element)):

            # skip the first and last element
            if i == 0 or i == len(element)-1:
                pass
            else:
                # this element is actually the sum of 2 elements above it in the previous list
                element[i]= prev_element[i] + prev_element[i - 1]

# printing the series in tree fasion
for row in series:
    print(row)



