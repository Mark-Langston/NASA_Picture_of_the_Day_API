<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NASA APOD Fetcher</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            background-color: #f4f4f4;
            margin: 0;
            padding: 0;
        }
        .container {
            max-width: 800px;
            margin: 30px auto;
            background: #fff;
            padding: 20px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h1 {
            color: #333;
            text-align: center;
        }
        pre {
            background: #333;
            color: #fff;
            padding: 10px;
            border-radius: 5px;
            overflow: auto;
        }
        .code {
            background: #272822;
            color: #f8f8f2;
            padding: 20px;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>NASA APOD Fetcher</h1>
        <p>This script fetches the Astronomy Picture of the Day (APOD) from NASA's API and displays it in your web browser.</p>
        <h2>Code</h2>
        <pre class="code">
import urllib.request
import json
import webbrowser

## Define APID
apodurl = 'https://api.nasa.gov/planetary/apod?'
mykey = 'api_key=DEMO_KEY' ## replace DEMO_KEY with your nasa api key

## Call the webservice
apodurlobj = urllib.request.urlopen(apodurl + mykey)

## read the file-like object
apodread = apodurlobj.read()

## decode json to python data structure
decodeapod = json.loads(apodread.decode('utf-8'))

## display our pythonic data
print("\n\nConverted python data")
print(decodeapod)

## use browser to open the https url
input('\nPress Enter to open NASA Picture of the Day in Browser')
webbrowser.open(decodeapod['url'])
        </pre>
        <h2>Usage</h2>
        <p>To use this script, follow these steps:</p>
        <ol>
            <li>Obtain a NASA API key from <a href="https://api.nasa.gov/">NASA API Portal</a>.</li>
            <li>Replace <code>DEMO_KEY</code> in the script with your own NASA API key.</li>
            <li>Run the script using Python 3.</li>
            <li>Press Enter when prompted to open the Astronomy Picture of the Day in your web browser.</li>
        </ol>
        <h2>Output</h2>
        <p>When you run the script, it will display the JSON response from the NASA API in your terminal and then open the picture in your default web browser.</p>
    </div>
</body>
</html>
