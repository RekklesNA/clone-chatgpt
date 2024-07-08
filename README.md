# Clone-ChatGPT

Clone-ChatGPT is a simple web application that replicates the functionality of OpenAI's ChatGPT using the OpenAI API and Streamlit framework. This application allows users to interact with an AI model that can generate human-like text responses based on user inputs.

## Features

- Interactive chat interface using Streamlit
- Uses OpenAI's GPT-4o model for generating responses
- Stores conversation history using LangChain's `ConversationBufferMemory`
- Simple and intuitive user interface

## Installation

### Prerequisites

- Python 3.9 or higher
- OpenAI API key

### Steps

1. **Clone the repository:**

    ```sh
    git clone https://github.com/RekklesNA/clone-chatgpt.git
    cd clone-chatgpt
    ```

2. **Create and activate a virtual environment:**

    ```sh
    python -m venv .venv
    .venv\Scripts\activate   # On Windows
    source .venv/bin/activate  # On macOS/Linux
    ```

3. **Install the required packages:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Run the application:**

    ```sh
    streamlit run main.py
    ```

## Usage

1. Open your web browser and navigate to `http://localhost:8501`.
2. Enter your OpenAI API key in the sidebar.
3. Start chatting with the AI model by entering text in the chat input.

## File Structure

- `main.py`: The main application file containing the Streamlit interface and chat logic.
- `utils.py`: Contains helper functions, including the `get_chat_response` function for interacting with the OpenAI API.
- `requirements.txt`: Lists all the Python packages required to run the application.
- `Dockerfile`: Contains instructions for building a Docker image for the application.

## Docker

To build and run the application using Docker, follow these steps:

1. **Build the Docker image:**

    ```sh
    docker build -t cloned-chatgpt .
    ```

2. **Run the Docker container:**

    ```sh
    docker run -p 8501:8501 cloned-chatgpt
    ```

3. Open your web browser and navigate to `http://localhost:8501`.

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

## Acknowledgments

- OpenAI for providing the GPT-4o model
- Streamlit for providing an easy-to-use framework for creating web applications
- LangChain for providing tools to manage conversation history

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an issue.


