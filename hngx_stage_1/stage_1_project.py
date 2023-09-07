from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/get_info', method=['GET'])

def get_info():

    # Get the query parameters from the request

    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    # Check if both parameters are provided

    if not slack_name or not track:

        return jsonify({'error': 'Both slack_name and track are required'})

    # Perform some processing based on the parameters

    result = {
            "slack_name": "ajiboye_habiibullah",
            "current_day": "Thursday",
            "utc_time": "2023-09-07T08:34:57Z",
            "track" : "backend",
            "github_file_url":"",
            "github_repo_url":"",
            "status_code": 200
            }
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
