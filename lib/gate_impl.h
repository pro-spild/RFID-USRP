/* -*- c++ -*- */
/*
 * Copyright 2024 gr-rfid author.
 *
 * SPDX-License-Identifier: GPL-3.0-or-later
 */

#ifndef INCLUDED_RFID_GATE_IMPL_H
#define INCLUDED_RFID_GATE_IMPL_H

#include <gnuradio/rfid/global_var.h>
#include <gnuradio/rfid/gate.h>

namespace gr {
namespace rfid {

  class gate_impl : public gate
  {
    private:

      enum SIGNAL_STATE {NEG_EDGE, POS_EDGE};

      int   n_samples, n_samples_T1, n_samples_PW, n_samples_TAG_BIT; 
      int  win_index, dc_index, win_length, dc_length, s_rate;
      float avg_ampl, num_pulses, sample_thresh;

      std::vector<float> win_samples,cw_samples;  
      std::vector<gr_complex> dc_samples;
      gr_complex dc_est;

      SIGNAL_STATE signal_state;

      public:
      gate_impl(int sample_rate);
      ~gate_impl();

      void forecast (int noutput_items, gr_vector_int &ninput_items_required);

      int general_work(int noutput_items,
            gr_vector_int &ninput_items,
            gr_vector_const_void_star &input_items,
            gr_vector_void_star &output_items);
  };

} // namespace rfid
} // namespace gr

#endif /* INCLUDED_RFID_GATE_IMPL_H */
