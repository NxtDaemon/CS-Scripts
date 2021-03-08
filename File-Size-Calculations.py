#File-Size-Calculations.py

def estimateTextFileSize(BitsPerChar,NumberOfChar):
  '''Function to estimate filesize for a text file'''
  if BitsPerChar == 7:
    Lang = "ASCII"
  elif BitsPerChar == 8:
    Lang = "EASCII"
  elif BitsPerChar == 16:
    Lang = "UTF-16"
  elif BitsPerChar == 32:
    Lang = "UTF-32"
  else:
    print(f"Error in Assigned Variable BitsPerChar , Value set as '{BitsPerChar}'")
    quit()
  
  TextFileSize = BitsPerChar * NumberOfChar
  return(ManageSize(TextFileSize))

def estimatePictureFileSize(ImgHeight,ImgWidth,ImgColorDepth):
  ''' Function to estimate filesize for a bitmap picture file '''
  PictureFileSize = ImgColorDepth * ImgHeight * ImgWidth
  return(ManageSize(PictureFileSize))

def estimateSoundFileSize(SampleRate,BitDepth,Duration,Channels):
  '''Function to estimate filesize for an audio file | Duration must be given in Seconds'''   
  SoundFileSize = SampleRate * Duration * BitDepth * Channels
  return(ManageSize(SoundFileSize))
  
def ManageSize(Size):
  '''Function to Manage filesize'''
  if Size > 8:
    Size = Size / 8
    type = "B"
    if Size > 1024:
      Size = Size / 1024
      Type = "KiB" 
      if Size > 1024:
        Size = Size / 1024
        Type = "MiB"
  
  return(f"{Size} {Type}")
  
print(estimateTextFileSize(8,3000))
print(estimateTextFileSize(16,12000))
print(estimatePictureFileSize(480,640,8))
print(estimatePictureFileSize(1080,1920,24))
print(estimateSoundFileSize(8000,16,30,1))
print(estimateSoundFileSize(44100,16,210,2))