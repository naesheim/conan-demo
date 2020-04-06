project(RuterCheck)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(rutercheck src/rutercheck.cpp)
target_link_libraries(rutercheck ${CONAN_LIBS})