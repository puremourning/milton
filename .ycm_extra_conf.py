import os
ROOT_DIR = os.path.dirname( os.path.abspath( __file__ ) )

def Settings( **kwargs ):
  return {
    'flags': [ "-xobjective-c++",
               "-DMILTON_DEBUG=1",
               f"-I{ ROOT_DIR }/src",
               f"-I{ ROOT_DIR }/third_party",
               f"-I{ ROOT_DIR }/third_party/imgui",
               f"-I{ ROOT_DIR }/third_party/SDL2-2.0.8/include",
               "-std=c++11",
               "-Wno-missing-braces",
               "-Wno-unused-function",
               "-Wno-unused-variable",
               "-Wno-unused-result",
               "-Wno-write-strings",
               "-Wno-c++11-compat-deprecated-writable-strings",
               "-Wno-null-dereference",
               "-Wno-format",
               "-fno-strict-aliasing",
               "-fno-omit-frame-pointer",
               "-Wno-extern-c-compat" ],
    'override_filename': f'{ ROOT_DIR }/src/unity.cc'
  }


