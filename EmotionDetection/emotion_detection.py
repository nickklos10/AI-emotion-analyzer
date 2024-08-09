import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def emotion_detector(text_to_analyze):
    """
    Send text to the OpenAI API and analyze the emotions.
    """
    try:
        response = openai.chat.completions.create(
            model="gpt-4o-mini",  
            messages=[
                {"role": "system", "content": "You are an assistant that helps analyze emotions in text. Provide the likelihood of each emotion (anger, disgust, fear, joy, sadness) as a percentage, formatted as 'emotion: percentage%'."},
                {"role": "user", "content": f"Please analyze the following text and identify the emotions with their likelihoods: '{text_to_analyze}'"}
            ]
        )

        # Extract the content of the assistant's response
        result_text = response.choices[0].message.content.strip()

        # Print the response for debugging purposes
        print("Assistant Response:", result_text)

        # Split the response by new lines
        emotion_lines = result_text.split('\n')
        emotions = {}
        for line in emotion_lines:
            # Attempt to split the line into two parts
            parts = line.split(':')
            if len(parts) != 2:
                continue  # Skip lines that don't match the expected format

            emotion = parts[0].strip().lower()
            try:
                percentage = float(parts[1].strip().replace('%', '')) / 100  # Convert to a 0-1 scale
            except ValueError:
                continue  # Skip lines with invalid percentage values

            emotions[emotion] = percentage

        if not emotions:
            raise ValueError("No valid emotions detected in the response.")

        # Determine the dominant emotion
        dominant_emotion = max(emotions, key=emotions.get)

        # Format the response
        formatted_response = {**emotions, 'dominant_emotion': dominant_emotion}

        return formatted_response

    except Exception as e:
        print(f"An error occurred: {e}")
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

def emotion_predictor(detected_text):
    """
    Format the response from the emotion_detector.
    """
    if all(value is None for value in detected_text.values()):
        return detected_text
    return detected_text




