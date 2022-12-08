from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/gg3', methods=['GET', 'POST'])
def main():
    minimum = 0
    maximum = 1000
    attempts = 10
    attempt = 1
    invitation_str = f'Computer: Think of a number between {minimum} and {maximum}, ' \
                     f'and I will try to guess it in {attempts} tries!'

    if request.method == 'POST':
        minimum = int(request.form.get('minimum', 0))
        maximum = int(request.form.get('maximum', 1000))
        guess = int(request.form.get('guess', 500))
        guess_str = f'Computer: My guess number {attempt}, is "{guess}"'
        user_info = request.form.get("info")

        if user_info == 'correct':
            guess_str = 'Computer: Yeah! I am always the best!'
        elif user_info == 'too small':
            minimum = guess
            attempt += 1
        elif user_info == 'too big':
            maximum = guess
            attempt += 1
        guess = int((maximum - minimum) / 2) + minimum

        return render_template('Guessing game 3.html', mtd='POST', guess=guess, guess_str=guess_str)

    return render_template('Guessing game 3.html', invitation=invitation_str, mtd='GET')


if __name__ == '__main__':
    app.run(debug=True)
