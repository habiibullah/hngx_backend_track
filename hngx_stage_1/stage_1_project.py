from flask import Flask, request, jsonify
from datetime import datetime, timedelta

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

     # Get the current UTC time accurate within a +/-2 minute window
    current_utc_time = (datetime.utcnow() + timedelta(minutes=2)).strftime('%Y-%m-%dT%H:%M:%SZ')

    # Get the current day of the week in full
    current_day = datetime.utcnow().strftime('%A')


    # Perform some processing based on the parameters

    result = {
            "slack_name": slack_name,
            "current_day": current_day,
            "utc_time": current_utc_time,
            "track" : track,
            "github_file_url":"https://github.com/habiibullah/hngx_backend_track/blob/main/hngx_stage_1/stage_1_project.py",
            "github_repo_url":"https://github.com/habiibullah/hngx_backend_track",
            "status_code": 200
            }
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
