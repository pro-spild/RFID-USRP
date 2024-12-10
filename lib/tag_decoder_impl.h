/* -*- c++ -*- */
/*
 * Copyright 2024 gr-rfid author.
 *
 * SPDX-License-Identifier: GPL-3.0-or-later
 */

#ifndef INCLUDED_RFID_TAG_DECODER_IMPL_H
#define INCLUDED_RFID_TAG_DECODER_IMPL_H

#include <gnuradio/rfid/tag_decoder.h>
#include <gnuradio/rfid/global_var.h>
#include <time.h>
#include <fstream>
#include <numeric>

namespace gr {
namespace rfid {

  class tag_decoder_impl : public tag_decoder
  {
    private:
    
      float n_samples_TAG_BIT;
      int s_rate;
      std::vector<float> pulse_bit;
      float T_global;
      gr_complex h_est;
      char * char_bits;

      std::vector<float> tag_detection_EPC(std::vector<gr_complex> &EPC_samples_complex, int index);
      std::vector<float> tag_detection_RN16(std::vector<gr_complex> &RN16_samples_complex);      
      int tag_sync(const gr_complex * in, int size);
       int check_crc(char * bits, int num_bits);

    public:
      tag_decoder_impl(int sample_rate, std::vector<int> output_sizes);
      ~tag_decoder_impl();

      void forecast (int noutput_items, gr_vector_int &ninput_items_required);

      int general_work(int noutput_items,
      gr_vector_int &ninput_items,
      gr_vector_const_void_star &input_items,
      gr_vector_void_star &output_items);
    };

} // namespace rfid
} // namespace gr

#endif /* INCLUDED_RFID_TAG_DECODER_IMPL_H */
