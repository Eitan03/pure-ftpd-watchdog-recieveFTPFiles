
from multiprocessing import Pool

from Communication.Logger import initLogger

pool = Pool(initializer=initLogger)