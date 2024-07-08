# clone-chatgpt

clone-chatgpt is an open-source project that replicates the functionality of OpenAI's ChatGPT using the OpenAI API and Streamlit framework. This project provides a simple interface for deploying a conversational AI model capable of generating human-like text based on user input.

## Features

- **Natural Language Understanding:** Efficiently processes and understands user inputs to generate coherent and contextually appropriate responses.
- **Customizable:** Easily modify the model's behavior and responses to suit specific use cases.
- **User-friendly Interface:** Simple and intuitive interface built with Streamlit for seamless interaction with the AI model.
- **Integration Ready:** Easily integrates with existing systems and applications for enhanced functionality.

## Requirements

- Python 3.9 or above
- OpenAI API Key

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/RekklesNA/clone-chatgpt.git
    cd clone-chatgpt
    ```

2. **Set up a virtual environment:**

    ```sh
    python -m venv .venv
    source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Set up your OpenAI API Key:**

    Create a `.env` file in the project root directory and add your OpenAI API key:

    ```plaintext
    OPENAI_API_KEY=your_openai_api_key
    ```

## Usage

1. **Run the Streamlit app:**

    ```sh
    streamlit run main.py
    ```

2. **Access the application:**

    Open your browser and go to `http://localhost:8501` to interact with the application.

## Docker

You can also run the application using Docker.

1. **Build the Docker image:**

    ```sh
    docker build -t clone-chatgpt .
    ```

2. **Run the Docker container:**

    ```sh
    docker run -p 8501:8501 clone-chatgpt
    ```

3. **Access the application:**

    Open your browser and go to `http://localhost:8501` to interact with the application.

## Files

- `main.py`: The main script that runs the Streamlit application.
- `utils.py`: Utility functions used in the application.
- `requirements.txt`: A file listing all the dependencies needed for the project.
- `Dockerfile`: Configuration file for Docker to build the application image.
- `LICENSE`: The license under which the project is distributed.

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request if you have any improvements or suggestions.

## Acknowledgements

- [OpenAI](https://www.openai.com) for providing the GPT-4o model.
- [Streamlit](https://www.streamlit.io) for providing the framework to build the application.

