# Model_Servicing
Implementation of chains of ML Models linked with RPC with possible real-life applications.

### Current Stage
Only 2 Models, one audio-transcriber and one sentimental-analyzer. We used a simple server-client pattern to link them.

The audio-transcriber runs on the client side, we use CMU-pcoketsphnix. Installation guide on Mac OS can be found [here](https://github.com/watsonbox/homebrew-cmu-sphinx).

The sentimental-analyzer runs on the server side, we trained our own models. It will output a 0/1 value based on the positivenss/negativeness of the unput text.

### File Structure
    .
    ├── server                   
        ├──  models1                   # tranied parameters of the sentimental analyzer
        ├──  wordsList.npy             # supporting file for the analyzer model
        ├──  wordVectors.npy           # supporting file for the analyzer model
        ├──  server.py                 # code for server (sentimental analyzer)
    ├── client                   
        ├──  client                    # code for client (Require installation of cmu-pocket-sphnix)
        ├──  wandering_earth_1.wav     # test audio input (someone commenting on a movie)
        ├──  wandering_earth_1.txt     # saved output of the transcriber of the test input
    ├── thoughts                  # some thoughts about the whole picture
    └── README.md
