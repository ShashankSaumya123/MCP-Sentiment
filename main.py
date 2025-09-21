import gradio as gr
import json
from textblob import TextBlob

def sentiment_analysis(text: str) -> str:
    """
    Analyze the sentiment of the given text.

    Args:
        text (str): The input text to analyze.

    Returns:
        str: A json stirng containing polarity and subjectivity and assessment.
    """
    
    blob = TextBlob(text)
    sentiment = blob.sentiment

    result = {"polarity": round(sentiment.polarity,2), "subjectivity": round(sentiment.subjectivity,2) "assessment": "positive" if sentiment.polarity > 0 else "negative" if sentiment.polarity < 0 else "neutral"}

    return json.dumps(result)

# Create a Gradio interface
demo = gr.Interface(
    fn=sentiment_analysis,
    inputs=gr.Textbox(placeholder="Enter text here..."),
    outputs=gr.Textbox(),
    title="Text Sentiment Analysis",
    description="Analyze the sentiment of text usng TextBlob."
)

# Launch the Gradio app
if __name__ == "__main__":
    demo.launch(mcp_server = True)