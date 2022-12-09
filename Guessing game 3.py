from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/gg3', methods=['GET', 'POST'])
def main():
    if request.method == 'GET':
        minimum = 0
        maximum = 1000
        attempts = 10
        invitation_str = f'Computer: Think of a number between {minimum} and {maximum}, ' \
                         f'and I will try to guess it in {attempts} tries!'
        return render_template('Guessing game 3.html', invitation=invitation_str, mtd='GET')

    elif request.method == 'POST':
        attempts = 10
        attempt = int(request.form.get('attempt', 1))
        min = int(request.form.get('minimum', 0))
        max = int(request.form.get('maximum', 1000))
        guess = int((max - min) / 2) + min

        user_info = request.form.get("info")
        if user_info == 'correct':
            return 'Computer: Yeah! I am always the best!'
        elif user_info == 'too small':
            min = guess
            attempt += 1
        elif user_info == 'too big':
            max = guess
            attempt += 1

        if attempt > attempts:
            return 'Computer: Noooo! I ran out of tries! You must have been cheating!'

        guess = int((max - min) / 2) + min
        guess_str = f'Computer: My guess number {attempt}, is "{guess}"'

        return render_template('Guessing game 3.html', mtd='POST', minimum=min, maximum=max,
                               attempt=attempt, guess_str=guess_str)


if __name__ == '__main__':
    app.run(debug=True)
