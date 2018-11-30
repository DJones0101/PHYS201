#!/usr/bin/env python3


import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np



def part1():

	x = np.asarray([i for i in range(20, 210, 10)])
	y = np.asarray([6.7,9.8,13.5,16.6,20.1,23.5,26.6,29.9,33.0,36.4,39.6,42.8,46.3,49.9,53.0,56.5,59.9,63.2,66.3,])

	
	slope, intercept, r_value, p_value, std_err = linregress(x,y)
	line = slope * x + intercept
	plt.plot(x, line, 'r', label=f' Linear Regression: y = {slope:.{4}f} (x) + {intercept:.{4}f} ')

	plt.scatter(x,y)
	plt.xticks(np.arange(min(x), max(x)+1, 10))
	plt.yticks(np.arange(min(y), max(y)+1, 10))


	plt.title("Axial Magnetic Field")
	plt.ylabel("B (Gauss)")
	plt.xlabel("I (mA)")
	plt.legend(fontsize=9)
	plt.show()

def main():
	part1()

if __name__ == '__main__':
	main()