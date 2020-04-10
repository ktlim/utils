add_library(utils SHARED)

target_compile_features(utils PRIVATE
    cxx_std_14
)

set_target_properties(utils PROPERTIES 
    CXX_EXTENSIONS OFF
    POSITION_INDEPENDENT_CODE ON
)

target_include_directories(utils PUBLIC
    ${PROJECT_SOURCE_DIR}/include
)

target_sources(utils PRIVATE
    Backtrace.cc
    Demangle.cc
    Magnitude.cc
    packaging.cc
)

target_link_libraries(utils PUBLIC
    pex_exceptions
)

install(TARGETS utils)
