from app.app import creat_app

app = creat_app()

@app.route('/v1/user/get')
def get_user():
    return 'I am tanliang'

if __name__ == '__main__':
    app.run(debug=True,port=8003)