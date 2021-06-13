from utils.util import get_log_files, get_data_to_export, export_to_file, search_re

__author__ = 'raviranjan'

LOG_DIR = "logs"
TIME_STAMP_PATTERN = "^(2[0-3]|[01]?[0-9]):(0[1-9]{1}|[1-5]{1}[0-9]):(0[1-9]{1}|[1-5]{1}[0-9])$"
HOST_PATTERN = r'(^\S+\.[\S+\.]+\S+)\s'
LOGGER_FILE_PATTERN = r'(^\S+\.[\S+\.]+\S+)\s'
ERROR_PATTERN = 'ERROR:'
INFO_PATTERN = 'INFO:'
DEBUG_PATTERN = 'DEBUG:'

log_files = get_log_files(log_dir=LOG_DIR)


excel_export_data = get_data_to_export(log_file=log_files[0], column_names=['line', 'info', 'error', 'debug', 'warn', 'exception'])

search_re(log_files[0], pattern="04/24/2021 11:23:41 am")

DATA_DIR = "data"
export_to_file(export_folder=DATA_DIR, dict_with_list_values=excel_export_data)