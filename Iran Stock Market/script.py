import numpy as np
import pandas as pd
import finpy_tse as fpy
# import mplfinance as mplf
# import scipy.stats as stt
import matplotlib.pyplot as plt

plt.style.use('ggplot')

doller = fpy.Get_USD_RIAL(
    start_date='1390-01-01',
    end_date='1391-12-02',
    ignore_date=False,
    show_weekday=False,
    double_date=False)

print (type(doller))
print(doller)

