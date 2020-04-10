find_package(pybind11 REQUIRED)

pybind11_add_module(_utils
    _Demangle.cc 
    _packaging.cc 
    _utils.cc 
    backtrace/_Backtrace.cc
)

target_link_libraries(_utils PUBLIC utils)

install(TARGETS _utils DESTINATION ${CMAKE_INSTALL_PREFIX}/python/lsst/utils)

install(
    DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/
    DESTINATION ${CMAKE_INSTALL_PREFIX}/python/lsst/utils
    FILES_MATCHING PATTERN "*.py"
    PATTERN "test*.py" EXCLUDE
)

add_custom_target(utils_version ALL
    ${CMAKE_COMMAND} -P ${CMAKE_CURRENT_SOURCE_DIR}/version.cmake
    BYPRODUCTS ${CMAKE_CURRENT_BINARY_DIR}/version.py
)

install(
    FILES ${CMAKE_CURRENT_BINARY_DIR}/version.py
    DESTINATION ${CMAKE_INSTALL_PREFIX}/python/lsst/utils
)
