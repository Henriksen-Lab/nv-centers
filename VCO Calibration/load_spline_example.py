# import scipy.interpolate as interp
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1, 15, num=400)
interpolatedCurve = np.load("./VCO_interpolated_spline_object.npy", allow_pickle=True)[()]
# interpolatedCurveArgs = np.load(
#     "./VCO_interpolated_spline_eval_args.npy", allow_pickle=True)

# interpolatedCurveFromArgs = interp.UnivariateSpline._from_tck(
#     interpolatedCurveArgs)
# plt.plot(x, interpolatedCurveFromArgs(x), label="Interpolation From Args")
plt.plot(x, interpolatedCurve(x), ":y", label="Interpolation From Object", )
plt.title("VCO Output Frequency vs. Vtune")
plt.xlabel("Voltage (V)")
plt.ylabel("Frequency (GHz)")
plt.legend()
plt.grid()
plt.show()
