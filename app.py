from flask import Flask, jsonify

app = Flask(__name__)
HTML_PAGE = """
<!doctype html>
<html>
  <head>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB" crossorigin="anonymous">
  <title>Addition App</title></head>
  <body style="font-family: Arial; margin: 40px;">
    <h1>Simple Addition Web App</h1>
    <form method="post">
      <label class="form-label">First number:</label>
      <input type="number" name="a" required class="form-control"><br><br>
      <label class="form-label">Second number:</label>
      <input type="number" name="b" required class="form-control"><br><br>
      <button type="submit" value="Add" class="btn btn-primary"></button>
    </form>
    {% if result is not none %}
      <h2>Result: {{ result }}</h2>
    {% endif %}
  </body>
</html>
"""

def add_numbers(a, b):
    return a + b

@app.route("/")
def home():
    return jsonify({"status": "ok", "message": "Hello from cloud-project-2! Sulieman Wardat says hello"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080) # nosec B104
