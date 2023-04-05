from flask import Flask, make_response, jsonify, request
import dataset

app = Flask(__name__)
db = dataset.connect('sqlite:///restAPI.db')

books = {}

table = db['restAPI']

def fetch_db(book_id):
    return table.find_one(book_id=book_id)

def fetch_db_all():
    books = []

    for book in table:
        books.append(book)

    return books 


@app.route('/root/populate')
def populate():
    table.insert(
        {
            "book_id": "1",
            "name": "A Game of Thrones",
            "author": "George R. R. Martin"
        }
    )
    
    table.insert(
        {
            "book_id": "2",
            "name": "Lord of the Rings",
            "author": "J. R. R. Tolkien"
        }
    )

    table.insert(
        {
            "book_id": "3",
            "name": "VRaptor Desenvolvimento Ágil para Web com Java",
            "author": "Casa do código"
        }
    )
    
    return make_response(jsonify(fetch_db_all()))


@app.route('/books', methods=['GET', 'POST'])
def index():
    if (request.method == 'GET'):
        return make_response(jsonify(fetch_db_all()), 200)
    elif (request.method == 'POST'):
        content = request.json
        book_id = content['book_id']
        table.insert(content)
        return make_response(jsonify(fetch_db(book_id)), 201)


@app.route('/books/<book_id>', methods=['GET', 'PUT', 'DELETE'])
def search(book_id):
    if (request.method == 'GET'):
        book_obj = fetch_db(book_id)

        if book_obj:
            return make_response(jsonify(book_obj), 200)
        else:
            return make_response(jsonify({}), 404)
        
    elif (request.method == 'PUT'):
        content = request.json
        table.update(content, ['book_id'])

        book_obj = fetch_db(book_id)
        return make_response(jsonify(book_obj), 200)
    
    elif (request.method == 'DELETE'):
        table.delete(book_id=book_id)

        return make_response(jsonify({}), 204)


if __name__ == '__main__':
    app.run(debug=True)