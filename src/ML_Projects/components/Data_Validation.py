import os
import pandas as pd
from ML_Projects import logger
from ML_Projects.entity.config_entity import DataValidationConfig

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self) -> bool:
        try:
            validation_status = None

            # Read the CSV file using the correct path
            data = pd.read_csv(self.config.data_file)  # Changed from unzip_data_dir to data_file
            all_cols = list(data.columns)

            all_schema = self.config.all_schema.keys()

            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
                    break  # Exit loop immediately if an invalid column is found
            
            # If all columns are valid, set validation_status to True
            if validation_status is None:
                validation_status = True

            # Write the validation status to the STATUS_FILE
            with open(self.config.STATUS_FILE, 'w') as f:
                f.write(f"Validation status: {validation_status}")

            return validation_status
        
        except Exception as e:
            raise e
