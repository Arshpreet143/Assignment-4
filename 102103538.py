{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "e10ec9ed",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Downloaded: Log Kehte Hai Main Sharaabi Hoon | Sharaabi | Amitabh Bachchan, Jaya Prada | Kishore Kumar\n",
      "MoviePy - Writing audio in C:\\Users\\Yash Pratap\\Log Kehte Hai Main Sharaabi Hoon  Sharaabi  Amitabh Bachchan Jaya Prada  Kishore Kumar.mp3\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "                                                                                                                       \r"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "MoviePy - Done.\n",
      "Converted to MP3: C:\\Users\\Yash Pratap\\Log Kehte Hai Main Sharaabi Hoon  Sharaabi  Amitabh Bachchan Jaya Prada  Kishore Kumar.mp3\n",
      "Error downloading/converting https://www.youtube.com/watch?v=S49wqVih7c8: [WinError 2] The system cannot find the file specified\n",
      "Downloaded: O Mere Dil Ke Chain - Jhankar Beats\n",
      "MoviePy - Writing audio in C:\\Users\\Yash Pratap\\O Mere Dil Ke Chain - Jhankar Beats.mp3\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "                                                                                                                       \r"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "MoviePy - Done.\n",
      "Converted to MP3: C:\\Users\\Yash Pratap\\O Mere Dil Ke Chain - Jhankar Beats.mp3\n",
      "Error downloading/converting https://www.youtube.com/watch?v=5eyflIV8pzM: [WinError 2] The system cannot find the file specified\n",
      "Downloaded: कौन दिसा में लेके चला | Jaspal Singh | Hemlata | Nadiya Ke Paar | Sachin | Sadhana Singh\n",
      "MoviePy - Writing audio in C:\\Users\\Yash Pratap\\कौन दिसा में लेके चला  Jaspal Singh  Hemlata  Nadiya Ke Paar  Sachin  Sadhana Singh.mp3\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "                                                                                                                       \r"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "MoviePy - Done.\n",
      "Converted to MP3: C:\\Users\\Yash Pratap\\कौन दिसा में लेके चला  Jaspal Singh  Hemlata  Nadiya Ke Paar  Sachin  Sadhana Singh.mp3\n",
      "Error downloading/converting https://www.youtube.com/watch?v=hjxl2czTzdk&pp=ygUNa2lzaG9yZSBrdW1hcg%3D%3D: [WinError 2] The system cannot find the file specified\n"
     ]
    }
   ],
   "source": [
    "from pytube import YouTube\n",
    "from moviepy.editor import VideoFileClip\n",
    "from pydub import AudioSegment\n",
    "\n",
    "video_urls = [\n",
    "    \"https://www.youtube.com/watch?v=S49wqVih7c8\",\n",
    "    # Add more video URLs as needed\n",
    "]\n",
    "\n",
    "for url in video_urls:\n",
    "    try:\n",
    "        yt = YouTube(url)\n",
    "        \n",
    "        stream = yt.streams.get_highest_resolution()\n",
    "        video_path = stream.download()\n",
    "        \n",
    "        print(f\"Downloaded: {yt.title}\")\n",
    "        \n",
    "        mp3_path = video_path[:-4] + \".mp3\" \n",
    "        video = VideoFileClip(video_path)\n",
    "        video.audio.write_audiofile(mp3_path)\n",
    "        \n",
    "        print(f\"Converted to MP3: {mp3_path}\")\n",
    "        \n",
    "        # Load the MP3 audio file\n",
    "        audio = AudioSegment.from_file(mp3_path)\n",
    "        \n",
    "        # Define the start and end time in milliseconds for the trim\n",
    "        start_time = 10000  # 10 seconds * 1000 (to convert to milliseconds)\n",
    "        end_time = len(audio)  # End time is the length of the audio\n",
    "        \n",
    "        # Trim the audio\n",
    "        trimmed_audio = audio[start_time:end_time]\n",
    "        \n",
    "        # Export the trimmed audio to the same file\n",
    "        trimmed_audio.export(mp3_path, format=\"mp3\")\n",
    "        \n",
    "        print(\"Trimmed audio saved successfully\")\n",
    "        \n",
    "    except Exception as e:\n",
    "        print(f\"Error downloading/converting {url}: {e}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9ec2d69d",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
