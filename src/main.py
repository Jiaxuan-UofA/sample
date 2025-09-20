from os import path

import dataPreprocessing
import config

dataPreprocessing.preprocessData(path.join(config.PROJECT_ROOT_PATH, 'data'))
