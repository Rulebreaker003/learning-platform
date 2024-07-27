from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a strong secret key

# Dummy data for course details
course_details = {
    "Python": {
        "name": "Python",
        "description": "A comprehensive course on Python programming. Learn Python syntax, data structures, and algorithms. Suitable for beginners and experienced developers.",
        "instructor": "Varun",
        "duration": "8 weeks",
        "level": "Intermediate",
        "syntax": "Python 3.x",
        "uses": "Web development, Data analysis, Automation",
        "urls": {
            "Learn More": "https://example.com/python-course",
            "w3schools": "https://www.w3schools.com/python/",
            "Advanced Topics": "https://www.geeksforgeeks.org/python-programming-language/",
        }
    },
    "Java": {
        "name": "Java",
        "description": "Master the Java programming language. Cover topics such as object-oriented programming, Java frameworks, and best practices. Suitable for Java enthusiasts.",
        "instructor": "Varun",
        "duration": "10 weeks",
        "level": "Intermediate",
        "syntax": "Java SE, Java EE",
        "uses": "Enterprise applications, Android development",
        "urls": {
            "Learn More": "https://example.com/java-course",
            "w3schools": "https://www.w3schools.com/java/",
            "Advanced Topics": "https://www.geeksforgeeks.org/java/",
        }
    },
    "C": {
        "name": "C",
        "description": "Explore the fundamentals of the C programming language. Focus on pointers, memory management, and low-level programming concepts. Ideal for system programming.",
        "instructor": "Varun",
        "duration": "6 weeks",
        "level": "Intermediate",
        "syntax": "C",
        "uses": "System programming, Embedded systems",
        "urls": {
            "Learn More": "https://example.com/c-course",
            "w3schools": "https://www.w3schools.com/c/",
            "Advanced Topics": "https://www.geeksforgeeks.org/c-programming-language/",
        }
    },
    "C++": {
        "name": "C++",
        "description": "Dive into C++ programming. Cover object-oriented principles, templates, and advanced C++ features. Suitable for those wanting to master C++ development.",
        "instructor": "Varun",
        "duration": "12 weeks",
        "level": "Advanced",
        "syntax": "C++",
        "uses": "Game development, Systems programming",
        "urls": {
            "Learn More": "https://example.com/cpp-course",
            "w3schools": "https://www.w3schools.com/cpp/",
            "Advanced Topics": "https://www.geeksforgeeks.org/c-plus-plus/",
        }
    },
}

users = {
    "Varun": "Varun123",
    "Bhavya": "Bhavya123",
}

@app.route('/')
def index():
    if 'username' in session:
        course_names = list(course_details.keys())
        return render_template('index.html', course_names=course_names)
    else:
        return redirect(url_for('login'))

@app.route('/course/<course_name>')
def course_page(course_name):
    if course_name in course_details:
        course_info = course_details[course_name]
        return render_template('course_page.html', course_info=course_info)
    else:
        return "Course not found", 404

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error='Invalid username or password')

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username not in users:
            users[username] = password
            return redirect(url_for('login'))
        else:
            return render_template('login.html', error='Username already exists')

    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True)