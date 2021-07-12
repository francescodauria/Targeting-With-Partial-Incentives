import matplotlib.pyplot as plt



def fromStringArrayToIntArray (list):
    list2 = []
    for i in range(len(list)):
        try:
            t = int(list[i])
            list2.append(t)
        except: print()
    return list2

def plotFileIncentives(test, plt):
    f = open('Tests/lastfm_tests/test_'+test+'.csv')
    x = [0,1,2,3,4,5,6,7,8,9]
    # x axis values

    y = fromStringArrayToIntArray(f.readline().replace('[','').replace(']','').replace(' ','').split('.'))
    #print(y)
    # corresponding y axis values
    #y2 = fromStringArrayToIntArray(f.readline().replace('[','').replace(']','').replace(' ','').split('.'))
    #print(y2)
    # plotting the points 
    plt.plot(x, y, label="incentives "+test)
    #plt.plot(x, y2, label="remaining nodes "+test)

def plotFileNodes(test, plt):
    f = open('Tests/lastfm_tests/test_'+test+'.csv')
    x = [0,1,2,3,4,5,6,7,8,9]
    # x axis values

    y = fromStringArrayToIntArray(f.readline().replace('[','').replace(']','').replace(' ','').split('.'))
    #print(y)
    # corresponding y axis values
    y2 = fromStringArrayToIntArray(f.readline().replace('[','').replace(']','').replace(' ','').split('.'))
    #print(y2)
    # plotting the points 
    #plt.plot(x, y, label="incentives "+test)
    plt.plot(x, y2, label="remaining nodes "+test)


'''plotFileIncentives('pf', plt)
plotFileIncentives('pm', plt)
plotFileIncentives('pmf', plt)
plotFileIncentives('pp', plt)
plotFileIncentives('pr', plt)
plotFileIncentives('rf', plt)
plotFileIncentives('rm', plt)
plotFileIncentives('rmf', plt)
plotFileIncentives('rp', plt)
plotFileIncentives('rr', plt)
plt.title('LstFm dataset incetives')'''

plotFileNodes('pf', plt)
plotFileNodes('pm', plt)
plotFileNodes('pmf', plt)
plotFileNodes('pp', plt)
plotFileNodes('pr', plt)
plotFileNodes('rf', plt)
plotFileNodes('rm', plt)
plotFileNodes('rmf', plt)
plotFileNodes('rp', plt)
plotFileNodes('rr', plt)
plt.title('LastFm dataset remaining nodes')
# naming the x axis
plt.xlabel('iteration')
# naming the y axis
plt.ylabel('value')
plt.legend()
  
# giving a title to my graph

  
# function to show the plot
plt.show()

