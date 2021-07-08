import uvicorn

if __name__ == '__main__':
    port = 8000
    uvicorn.run("application:app", host="0.0.0.0", port=port,
                reload=True, debug=True)
