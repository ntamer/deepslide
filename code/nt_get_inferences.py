import config
from utils_evaluation import (parse_thresholds,output_all_predictions)

# Running the code on the testing set.
print("\n\n+++++ Running nt_get_inferences.py +++++")
print("\n----- Reading best thresholds -----")
thresholds_folder=config.args.inference_test
ls_output = os.popen('ls {thresholds_folder}/*').read()
# Split the output into a list of strings
files = ls_output.splitlines()
# Get the first file in the list (there should only be one file)
first_file = files[0]
print('Thresholds file: ' + first_file)
best_thresholds = parse_thresholds(Path(first_file))
print(best_thresholds)
os.rename(first_file, first_file + '_training')
print("----- Finished reading best thresholds -----\n")
print("----- Outputting all predictions -----")
output_all_predictions(patches_pred_folder=config.args.preds_test,
                       output_folder=config.args.inference_test,
                       conf_thresholds=best_thresholds,
                       classes=config.classes,
                       image_ext=config.args.image_ext)
print("----- Finished outputting all predictions -----\n")
print("+++++ Finished running nt_get_inferences.py +++++\n\n")
