#!/usr/bin/env python3

# Darius Jones
# 12/5/2018



import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np



def part1():

	x = np.asarray([.00365, .00442, .00446, .00452, .00486, .00480, .00592, .00593])
	y = np.asarray([i for i in range(200, 280, 10)])

	
	slope, intercept, r_value, p_value, std_err = linregress(x,y)
	line = slope * x + intercept
	plt.plot(x, line, 'r', label=f' Linear Regression: y = {slope:.{4}f} (x) + {intercept:.{4}f} ')

	plt.scatter(x,y)	


	plt.title("Change to Mass Ratio of Elecetrons")
	plt.ylabel("V")
	plt.xlabel("(Ir)^2")
	plt.legend(fontsize=9)
	plt.show()

def main():
	part1()

if __name__ == '__main__':
	main()