webpage = """
<html>
<h1>Hello!</h1>
<p>This is a webpage. You can open it in a web browser.</p>
</html>
"""
image = """
<svg xmlns="http://www.w3.org/2000/svg" height="210" width="210">
  <polygon points="100,10 40,198 190,78 10,78 160,198"/>
</svg>
"""

# Write the string `webpage` to a file called "hello.html"

file = open("hello.html", "w")
file.write(webpage)
file.close()

# Write the string `image` to a file called "star.svg"
# Check that you can open the files in your file explorer

file = open("star.svg", "w")
file.write(image)
file.close()

