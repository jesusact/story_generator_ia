# Story Creator API: Interactive Story Generator

This project is a **Story Creator API** that allows users to generate creative, detailed, and engaging stories interactively. Built on a language model API, it takes user inputs for key story elements and generates a narrative tailored to their specifications. The tool is designed for creative writing, entertainment, and brainstorming purposes.

## Features

- **Interactive Input:** Users can specify:
  - Main character's name
  - Secondary character's name
  - Setting of the story
  - Main action or plot
  - Creativity level (temperature)
  - Maximum story length (tokens)
  - Nucleus sampling value for output variability
- **Dynamic Story Generation:** Creates stories with a structured narrative, including a clear beginning, middle, and end.
- **Customizable Parameters:** Adjust temperature, token limits, and more to influence story style and length.
- **User-Friendly Design:** Prompts guide users through input to ensure engaging story creation.

### Prerequisites

- **Python 3.8 or later**
- **text-generation-webui:** 

   The Story Creator API requires **text-generation-webui** to provide the language model backend for generating stories. Make sure you have text-generation-webui installed and configured before using this script.

   - **Installation Instructions for text-generation-webui:**  
     Follow the official instructions from the [text-generation-webui GitHub repository](https://github.com/oobabooga/text-generation-webui).  
     Ensure the web UI is running locally before using this script.  

---

API Setup
The script requires a running language model API to generate stories. Ensure you have the API set up and update the script’s url variable with the correct endpoint.

## Usage

### 1. Clone the Repository
```bash
git clone https://github.com/jaceval/story_generator_ia.git
cd story_generator_ia
```
### 2. Create and Activate a Virtual Environment
On Windows:
```
python -m venv venv
venv\Scripts\activate
```
On macOS/Linux:
```
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
With the virtual environment activated, install the required dependencies:
```
pip install requests
```

## Usage

### 1.Start the text-generation-webui Server
Ensure that text-generation-webui is running locally on http://127.0.0.1:5000. You can modify the URL in the script if the server runs on a different endpoint.

### 2. Run the Script
Run the script using Python:
```
python story_creator.py
```
### 3. Input Story Details
Follow the prompts in the terminal to provide story details:

Enter character names, the setting, and the main action.
Specify creativity (temperature) and story length (max_tokens).
Example:
```
Enter the name of the main character: Alice  
Enter the name of the secondary character: Bob  
Where does the story take place? Wonderland  
What's the main action of the story? Alice and Bob explore an enchanted forest  
Set creativity level (0.0 to 1.0, default 0.7): 0.8  
Set max tokens for the story (default 200): 300  
Set nucleus sampling value (0.0 to 1.0, default 1.0): 0.9
```
Example Output
```
Generated Story:

Alice and Bob wandered into the heart of the enchanted forest, where every step seemed to echo with whispers of magic. Towering trees with leaves that shimmered like emeralds cast dappled light on the soft mossy ground...

```
