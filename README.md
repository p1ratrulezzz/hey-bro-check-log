# hey-bro-check-log

[![Build Status](https://travis-ci.org/ligh7s/hey-bro-check-log.svg?branch=master)](https://travis-ci.org/ligh7s/hey-bro-check-log)

A python tool which analyzes and verifies good ripping practices and potential inaccuracies
in CD ripping logs for EAC/XLD software.

## Support

- Supports checking EAC and XLD logs.
- Matches deductions on Redacted (minus stupid aggregate ones)
- Supports combined EAC logs
- Detects other irregularities and special occurrences in the rip
  - Data tracks
  - Irregular AR results
  - Hidden tracks and extraction
- Foreign language support (temperamental, as it's based on the most recent translation files).
- Translate logs from foreign languages (Russian, Slovak and etc) to English with fixed checksum.

## Installation and usage

### Required Python3

#### Ubuntu
```bash
apt install python3
```

#### Windows

[Install from here](https://www.python.org/downloads/windows/)

## Install globally
```bash
git clone -b '1.4.0' https://github.com/p1ratrulezzz/hey-bro-check-log.git
cd hey-bro-check-log
sudo python3 setup.py install
```

## OR Use without installation
```bash
pip install chardet=='3.*,>=3.0.4' eac_logchecker
```

or 

```bash
pip3 install chardet=='3.*,>=3.0.4' eac_logchecker
```

then

```bash
cd hey-bro-check-log
python3 -m heybrochecklog -h
python3 -m heybrochecklog -t yourlogfile --pure-translate --fix-checksum
```

## Running CLI

```
usage: heybrochecklog [-h] [-t] [-m] [-s] log

Tool to analyze, translate, and score a CD Rip Log.

positional arguments:
  log               log file to check.

optional arguments:
  -h, --help            show this help message and exit
  -t, --translate       translate a foreign log to English
  -m, --markup          print the marked up version of the log after analyzing
  -s, --score-only      Only print the score of the log.
  -c, --check-checksum  Check the checksum
  -z, --no-sub-zero     Display 0 score if the score is lower than zero
  -p, --pure-translate  Do not include translation header info
  -f, --fix-checksum    Only for -t (--translate). Fix checksum for the new
                        log (works only for EAC)

```
