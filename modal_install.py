import modal

image = (
    modal.Image.from_registry(
        "nvidia/cuda:12.9.1-cudnn-devel-ubuntu24.04",
        add_python="3.12",
    )
    .apt_install(
        "libglib2.0-0",  # GLib library of C routines
        "libsm6",  # X11 Session Management library
        "libxrender1",  # X Rendering Extension client library
        "libxext6",  # X11 miscellaneous extension library
        "ffmpeg",  # Tools for transcoding, streaming and playing of multimedia files
        "libgl1",  # Vendor neutral GL dispatch library -- legacy GL support
        "clang",
        "git",
    )
    .pip_install(
        "torch",
        "torchvision",
        "torchcodec",
        "xformers",
        index_url="https://download.pytorch.org/whl/cu128",
    )
    .run_commands(
        "git clone https://github.com/sarmientoF/Forward-Warp /root/Forward-Warp",
    )
    .run_commands(
        "cd /root/Forward-Warp && chmod a+x install.sh && ./install.sh",
        gpu="A10G",
    )
    # Add additional dependencies here
    # ...
)
