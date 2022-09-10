from flask import Flask

app = Flask('main')
app.app_context()

@app.route('/videos/<vid_name>')
def render_videos(vid_name):
    return f'Here will be a video with {vid_name}'