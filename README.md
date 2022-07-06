# Gym Reservation

![](https://img.shields.io/badge/Activity-Reserve-yellowgreen)

Gym auto reservation script using requests and OCR.

## Requirements

```text
requests
PIL
ddddocr
re
```

## Environment

`Windows` using `schtasks`.

## Configuration

Configure parameters in `config.py`. `gym-id` and `item-id` can be fetched on [50.tsinghua](https://50.tsinghua.edu.cn/).

Set start time in `cmd.bat`, format `YYYY/MM/DD`.

## TODO

* Online payment
* Multi-thread
