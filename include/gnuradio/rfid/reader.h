/* -*- c++ -*- */
/*
 * Copyright 2024 gr-rfid author.
 *
 * SPDX-License-Identifier: GPL-3.0-or-later
 */

#ifndef INCLUDED_RFID_READER_H
#define INCLUDED_RFID_READER_H

#include <gnuradio/block.h>
#include <gnuradio/rfid/api.h>

namespace gr {
namespace rfid {

/*!
 * \brief <+description of block+>
 * \ingroup rfid
 *
 */
class RFID_API reader : virtual public gr::block
{
public:
    typedef std::shared_ptr<reader> sptr;

    /*!
     * \brief Return a shared_ptr to a new instance of rfid::reader.
     *
     * To avoid accidental use of raw pointers, rfid::reader's
     * constructor is in a private implementation
     * class. rfid::reader::make is the public interface for
     * creating new instances.
     */
    static sptr make(int sample_rate, int dac_rate);
};

} // namespace rfid
} // namespace gr

#endif /* INCLUDED_RFID_READER_H */
