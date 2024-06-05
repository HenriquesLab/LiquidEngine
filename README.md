# Liquid Engine

[![PyPI](https://img.shields.io/pypi/v/liquid_engine.svg?color=green)](https://pypi.org/project/liquid_engine)
[![Python Version](https://img.shields.io/pypi/pyversions/liquid_engine.svg?color=green)](https://python.org)
[![Downloads](https://img.shields.io/pypi/dm/liquid_engine)](https://pypi.org/project/liquid_engine)
[![Docs](https://img.shields.io/badge/documentation-link-blueviolet)](https://henriqueslab.github.io/LiquidEngine)
[![License](https://img.shields.io/github/license/HenriquesLab/LiquidEngine?color=Green)](https://github.com/HenriquesLab/LiquidEngine/blob/main/LICENSE.txt)
[![Tests](https://github.com/HenriquesLab/LiquidEngine/actions/workflows/nightly.yml/badge.svg)](https://github.com/HenriquesLab/LiquidEngine/actions/workflows/nightly.yml)
[![Contributors](https://img.shields.io/github/contributors-anon/HenriquesLab/LiquidEngine)](https://github.com/HenriquesLab/LiquidEngine/graphs/contributors)
[![GitHub stars](https://img.shields.io/github/stars/HenriquesLab/LiquidEngine?style=social)](https://github.com/HenriquesLab/LiquidEngine/)
[![GitHub forks](https://img.shields.io/github/forks/HenriquesLab/LiquidEngine?style=social)](https://github.com/HenriquesLab/LiquidEngine/)
[![DOI](https://zenodo.org/badge/505388398.svg)](https://zenodo.org/badge/latestdoi/505388398)

Liquid Engine - Accelerating Bioimage Analysis with dynamic selection of algorithm variations

---

## Liquid Engine

The Liquid Engine is a high-performance, adaptive framework designed to optimize computational workflows for bioimage analysis. It dynamically generates optimized CPU and GPU-based code variations and selects the fastest combination based on input parameters and device performance, significantly enhancing computational speed. The Liquid Engine employs a machine learning-based Agent to predict the optimal combination of implementations, adaptively responding to delays and performance variations.

Key features include:

    - Multiple Implementations: Utilizes various acceleration strategies such as PyOpenCL, CUDA, Cython, Numba, Transonic, and Dask to deliver optimal performance.
    - Machine Learning Agent: Predicts the best-performing implementation combinations and adapts dynamically to ensure maximum efficiency.
    - Automatic Benchmarking: Continuously benchmarks different implementations to maintain a historical record of runtimes and improve performance over time.
    - Seamless Integration: Can easily be integrated into any existing workflow with no extra work for end users.

The Liquid Engine's adaptability and optimization capabilities make it a powerful tool for researchers handling extensive microscopy datasets and requiring high computational efficiency.

if you found this work useful, please cite: [preprint](https://www.biorxiv.org/content/10.1101/2023.08.13.553080v1) and  [![DOI](https://zenodo.org/badge/505388398.svg)](https://zenodo.org/badge/latestdoi/505388398)



## Instalation

`Liquid Engine` is compatible and tested with Python 3.9, 3.10 and 3.11 in MacOS, Windows and Linux.
You can install `Liquid Engine`via [pip]:

```shell
pip install liquid_engine
```

## License

Distributed under the terms of the [CC-By v4.0] license,
"Liquid Engine" is free and open source software

## Issues

If you encounter any problems, please [file an issue] along with a detailed description.

[CC-By v4.0]: https://creativecommons.org/licenses/by/4.0/
[file an issue]: https://github.com/HenriquesLab/LiquidEngine/issues
[pip]: https://pypi.org/project/pip/