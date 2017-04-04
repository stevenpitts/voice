import pyaudio
makuServerIP = '10.200.41.37'
makuChunk = 1024
makuFormat = pyaudio.paInt16
makuChannels = 2
makuRate = 44100
makuRecordSeconds = 3
makuOutputFilename = "sentVoice.wav"
makuInputFilename = "receivedVoice.wav"
makuClientInputFilename = "clientSecondFile.wav"
makuPort = 12345
makuMaxClients = 5
makuRecVal = 1024
