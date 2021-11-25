from IPython.core.display import display, HTML

def browse_trees():
    html = """
    <!DOCTYPE html>
    <html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    </head>
    <body>

    <h1>Browse a tree by ID</h1>
    <p>Current tree:</p>

    <div class="slidecontainer">
      <input type="range" min="0" max="199" value="0" class="slider" id="myRange">
      <p>ID: <span id="demo"></span></p>
    </div>

    <div id="tree_image">
          <img id="tree_url" src="trees/tree_0.png">
    </div>

    <p id="link"></p>

    <script>
    var slider = document.getElementById("myRange");
    var output = document.getElementById("demo");
    output.innerHTML = slider.value;

    slider.oninput = function() {
      output.innerHTML = this.value;

      var x = "trees/tree_"+this.value+".png";
      document.getElementById("tree_url").src = x;
    }
    </script>

    </body>
    </html>

    """
    display(HTML(html))
