from flask import Flask, render_template, request, send_file
from langchain import OpenAI, SQLDatabase, SQLDatabaseChain
import os
import webbrowser
app = Flask(__name__)

os.environ['OPENAI_API_KEY'] = "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"  # Expires on January 1st, 2024
database_uri = "sqlite:///Database/DATABASE.db"  # database file (sqlite)
database = SQLDatabase.from_uri(database_uri)
large_language_model = OpenAI(temperature=0)
database_chain = SQLDatabaseChain(llm=large_language_model, database=database, verbose=False)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_input = request.form["user_input"]
        try:
            response = database_chain.run(user_input)
            return render_template("index.html", response=response)
        except Exception as e:
            return render_template("index.html", error=f"Oops.. An Error Occurred: {e}")
    return render_template("index.html")

@app.route("/Readme.txt")
def get_readme():
    try:
        # Provide the correct path to the Readme.txt file
        readme_path = "templates/Readme.txt"  # Update this path as needed
        return send_file(readme_path, as_attachment=False)
    except Exception as e:
        return render_template("index.html", error=f"Oops.. An Error Occurred: {e}")

if __name__ == "__main__":
    port = 5000
    url = f"http://localhost:{port}"
    webbrowser.open(url)    #To automatically open the browser with localhost
    app.run(debug=True, port=port, use_reloader=False)
