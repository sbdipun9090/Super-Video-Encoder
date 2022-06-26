#    This file is part of the Compressor distribution.
#    Copyright (c) 2021 Danish_00
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
# License can be found in <
# https://github.com/1Danish-00/CompressorQueue/blob/main/License> .

from decouple import config

try:
    APP_ID = config("APP_ID", cast=int)
    API_HASH = config("API_HASH")
    BOT_TOKEN = config("BOT_TOKEN")
    DEV = 1322549723
    OWNER = config("OWNER")
    FFMPEG = config(
        "FFMPEG",
        default='ffmpeg i "{}" -hide_banner -c:v libx265 -vf scale=1280:-2 -x265-params log-level=error:limit-sao:psy-rd=1.5:psy-rdoq=2:aq-mode=3:qcomp=0.75:ref=6:deblock=-1,-1 -pix_fmt yuv420p10 -metadata title="t.me/kingsb007" -preset veryfast -crf 25 -r 23.976 -map 0:v -c:a aac -b:a 48k -cutoff 20000 -vbr on -map 0:a -c:s copy -map 0:s?"{}" -y ,
    )
    THUMB = config("THUMBNAIL")
except Exception as e:
    LOGS.info("Environment vars Missing")
    LOGS.info("something went wrong")
    LOGS.info(str(e))
    exit(1)
