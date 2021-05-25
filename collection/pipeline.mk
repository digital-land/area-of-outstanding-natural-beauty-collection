AREA_OF_OUTSTANDING_NATURAL_BEAUTY_DATASET=$(DATASET_DIR)area-of-outstanding-natural-beauty.csv
AREA_OF_OUTSTANDING_NATURAL_BEAUTY_TRANSFORMED_FILES=\
    $(TRANSFORMED_DIR)area-of-outstanding-natural-beauty/4b547b34097e08ee4a41df14429738870c4d0f2b09cd2669f3cbde96e6949fba.csv

$(TRANSFORMED_DIR)area-of-outstanding-natural-beauty/4b547b34097e08ee4a41df14429738870c4d0f2b09cd2669f3cbde96e6949fba.csv: collection/resource/4b547b34097e08ee4a41df14429738870c4d0f2b09cd2669f3cbde96e6949fba
	$(run-pipeline)

$(AREA_OF_OUTSTANDING_NATURAL_BEAUTY_DATASET): $(AREA_OF_OUTSTANDING_NATURAL_BEAUTY_TRANSFORMED_FILES)
	$(build-dataset)

transformed:: $(AREA_OF_OUTSTANDING_NATURAL_BEAUTY_TRANSFORMED_FILES)

dataset:: $(AREA_OF_OUTSTANDING_NATURAL_BEAUTY_DATASET)
