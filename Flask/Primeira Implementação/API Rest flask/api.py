from flask import Flask, make_response, jsonify, request
app = Flask(__name__)

books = {
    '1': {
        "id": "1",
        "name": "A Game of Thrones",
        "author": "George R. R. Martin"
    },
    '2': {
        "id": "2",
        "name": "Lord of the Rings",
        "author": "J. R. R. Tolkien"
    }
}

id = 2

@app.route('/books', methods=['GET', 'POST'])
def index():
    if (request.method == 'GET'):
        return make_response(jsonify(books))
    elif (request.method == 'POST'):

        content = request.json
        book_id = content['id']
        books[book_id] = content

        book_obj = books.get(book_id, {})
        return make_response(jsonify(book_obj), 201)


@app.route('/books/<book_id>', methods=['GET', 'PUT', 'DELETE'])
def search(book_id):
    if (request.method == 'GET'):
        book_obj = books.get(book_id, {})

        if book_obj:
            return make_response(jsonify(book_obj), 200)
        else:
            return make_response(jsonify({}), 404)
    elif (request.method == 'PUT'):
        content = request.json
        books[book_id] = content
        book_obj = books.get(book_id, {})

        return make_response(jsonify(book_obj), 200)
    elif (request.method == 'DELETE'):
        if (book_id in books):
            del books[book_id]

        return make_response(jsonify({}), 204)


if __name__ == '__main__':
    app.run(debug=True)