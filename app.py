from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# Sample questions for each category
questions_data = {
    "coding": [
        {
            "question": "What does HTML stand for?",
            "answer": "HyperText Markup Language",
            "explanation": "HTML is the standard markup language for creating web pages."
        },
        {
            "question": "Which HTML element is used for the largest heading?",
            "answer": "h1",
            "explanation": "The <h1> element defines the most important heading."
        },
        {
            "question": "What is the purpose of CSS?",
            "answer": "Style the layout of web pages",
            "explanation": "CSS is used to control the style and layout of multiple web pages all at once."
        },
        {
            "question": "What does CSS stand for?",
            "answer": "Cascading Style Sheets",
            "explanation": "CSS describes how HTML elements are to be displayed on screen."
        },
        {
            "question": "Which is a JavaScript framework?",
            "answer": "Angular",
            "explanation": "Angular is a platform and framework for building single-page client applications using HTML and TypeScript."
        },
        {
            "question": "What is the correct syntax for referring to an external script called 'script.js'?",
            "answer": "<script src='script.js'></script>",
            "explanation": "This syntax allows you to include an external JavaScript file."
        },
        {
            "question": "What does DOM stand for?",
            "answer": "Document Object Model",
            "explanation": "DOM is a programming interface for web documents."
        },
    ],
    "carpentry": [
        {
            "question": "What is the main purpose of a saw?",
            "answer": "Cut wood",
            "explanation": "Saws are used to cut hard materials like wood."
        },
        {
            "question": "Which tool is used to drive nails?",
            "answer": "Hammer",
            "explanation": "A hammer is a hand tool used to drive nails into wood."
        },
        {
            "question": "What type of wood is commonly used for furniture?",
            "answer": "Hardwood",
            "explanation": "Hardwood is known for its durability and aesthetic appeal."
        },
        {
            "question": "What is a chisel used for?",
            "answer": "Carving or cutting",
            "explanation": "Chisels are used for carving or cutting hard materials."
        },
        {
            "question": "What tool is used to measure angles?",
            "answer": "Protractor",
            "explanation": "A protractor is used to measure angles in degrees."
        },
        {
            "question": "What is the purpose of wood glue?",
            "answer": "Bond wood pieces together",
            "explanation": "Wood glue is used to bond wooden pieces together in carpentry."
        },
        {
            "question": "What is a planer used for?",
            "answer": "Flattening wood surfaces",
            "explanation": "A planer is used to smooth and flatten wood surfaces."
        },
    ],
    "healthcare": [
        {
            "question": "What is the normal body temperature in Celsius?",
            "answer": "37",
            "explanation": "The normal body temperature is around 37 degrees Celsius."
        },
        {
            "question": "What does CPR stand for?",
            "answer": "Cardiopulmonary resuscitation",
            "explanation": "CPR is an emergency procedure to help someone whose heart has stopped."
        },
        {
            "question": "What is the main function of red blood cells?",
            "answer": "Carry oxygen",
            "explanation": "Red blood cells carry oxygen from the lungs to the rest of the body."
        },
        {
            "question": "What is hypertension commonly known as?",
            "answer": "High blood pressure",
            "explanation": "Hypertension is a condition in which the blood pressure in the arteries is persistently elevated."
        },
        {
            "question": "What is a common symptom of diabetes?",
            "answer": "Increased thirst",
            "explanation": "Increased thirst is a common symptom of diabetes."
        },
        {
            "question": "What is the role of a nurse?",
            "answer": "Provide patient care",
            "explanation": "Nurses provide care and support to patients in various healthcare settings."
        },
        {
            "question": "What is a vaccine used for?",
            "answer": "Prevent disease",
            "explanation": "Vaccines are used to stimulate the immune system to prevent disease."
        },
    ]
}

# Route to serve the main quiz page
@app.route('/')
def index():
    return render_template('index.html')

# Route to fetch questions based on category
@app.route('/get_questions', methods=['GET'])
def get_questions():
    category = request.args.get('category')
    if category in questions_data:
        return jsonify(questions_data[category])
    else:
        return jsonify([]), 404

if __name__ == '__main__':
    app.run(debug=True, port=8000)
