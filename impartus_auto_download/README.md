# Please ensure you have done the setup as listed below before running the auto download script

1. Ensure you have [Python 3.7](https://www.python.org/downloads/) or higher installed, and available in your system `PATH`. To check, run `python --version` from command line/terminal.
2. Install `ffmpeg` from [here](http://ffmpeg.org/download.html). Ensure it is in your PATH variable. To check, run `ffmpeg -version` from command line/terminal.
3. Install [poetry](https://github.com/sdispater/poetry) using `pip install --user poetry`. Restart your PC.
4. Clone this repo if you know git, or click [`Download as ZIP`](https://github.com/iamkroot/ilc-scraper/archive/master.zip) and extract it to some location.
5. Open terminal and cd to download/clone directory.
6. Run `poetry install --no-dev -E gui` for the default installation. (If you don't want the GUI, which takes up a lot of extra space, omit the `-E gui` from the command.)

For more details, please check out the official repository - [`ilc scraper`](https://github.com/iamkroot/ilc-scraper)
