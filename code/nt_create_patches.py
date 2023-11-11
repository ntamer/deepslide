import config

from utils_processing import produce_patches

###########################################
#                  MAIN                   #
###########################################
print("\n\n+++++ Running nt_create_patches.py +++++")
print("----- Generating test evaluation patches -----")
# Generate test evaluation patches.
produce_patches(input_folder=config.args.wsi_test,
                output_folder=config.args.patches_eval_test,
                inverse_overlap_factor=config.args.slide_overlap,
                by_folder=config.args.by_folder,
                num_workers=config.args.num_workers,
                patch_size=config.args.patch_size,
                purple_threshold=config.args.purple_threshold,
                purple_scale_size=config.args.purple_scale_size,
                image_ext=config.args.image_ext,
                type_histopath=config.args.type_histopath)
print("----- Finished generating test evaluation patches -----\n")
print("+++++ Finished running nt_create_patches.py +++++\n\n")
