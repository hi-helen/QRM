import pandas as pd
df = pd.read_excel(r'Downloads/SampleStock(1).xlsx')





def value_at_risk(returns, confidence_level):
    """
    Compute the Value-at-Risk metric of returns at confidence_level
    :param returns: DataFrame
    :param confidence_level: float
    :return: float
    """

    # Calculate the highest return in the lowest quantile (based on confidence level)
    var = returns.quantile(q=confidence_level, interpolation="higher")
    return var


def expected_shortfall(returns, confidence_level):
    """
    Compute the Value-at-Risk metric of returns at confidence_level
    :param returns: DataFrame
    :param confidence_level: float
    :return: float
    """

    # Calculate the VaR of the returns
    var = value_at_risk(returns, confidence_level)
    # Find all returns in the worst quantitle
    worst_returns = returns[returns.lt(var)]
    # Calculate mean of all the worst returns
    es = worst_returns.mean()

    return es
    
    
    
    
    
    
import numpy
def plot_alpha(returns):
    temp1 = []
    temp2 = []
    temp3 = []
    for alpha in numpy.arange(0.80,0.95,0.01):
        temp1.append(value_at_risk(returns, alpha))
        temp2.append(expected_shortfall(returns,alpha))
        temp3.append(alpha)
    return (temp1, temp2, temp3)   
    
    
    
    
    
    
    
outcome11 = plot_alpha(df['log_return1'])
import matplotlib.pyplot as plt
plt.scatter(outcome11[2], outcome11[0], color='skyblue')
plt.xlabel('alpha')
plt.ylabel('VaR')
obj1.savefig('alpha_VaR.png')
plt.show()








def plot_t(n):
    var = []
    es = []
    t = []
    for x in range(1,342):
        t.append(x)
        temp_returns = df["log_return"+str(n)][x:x+21]
        var.append(value_at_risk(temp_returns,0.95))
        es.append(expected_shortfall(temp_returns,0.95))

    plt.scatter(t, var, color='skyblue')
    plt.xlabel('t')
    plt.ylabel('VaR')
    plt.savefig('t_VaR'+str(n)+'.png')
    plt.show()

    plt.scatter(t, es, color='skyblue')
    plt.xlabel('t')
    plt.ylabel('ES')
    plt.savefig('t_ES'+str(n)+'.png')
    plt.show()
    
    
    
plot_t(1) 
