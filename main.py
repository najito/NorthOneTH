import helper
from flask import Flask, request, Response
import json

app = Flask(__name__)

@app.route('/item/new', methods=['POST'])
def add_item():
  req_body = request.get_json()
  title = req_body['title']
  description = req_body['description']
  date = req_body['date']

  res_data = helper.add_to_list(title, description, date)

  # if helper function is unable to write to DB
  if res_data is None:
        response = Response("{'error': 'Item not added - " + title + "'}", status=400 , mimetype='application/json')
        return response

  response = Response(json.dumps(res_data), mimetype='application/json')

  return response

@app.route('/item/all')
def get_all_items():
  res_data = helper.get_all_items()

  response = Response(json.dumps(res_data), mimetype='application/json')
  return response

@app.route('/item/status', methods=['GET'])
def get_item():
    item_title = request.args.get('title')

    item = helper.get_item(item_title)

    # Return 404 if item not found
    if item is None:
        response = Response("{'error': 'Item Not Found - %s'}"  % item_title, status=404 , mimetype='application/json')
        return response

    res_data = item

    response = Response(json.dumps(res_data), status=200, mimetype='application/json')
    return response

@app.route('/item/update', methods=['PUT'])
def update_status():
    req_data = request.get_json()
    title = req_data['title']
    status = req_data['status']

    # Update item in the list
    res_data = helper.update_status(title, status)

    # if helper function is unable to write to DB
    if res_data is None:
        response = Response("{'error': 'Error updating item - '" + title + ", " + status   +  "}", status=400 , mimetype='application/json')
        return response

    response = Response(json.dumps(res_data), mimetype='application/json')

    return response

@app.route('/item/remove', methods=['DELETE'])
def delete_item():
    req_data = request.get_json()
    title = req_data['title']

    res_data = helper.delete_item(title)

    # Return error if the item could not be deleted
    if res_data is None:
        response = Response("{'error': 'Error deleting item - '" + title +  "}", status=400 , mimetype='application/json')
        return response

    # Return response
    response = Response(json.dumps(res_data), mimetype='application/json')

    return response

@app.route('/item/findstatus')
def find_by_status():
    status = request.args.get('status')
    
    item = helper.find_by_status(status)

    # Return 404 if item not found
    if item is None:
        response = Response("{'error': 'Status type Not Found - %s'}"  % status, status=404 , mimetype='application/json')
        return response

    res_data = item

    response = Response(json.dumps(res_data), status=200, mimetype='application/json')
    return response