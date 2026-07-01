#JPEG Image Compression using Manual DCT
A Multimedia Engineering implementation of the Baseline JPEG compression algorithm using the mathematical formulation of the Discrete Cosine Transform (DCT).

#OVERVIEW
This project implements the core stages of JPEG image compression from scratch using the mathematical equations of the two-dimensional Discrete Cosine Transform (2D-DCT).This project implements the core stages of JPEG image compression from scratch using the mathematical equations of the two-dimensional Discrete Cosine Transform (2D-DCT).
Instead of using built-in DCT libraries such as OpenCV or SciPy, the transform and inverse transform are manually implemented based on the equations presented in the Multimedia Engineering course.

#FEATURES
Manual 2D-DCT implementation
Manual Inverse DCT (IDCT)
JPEG Quantization
Image Reconstruction
Histogram Comparison
Difference Image
MSE Calculation
PSNR Calculation
Compression Ratio Estimation
Command Line Interface (CLI)

#PROJECT STRUCTURE
dct.py              DCT and IDCT
quantization.py     JPEG Quantization
metrics.py          MSE PSNR Compression Ratio
graphs.py           Visualization
utils.py            Image Processing
jpeg_dct.py         Main Program

#WORKFLOW
Input Image
      │
      ▼
8×8 Block Division
      │
      ▼
Level Shift
      │
      ▼
Manual 2D DCT
      │
      ▼
Quantization
      │
      ▼
Inverse Quantization
      │
      ▼
Manual IDCT
      │
      ▼
Image Reconstruction
      │
      ▼
Performance Evaluation

#SAMPLE RESULTS
![alt text](image.png)

#SAMPLE HISTOGRAM COMPARASION
![alt text](image-1.png)

#DIFFERENCE IMAGE
![alt text](image-2.png)

#PERFORMANCE AT DIFFERNT Q, FROM Q=20 - Q=90 OF THE SELECTED IMAGE DATASET BENCHMARK AT TIME OF IMPLEMENTATION
![alt text](image-3.png)

#INSTALLATION GUIDE 
git clone ---(repo)

python install -r requirements.txt


#AUTHOR
Zayyanu Awwal
Informatics
Universitas Sebelas Maret, Surakarta