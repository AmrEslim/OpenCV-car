# OpenCV Car Project

An autonomous car project using OpenCV on Raspberry Pi 3 B+ with omnidirectional movement capabilities.

## Overview

This project is part of the OmniCar initiative and demonstrates computer vision-based autonomous navigation using OpenCV. The system is designed to run on a Raspberry Pi 3 B+ and implements omni-directional kinematics, allowing the car to move in all directions while processing visual input for navigation and obstacle avoidance.

## Features

- **Computer Vision Navigation**: Real-time image processing using OpenCV
- **Omnidirectional Movement**: Advanced kinematics for movement in all directions
- **Raspberry Pi Integration**: Optimized for Raspberry Pi 3 B+ hardware
- **Real-time Processing**: Live camera feed analysis and decision making
- **Autonomous Control**: Self-directed movement based on visual input

## Hardware Requirements

- Raspberry Pi 3 B+
- Raspberry Pi Camera Module or USB Camera
- Omnidirectional wheels/motors setup
- Motor driver board
- Power supply
- Chassis and mounting hardware

## Software Requirements

- Python 3.7+
- OpenCV 4.0+
- NumPy
- RPi.GPIO (for Raspberry Pi GPIO control)
- Additional Python libraries as specified in requirements.txt

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/AmrEslim/OpenCV-car.git
   cd OpenCV-car
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Enable camera on Raspberry Pi**:
   ```bash
   sudo raspi-config
   # Navigate to Interface Options > Camera > Enable
   ```

4. **Set up hardware connections** according to the wiring diagram (see documentation)

## Usage

1. **Basic operation**:
   ```bash
   python main.py
   ```

2. **Run with specific parameters**:
   ```bash
   python main.py --camera-index 0 --resolution 640x480
   ```

3. **Debug mode**:
   ```bash
   python main.py --debug
   ```

## Project Structure

```
OpenCV-car/
├── src/
│   ├── main.py              # Main application entry point
│   ├── vision/              # Computer vision modules
│   ├── control/             # Motor control and kinematics
│   └── utils/               # Utility functions
├── config/                  # Configuration files
├── docs/                    # Documentation
├── tests/                   # Unit tests
└── requirements.txt         # Python dependencies
```

## Configuration

Edit the configuration files in the `config/` directory to customize:
- Camera parameters
- Motor control settings
- Vision processing parameters
- Movement algorithms

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Part of the OmniCar project initiative
- Built for educational and research purposes
- Thanks to the OpenCV community for excellent documentation and examples

## Support

If you encounter any issues or have questions:
- Open an issue on GitHub
- Check the documentation in the `docs/` folder
- Review existing issues for solutions

## Project Status

This project was maintained and under development as a Uni Project.

---

**Note**: This project was developed as part of academic research. Please ensure you have the necessary hardware setup before attempting to run the code.
