import glob
import logging
import os
from datetime import datetime

from project_constants import project_path


class CommonActions:
    @staticmethod
    def create_screenshot(driver, test_name):
        current_date = datetime.now().strftime("%m_%d_%Y_%H-%M")
        path_to_file = os.path.join(project_path, "screenshots")
        if not os.path.exists(path_to_file):
            os.makedirs(path_to_file)
        driver.save_screenshot(os.path.join(path_to_file, f"{test_name}_{current_date}.png"))

    @staticmethod
    def clean_screenshot_folder():
        logging.info("Clean screenshot folder")
        folder_path = os.path.join(project_path, "screenshots")
        file_list = glob.glob(os.path.join(folder_path, "*.png"))
        for file in file_list:
            os.remove(file)
