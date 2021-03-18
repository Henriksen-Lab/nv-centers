import numpy as np
import pandas as pd
import scipy.interpolate as interp

dfPath = "VCO_voltage_vs_frequency_curve.csv"
columnNames = ["Voltage", "Frequency"]
df = pd.read_csv(dfPath, header=0, names=columnNames)
calibrationData = np.concatenate(([df[columnNames[0]].to_numpy()], [df[columnNames[1]].to_numpy()]), axis=0)
interpolatedCurve = interp.UnivariateSpline(
    calibrationData[0], calibrationData[1], s=0.0001, k=1)
# np.save("./VCO_interpolated_spline_object",
# interpolatedCurve, allow_pickle = True)
print(interpolatedCurve._eval_args)
np.save("./VCO_interpolated_spline_eval_args",
        interpolatedCurve._eval_args, allow_pickle=True)
