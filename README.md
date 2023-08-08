# Transcribe audio

**Transcribe audio** is a Python application designed to transcribe audio files, like podcasts or home videos. Its primary use case is for searching through audio files for specific words or phrases.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You need Python 3.x to run the following code. You can check your Python version using the command:

```bash
python --version
```

### Installing

After confirming your Python installation and cloning the repository, run:

```bash
pip install -r requirements.txt
```

#### Configuring Environment Variables

Copy the `example.env` file and rename it to `.env`:

```bash
cp example.env .env
```

Open the `.env` file and replace the placeholders with your actual values.

### Running the Application

You can run the application using the following command:

```bash
python run.py
```

Alternatively, use the provided `run.sh` script.

## Docker Support

This application comes with Docker support. You can build a Docker image using the provided Dockerfile:

```bash
docker build -t my-python-app .
```

Then run the application:

```bash
docker run -it --rm --name my-running-app my-python-app
```

## VSCode Settings

The repository includes a `.vscode` folder for those who prefer to use Visual Studio Code as their IDE.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.
