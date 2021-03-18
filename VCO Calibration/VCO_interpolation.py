import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.interpolate as interp
import scipy.optimize as opt

dfPath = "./VCO_voltage_vs_frequency_curve.csv"

columnNames = ["Voltage", "Frequency"]
df = pd.read_csv(dfPath, header=0, names=columnNames)
calibrationData = np.concatenate(([df[columnNames[0]].to_numpy()], [
                                 df[columnNames[1]].to_numpy()]), axis=0)


def linear(x, a, b):
    return (a*x+b)


def quadratic(x, a, b, c):
    return (a*x**2+b*x+c)


def cubic(x, a, b, c, d):
    return (a*x**3+b*x**2+c*x**1+d)


def degFour(x, a, b, c, d, e):
    return (a*x**4+b*x**3+c*x**2+d*x**1+e)


def degFive(x, a, b, c, d, e, f):
    return (a*x**5+b*x**4+c*x**3+d*x**2+e*x+f)


sigma = np.zeros_like(calibrationData[1])
sigma[:] = 0.00003

pOpt, pCov = opt.curve_fit(
    linear, calibrationData[0], calibrationData[1], sigma=sigma, absolute_sigma=True)
x = np.linspace(1, 15, num=400)
y = linear(x, pOpt[0], pOpt[1])
plt.plot(x, y, label="Linear Curve Fit", color="magenta")

pOpt, pCov = opt.curve_fit(
    quadratic, calibrationData[0], calibrationData[1], sigma=sigma, absolute_sigma=True)
y = quadratic(x, pOpt[0], pOpt[1], pOpt[2])
plt.plot(x, y, label="Quadratic Curve Fit", color="red")

pOpt, pCov = opt.curve_fit(
    cubic, calibrationData[0], calibrationData[1], sigma=sigma, absolute_sigma=True)
y = cubic(x, pOpt[0], pOpt[1], pOpt[2], pOpt[3])
plt.plot(x, y, label="Cubic Curve Fit", color="blue")

pOpt, pCov = opt.curve_fit(
    degFour, calibrationData[0], calibrationData[1], sigma=sigma, absolute_sigma=True)
y = degFour(x, pOpt[0], pOpt[1], pOpt[2], pOpt[3], pOpt[4])
plt.plot(x, y, label="4th Degree Curve Fit", color="brown")

pOpt, pCov = opt.curve_fit(
    degFive, calibrationData[0], calibrationData[1], sigma=sigma, absolute_sigma=True)
y = degFive(x, pOpt[0], pOpt[1], pOpt[2], pOpt[3], pOpt[4], pOpt[5])
plt.plot(x, y, label="5th Degree Curve Fit", color="green")


plt.scatter(calibrationData[0], calibrationData[1],
            s=4, label="Raw Data", color="black")

plt.title("VCO Output Frequency vs. Vtune")
plt.xlabel("Voltage (V)")
plt.ylabel("Frequency (GHz)")
plt.legend()
plt.grid()
plt.show()


interpolatedCurve = interp.UnivariateSpline(
    calibrationData[0], calibrationData[1], s=0.0001, k=1)

plt.scatter(calibrationData[0], calibrationData[1],
            s=4, label="Raw Data", color="black")
plt.plot(x, interpolatedCurve(x), label="Interpolation")
plt.title("VCO Output Frequency vs. Vtune")
plt.xlabel("Voltage (V)")
plt.ylabel("Frequency (GHz)")
plt.legend()
plt.grid()
plt.show()
