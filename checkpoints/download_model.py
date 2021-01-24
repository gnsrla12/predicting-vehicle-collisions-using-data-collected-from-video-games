import requests, os

def download_file_from_google_drive(id, destination):
    URL = "https://docs.google.com/uc?export=download"

    session = requests.Session()

    response = session.get(URL, params = { 'id' : id }, stream = True)
    token = get_confirm_token(response)

    if token:
        params = { 'id' : id, 'confirm' : token }
        response = session.get(URL, params = params, stream = True)

    save_response_content(response, destination)    

def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value

    return None

def save_response_content(response, destination):
    CHUNK_SIZE = 32768

    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)

if __name__ == "__main__":
    print("downloading pretrained model...")
    file_id = str("1ZNJSAN-96CVUakwtd1YMW70t2YXSVIdn")
    destination = str("./checkpoints/gtaCrash.1.0.t-1.8.zip")
    download_file_from_google_drive(file_id, destination)
    print("download completed!")

    print("unzipping pretrained model...")
    os.system("unzip ./checkpoints/gtaCrash.1.0.t-1.8.zip -d ./checkpoints")
    print("unzipping completed!")

    os.system("rm ./checkpoints/gtaCrash.1.0.t-1.8.zip")
    print("zip file removed")


