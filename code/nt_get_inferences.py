import config
from utils_evaluation import (parse_thresholds,output_all_predictions)

import os
from pathlib import Path

# Running the code on the testing set.
print("\n\n+++++ Running nt_get_inferences.py +++++")
print("\n----- Reading best thresholds -----")
thresholds_folder=config.args.inference_test
ls_output = os.listdir(thresholds_folder)
# Get the first file in the list (there should only be one file)
first_file = ls_output[0]
print('Thresholds file: ' + first_file)
best_thresholds = parse_thresholds(Path(first_file))
print(best_thresholds)
renamed_file = Path(first_file + '_training')
csv_path = thresholds_folder / first_file
renamed_path = thresholds_folder / renamed_file
os.rename(csv_path, renamed_path)
print("----- Finished reading best thresholds -----\n")
print("----- Outputting all predictions -----")
output_all_predictions(patches_pred_folder=config.args.preds_test,
                       output_folder=config.args.inference_test,
                       conf_thresholds=best_thresholds,
                       classes=config.classes,
                       image_ext=config.args.image_ext)
print("----- Finished outputting all predictions -----\n")
print("+++++ Finished running nt_get_inferences.py +++++\n\n")
