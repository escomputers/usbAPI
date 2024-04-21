"""Script that spawns a REST API server and translates HTTP requests
to commands for dealing with a USB device"""

import json
import time
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse

import dae_RelayBoard
from helpers import common

# Init DR object for dealing with Denkovi Relay Boards
dr = dae_RelayBoard.DAE_RelayBoard(common.BOARDS[common.BOARD_TYPE]["lib_name"])
dr.initialise()


class USBDeviceHandler(BaseHTTPRequestHandler):
    """Main HTTP Class for USB device handling"""

    def _set_response(self):
        """Function to handle HTTP response"""
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

    def do_GET(self):
        """Function for handling HTTP GET requests for the Status of a specific relay port"""

        # Parse received path
        parsed_path = urlparse(self.path)
        path_components = parsed_path.path.split("/")

        try:
            relay_port = int(path_components[1])
            if self.path == f"/{relay_port}/status":
                if (
                    common.BOARDS[common.BOARD_TYPE]["ports"][0]
                    < relay_port
                    < common.BOARDS[common.BOARD_TYPE]["ports"][1]
                ):
                    status = dr.getState(relay_port)

                    response = {
                        f"Status for device on port {relay_port}": common.STATUS_DICT[
                            status
                        ]
                    }
                    self._set_response()
                    self.wfile.write(json.dumps(response).encode())
                # Case where relay port in received path is not valid
                else:
                    response = {"Error": "Invalid relay port " + path_components[1]}
                    self._set_response()
                    self.wfile.write(json.dumps(response).encode())

            else:
                try:
                    inverted_status_dict = {v: k for k, v in common.STATUS_DICT.items()}
                    command = inverted_status_dict[path_components[2]]
                    if (
                        common.BOARDS[common.BOARD_TYPE]["ports"][0]
                        < relay_port
                        < common.BOARDS[common.BOARD_TYPE]["ports"][1]
                    ):
                        dr.setState(relay_port, command)
                        time.sleep(0.5)
                        new_status = dr.getState(relay_port)

                        response = {
                            f"Device on port {relay_port}": common.STATUS_DICT[
                                new_status
                            ]
                        }
                        self._set_response()
                        self.wfile.write(json.dumps(response).encode())
                    # Case where relay port in received path is not valid
                    else:
                        response = {"Error": "Invalid relay port " + path_components[1]}
                        self._set_response()
                        self.wfile.write(json.dumps(response).encode())
                # Case where turn command is wrong
                except KeyError:
                    self._set_response()
                    self.wfile.write(
                        b'{"Error": "Invalid turn command. Valid values are "on" or "off" (lowercase)"}'
                    )

        # Case where relay port in received path is not an integer
        except ValueError:
            self._set_response()
            self.wfile.write(b'{"error": "Invalid path"}')


def run(server_class=HTTPServer, handler_class=USBDeviceHandler, port=common.HTTP_PORT):
    """Spawn HTTP server process for all IP addresses"""
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {port}...")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    dr.disconnect()
    print("Stopping httpd and DR object...\n")


if __name__ == "__main__":
    run()
