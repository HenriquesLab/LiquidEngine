import os
import warnings

os.environ["PYOPENCL_COMPILER_OUTPUT"] = "1"


class NoCL(object):
    class MemoryError(Exception):
        def __init__(self):
            self.message = "NoCL memory error"

        def __str__(self):
            print(self.message)

    class LogicError(Exception):
        def __init__(self):
            self.message = "NoCL logic error"

        def __str__(self):
            print(self.message)

    class Error(Exception):
        def __init__(self):
            self.message = "NoCL error"

        def __str__(self):
            print(self.message)

    def __init__(self):
        pass

    def __bool__(self):
        return False


try:
    import pyopencl as cl
    import pyopencl.array as cl_array

    devices = []
    _fastest_device = None
    max_perf = 0

    if len(cl.get_platforms()) == 1 and len(cl.get_platforms()[0].get_devices()) == 1:
        dev = cl.get_platforms()[0].get_devices()[0]
        _fastest_device = {"device": dev, "DP": False}
        devices.append({"device": dev, "DP": False})

    else:
        for platform in cl.get_platforms():
            if "Microsoft" in platform.vendor:  # TODO this takes out emulated GPUs
                continue
            for dev in platform.get_devices():
                # check if the device is a GPU
                if "GPU" not in cl.device_type.to_string(dev.type):
                    continue
                if "cl_khr_fp64" in dev.extensions.strip().split(" "):
                    cl_dp = False
                else:
                    cl_dp = False
                if "Intel" in platform.vendor:
                    # penalty for Intel based integrated GPUs as compute units here refer to threads
                    perf = dev.max_compute_units/2 * dev.max_clock_frequency * dev.max_mem_alloc_size
                else:
                    perf = dev.max_compute_units * dev.max_clock_frequency * dev.max_mem_alloc_size
                if perf > max_perf:
                    max_perf = perf
                    _fastest_device = {"device": dev, "DP": cl_dp}
                devices.append({"device": dev, "DP": cl_dp})


except (ImportError, OSError, Exception) as e:
    print("This exception is what's causing cl equals None:", e)
    cl = NoCL()
    cl_array = None
    devices = None
    _fastest_device = None


def print_opencl_info():
    """
    Prints information about the OpenCL devices on the system
    """
    # REF: https://github.com/benshope/PyOpenCL-Tutorial

    msg = "\n" + "=" * 60 + "\nOpenCL Platforms and Devices \n"
    # Print each platform on this computer
    for platform in cl.get_platforms():
        msg += "=" * 60 + "\n"
        msg += "Platform - Name:  " + platform.name + "\n"
        msg += "Platform - Vendor:  " + platform.vendor + "\n"
        msg += "Platform - Version:  " + platform.version + "\n"
        msg += "Platform - Profile:  " + platform.profile + "\n"
        # Print each device per-platform
        for device in platform.get_devices():
            msg += "\t" + "-" * 56 + "\n"
            msg += "\tDevice - Name: " + device.name + "\n"
            msg += "\tDevice - Type: " + cl.device_type.to_string(device.type) + "\n"
            msg += f"\tDevice - Max Clock Speed:  {device.max_clock_frequency} Mhz" + "\n"

            msg += f"\tDevice - Compute Units:  {device.max_compute_units}" + "\n"
            msg += f"\tDevice - Local Memory:  {device.local_mem_size / 1024.0:.0f} KB" + "\n"
            msg += f"\tDevice - Constant Memory:  {device.max_constant_buffer_size / 1024.0:.0f} KB" + "\n"
            msg += f"\tDevice - Global Memory: {device.global_mem_size / 1073741824.0:.0f} GB" + "\n"
            msg += f"\tDevice - Max Buffer/Image Size: {device.max_mem_alloc_size / 1048576.0:.0f} MB" + "\n"
            msg += f"\tDevice - Max Work Group Size: {device.max_work_group_size:.0f}" + "\n"

    return msg


def opencl_works():
    """
    Checks if the system has OpenCL compatibility
    :return: True if the system has OpenCL compatibility, False otherwise
    """
    disabled = os.environ.get("NANOPYX_DISABLE_OPENCL", "0") == "1"
    enabled = os.environ.get("NANOPYX_ENABLE_OPENCL", "1") == "1"

    if disabled or not enabled:
        warnings.warn("OpenCL is disabled. To enable it, set the environment variable NANOPYX_ENABLE_OPENCL=1")
        return False

    elif enabled:
        if not cl:
            warnings.warn("tap... tap... tap... COMPUTER SAYS NO (OpenCL)!")
            os.environ["NANOPYX_DISABLE_OPENCL"] = "1"
            return False

    return True
