# Fortune Telling & Product Recommendation Agent System

This project implements a multi-agent system designed to provide users with personalized fortune predictions (work, love, wealth) based on their name, date of birth, and handprint. It then recommends a product based on a color associated with their fortune.

---

## 🚀 How to Set Up and Run

### Prerequisites
* Docker and Docker Compose installed on your system.
* An OpenAI API Key.

### Steps
1.  **Clone the Repository:**
    ```bash
    git clone (https://github.com/arkadaz/assignment_CJ.git)
    cd assignment_CJ
    ```

2.  **Create an Environment File:**
    Create a `.env` file in the root directory of the project with your OpenAI API Key:
    ```env
    OPENAI_API_KEY="your_openai_api_key_here"
    ```

3.  **Build and Run with Docker Compose:**
    Navigate to the project's root directory in your terminal and run:
    ```bash
    docker-compose up --build -d
    ```
    The `-d` flag runs the containers in detached mode.

4.  **Access the Application:**
    Open your web browser and go to:
    ```
    http://localhost:8501
    ```

---

## 💡 Solution Design Overview

This project utilizes a multi-agent system powered by an **OpenAI LLM** (e.g., GPT-3.5/4) and an agentic framework to deliver personalized fortune predictions and product recommendations.

* **Agent Architecture:**
    The system employs several specialized agents:
    1.  **Fortune Agent (Controller):** Manages the overall user interaction and prediction workflow. It prompts for the user's name and date of birth, and guides the prediction process.
    2.  **Extractor Agent:** Responsible for parsing and extracting key information (name, date of birth) from user inputs. This data is stored temporarily for use by other agents.
    3.  **Analyzer Agent (Vision Agent):** This agent processes an image of the user's handprint, performing analysis to contribute to the fortune prediction.
    4.  **Workflow (Pipeline):** Defines the sequence and logic governing how the Fortune, Extractor, and Analyzer agents collaborate to generate the prediction.

---

## ✨ Features Implemented

* **Personalized Fortune Telling:** Utilizes the user's **name** and **date of birth** for tailored predictions.
* **Multi-modal Input:** Accepts both textual input (name, DOB) and image input (**handprint analysis**) for comprehensive predictions.
* **Targeted Predictions:** Offers insights across various life aspects such as **work, love, or wealth**.
* **Color-Based Product Recommendation:**
    * Associates the fortune prediction outcome with a specific **color**.
    * Maps this color to a relevant **product**, which is then recommended to the user.

---

## 🎨 Notable Design Choices

* **Multi-Agent System:** A modular architecture with distinct agents for control, information extraction, and image analysis. This promotes maintainability and scalability.
* **Vision Capabilities:** Integration of a vision agent for handprint analysis adds a unique, interactive element to the fortune-telling process.
* **Dockerized Deployment:** The application is containerized using Docker, simplifying setup and ensuring consistent environments.
* **Pipeline Workflow:** A structured pipeline ensures a logical progression from data collection to the final prediction and recommendation.
* **Integrated Recommendation:** The fortune-telling feature is directly linked to a tangible product recommendation via a color-mapping mechanism, enhancing user engagement.

---

## 🔧 Dependencies

All necessary dependencies are listed in the `requirements.txt` file and are managed by the Docker build process.

---

## (Optional) 🚧 Challenges Faced & Solutions

*(This section is optional but highly recommended. You can describe any technical hurdles you encountered during development and how you overcame them. For example:*

* ***Challenge:*** *Integrating the handprint image analysis with the text-based agent flow within the Docker environment.*
    * ***Solution:*** *Developed a clear API endpoint for the Analyzer Agent that the Fortune Agent could call, ensuring proper data handling (e.g., image encoding/decoding) between containerized services or within the application flow.*
* ***Challenge:*** *Ensuring secure handling of the OpenAI API key.*
    * ***Solution:*** *Utilized a `.env` file to store the API key, which is loaded by the application at runtime and kept out of version control (via `.gitignore`).*)
