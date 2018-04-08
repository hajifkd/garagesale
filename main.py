import run

app = run.app

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    run.init_slack_timer()
    app.run()
