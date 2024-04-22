import json
import re
import nltk
from nltk.tokenize import word_tokenize

# Load the dataset from JSON
with open('crop_info.json') as f:
    crop_data = json.load(f)

# Function to get information about a specific crop or pest
def get_info(input_text):
    tokens = word_tokenize(input_text.lower())
    for crop in crop_data:
        crop_tokens = word_tokenize(crop['CROP TYPE'].lower())
        if any(token in crop_tokens for token in tokens):
            return crop
        pests = crop['MAJOR PESTS'].lower().split(', ')
        for pest in pests:
            pest_tokens = word_tokenize(pest)
            if any(token in pest_tokens for token in tokens):
                return crop
    return None

# Function to extract temperature from text
def extract_temperature(text):
    temperatures = re.findall(r'\b\d{1,2}\b', text)
    if temperatures:
        return int(temperatures[0])
    return None

# Function to generate a response based on user input
def generate_response(user_input):
    temperature = extract_temperature(user_input)
    if temperature:
        temperature_condition = None
        for condition in ['hot', 'warm', 'cold', 'cool']:
            if condition in user_input.lower():
                temperature_condition = condition
                break
        
        if temperature_condition:
            relevant_crops = []
            for crop in crop_data:
                temp_range = re.findall(r'\d{1,2}-\d{1,2}', crop['Weather Conditions'])
                if temp_range:
                    min_temp, max_temp = map(int, temp_range[0].split('-'))
                    if min_temp <= temperature <= max_temp:
                        relevant_crops.append(crop)
            
            if relevant_crops:
                response = ""
                for crop in relevant_crops:
                    response += f"For {crop['CROP TYPE']}:\n"
                    response += f"Major pests: {crop['MAJOR PESTS']}\n"
                    response += f"Frequency they hate: {crop['Frequency they hate']}\n"
                    response += f"Weather Conditions: {crop['Weather Conditions']}\n"
                    response += f"Geological location: {crop['Geological location']}\n\n"
            else:
                response = f"No crops found suitable for {temperature}°C temperature."
        else:
            response = "Sorry, I couldn't determine the temperature condition from your input."
    else:
        response = ""
        info = get_info(user_input)
        if info:
            response += f"For {info['CROP TYPE']}:\n"
            response += f"Major pests: {info['MAJOR PESTS']}\n"
            response += f"Frequency they hate: {info['Frequency they hate']}\n"
            response += f"Weather Conditions: {info['Weather Conditions']}\n"
            response += f"Geological location: {info['Geological location']}\n\n"
        else:
            response = "Sorry, I couldn't find information about that crop or pest."
    
    return response

# Main function to run the chatbot
def main():
    print("Welcome to the Crop Information Chatbot!")
    while True:
        user_input = input("Enter a description of temperature conditions, crop type, or pest, or 'exit' to quit: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        response = generate_response(user_input)
        print(response)

if __name__ == "__main__":
    main()