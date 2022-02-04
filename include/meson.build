# ------------------------------ Target: argparse ----------------------------

# Skip the install here. The output file will be bundled with the main target
argparse_header = configure_file(input: 'argparse/argparse.hpp',
                                 output: 'argparse.hpp',
                                 configuration: config_data,
                                 install: true,
                                 install_dir: project_name)
# install_headers('include/argparse.hpp', subdir: project_name)
