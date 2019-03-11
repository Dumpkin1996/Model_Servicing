# Model_Servicing
Implementation of chains of ML Models linked with RPC with possible real-life applications.

Current Stage: Only 2 Models, one audio-transcriber and one sentimental-analyzer. We used a simple server-client pattern to link them.

For audio-transcriber, we use CMU-pcoketsphnix. Installation guide on Mac OS can be found [here](https://github.com/watsonbox/homebrew-cmu-sphinx).

For sentimental-analyzer, we trained our own models. It will output a 0/1 value based on the positivenss/negativeness of the unput text.
