"""Common module for storing constants and user settings"""

########################################################################
# USER SETTINGS

# Set Denkovi Relay USB Board type here:
BOARD_TYPE = 8  # available types are: 4,8,16

# Set HTTP Port to listen to
HTTP_PORT = 8000
# Set IP address for HTTP port binding
ADDRESS = "0.0.0.0"  # Default: listen to all host network interfaces

########################################################################
# DO NOT EDIT
# Dictionary containing boards details
BOARDS = {
    4: {"lib_name": "type4", "ports": [0, 5]},
    8: {"lib_name": "type8", "ports": [0, 9]},
    16: {"lib_name": "type16", "ports": [0, 17]},
}

# Dictionary for storing Status more meaningful values
STATUS_DICT = {False: "off", True: "on"}
