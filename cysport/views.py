from flask import current_app as app
from flask import render_template

@app.route('/')
def index():

    products = []
    for i in range(1,4):
        products.append({
          'name': 'TUTU Product %s' % i,
          'description': 'shooboo shooboo',
          'size': 'L',
          'width': '%scm' % (100+i),
          'pic': 'http://placehold.it/600x300&text=Product%s' % i,
        })

    args = {
        'products': products
    }

    return render_template('index.html', **args)

@app.route('/a-line')
@app.route('/b-line')
@app.route('/c-line')
def a_line():

    products = []
    for i in range(1,9):
        products.append({
          'name': 'TUTU Product %s' % i,
          'description': 'shooboo shooboo',
          'size': 'L',
          'width': '%scm' % (100+i),
          'pic': 'http://placehold.it/600x300&text=Product%s' % i,
        })


    args = {
        'id': 'a-line',
        'page_header': 'A-Line',
        'products': products,
    }

    return render_template('product-line.html', **args)
