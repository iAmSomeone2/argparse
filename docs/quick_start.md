# Quick Start

Simply include argparse.hpp and you're good to go.

```cpp
#include <argparse/argparse.hpp>
```

To start parsing command-line arguments, create an ```ArgumentParser```.

```cpp
argparse::ArgumentParser program("program name");
```

**NOTE:** There is an optional second argument to the `ArgumentParser` which is the program version. Example: `argparse::ArgumentParser program("libfoo", "1.9.0");`

To add a new argument, simply call ```.add_argument(...)```. You can provide a variadic list of argument names that you want to group together, e.g., ```-v``` and ```--verbose```

```cpp
program.add_argument("foo");
program.add_argument("-v", "--verbose"); // parameter packing
```