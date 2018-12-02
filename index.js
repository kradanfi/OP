const https = require('https');
const AWS = require('aws-sdk');
var body
exports.handler = async (event) = {
    
    const post_data = JSON.stringify({
        replyToken event.events[0].replyToken,
        messages [{
            type 'text',
            text JSON.stringify(event)
        }]
    })
    
    
    await makeRequest(post_data);

    return event.events[0].message;
};


function makeRequest(post_data) {

    const options = {
        host 'api.line.me',
        path 'v2botmessagereply',
        method 'POST',
        headers {
            'Content-Type' 'applicationjson',
            'Content-Length' Buffer.byteLength(post_data),
            'Authorization' 'Bearer {rbhLGrnGHCxPK8NLm0s0B1aTsWGridxxhjFdgoQwrW1EnF1l8b5Jz462P9O+7OJPT9SwDrTyYs4KdMzISJoXYsToY7MKKce6YhcNo9mNbstv6UpWUrJ0I4cki6trAIW9XFlGnt1Ssh1XQKFWKQdB04t891Ow1cDnyilFU=}'
        }
    }

    return new Promise((resolve, reject) = {
        const request = https.request(options, (res) = {
            res.on('data', (data) = console.log(data));
            res.on('end', () = {
                resolve();
            })
        })
        request.on('error', (error) = {
            console.log(error)
            reject(error);
        });
        request.write(post_data);
        request.end();
    })
}

