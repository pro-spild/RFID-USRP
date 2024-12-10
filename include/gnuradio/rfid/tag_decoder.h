/* -*- c++ -*- */
/*
 * Copyright 2024 gr-rfid author.
 *
 * SPDX-License-Identifier: GPL-3.0-or-later
 */

#ifndef INCLUDED_RFID_TAG_DECODER_H
#define INCLUDED_RFID_TAG_DECODER_H

#include <gnuradio/block.h>
#include <gnuradio/rfid/api.h>

namespace gr {
namespace rfid {

/*!
 * \brief <+description of block+>
 * \ingroup rfid
 *
 */
class RFID_API tag_decoder : virtual public gr::block
{
public:
    typedef std::shared_ptr<tag_decoder> sptr;

    /*!
     * \brief Return a shared_ptr to a new instance of rfid::tag_decoder.
     *
     * To avoid accidental use of raw pointers, rfid::tag_decoder's
     * constructor is in a private implementation
     * class. rfid::tag_decoder::make is the public interface for
     * creating new instances.
     */
    static sptr make(int sample_rate);
};

} // namespace rfid
} // namespace gr

#endif /* INCLUDED_RFID_TAG_DECODER_H */
