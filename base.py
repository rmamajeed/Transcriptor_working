poetry install --no-root

#==============get path and activate the location manually, not needed now===========
poetry env info --path

\Scripts\activate

#==============activate the venv environment in the current terminal=====================
poetry env use python
poetry --directory Trip_Planner_from_scratch env use python
poetry run python main.py #this helps running the application with the env and dependecies

#==============deactivate & remove the venv environment=====================
poetry env remove --all
poetry env remove recruitment-assistant-bq3u0rpZ-py3.11

#=======================clear the poetry cache
poetry cache clear . --all

#===============run the initial setup========================================================
poetry lock
poetry install

python Run_First.py

#============
poetry --directory Trip_Planner_from_scratch env remove --all
poetry --directory Trip_Planner_from_scratch lock
poetry --directory Trip_Planner_from_scratch install
#==================

python -m pip install pytube whisper

python -m pip --version


https://www.youtube.com/watch?v=iK0Gwk56g_M&list=WL&index=55&t=2s
================================
Remove-Item -Path "venv" -Recurse -Force
python -m venv venv
venv\Scripts\activate.bat

=================
:: Upgrade pip first
python -m pip install --upgrade pip

:: Install core packages with specific versions
pip install --no-cache-dir torch==1.10.0 torchaudio==0.10.0
pip install --no-cache-dir pyannote.audio==0.0.1

:: Install remaining requirements
pip install -r requirements.txt

:: Set environment variables
setx HF_HUB_DISABLE_SYMLINKS 1
set HF_HUB_DISABLE_SYMLINKS=1
setx PYTHONPATH "%CD%"
set PYTHONPATH=%CD%


# Check if FFmpeg is installed
ffmpeg -version
# If not installed:
# Ubuntu: sudo apt-get install ffmpeg
# Mac: brew install ffmpeg
# Windows: Download from ffmpeg.org



pip install google-cloud-genai

#   Remove-Item -Path "venv" -Recurse -Force
#   python -m venv venv
#   py -3.11 -m venv venv
#   C:\Users\ASD\AppData\Local\Programs\Python\Python311\python.exe -m venv venv

#   venv\Scripts\activate.bat
#   pip install -r requirements.txt

#   rm -rf venv
#   python3 -m venv venv
#   source venv/bin/activate
#   sudo apt install python3.11-venv

python -m uvicorn main:app --reload

python3 audio_process_and_transcribe.py Audio_Files/

python3 run_full_audio_pipeline.py

https://www.youtube.com/playlist?list=PLA67COBNthEJbJCXwyjR9uHS1SJEOaRa5

source venv/bin/activate 

python audio_process_and_transcribe.py Audio_Files/ --metadata-level basic


############
crontab -e
# Daily Transcriptinator Run (Added 2026-02-07)
00 12 * * * /home/asd/Python/Transcriptinator_working/run_daily.sh

tail -f /home/asd/Python/Transcriptinator_working/daily_run.log
##################
crontab -e
# Daily Transcriptinator Run (Added 2026-02-07)
# 45 11 * * * /home/asd/Python/Transcriptinator_working/run_daily.sh

Save and Exit:
In nano: Press Ctrl+O, Enter, then Ctrl+X.
In 
vi
: Press Esc, type :wq, and press Enter.


crontab -l