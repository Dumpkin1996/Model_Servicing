# Model_Servicing
Implementation of chains of ML Models linked with RPC with possible real-life applications.

Current Stage: Only 2 Models, one audio-transcriber and one sentimental-analyzer. We used a simple server-client pattern to link them.

The audio-transcriber runs on the client side, we use CMU-pcoketsphnix. Installation guide on Mac OS can be found [here](https://github.com/watsonbox/homebrew-cmu-sphinx).

The sentimental-analyzer runs on the server side, we trained our own models. It will output a 0/1 value based on the positivenss/negativeness of the unput text.

As an example, we have included a wav file of someone commenting the movie "Wandering Earth" on the client folder. It will first be transcribed to text (and saved in txt format in the client folder) and then evaluated by the server to output 1.
