# AudioVisual Fusion Suite

Please read our research paper (Project_latex.pdf) for complete explanations in all respects about this repo. Because we only mentioned a summary in this Github README. 

This project goes beyond simply finding and evaluating models; it combines selected models into an interesting application. Our chosen model for image segmentation is SAM, and we've successfully applied it to video (Approach 3 and 2). We also utilized the DETR (End-to-End Object Detection) model with a ResNet-50 backbone, and pushed the dockerized application to Docker Hub for use. For voice conversion, we selected the so-vits-svc-fork Model, which enables us to change a singer's voice to any desired sound. Finally, we integrated these two applications into one: Combination of vi & vc.

## Getting Started

To use the video inpainting, navigate to the `video inpainting` directory. If you want to segment an image, go to the `image segmentation` folder, where you will find notebooks with the relevant codes. If you want to apply image inpainting, we have a combination of segmentation and inpainting for Photoshop work in a notebook called `image inpainting` (this section may be made a separate project in the future). Lastly, if you want to apply image segmentation to a video, go to the `applying Is to video` directory. In this directory, there are three notebooks about SAM; we recommend using Approach 3. The last notebook implements the DETR model with ResNet-50 backbone. In addition, all Docker-related files are in the video inpainting directory for future modifications.

For the `voice cloning` directory, it contains a single notebook that specifies model training, testing, and usage. For more information, please refer to the paper.

Finally, to use the combination of these two applications (video inpaintig and voice conversion), which uses SAM for the video section, go to the `combination of vi & vc` directory.

## Prerequisites

  - Python 3.x
  - oogle Colab or Jupyter Notebook
  - Docker
  - Linux system (Ubuntu 22.04)
  - Nvidia GPU
  - CUDA Toolkit

## Installation

Clone the repository:

```bash
git clone https://github.com/<your-repo>/your-project.git
```

## Usage

Detailed usage instructions are provided in each directory's notebooks. Please refer to them for specific steps to run the models.

## Contributing

Contributions are welcome. Please open an issue to discuss the change or improvement you want to make, or create a pull request to propose your changes.


