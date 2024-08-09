from EmotionDetection.emotion_detection import emotion_detector
from EmotionDetection.emotion_detection import emotion_predictor

def run_tests():
    # Test 1: Simple text with positive emotion
    text = "I'm happy I got the job, but I'm nervous about the responsibilities."
    print(f"Testing with text: {text}")
    detected_emotions = emotion_detector(text)
    print("Detected Emotions:", detected_emotions)
    formatted_response = emotion_predictor(detected_emotions)
    print("Formatted Response:", formatted_response)
    print("-----------")

if __name__ == "__main__":
    run_tests()