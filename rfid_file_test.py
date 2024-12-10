#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Rfid File Test
# GNU Radio version: 3.10.11.0

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio import blocks
import pmt
from gnuradio import filter
from gnuradio import gr
import sys
import signal
from gnuradio import rfid
import threading


class rfid_file_test(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Rfid File Test", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Rfid File Test")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme("gnuradio-grc"))
        except BaseException as exc:
            print(f"Qt GUI: Could not set Icon: {str(exc)}", file=sys.stderr)
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("gnuradio/flowgraphs", "rfid_file_test")

        try:
            geometry = self.settings.value("geometry")
            if geometry:
                self.restoreGeometry(geometry)
        except BaseException as exc:
            print(
                f"Qt GUI: Could not restore geometry: {str(exc)}",
                file=sys.stderr,
            )
        self.flowgraph_started = threading.Event()

        ##################################################
        # Variables
        ##################################################
        self.n_taps = n_taps = [1] * 25
        self.decim = decim = 5
        self.dac_rate = dac_rate = 1000000
        self.ampl = ampl = 0.1
        self.adc_rate = adc_rate = 2000000

        ##################################################
        # Blocks
        ##################################################

        self.rfid_tag_decoder_0 = rfid.tag_decoder((int(adc_rate / decim)))
        self.rfid_reader_0 = rfid.reader((int(adc_rate / decim)), dac_rate)
        self.rfid_gate_0 = rfid.gate((int(adc_rate / decim)))
        self.fir_filter_xxx_0 = filter.fir_filter_ccf(decim, n_taps)
        self.fir_filter_xxx_0.declare_sample_delay(0)
        self.blocks_throttle_0 = blocks.throttle(
            gr.sizeof_gr_complex * 1, adc_rate, True
        )
        self.blocks_null_source_0 = blocks.null_source(gr.sizeof_float * 1)
        self.blocks_null_sink_1 = blocks.null_sink(gr.sizeof_gr_complex * 1)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_ff(ampl)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_file_source_0 = blocks.file_source(
            gr.sizeof_gr_complex * 1,
            "/home/wuyun/Code/USRP/gr-rfid/misc/data/file_source_test",
            True,
            0,
            0,
        )
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_file_sink_0 = blocks.file_sink(
            gr.sizeof_gr_complex * 1,
            "/home/wuyun/Code/USRP/gr-rfid/misc/data/file_sink",
            False,
        )
        self.blocks_file_sink_0.set_unbuffered(False)

        ##################################################
        # Connections
        ##################################################
        self.connect(
            (self.blocks_file_source_0, 0), (self.blocks_throttle_0, 0)
        )
        self.connect(
            (self.blocks_float_to_complex_0, 0), (self.blocks_file_sink_0, 0)
        )
        self.connect(
            (self.blocks_multiply_const_vxx_0, 0),
            (self.blocks_float_to_complex_0, 0),
        )
        self.connect(
            (self.blocks_null_source_0, 0), (self.blocks_float_to_complex_0, 1)
        )
        self.connect((self.blocks_throttle_0, 0), (self.fir_filter_xxx_0, 0))
        self.connect((self.fir_filter_xxx_0, 0), (self.rfid_gate_0, 0))
        self.connect((self.rfid_gate_0, 0), (self.rfid_tag_decoder_0, 0))
        self.connect(
            (self.rfid_reader_0, 0), (self.blocks_multiply_const_vxx_0, 0)
        )
        self.connect(
            (self.rfid_tag_decoder_0, 1), (self.blocks_null_sink_1, 0)
        )
        self.connect((self.rfid_tag_decoder_0, 0), (self.rfid_reader_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("gnuradio/flowgraphs", "rfid_file_test")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_tx_gain(self):
        return self.tx_gain

    def set_tx_gain(self, tx_gain):
        self.tx_gain = tx_gain

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate

    def get_rx_gain(self):
        return self.rx_gain

    def set_rx_gain(self, rx_gain):
        self.rx_gain = rx_gain

    def get_n_taps(self):
        return self.n_taps

    def set_n_taps(self, n_taps):
        self.n_taps = n_taps
        self.fir_filter_xxx_0.set_taps(self.n_taps)

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq

    def get_decim(self):
        return self.decim

    def set_decim(self, decim):
        self.decim = decim

    def get_dac_rate(self):
        return self.dac_rate

    def set_dac_rate(self, dac_rate):
        self.dac_rate = dac_rate

    def get_ampl(self):
        return self.ampl

    def set_ampl(self, ampl):
        self.ampl = ampl
        self.blocks_multiply_const_vxx_0.set_k(self.ampl)

    def get_adc_rate(self):
        return self.adc_rate

    def set_adc_rate(self, adc_rate):
        self.adc_rate = adc_rate
        self.blocks_throttle_0.set_sample_rate(self.adc_rate)


def main(top_block_cls=rfid_file_test, options=None):

    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()
    tb.flowgraph_started.set()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()


if __name__ == "__main__":
    main()
