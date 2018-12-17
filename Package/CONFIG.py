import ops
import ops_git
import iopc

TARBALL_FILE="node-v6.11.1-linux-x64.tar.xz"
TARBALL_DIR="node-v6.11.1-linux-x64"
pkg_path = ""
output_dir = ""
tarball_pkg = ""
tarball_dir = ""
install_dir = ""

def set_global(args):
    global pkg_path
    global output_dir
    global tarball_pkg
    global install_dir
    global tarball_dir
    global NODEJSROOT
    pkg_path = args["pkg_path"]
    output_dir = args["output_path"]
    pkg_args = args["pkg_args"]
    tarball_pkg = ops.path_join(pkg_path, TARBALL_FILE)
    tarball_dir = ops.path_join(output_dir, TARBALL_DIR)

def MAIN_ENV(args):
    set_global(args)

    ops.exportEnv(ops.setEnv("NODEJSROOT", tarball_dir))
    ops.exportEnv(ops.addEnv("PATH", ops.path_join(tarball_dir, "bin")))

    return False

def MAIN_EXTRACT(args):
    set_global(args)

    ops.unTarXz(tarball_pkg, output_dir)

    return True

def MAIN_PATCH(args, patch_group_name):
    set_global(args)
    for patch in iopc.get_patch_list(pkg_path, patch_group_name):
        if iopc.apply_patch(tarball_dir, patch):
            continue
        else:
            sys.exit(1)

    return True

def MAIN_CONFIGURE(args):
    set_global(args)

    return True

def MAIN_BUILD(args):
    set_global(args)

    return False

def MAIN_INSTALL(args):
    set_global(args)

    return False

def MAIN_SDKENV(args):
    set_global(args)

    return False

def MAIN_CLEAN_BUILD(args):
    set_global(args)

    return False

def MAIN(args):
    set_global(args)

