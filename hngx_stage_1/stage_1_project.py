from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/get_info', methods=['GET'])

def get_info():

    slack_name = 'Ajiboye Habiibullah'
    track = 'Backend'

    # Get the query parameters from the request

    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    # Check if both parameters are provided

    if not slack_name or not track:

        return jsonify({'error': 'Both slack_name and track are required'})

    # Perform some processing based on the parameters

    result = {
            "slack_name": slack_name,
            "current_day": "Thursday",
            "utc_time": "2023-09-07T08:34:57Z",
            "track" : track,
            "github_file_url":"https://github.com/habiibullah/hngx_backend_track/blob/main/hngx_stage_1/stage_1_project.py",
            "github_repo_url":"https://github.com/habiibullah/hngx_backend_track",
            "status_code": 200
            }
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
