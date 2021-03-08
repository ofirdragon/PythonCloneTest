import pandas as pd
import numpy as np
import  logging
import matplotlib.pyplot as plt

dataTest = np.random.normal(100.0, 900000.0,100000);

plotHistogram = plt.hist(dataTest,150,color='red');
dd = dataTest.std();
logging.warning(dd);
logging.warning(dataTest.var())
plt.show()

dataTest.std();
