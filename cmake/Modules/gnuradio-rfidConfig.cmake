find_package(PkgConfig)

PKG_CHECK_MODULES(PC_GR_RFID gnuradio-rfid)

FIND_PATH(
    GR_RFID_INCLUDE_DIRS
    NAMES gnuradio/rfid/api.h
    HINTS $ENV{RFID_DIR}/include
        ${PC_RFID_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    GR_RFID_LIBRARIES
    NAMES gnuradio-rfid
    HINTS $ENV{RFID_DIR}/lib
        ${PC_RFID_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
          )

include("${CMAKE_CURRENT_LIST_DIR}/gnuradio-rfidTarget.cmake")

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(GR_RFID DEFAULT_MSG GR_RFID_LIBRARIES GR_RFID_INCLUDE_DIRS)
MARK_AS_ADVANCED(GR_RFID_LIBRARIES GR_RFID_INCLUDE_DIRS)
