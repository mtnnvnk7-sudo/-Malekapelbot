10.31 16:30
pip3.11 install marker-pdf                                      ─╯
Collecting marker-pdf
  Using cached marker_pdf-0.3.9-py3-none-any.whl.metadata (16 kB)
Collecting Pillow<11.0.0,>=10.1.0 (from marker-pdf)
  Using cached pillow-10.4.0.tar.gz (46.6 MB)
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Collecting filetype<2.0.0,>=1.2.0 (from marker-pdf)
  Using cached filetype-1.2.0-py2.py3-none-any.whl.metadata (6.5 kB)
Collecting ftfy<7.0.0,>=6.1.1 (from marker-pdf)
  Using cached ftfy-6.3.1-py3-none-any.whl.metadata (7.3 kB)
Collecting pdftext<0.4.0,>=0.3.17 (from marker-pdf)
  Using cached pdftext-0.3.18-py3-none-any.whl.metadata (8.2 kB)
Requirement already satisfied: pydantic<3.0.0,>=2.4.2 in /data/data/com.termux/files/usr/lib/python3.11/site-packages (from marker-pdf) (2.9.2)
Collecting pydantic-settings<3.0.0,>=2.0.3 (from marker-pdf)
  Using cached pydantic_settings-2.6.0-py3-none-any.whl.metadata (3.5 kB)
Collecting python-dotenv<2.0.0,>=1.0.0 (from marker-pdf)
  Using cached python_dotenv-1.0.1-py3-none-any.whl.metadata (23 kB)
Requirement already satisfied: rapidfuzz<4.0.0,>=3.8.1 in /data/data/com.termux/files/usr/lib/python3.11/site-packages (from marker-pdf) (3.10.0)
Requirement already satisfied: regex<2025.0.0,>=2024.4.28 in /data/data/com.termux/files/usr/lib/python3.11/site-packages (from marker-pdf) (2024.9.11)
Collecting surya-ocr<0.7.0,>=0.6.11 (from marker-pdf)
  Using cached surya_ocr-0.6.13-py3-none-any.whl.metadata (30 kB)
Collecting tabled-pdf<0.2.0,>=0.1.4 (from marker-pdf)
  Using cached tabled_pdf-0.1.4-py3-none-any.whl.metadata (8.3 kB)
Collecting tabulate<0.10.0,>=0.9.0 (from marker-pdf)
  Using cached tabulate-0.9.0-py3-none-any.whl.metadata (34 kB)
Collecting texify<0.3.0,>=0.2.0 (from marker-pdf)
  Using cached texify-0.2.0-py3-none-any.whl.metadata (10 kB)
INFO: pip is looking at multiple versions of marker-pdf to determine which version is compatible with other requirements. This could take a while.
Collecting marker-pdf
  Using cached marker_pdf-0.3.8-py3-none-any.whl.metadata (16 kB)
  Using cached marker_pdf-0.3.7-py3-none-any.whl.metadata (16 kB)
  Using cached marker_pdf-0.3.6-py3-none-any.whl.metadata (16 kB)
  Using cached marker_pdf-0.3.5-py3-none-any.whl.metadata (16 kB)
  Using cached marker_pdf-0.3.4-py3-none-any.whl.metadata (16 kB)
  Using cached marker_pdf-0.3.3-py3-none-any.whl.metadata (16 kB)
  Using cached marker_pdf-0.3.2-py3-none-any.whl.metadata (16 kB)
INFO: pip is still looking at multiple versions of marker-pdf to determine which version is compatible with other requirements. This could take a while.
  Using cached marker_pdf-0.3.1-py3-none-any.whl.metadata (16 kB)
  Using cached marker_pdf-0.3.0-py3-none-any.whl.metadata (15 kB)
  Using cached marker_pdf-0.2.17-py3-none-any.whl.metadata (15 kB)
Collecting grpcio<2.0.0,>=1.63.0 (from marker-pdf)
  Using cached grpcio-1.67.1.tar.gz (12.6 MB)
  Preparing metadata (setup.py) ... done
Collecting numpy<2.0.0,>=1.26.1 (from marker-pdf)
  Using cached numpy-1.26.4.tar.gz (15.8 MB)
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Collecting scikit-learn<=1.4.2,>=1.3.2 (from marker-pdf)
  Using cached scikit-learn-1.4.2.tar.gz (7.8 MB)
  Installing build dependencies ... error
  error: subprocess-exited-with-error
  × pip subprocess to install build dependencies did not run successfully.
  │ exit code: 1
  ╰─> [9 lines of output]
      Collecting setuptools
        Using cached setuptools-75.3.0-py3-none-any.whl.metadata (6.9 kB)
      Collecting wheel
        Using cached wheel-0.44.0-py3-none-any.whl.metadata (2.3 kB)
      Collecting Cython>=3.0.8
        Using cached Cython-3.0.11-py2.py3-none-any.whl.metadata (3.2 kB)
      ERROR: Ignored the following versions that require a different python version: 1.21.2 Requires-Python >=3.7,<3.11; 1.21.3 Requires-Python >=3.7,<3.11; 1.21.4 Requires-Python >=3.7,<3.11; 1.21.5 Requires-Python >=3.7,<3.11; 1.21.6 Requires-Python >=3.7,<3.11
      ERROR: Could not find a version that satisfies the requirement numpy==2.0.0rc1 (from versions: 1.3.0, 1.4.1, 1.5.0, 1.5.1, 1.6.0, 1.6.1, 1.6.2, 1.7.0, 1.7.1, 1.7.2, 1.8.0, 1.8.1, 1.8.2, 1.9.0, 1.9.1, 1.9.2, 1.9.3, 1.10.0.post2, 1.10.1, 1.10.2, 1.10.4, 1.11.0, 1.11.1, 1.11.2, 1.11.3, 1.12.0, 1.12.1, 1.13.0, 1.13.1, 1.13.3, 1.14.0, 1.14.1, 1.14.2, 1.14.3, 1.14.4, 1.14.5, 1.14.6, 1.15.0, 1.15.1, 1.15.2, 1.15.3, 1.15.4, 1.16.0, 1.16.1, 1.16.2, 1.16.3, 1.16.4, 1.16.5, 1.16.6, 1.17.0, 1.17.1, 1.17.2, 1.17.3, 1.17.4, 1.17.5, 1.18.0, 1.18.1, 1.18.2, 1.18.3, 1.18.4, 1.18.5, 1.19.0, 1.19.1, 1.19.2, 1.19.3, 1.19.4, 1.19.5, 1.20.0, 1.20.1, 1.20.2, 1.20.3, 1.21.0, 1.21.1, 1.22.0, 1.22.1, 1.22.2, 1.22.3, 1.22.4, 1.23.0, 1.23.1, 1.23.2, 1.23.3, 1.23.4, 1.23.5, 1.24.0, 1.24.1, 1.24.2, 1.24.3, 1.24.4, 1.25.0, 1.25.1, 1.25.2, 1.26.0, 1.26.1, 1.26.2, 1.26.3, 1.26.4, 2.0.0, 2.0.1, 2.0.2, 2.1.0rc1, 2.1.0, 2.1.1, 2.1.2)
      ERROR: No matching distribution found for numpy==2.0.0rc1
      [end of output]
  note: This error originates from a subprocess, and is likely not a problem with pip.
error: subprocess-exited-with-error
× pip subprocess to install build dependencies did not run successfully.
│ exit code: 1
╰─> See above for output.
note: This error originates from a subprocess, and is likely not a problem with pip.

