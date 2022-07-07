# Gym Reservation

![](https://img.shields.io/badge/Activity-Reserve-yellowgreen) ![](https://img.shields.io/badge/Auto-Script-orange)

Gym auto reservation script using requests and OCR.

## Requirements

```text
requests
PIL
ddddocr
re
apscheduler
```

## Environment

`Python 3.9.7`.

## Configuration

Configure parameters in `config.py`. `gym-id` and `item-id` can be fetched on [50.tsinghua](https://50.tsinghua.edu.cn/).

Set start time in `main.py`, using `apscheduler` for job manager. After runing, do not enter anything to console until reservation result comes out.

## TODO

* Online payment
* Multi-thread
