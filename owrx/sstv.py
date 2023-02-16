from csdr.module import ThreadModule
from pycsdr.types import Format
from datetime import datetime
import base64
import pickle

import logging

logger = logging.getLogger(__name__)

modeNames = {
    8:  "Robot 36",
    12: "Robot 72",
    40: "Martin 2",
    44: "Martin 1",
    56: "Scottie 2",
    60: "Scottie 1",
    76: "Scottie DX",

    # Unsupported modes
    0:  "Robot 12",
    1:  "Robot 12",
    2:  "Robot 12",
    3:  "Robot BW8",
    4:  "Robot 24",
    5:  "Robot 24",
    6:  "Robot 24",
    7:  "Robot BW12",
    9:  "Robot BW12",
    10: "Robot BW12",
    11: "Robot BW24",
    13: "Robot BW24",
    14: "Robot BW24",
    15: "Robot BW36",
    32: "Martin M4",
    36: "Martin M3",
    41: "Martin HQ1",
    42: "Martin HQ2",
    48: "Scottie 4",
    52: "Scottie 3",
    85: "FAX480",
    90: "FAST FM",
    93: "PD 50",
    95: "PD 120",
    96: "PD 180",
    97: "PD 240",
    98: "PD 160",
    99: "PD 90",
    100: "Proskan J120",
    104: "MSCAN TV-1",
    105: "MSCAN TV-2",
    113: "Pasokon P3",
    114: "Pasokon P5",
    115: "Pasokon P7",
}

class SstvParser(ThreadModule):
    def __init__(self):
        self.data   = bytearray(b'')
        self.width  = 0
        self.height = 0
        self.line   = 0
        self.mode   = 0
        super().__init__()

    def getInputFormat(self) -> Format:
        return Format.CHAR

    def getOutputFormat(self) -> Format:
        return Format.CHAR

    def run(self):
        # Run while there is input data
        while self.doRun:
            # Read input data
            inp = self.reader.read()
            # Terminate if no input data
            if inp is None:
                self.doRun = False
                break
            # Add read data to the buffer
            self.data = self.data + inp.tobytes()
            # Process buffer contents
            out = self.process()
            # Keep processing while there is input to parse
            while out is not None:
                self.writer.write(pickle.dumps(out))
                out = self.process()

    def process(self):
        try:
            # Parse bitmap (BMP) file header starting with 'BM'
            if len(self.data)>=54 and self.data[0]==ord(b'B') and self.data[1]==ord(b'M'):
                self.width  = self.data[18] + (self.data[19]<<8) + (self.data[20]<<16) + (self.data[21]<<24)
                self.height = self.data[22] + (self.data[23]<<8) + (self.data[24]<<16) + (self.data[25]<<24)
                # BMP height value is negative
                self.height = 0x100000000 - self.height
                # SSTV mode is passed via reserved area at offset 6
                self.mode   = self.data[6]
                self.line   = 0
                # Remove parsed data
                del self.data[0:54]
                # Find mode name and time
                modeName  = modeNames.get(self.mode) if self.mode in modeNames else "Unknown Mode"
                timeStamp = datetime.now().strftime("%H:%M:%S")
                fileName  = datetime.now().strftime("SSTV-%y%m%d-%H%M%S")
                # Return parsed values
                return {
                    "mode": "SSTV",
                    "width": self.width,
                    "height": self.height,
                    "sstvMode": modeName,
                    "timestamp": timeStamp,
                    "filename": fileName
                }

            # Parse debug messages enclosed in ' [...]'
            elif len(self.data)>=2 and self.data[0]==ord(b' ') and self.data[1]==ord(b'['):
                # Wait until we find the closing bracket
                w = self.data.find(b']')
                if w>=0:
                    # Extract message contents
                    msg = self.data[0:w+1].decode()
                    # Log message
                    logger.debug(msg)
                    # Compose result
                    out = {
                        "mode": "SSTV",
                        "message": msg
                    }
                    # Remove parsed data
                    del self.data[0:w+1]
                    # Return parsed values
                    return out

            # Parse bitmap file data (scanlines)
            elif self.width>0 and len(self.data)>=self.width*3:
                w = self.width * 3
                # Compose result
                out = {
                    "mode":   "SSTV",
                    "pixels": base64.b64encode(self.data[0:w]).decode(),
                    "line":   self.line,
                    "width":  self.width,
                    "height": self.height
                }
                # Advance scanline
                self.line = self.line + 1
                # If we reached the end of frame, finish scan
                if self.line>=self.height:
                    self.width  = 0
                    self.height = 0
                    self.line   = 0
                    self.mode   = 0
                # Remove parsed data
                del self.data[0:w]
                # Return parsed values
                return out

            # Could not parse input data (yet)
            return None

        except Exception:
            logger.exception("Exception while parsing SSTV data")
