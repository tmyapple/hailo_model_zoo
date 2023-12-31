from hailo_model_zoo.utils.platform_discovery import PLATFORM_AVAILABLE


PROFILER_MODE_NAMES = {'pre_placement', 'post_placement'}

TARGETS = [
    'hailo8',
    'full_precision',
    'emulator',
]


DEVICE_NAMES = set()
if PLATFORM_AVAILABLE:
    from hailo_platform.pyhailort._pyhailort import HailoRTStatusException
    from hailo_platform import Device, HailoRTException
    try:
        device = Device()
        devices = device.scan()
        DEVICE_NAMES.update([str(name) for name in devices])
    except (HailoRTException, HailoRTStatusException):
        # Ignore HailoRT exception when the driver is not installed
        pass
