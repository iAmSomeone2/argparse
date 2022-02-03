# ------------------------------ Write Config ----------------------------

# Skip the install here. The output file will be bundled with the main target
build_inc_path = MESON_BUILD_ROOT / 'include'
config_file = configure_file(input: 'argparse/config.hpp.in',
                             output: 'config.hpp',
                             configuration: config_data,
                             install: false)
build_inc_dir = include_directories(MESON_BUILD_ROOT)

# --------------------------- Target: argparse ---------------------------
# argparse_lib = shared_library('argparse', 'include/argparse.hpp',
#                include_directories: ['include', '{MESON_BUILD_ROOT}/include'],
#                install: true,
#                version: project_major_ver,
#                soversion: '{project_major_ver}.{project_minor_ver}_{project_tag}')
# install_headers('include/argparse.hpp', subdir: project_name)