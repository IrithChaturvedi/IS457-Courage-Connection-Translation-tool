from flask import Flask, render_template, request
from googletrans import Translator
from utils import extract_text_from_file

app = Flask(__name__)
translator = Translator()

LANGUAGES = {
    "Spanish": "es",
    "French": "fr"
}

@app.route("/", methods=["GET", "POST"])
def index():
    original_text = ""
    translated_text = ""
    error_message = ""
    selected_language = "Spanish"

    if request.method == "POST":
        selected_language = request.form.get("language", "Spanish")
        target_lang = LANGUAGES[selected_language]

        # Text from textarea
        original_text = request.form.get("text_input", "").strip()

        # Check if file was uploaded
        file = request.files.get("file_input")

        try:
            if file and file.filename:
                # If a file is uploaded, we ignore the text box and use the file content
                original_text = extract_text_from_file(file)

            if not original_text:
                error_message = "Please enter text or upload a document."
            else:
                # Translate using googletrans
                result = translator.translate(original_text, dest=target_lang)
                translated_text = result.text

        except ValueError as ve:
            error_message = str(ve)
        except Exception as e:
            error_message = f"Translation failed: {e}"

    return render_template(
        "index.html",
        languages=LANGUAGES.keys(),
        selected_language=selected_language,
        original_text=original_text,
        translated_text=translated_text,
        error_message=error_message,
    )

if __name__ == "__main__":
    app.run(debug=True)
