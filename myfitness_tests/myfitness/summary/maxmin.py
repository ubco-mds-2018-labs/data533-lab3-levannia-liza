
# coding: utf-8

# In[ ]:


def getMax(data):
    """ Find the maximum number of steps in the data and the date it was achieved.
        Parameters:
            data: Pandas DataFrame containing Apple Health data imported from a
                  .csv file.
        Return:
            The row of values for when the maximum number of steps were achieved:
            Start date, Finish date, Distance(mi), Steps (count)"""


    import pandas as pd             # ensure pandas has been imported

    # find the row containing the maximum steps and return that row.
    maximum = data.loc[data['Steps (count)'].idxmax()]
    return maximum

def getMin(data):
    """ Find the maximum number of steps in the data and the date it was achieved.
        Parameters:
            data: Pandas DataFrame containing Apple Health data imported from a
                  .csv file.
        Return:
            The row of values for when the maximum number of steps were achieved:
            Start date, Finish date, Distance(mi), Steps (count)"""

    import pandas as pd             #ensure pandas has been imported

    # find the row containing the minimum steps and return that row.
    minimum = data.loc[data['Steps (count)'].idxmin()]
    return minimum
