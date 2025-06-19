from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CUDAExtension, CppExtension

setup(
    name="forward_warp_cuda",
    ext_modules=[
        CUDAExtension(
            name="forward_warp_cuda",
            sources=[
                "forward_warp_cuda.cpp",
                "forward_warp_cuda_kernel.cu",
            ],
            extra_compile_args={
                "cxx": ["-O3"],
                "nvcc": [
                    "-O3",
                    "--use_fast_math",
                    "-gencode=arch=compute_75,code=sm_75",
                    "-gencode=arch=compute_80,code=sm_80",
                    "-gencode=arch=compute_86,code=sm_86",
                    "-gencode=arch=compute_89,code=sm_89",
                    "-gencode=arch=compute_90,code=sm_90",
                    # "-gencode=arch=compute_100,code=sm_100",  # B200
                    "-gencode=arch=compute_90,code=compute_90",
                ],
            },
        ),
    ],
    cmdclass={"build_ext": BuildExtension},
)
