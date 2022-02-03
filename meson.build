# ============================= Project Setup ============================

# -------------------------- Initialize Project --------------------------
project('argparse', 'cpp',
  version : '2.2-SM23',
  default_options : [
    'warning_level=3',
    'c_std=c17',
    'cpp_std=c++17'
  ],
  license: 'MIT',
  meson_version: '>=0.58')

# ------------------------- Main Project Variables -----------------------
project_name = 'argparse'
project_major_ver = '2'
project_minor_ver = '2'
project_tag = 'SM23'
project_version = f'@project_major_ver@.@project_minor_ver@-@project_tag@'
project_desc = 'A single header argument parser for C++17'
project_url = 'https://github.com/p-ranav/argparse'

# ----------------------- Set project info in summary --------------------
summary({
        'Name': project_name,
        'Version': project_version,
        'Description': project_desc,
        'Homepage URL': project_url
        }, section: 'Project Information')

# --------------------- Project options and configuration ----------------
config_data = configuration_data()

config_data.set('major_version', project_major_ver)
config_data.set('minor_version', project_minor_ver)
config_data.set('version_tag', project_tag)
config_data.set('version', project_version)

# Allow toggling tests
set_variable('build_tests', get_option('build_tests'))

# Allow setting ARGPARSE_LONG_VERSION_ARG_ONLY
set_variable('long_args_only', get_option('long_version_args_only'))
config_data.set('ARGPARSE_LONG_VERSION_ARG_ONLY', long_args_only)

# ======================== Build Project Targets =========================

# ------------------ Set project configuration info in summary -----------
summary({
        'Build tests': build_tests,
        'Allow Long Version Arguments Only': long_args_only
        }, section: 'Configuration')

# -------------------------- 'include' Targets ---------------------------
subdir('include')

# ---------------------------- Target: tests -----------------------------
if build_tests
    subdir(test)
endif