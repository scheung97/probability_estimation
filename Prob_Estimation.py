from scipy import special as sp
import math as m

def qfunc(x):
    return 0.5-0.5*sp.erf(x/m.sqrt(2))
def invQfunc(x):
    return m.sqrt(2)*sp.erfinv(1-2*x)

def prob_estimation(p_percentage, n, confidence_percentage):
    alpha = ((-1)*(confidence_percentage - 1))/2
    alpha = invQfunc(alpha) #leaves us with alpha*sqrt(n)
    alpha /= m.sqrt(n)

    p_percentage_2 = p_percentage**2
    alpha = alpha**2

    p_1 = ((2.0* p_percentage + alpha) - m.sqrt((2*p_percentage + alpha)**2 - 4*(1+alpha)*(p_percentage_2)))/(2*(1+alpha))

    p_2 = ((2.0* p_percentage + alpha) + m.sqrt((2*p_percentage + alpha)**2 - 4*(1+alpha)*(p_percentage_2)))/(2*(1+alpha))

    p_1_percent=p_1*100
    p_2_percent=p_2*100
    return [p_1,p_2], [p_1_percent, p_2_percent]


def main():
    p_percentage = .0011 #estimate of p (in decimal) --> positive_results/sample_group_size
    #please input this value as a decimal

    n = 2790 #sample_group_size

    confidence_percentage = 0.99 #confidence percentage (in decimal)

    total_population = 13500 #if needed

    """

    """

    raw, percent = prob_estimation(p_percentage, n, confidence_percentage)
    print("p_1 and p_2 raw values: " +str(raw))
    print("Confidence Interval: [" + str(raw[0]*total_population) + " " + str(raw[1]*total_population) + "]")
    print() #empty print for spacing
    print("p_1 and p_1 as percentages: " + str(percent))


if __name__ == "__main__":
    main()
