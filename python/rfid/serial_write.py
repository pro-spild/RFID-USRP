#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2024 gr-rfid author.
#
# SPDX-License-Identifier: GPL-3.0-or-later
#


import numpy as np
from gnuradio import gr

# others import
import serial
import serial.tools.list_ports


class serial_write(gr.sync_block):
    def __init__(self, serial_port):
        gr.sync_block.__init__(
            self,
            name="serial_write",
            in_sig=[np.float64, np.float64, np.float64],
            out_sig=None,
        )
        port_list = list(serial.tools.list_ports.comports())
        self.serial_port = serial.Serial(str[port_list[serial_port][0], 9600])

    def tx_serial(self, str):
        input_str = input(str).encode("utf-8")
        self.serial_port.write(input_str)

    def work(self, input_items, output_items):
        in0 = input_items[0]
        if len(in0) == 0:
            in0 = 0
        in1 = input_items[1]
        if len(in1 == 0):
            in1 = 0
        in2 = input_items[2]
        if len(in2) == 0:
            in2 = 0

        writeStr = f"{in0}{in1}{in2}"
        self.tx_serial(writeStr)
        return len(input_items[0])
