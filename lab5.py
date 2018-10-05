#!/usr/bin/env python3


import matplotlib.pyplot as plt, pylab


def part1():
	# I (amps)
	x = [3.12, 6.18, 9.28, 12.36, 15.52, 18.62, 21.8, 24.9, 28.0, 31.4]
	# V (Volts)
	y = [ float(v) for v in range(1, 11)]


	# This gives m,b from (y = mx + b)
	m, b = pylab.polyfit(x, y, 1)
	# This calculates the slope for us
	slope = pylab.polyval([m,b], x)

	# Acordding to the lab R = m, but it's * 10 ^-3
	R_slope = m * 10 ** -3 
	R_dmm = .000325
	print("Part 1")
	print("R_slope = %f" %(R_slope))
	percent_diff = (abs(R_dmm - R_slope) / R_dmm + R_slope / 2) * 100
	print("percent difference %f" %(percent_diff))

	plt.plot(x, slope, "-r", label="slope")
	plt.scatter(x,y)
	plt.title("Carbon Resistor ")
	plt.ylabel("V (Volts)")
	plt.xlabel("I (amps) * 10^-3")
	plt.show()

def part2():

	# I (amps)
	x = [67.3, 93.0, 114.7, 133.6, 150.4, 166.4, 180.9, 194.6]
	# V (Volts)
	y = [ (v * .50)  for v in range(0, 8)]

	# This gives m,b from (y = mx + b)
	m, b = pylab.polyfit(x, y, 1)
	# This calculates the slope for us
	slope = pylab.polyval([m,b], x)

	# Acordding to the lab R_min and R_max are the lowest and highest values of the slope
	# removing the first value becaue it's negative
	slope1 = list(filter(lambda x: x > 0, slope))
	print(slope1)
	R_min = min(slope1) * 10 ** -3
	R_max = max(slope1) * 10 ** -3
	print("Part 2")
	print("R_min = %f" %(R_min))
	print("R_max = %f" %(R_max))
	percent_diff = (abs(R_max - R_min) / R_max + R_min / 2) * 100 
	print("percent difference %f" %(percent_diff))

	plt.plot(x, slope, "-r", label="slope")
	plt.scatter(x,y)
	plt.title("Light Bulb")
	plt.ylabel("V (Volts)")
	plt.xlabel("I (amps) * 10^-3")
	plt.show()



def main():
	part1()
	part2()





if __name__ == "__main__":
	main()