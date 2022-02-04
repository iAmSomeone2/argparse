# ============================= Project Setup ============================

# -------------------------- Initialize Project --------------------------
project('argparse', 'cpp',
  default_options : [
    'warning_level=3',
    'cpp_std=c++17'
  ],
  license: 'MIT',
  meson_version: '>=0.59')

# Import filesystem (fs) module
fs = import('fs',
            required: false,
            disabler: true)

# ------------------------- Main Project Variables -----------------------
# Read project version from VERSION.txt.
ver_file = 'VERSION.txt'
if fs.found() and fs.exists(ver_file) 
    version = fs.read(ver_file)
else
    version = '0.0.0'
endif

# TODO: Add build # tag for dev-branch builds on CI systems

project_name = 'argparse'
project_desc = 'A single header argument parser for C++17'
project_url = 'https://github.com/p-ranav/argparse'

# ----------------------- Set project info in summary --------------------
summary({
        'Name': project_name,
        'Version': version,
        'Description': project_desc,
        'Homepage URL': project_url
        }, section: 'Project Information')

# --------------------- Project options and configuration ----------------

# ++++++++++++++++++++++++++++++ Read Options ++++++++++++++++++++++++++++
# Allow enabling unit tests
unit_tests = get_option('enable_unit_tests')

# Allow enabling ARGPARSE_LONG_VERSION_ARG_ONLY
long_version_args_only = get_option('long_version_args_only')

# +++++++++++++++++++++++++++ Init Config Data +++++++++++++++++++++++++++
config_data = configuration_data()

config_data.set('LONG_VERSION_ARGS_ONLY', long_version_args_only.enabled())
config_data.set('version', version)

# ------------------ Set project configuration info in summary -----------
summary({
        'Snapshot build': snapshot_build,
        'Build tests': unit_tests,
        'Allow Long Version Arguments Only': long_version_args_only
        }, section: 'Configuration')

# ======================== Build Project Targets =========================

# -------------------------- 'include' Targets ---------------------------
subdir('include')

# ---------------------------- Target: tests -----------------------------
if unit_tests.enabled()
    subdir(test)
endif