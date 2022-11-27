{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "78959e89"
      },
      "source": [
        "### Importing important and useful libraries"
      ],
      "id": "78959e89"
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "background_save": true,
          "base_uri": "https://localhost:8080/"
        },
        "id": "f094b148",
        "outputId": "12d30aab-0511-44e3-d5eb-824aad8bf98e"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/\n",
            "Collecting selenium\n",
            "  Downloading selenium-4.6.0-py3-none-any.whl (5.2 MB)\n",
            "\u001b[K     |████████████████████████████████| 5.2 MB 4.7 MB/s \n",
            "\u001b[?25hRequirement already satisfied: certifi>=2021.10.8 in /usr/local/lib/python3.7/dist-packages (from selenium) (2022.9.24)\n",
            "Collecting trio~=0.17\n",
            "  Downloading trio-0.22.0-py3-none-any.whl (384 kB)\n",
            "\u001b[K     |████████████████████████████████| 384 kB 49.6 MB/s \n",
            "\u001b[?25hCollecting trio-websocket~=0.9\n",
            "  Downloading trio_websocket-0.9.2-py3-none-any.whl (16 kB)\n",
            "Collecting urllib3[socks]~=1.26\n",
            "  Downloading urllib3-1.26.13-py2.py3-none-any.whl (140 kB)\n",
            "\u001b[K     |████████████████████████████████| 140 kB 63.5 MB/s \n",
            "\u001b[?25hRequirement already satisfied: sortedcontainers in /usr/local/lib/python3.7/dist-packages (from trio~=0.17->selenium) (2.4.0)\n",
            "Collecting async-generator>=1.9\n",
            "  Downloading async_generator-1.10-py3-none-any.whl (18 kB)\n",
            "Collecting exceptiongroup>=1.0.0rc9\n",
            "  Downloading exceptiongroup-1.0.4-py3-none-any.whl (14 kB)\n",
            "Requirement already satisfied: attrs>=19.2.0 in /usr/local/lib/python3.7/dist-packages (from trio~=0.17->selenium) (22.1.0)\n",
            "Collecting sniffio\n",
            "  Downloading sniffio-1.3.0-py3-none-any.whl (10 kB)\n",
            "Requirement already satisfied: idna in /usr/local/lib/python3.7/dist-packages (from trio~=0.17->selenium) (2.10)\n",
            "Collecting outcome\n",
            "  Downloading outcome-1.2.0-py2.py3-none-any.whl (9.7 kB)\n",
            "Collecting wsproto>=0.14\n",
            "  Downloading wsproto-1.2.0-py3-none-any.whl (24 kB)\n",
            "Requirement already satisfied: PySocks!=1.5.7,<2.0,>=1.5.6 in /usr/local/lib/python3.7/dist-packages (from urllib3[socks]~=1.26->selenium) (1.7.1)\n",
            "Collecting h11<1,>=0.9.0\n",
            "  Downloading h11-0.14.0-py3-none-any.whl (58 kB)\n",
            "\u001b[K     |████████████████████████████████| 58 kB 6.0 MB/s \n",
            "\u001b[?25hRequirement already satisfied: typing-extensions in /usr/local/lib/python3.7/dist-packages (from h11<1,>=0.9.0->wsproto>=0.14->trio-websocket~=0.9->selenium) (4.1.1)\n",
            "Installing collected packages: sniffio, outcome, h11, exceptiongroup, async-generator, wsproto, urllib3, trio, trio-websocket, selenium\n",
            "  Attempting uninstall: urllib3\n",
            "    Found existing installation: urllib3 1.24.3\n",
            "    Uninstalling urllib3-1.24.3:\n",
            "      Successfully uninstalled urllib3-1.24.3\n",
            "\u001b[31mERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.\n",
            "requests 2.23.0 requires urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1, but you have urllib3 1.26.13 which is incompatible.\u001b[0m\n",
            "Successfully installed async-generator-1.10 exceptiongroup-1.0.4 h11-0.14.0 outcome-1.2.0 selenium-4.6.0 sniffio-1.3.0 trio-0.22.0 trio-websocket-0.9.2 urllib3-1.26.13 wsproto-1.2.0\n",
            "Get:1 http://security.ubuntu.com/ubuntu bionic-security InRelease [88.7 kB]\n",
            "Get:2 https://cloud.r-project.org/bin/linux/ubuntu bionic-cran40/ InRelease [3,626 B]\n",
            "Ign:3 https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64  InRelease\n",
            "Hit:4 http://ppa.launchpad.net/c2d4u.team/c2d4u4.0+/ubuntu bionic InRelease\n",
            "Get:5 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64  InRelease [1,581 B]\n",
            "Hit:6 http://archive.ubuntu.com/ubuntu bionic InRelease\n",
            "Hit:7 https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64  Release\n",
            "Get:8 http://archive.ubuntu.com/ubuntu bionic-updates InRelease [88.7 kB]\n",
            "Hit:9 http://ppa.launchpad.net/cran/libgit2/ubuntu bionic InRelease\n",
            "Hit:10 http://ppa.launchpad.net/deadsnakes/ppa/ubuntu bionic InRelease\n",
            "Get:11 http://archive.ubuntu.com/ubuntu bionic-backports InRelease [83.3 kB]\n",
            "Get:12 http://security.ubuntu.com/ubuntu bionic-security/main amd64 Packages [3,068 kB]\n",
            "Hit:13 http://ppa.launchpad.net/graphics-drivers/ppa/ubuntu bionic InRelease\n",
            "Get:14 http://security.ubuntu.com/ubuntu bionic-security/universe amd64 Packages [1,563 kB]\n",
            "Get:15 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64  Packages [1,038 kB]\n",
            "Get:17 http://archive.ubuntu.com/ubuntu bionic-updates/universe amd64 Packages [2,338 kB]\n",
            "Get:18 http://archive.ubuntu.com/ubuntu bionic-updates/main amd64 Packages [3,496 kB]\n",
            "Get:19 http://archive.ubuntu.com/ubuntu bionic-updates/restricted amd64 Packages [1,303 kB]\n",
            "Fetched 13.1 MB in 3s (3,794 kB/s)\n",
            "Reading package lists... Done\n",
            "Reading package lists... Done\n",
            "Building dependency tree       \n",
            "Reading state information... Done\n",
            "The following package was automatically installed and is no longer required:\n",
            "  libnvidia-common-460\n",
            "Use 'apt autoremove' to remove it.\n",
            "The following additional packages will be installed:\n",
            "  chromium-browser chromium-browser-l10n chromium-codecs-ffmpeg-extra\n",
            "Suggested packages:\n",
            "  webaccounts-chromium-extension unity-chromium-extension\n",
            "The following NEW packages will be installed:\n",
            "  chromium-browser chromium-browser-l10n chromium-chromedriver\n",
            "  chromium-codecs-ffmpeg-extra\n",
            "0 upgraded, 4 newly installed, 0 to remove and 11 not upgraded.\n",
            "Need to get 95.1 MB of archives.\n",
            "After this operation, 319 MB of additional disk space will be used.\n",
            "Get:1 http://archive.ubuntu.com/ubuntu bionic-updates/universe amd64 chromium-codecs-ffmpeg-extra amd64 107.0.5304.87-0ubuntu11.18.04.1 [1,158 kB]\n",
            "Get:2 http://archive.ubuntu.com/ubuntu bionic-updates/universe amd64 chromium-browser amd64 107.0.5304.87-0ubuntu11.18.04.1 [83.1 MB]\n",
            "Get:3 http://archive.ubuntu.com/ubuntu bionic-updates/universe amd64 chromium-browser-l10n all 107.0.5304.87-0ubuntu11.18.04.1 [5,260 kB]\n",
            "Get:4 http://archive.ubuntu.com/ubuntu bionic-updates/universe amd64 chromium-chromedriver amd64 107.0.5304.87-0ubuntu11.18.04.1 [5,570 kB]\n",
            "Fetched 95.1 MB in 4s (24.1 MB/s)\n",
            "Selecting previously unselected package chromium-codecs-ffmpeg-extra.\n",
            "(Reading database ... 123991 files and directories currently installed.)\n",
            "Preparing to unpack .../chromium-codecs-ffmpeg-extra_107.0.5304.87-0ubuntu11.18.04.1_amd64.deb ...\n",
            "Unpacking chromium-codecs-ffmpeg-extra (107.0.5304.87-0ubuntu11.18.04.1) ...\n",
            "Selecting previously unselected package chromium-browser.\n",
            "Preparing to unpack .../chromium-browser_107.0.5304.87-0ubuntu11.18.04.1_amd64.deb ...\n",
            "Unpacking chromium-browser (107.0.5304.87-0ubuntu11.18.04.1) ...\n",
            "Selecting previously unselected package chromium-browser-l10n.\n",
            "Preparing to unpack .../chromium-browser-l10n_107.0.5304.87-0ubuntu11.18.04.1_all.deb ...\n",
            "Unpacking chromium-browser-l10n (107.0.5304.87-0ubuntu11.18.04.1) ...\n",
            "Selecting previously unselected package chromium-chromedriver.\n",
            "Preparing to unpack .../chromium-chromedriver_107.0.5304.87-0ubuntu11.18.04.1_amd64.deb ...\n",
            "Unpacking chromium-chromedriver (107.0.5304.87-0ubuntu11.18.04.1) ...\n",
            "Setting up chromium-codecs-ffmpeg-extra (107.0.5304.87-0ubuntu11.18.04.1) ...\n",
            "Setting up chromium-browser (107.0.5304.87-0ubuntu11.18.04.1) ...\n",
            "update-alternatives: using /usr/bin/chromium-browser to provide /usr/bin/x-www-browser (x-www-browser) in auto mode\n",
            "update-alternatives: using /usr/bin/chromium-browser to provide /usr/bin/gnome-www-browser (gnome-www-browser) in auto mode\n",
            "Setting up chromium-chromedriver (107.0.5304.87-0ubuntu11.18.04.1) ...\n",
            "Setting up chromium-browser-l10n (107.0.5304.87-0ubuntu11.18.04.1) ...\n",
            "Processing triggers for man-db (2.8.3-2ubuntu0.1) ...\n",
            "Processing triggers for hicolor-icon-theme (0.17-2) ...\n",
            "Processing triggers for mime-support (3.60ubuntu1) ...\n",
            "Processing triggers for libc-bin (2.27-3ubuntu1.6) ...\n"
          ]
        }
      ],
      "source": [
        "import pandas as pd\n",
        "import numpy as np \n",
        "\n",
        "import seaborn as sns\n",
        "import matplotlib.pyplot as plt \n",
        "%matplotlib inline \n",
        "import time  \n",
        "\n",
        "from sklearn.linear_model import LogisticRegression \n",
        "from sklearn.naive_bayes import MultinomialNB \n",
        "from sklearn.model_selection import train_test_split \n",
        "from sklearn.metrics import classification_report \n",
        "from sklearn.metrics import confusion_matrix\n",
        "from nltk.tokenize import RegexpTokenizer  \n",
        "from nltk.stem.snowball import SnowballStemmer \n",
        "from sklearn.feature_extraction.text import CountVectorizer  \n",
        "from sklearn.pipeline import make_pipeline \n",
        "\n",
        "from PIL import Image \n",
        "from bs4 import BeautifulSoup \n",
        "!pip install selenium\n",
        "!apt-get update \n",
        "!apt install chromium-chromedriver\n",
        "from selenium import webdriver\n",
        "import networkx as nx \n",
        "\n",
        "import pickle\n",
        "\n",
        "import warnings \n",
        "warnings.filterwarnings('ignore')"
      ],
      "id": "f094b148"
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "83b079a1"
      },
      "outputs": [],
      "source": [
        "phish_data = pd.read_csv(r'phishing_site_urls.csv')"
      ],
      "id": "83b079a1"
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        },
        "id": "ded2f44a",
        "outputId": "a8a7b4af-26d5-4259-a082-a683134119a0"
      },
      "outputs": [
        {
          "data": {
            "text/html": [
              "\n",
              "  <div id=\"df-30cc91e2-d20e-4192-a85d-1b8067e065e2\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>URL</th>\n",
              "      <th>Label</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>nobell.it/70ffb52d079109dca5664cce6f317373782/...</td>\n",
              "      <td>bad</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>www.dghjdgf.com/paypal.co.uk/cycgi-bin/webscrc...</td>\n",
              "      <td>bad</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>serviciosbys.com/paypal.cgi.bin.get-into.herf....</td>\n",
              "      <td>bad</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>mail.printakid.com/www.online.americanexpress....</td>\n",
              "      <td>bad</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>thewhiskeydregs.com/wp-content/themes/widescre...</td>\n",
              "      <td>bad</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-30cc91e2-d20e-4192-a85d-1b8067e065e2')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-30cc91e2-d20e-4192-a85d-1b8067e065e2 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-30cc91e2-d20e-4192-a85d-1b8067e065e2');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ],
            "text/plain": [
              "                                                 URL Label\n",
              "0  nobell.it/70ffb52d079109dca5664cce6f317373782/...   bad\n",
              "1  www.dghjdgf.com/paypal.co.uk/cycgi-bin/webscrc...   bad\n",
              "2  serviciosbys.com/paypal.cgi.bin.get-into.herf....   bad\n",
              "3  mail.printakid.com/www.online.americanexpress....   bad\n",
              "4  thewhiskeydregs.com/wp-content/themes/widescre...   bad"
            ]
          },
          "execution_count": 5,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "phish_data.head()"
      ],
      "id": "ded2f44a"
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        },
        "id": "dec0a369",
        "outputId": "39888c42-91d4-4a62-8e64-a85e89022cec"
      },
      "outputs": [
        {
          "data": {
            "text/html": [
              "\n",
              "  <div id=\"df-77f46b75-6902-4087-ada3-5110920062fe\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>URL</th>\n",
              "      <th>Label</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>549341</th>\n",
              "      <td>23.227.196.215/</td>\n",
              "      <td>bad</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>549342</th>\n",
              "      <td>apple-checker.org/</td>\n",
              "      <td>bad</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>549343</th>\n",
              "      <td>apple-iclods.org/</td>\n",
              "      <td>bad</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>549344</th>\n",
              "      <td>apple-uptoday.org/</td>\n",
              "      <td>bad</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>549345</th>\n",
              "      <td>apple-search.info</td>\n",
              "      <td>bad</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-77f46b75-6902-4087-ada3-5110920062fe')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-77f46b75-6902-4087-ada3-5110920062fe button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-77f46b75-6902-4087-ada3-5110920062fe');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ],
            "text/plain": [
              "                       URL Label\n",
              "549341     23.227.196.215/   bad\n",
              "549342  apple-checker.org/   bad\n",
              "549343   apple-iclods.org/   bad\n",
              "549344  apple-uptoday.org/   bad\n",
              "549345   apple-search.info   bad"
            ]
          },
          "execution_count": 6,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "phish_data.tail()"
      ],
      "id": "dec0a369"
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "5254e083",
        "outputId": "571ec9ec-0e6b-440a-f0f9-a98f17de312b"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 549346 entries, 0 to 549345\n",
            "Data columns (total 2 columns):\n",
            " #   Column  Non-Null Count   Dtype \n",
            "---  ------  --------------   ----- \n",
            " 0   URL     549346 non-null  object\n",
            " 1   Label   549346 non-null  object\n",
            "dtypes: object(2)\n",
            "memory usage: 8.4+ MB\n"
          ]
        }
      ],
      "source": [
        "phish_data.info()"
      ],
      "id": "5254e083"
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "f3b81b8b",
        "outputId": "e2344a7a-870e-4c6a-d16f-4c021613bbbe"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "URL      0\n",
              "Label    0\n",
              "dtype: int64"
            ]
          },
          "execution_count": 8,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "phish_data.isnull().sum()"
      ],
      "id": "f3b81b8b"
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "f8f246d8"
      },
      "outputs": [],
      "source": [
        "label_counts = pd.DataFrame(phish_data.Label.value_counts())"
      ],
      "id": "f8f246d8"
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 282
        },
        "id": "263fc7ab",
        "outputId": "53ef23fc-3339-4a03-d68a-12dc6d5cc8b9"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "<matplotlib.axes._subplots.AxesSubplot at 0x7f1299708890>"
            ]
          },
          "execution_count": 10,
          "metadata": {},
          "output_type": "execute_result"
        },
        {
          "data": {
            "image/png": "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v8s///M/8/bbb3PlyhXuv/9+KioqMAxDezJMdOUi09Ld3U1rayvHjh3jxz/+MWfPngXg+eef57nnnuPnP/85S5Ysobq6esr67t27+c53vsOxY8dmbS0y9/32t7/lySef5N///d+ZP38+b775Jn/zN3/DW2+9RXNzM6Ojo7z99tuA9mS4KFxkWj744APWrVvHl770JWJiYnj44Yf57LPPGBkZ4aGHHgKgoKCA999/n5GRkRvWh4eHGRkZ4cEHHwRg48aNs7YemdsWLlzIAw88AMCjjz7K6dOn+fWvf01RURF5eXmcOnWKnp4e7ckw0pO/1x4AAAFASURBVG0xEZlzDMP4ws/79+/nrbfeYuHChbz66qtcuXJllrq7PejKRablL/7iL0L3qy9fvsw777zDvHnziIuL4/333wegqamJBx98kNjY2BvW4+LiiI2NDdV//vOfz9p6ZG77n//5Hz788EMAmpubQ1cxCQkJXL58mZaWFgDtyTDSlYtMy/Lly3G5XDz66KMsWLCAJUuWEBsby3e/+93Qg/uUlBReeuklgEnrL730Env27MEwDD08lbD5sz/7M9544w327NnDV7/6VZ544gmGhoZ45JFHuPvuu0lPTw8dqz0ZHvrzLzJtly9fZv78+Xz22Wf89V//NZWVlSxbtmy22xKRm5CuXGTaysvL6enp4cqVKxQUFChYRGRSunIRERHL6YG+iIhYTuEiIiKWU7iIiIjlFC4iImI5hYuIiFjufwH1UT1pPldi7AAAAABJRU5ErkJggg==\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {},
          "output_type": "display_data"
        }
      ],
      "source": [
        "sns.set_style('darkgrid')\n",
        "sns.barplot(label_counts.index,label_counts.Label)"
      ],
      "id": "263fc7ab"
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "eb99a5a7"
      },
      "source": [
        "#### Data Preprocessing "
      ],
      "id": "eb99a5a7"
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "051e9230"
      },
      "outputs": [],
      "source": [
        "tokenizer = RegexpTokenizer(r'[A-Za-z]+')"
      ],
      "id": "051e9230"
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 53
        },
        "id": "12757d00",
        "outputId": "7755cc28-e54a-498b-b30b-e0206f3bb45f"
      },
      "outputs": [
        {
          "data": {
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            },
            "text/plain": [
              "'nobell.it/70ffb52d079109dca5664cce6f317373782/login.SkyPe.com/en/cgi-bin/verification/login/70ffb52d079109dca5664cce6f317373/index.php?cmd=_profile-ach&outdated_page_tmpl=p/gen/failed-to-load&nav=0.5.1&login_access=1322408526'"
            ]
          },
          "execution_count": 12,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "phish_data.URL[0]"
      ],
      "id": "12757d00"
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "c53fa4a1",
        "outputId": "e151c9c1-2e43-41a5-db5a-d159958ced08"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "['nobell',\n",
              " 'it',\n",
              " 'ffb',\n",
              " 'd',\n",
              " 'dca',\n",
              " 'cce',\n",
              " 'f',\n",
              " 'login',\n",
              " 'SkyPe',\n",
              " 'com',\n",
              " 'en',\n",
              " 'cgi',\n",
              " 'bin',\n",
              " 'verification',\n",
              " 'login',\n",
              " 'ffb',\n",
              " 'd',\n",
              " 'dca',\n",
              " 'cce',\n",
              " 'f',\n",
              " 'index',\n",
              " 'php',\n",
              " 'cmd',\n",
              " 'profile',\n",
              " 'ach',\n",
              " 'outdated',\n",
              " 'page',\n",
              " 'tmpl',\n",
              " 'p',\n",
              " 'gen',\n",
              " 'failed',\n",
              " 'to',\n",
              " 'load',\n",
              " 'nav',\n",
              " 'login',\n",
              " 'access']"
            ]
          },
          "execution_count": 13,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "tokenizer.tokenize(phish_data.URL[0])"
      ],
      "id": "c53fa4a1"
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "41b0aaae",
        "outputId": "21094566-ad25-43b6-e318-5e21d0db36d2"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Getting words tokenized ...\n",
            "Time taken 4.019783544999996 sec\n"
          ]
        }
      ],
      "source": [
        "print('Getting words tokenized ...')\n",
        "t0= time.perf_counter()\n",
        "phish_data['text_tokenized'] = phish_data.URL.map(lambda t: tokenizer.tokenize(t)) # doing with all rows\n",
        "t1 = time.perf_counter() - t0\n",
        "print('Time taken',t1 ,'sec')"
      ],
      "id": "41b0aaae"
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        },
        "id": "7bda65a2",
        "outputId": "7ade743f-1782-4a0f-dc7c-a19fad696702"
      },
      "outputs": [
        {
          "data": {
            "text/html": [
              "\n",
              "  <div id=\"df-fa391deb-21ca-47b9-b962-fd5ecc0dd9f2\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>URL</th>\n",
              "      <th>Label</th>\n",
              "      <th>text_tokenized</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>3881</th>\n",
              "      <td>www.cartazi.go.ro/</td>\n",
              "      <td>bad</td>\n",
              "      <td>[www, cartazi, go, ro]</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>518199</th>\n",
              "      <td>onnettomuuskonetta.kioskey.com/q96dmnwesx.php\\n</td>\n",
              "      <td>bad</td>\n",
              "      <td>[onnettomuuskonetta, kioskey, com, q, dmnwesx,...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>362745</th>\n",
              "      <td>insurance.utah.gov/</td>\n",
              "      <td>good</td>\n",
              "      <td>[insurance, utah, gov]</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>490441</th>\n",
              "      <td>enocuae.com/324/cp.php?m=login</td>\n",
              "      <td>bad</td>\n",
              "      <td>[enocuae, com, cp, php, m, login]</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>186678</th>\n",
              "      <td>familytreemaker.genealogy.com/users/v/o/l/Laur...</td>\n",
              "      <td>good</td>\n",
              "      <td>[familytreemaker, genealogy, com, users, v, o,...</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-fa391deb-21ca-47b9-b962-fd5ecc0dd9f2')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-fa391deb-21ca-47b9-b962-fd5ecc0dd9f2 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-fa391deb-21ca-47b9-b962-fd5ecc0dd9f2');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ],
            "text/plain": [
              "                                                      URL Label  \\\n",
              "3881                                   www.cartazi.go.ro/   bad   \n",
              "518199    onnettomuuskonetta.kioskey.com/q96dmnwesx.php\\n   bad   \n",
              "362745                                insurance.utah.gov/  good   \n",
              "490441                     enocuae.com/324/cp.php?m=login   bad   \n",
              "186678  familytreemaker.genealogy.com/users/v/o/l/Laur...  good   \n",
              "\n",
              "                                           text_tokenized  \n",
              "3881                               [www, cartazi, go, ro]  \n",
              "518199  [onnettomuuskonetta, kioskey, com, q, dmnwesx,...  \n",
              "362745                             [insurance, utah, gov]  \n",
              "490441                  [enocuae, com, cp, php, m, login]  \n",
              "186678  [familytreemaker, genealogy, com, users, v, o,...  "
            ]
          },
          "execution_count": 15,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "phish_data.sample(5)"
      ],
      "id": "7bda65a2"
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "61db80a4"
      },
      "outputs": [],
      "source": [
        "stemmer = SnowballStemmer(\"english\")"
      ],
      "id": "61db80a4"
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "6f0e6b67",
        "outputId": "795a77f2-628a-4bf2-d2f0-106c3fe53b19"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Getting words stemmed ...\n",
            "Time taken 49.971030181999936 sec\n"
          ]
        }
      ],
      "source": [
        "print('Getting words stemmed ...')\n",
        "t0= time.perf_counter()\n",
        "phish_data['text_stemmed'] = phish_data['text_tokenized'].map(lambda l: [stemmer.stem(word) for word in l])\n",
        "t1= time.perf_counter() - t0\n",
        "print('Time taken',t1 ,'sec')"
      ],
      "id": "6f0e6b67"
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 320
        },
        "id": "ba9d30fa",
        "outputId": "11b5166e-be53-47c8-f8ce-a88eaec0ee56"
      },
      "outputs": [
        {
          "data": {
            "text/html": [
              "\n",
              "  <div id=\"df-d446fc64-2962-40da-a4ec-6cae8c2f9d6d\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>URL</th>\n",
              "      <th>Label</th>\n",
              "      <th>text_tokenized</th>\n",
              "      <th>text_stemmed</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>174706</th>\n",
              "      <td>en.wikipedia.org/wiki/Football_at_the_1976_Sum...</td>\n",
              "      <td>good</td>\n",
              "      <td>[en, wikipedia, org, wiki, Football, at, the, ...</td>\n",
              "      <td>[en, wikipedia, org, wiki, footbal, at, the, s...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>279996</th>\n",
              "      <td>answers.com/topic/catholic-encyclopedia-1913</td>\n",
              "      <td>good</td>\n",
              "      <td>[answers, com, topic, catholic, encyclopedia]</td>\n",
              "      <td>[answer, com, topic, cathol, encyclopedia]</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>198647</th>\n",
              "      <td>hrvatski-nogometasi.blogspot.com/</td>\n",
              "      <td>good</td>\n",
              "      <td>[hrvatski, nogometasi, blogspot, com]</td>\n",
              "      <td>[hrvatski, nogometasi, blogspot, com]</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>445386</th>\n",
              "      <td>thehockeystore.net/california-golden-seals-hoc...</td>\n",
              "      <td>good</td>\n",
              "      <td>[thehockeystore, net, california, golden, seal...</td>\n",
              "      <td>[thehockeystor, net, california, golden, seal,...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>10780</th>\n",
              "      <td>www.engdocarmo.com/~mpolvora/accounts.departme...</td>\n",
              "      <td>bad</td>\n",
              "      <td>[www, engdocarmo, com, mpolvora, accounts, dep...</td>\n",
              "      <td>[www, engdocarmo, com, mpolvora, account, depa...</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-d446fc64-2962-40da-a4ec-6cae8c2f9d6d')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-d446fc64-2962-40da-a4ec-6cae8c2f9d6d button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-d446fc64-2962-40da-a4ec-6cae8c2f9d6d');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ],
            "text/plain": [
              "                                                      URL Label  \\\n",
              "174706  en.wikipedia.org/wiki/Football_at_the_1976_Sum...  good   \n",
              "279996       answers.com/topic/catholic-encyclopedia-1913  good   \n",
              "198647                  hrvatski-nogometasi.blogspot.com/  good   \n",
              "445386  thehockeystore.net/california-golden-seals-hoc...  good   \n",
              "10780   www.engdocarmo.com/~mpolvora/accounts.departme...   bad   \n",
              "\n",
              "                                           text_tokenized  \\\n",
              "174706  [en, wikipedia, org, wiki, Football, at, the, ...   \n",
              "279996      [answers, com, topic, catholic, encyclopedia]   \n",
              "198647              [hrvatski, nogometasi, blogspot, com]   \n",
              "445386  [thehockeystore, net, california, golden, seal...   \n",
              "10780   [www, engdocarmo, com, mpolvora, accounts, dep...   \n",
              "\n",
              "                                             text_stemmed  \n",
              "174706  [en, wikipedia, org, wiki, footbal, at, the, s...  \n",
              "279996         [answer, com, topic, cathol, encyclopedia]  \n",
              "198647              [hrvatski, nogometasi, blogspot, com]  \n",
              "445386  [thehockeystor, net, california, golden, seal,...  \n",
              "10780   [www, engdocarmo, com, mpolvora, account, depa...  "
            ]
          },
          "execution_count": 18,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "phish_data.sample(5)"
      ],
      "id": "ba9d30fa"
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "c3ce8b95",
        "outputId": "0b01349f-0578-48f6-c429-471bb702deff"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Getting joiningwords ...\n",
            "Time taken 0.2910122450000472 sec\n"
          ]
        }
      ],
      "source": [
        "print('Getting joiningwords ...')\n",
        "t0= time.perf_counter()\n",
        "phish_data['text_sent'] = phish_data['text_stemmed'].map(lambda l: ' '.join(l))\n",
        "t1= time.perf_counter() - t0\n",
        "print('Time taken',t1 ,'sec')"
      ],
      "id": "c3ce8b95"
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 337
        },
        "id": "c776a8d5",
        "outputId": "3f39fc67-1d40-4ad5-c6d6-9b2b6f929892"
      },
      "outputs": [
        {
          "data": {
            "text/html": [
              "\n",
              "  <div id=\"df-9e914b67-cb8c-4bad-9c03-285a5b4f655c\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>URL</th>\n",
              "      <th>Label</th>\n",
              "      <th>text_tokenized</th>\n",
              "      <th>text_stemmed</th>\n",
              "      <th>text_sent</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>78890</th>\n",
              "      <td>news.cnet.com/2100-1013_3-5053623.html</td>\n",
              "      <td>good</td>\n",
              "      <td>[news, cnet, com, html]</td>\n",
              "      <td>[news, cnet, com, html]</td>\n",
              "      <td>news cnet com html</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>165374</th>\n",
              "      <td>digiguide.tv/programme/Plunkett+and+Macleane/F...</td>\n",
              "      <td>good</td>\n",
              "      <td>[digiguide, tv, programme, Plunkett, and, Macl...</td>\n",
              "      <td>[digiguid, tv, programm, plunkett, and, maclea...</td>\n",
              "      <td>digiguid tv programm plunkett and maclean film</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>113657</th>\n",
              "      <td>carloscarreno.cl/carloscarreno.cl/web/admin/va...</td>\n",
              "      <td>bad</td>\n",
              "      <td>[carloscarreno, cl, carloscarreno, cl, web, ad...</td>\n",
              "      <td>[carloscarreno, cl, carloscarreno, cl, web, ad...</td>\n",
              "      <td>carloscarreno cl carloscarreno cl web admin va...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>347162</th>\n",
              "      <td>goodreads.com/list/show/824.Best_Non_fiction_W...</td>\n",
              "      <td>good</td>\n",
              "      <td>[goodreads, com, list, show, Best, Non, fictio...</td>\n",
              "      <td>[goodread, com, list, show, best, non, fiction...</td>\n",
              "      <td>goodread com list show best non fiction war book</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>141874</th>\n",
              "      <td>ameon.wordpress.com/</td>\n",
              "      <td>good</td>\n",
              "      <td>[ameon, wordpress, com]</td>\n",
              "      <td>[ameon, wordpress, com]</td>\n",
              "      <td>ameon wordpress com</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-9e914b67-cb8c-4bad-9c03-285a5b4f655c')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-9e914b67-cb8c-4bad-9c03-285a5b4f655c button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-9e914b67-cb8c-4bad-9c03-285a5b4f655c');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ],
            "text/plain": [
              "                                                      URL Label  \\\n",
              "78890              news.cnet.com/2100-1013_3-5053623.html  good   \n",
              "165374  digiguide.tv/programme/Plunkett+and+Macleane/F...  good   \n",
              "113657  carloscarreno.cl/carloscarreno.cl/web/admin/va...   bad   \n",
              "347162  goodreads.com/list/show/824.Best_Non_fiction_W...  good   \n",
              "141874                               ameon.wordpress.com/  good   \n",
              "\n",
              "                                           text_tokenized  \\\n",
              "78890                             [news, cnet, com, html]   \n",
              "165374  [digiguide, tv, programme, Plunkett, and, Macl...   \n",
              "113657  [carloscarreno, cl, carloscarreno, cl, web, ad...   \n",
              "347162  [goodreads, com, list, show, Best, Non, fictio...   \n",
              "141874                            [ameon, wordpress, com]   \n",
              "\n",
              "                                             text_stemmed  \\\n",
              "78890                             [news, cnet, com, html]   \n",
              "165374  [digiguid, tv, programm, plunkett, and, maclea...   \n",
              "113657  [carloscarreno, cl, carloscarreno, cl, web, ad...   \n",
              "347162  [goodread, com, list, show, best, non, fiction...   \n",
              "141874                            [ameon, wordpress, com]   \n",
              "\n",
              "                                                text_sent  \n",
              "78890                                  news cnet com html  \n",
              "165374     digiguid tv programm plunkett and maclean film  \n",
              "113657  carloscarreno cl carloscarreno cl web admin va...  \n",
              "347162   goodread com list show best non fiction war book  \n",
              "141874                                ameon wordpress com  "
            ]
          },
          "execution_count": 20,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "phish_data.sample(5)"
      ],
      "id": "c776a8d5"
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "dd75b37a"
      },
      "source": [
        "### Model and Data Visualization"
      ],
      "id": "dd75b37a"
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "c433bad9"
      },
      "outputs": [],
      "source": [
        "bad_sites = phish_data[phish_data.Label == 'bad']\n",
        "good_sites = phish_data[phish_data.Label == 'good']"
      ],
      "id": "c433bad9"
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 337
        },
        "id": "829b80f1",
        "outputId": "8dc1e906-ae65-4dc0-b3b7-a42cf823343d"
      },
      "outputs": [
        {
          "data": {
            "text/html": [
              "\n",
              "  <div id=\"df-d5152500-ab97-4ba8-a690-61f646349fb6\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>URL</th>\n",
              "      <th>Label</th>\n",
              "      <th>text_tokenized</th>\n",
              "      <th>text_stemmed</th>\n",
              "      <th>text_sent</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>nobell.it/70ffb52d079109dca5664cce6f317373782/...</td>\n",
              "      <td>bad</td>\n",
              "      <td>[nobell, it, ffb, d, dca, cce, f, login, SkyPe...</td>\n",
              "      <td>[nobel, it, ffb, d, dca, cce, f, login, skype,...</td>\n",
              "      <td>nobel it ffb d dca cce f login skype com en cg...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>www.dghjdgf.com/paypal.co.uk/cycgi-bin/webscrc...</td>\n",
              "      <td>bad</td>\n",
              "      <td>[www, dghjdgf, com, paypal, co, uk, cycgi, bin...</td>\n",
              "      <td>[www, dghjdgf, com, paypal, co, uk, cycgi, bin...</td>\n",
              "      <td>www dghjdgf com paypal co uk cycgi bin webscrc...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>serviciosbys.com/paypal.cgi.bin.get-into.herf....</td>\n",
              "      <td>bad</td>\n",
              "      <td>[serviciosbys, com, paypal, cgi, bin, get, int...</td>\n",
              "      <td>[serviciosbi, com, paypal, cgi, bin, get, into...</td>\n",
              "      <td>serviciosbi com paypal cgi bin get into herf s...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>mail.printakid.com/www.online.americanexpress....</td>\n",
              "      <td>bad</td>\n",
              "      <td>[mail, printakid, com, www, online, americanex...</td>\n",
              "      <td>[mail, printakid, com, www, onlin, americanexp...</td>\n",
              "      <td>mail printakid com www onlin americanexpress c...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>thewhiskeydregs.com/wp-content/themes/widescre...</td>\n",
              "      <td>bad</td>\n",
              "      <td>[thewhiskeydregs, com, wp, content, themes, wi...</td>\n",
              "      <td>[thewhiskeydreg, com, wp, content, theme, wide...</td>\n",
              "      <td>thewhiskeydreg com wp content theme widescreen...</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-d5152500-ab97-4ba8-a690-61f646349fb6')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-d5152500-ab97-4ba8-a690-61f646349fb6 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-d5152500-ab97-4ba8-a690-61f646349fb6');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ],
            "text/plain": [
              "                                                 URL Label  \\\n",
              "0  nobell.it/70ffb52d079109dca5664cce6f317373782/...   bad   \n",
              "1  www.dghjdgf.com/paypal.co.uk/cycgi-bin/webscrc...   bad   \n",
              "2  serviciosbys.com/paypal.cgi.bin.get-into.herf....   bad   \n",
              "3  mail.printakid.com/www.online.americanexpress....   bad   \n",
              "4  thewhiskeydregs.com/wp-content/themes/widescre...   bad   \n",
              "\n",
              "                                      text_tokenized  \\\n",
              "0  [nobell, it, ffb, d, dca, cce, f, login, SkyPe...   \n",
              "1  [www, dghjdgf, com, paypal, co, uk, cycgi, bin...   \n",
              "2  [serviciosbys, com, paypal, cgi, bin, get, int...   \n",
              "3  [mail, printakid, com, www, online, americanex...   \n",
              "4  [thewhiskeydregs, com, wp, content, themes, wi...   \n",
              "\n",
              "                                        text_stemmed  \\\n",
              "0  [nobel, it, ffb, d, dca, cce, f, login, skype,...   \n",
              "1  [www, dghjdgf, com, paypal, co, uk, cycgi, bin...   \n",
              "2  [serviciosbi, com, paypal, cgi, bin, get, into...   \n",
              "3  [mail, printakid, com, www, onlin, americanexp...   \n",
              "4  [thewhiskeydreg, com, wp, content, theme, wide...   \n",
              "\n",
              "                                           text_sent  \n",
              "0  nobel it ffb d dca cce f login skype com en cg...  \n",
              "1  www dghjdgf com paypal co uk cycgi bin webscrc...  \n",
              "2  serviciosbi com paypal cgi bin get into herf s...  \n",
              "3  mail printakid com www onlin americanexpress c...  \n",
              "4  thewhiskeydreg com wp content theme widescreen...  "
            ]
          },
          "execution_count": 22,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "bad_sites.head()"
      ],
      "id": "829b80f1"
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 389
        },
        "id": "7898f327",
        "outputId": "09a1faa7-1f4b-41e3-d349-9819891ba24f"
      },
      "outputs": [
        {
          "data": {
            "text/html": [
              "\n",
              "  <div id=\"df-963bd10c-88f2-49e4-a1c5-9163bf0ee430\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>URL</th>\n",
              "      <th>Label</th>\n",
              "      <th>text_tokenized</th>\n",
              "      <th>text_stemmed</th>\n",
              "      <th>text_sent</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>18231</th>\n",
              "      <td>esxcc.com/js/index.htm?us.battle.net/noghn/en/...</td>\n",
              "      <td>good</td>\n",
              "      <td>[esxcc, com, js, index, htm, us, battle, net, ...</td>\n",
              "      <td>[esxcc, com, js, index, htm, us, battl, net, n...</td>\n",
              "      <td>esxcc com js index htm us battl net noghn en r...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>18232</th>\n",
              "      <td>www\u000eeira¯&amp;nvinip¿ncH¯wVö%ÆåyDaHðû/ÏyEùu\u0003Ë\\nÓ\u00176...</td>\n",
              "      <td>good</td>\n",
              "      <td>[www, eira, nvinip, ncH, wV, yDaH, yE, u, rT, ...</td>\n",
              "      <td>[www, eira, nvinip, nch, wv, ydah, ye, u, rt, ...</td>\n",
              "      <td>www eira nvinip nch wv ydah ye u rt u g m i xz...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>18233</th>\n",
              "      <td>'www.institutocgr.coo/web/media/syqvem/dk-\u000fóij...</td>\n",
              "      <td>good</td>\n",
              "      <td>[www, institutocgr, coo, web, media, syqvem, d...</td>\n",
              "      <td>[www, institutocgr, coo, web, media, syqvem, d...</td>\n",
              "      <td>www institutocgr coo web media syqvem dk ij r ...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>18234</th>\n",
              "      <td>\u0011\u0018Yìê\fkoãÕ»Î§DéÎ\u0002l½ñ¡ââqtò¸/à; Í</td>\n",
              "      <td>good</td>\n",
              "      <td>[Y, ko, D, l, qt]</td>\n",
              "      <td>[y, ko, d, l, qt]</td>\n",
              "      <td>y ko d l qt</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>18236</th>\n",
              "      <td>ruta89fm.com/images/AS@Vies/1i75cf7b16vc&lt;F\u0015d16...</td>\n",
              "      <td>good</td>\n",
              "      <td>[ruta, fm, com, images, AS, Vies, i, cf, b, vc...</td>\n",
              "      <td>[ruta, fm, com, imag, as, vie, i, cf, b, vc, f...</td>\n",
              "      <td>ruta fm com imag as vie i cf b vc f d b g sd v...</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-963bd10c-88f2-49e4-a1c5-9163bf0ee430')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-963bd10c-88f2-49e4-a1c5-9163bf0ee430 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-963bd10c-88f2-49e4-a1c5-9163bf0ee430');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ],
            "text/plain": [
              "                                                     URL Label  \\\n",
              "18231  esxcc.com/js/index.htm?us.battle.net/noghn/en/...  good   \n",
              "18232  www\u000eeira¯&nvinip¿ncH¯wVö%ÆåyDaHðû/ÏyEùu\u0003Ë\\nÓ\u00176...  good   \n",
              "18233  'www.institutocgr.coo/web/media/syqvem/dk-\u000fóij...  good   \n",
              "18234                  \u0011\u0018Yìê\n",
              "koãÕ»Î§DéÎ\u0002l½ñ¡ââqtò¸/à; Í  good   \n",
              "18236  ruta89fm.com/images/AS@Vies/1i75cf7b16vc<F\u0015d16...  good   \n",
              "\n",
              "                                          text_tokenized  \\\n",
              "18231  [esxcc, com, js, index, htm, us, battle, net, ...   \n",
              "18232  [www, eira, nvinip, ncH, wV, yDaH, yE, u, rT, ...   \n",
              "18233  [www, institutocgr, coo, web, media, syqvem, d...   \n",
              "18234                                  [Y, ko, D, l, qt]   \n",
              "18236  [ruta, fm, com, images, AS, Vies, i, cf, b, vc...   \n",
              "\n",
              "                                            text_stemmed  \\\n",
              "18231  [esxcc, com, js, index, htm, us, battl, net, n...   \n",
              "18232  [www, eira, nvinip, nch, wv, ydah, ye, u, rt, ...   \n",
              "18233  [www, institutocgr, coo, web, media, syqvem, d...   \n",
              "18234                                  [y, ko, d, l, qt]   \n",
              "18236  [ruta, fm, com, imag, as, vie, i, cf, b, vc, f...   \n",
              "\n",
              "                                               text_sent  \n",
              "18231  esxcc com js index htm us battl net noghn en r...  \n",
              "18232  www eira nvinip nch wv ydah ye u rt u g m i xz...  \n",
              "18233  www institutocgr coo web media syqvem dk ij r ...  \n",
              "18234                                        y ko d l qt  \n",
              "18236  ruta fm com imag as vie i cf b vc f d b g sd v...  "
            ]
          },
          "execution_count": 23,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "good_sites.head()"
      ],
      "id": "7898f327"
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "a74d4650"
      },
      "outputs": [],
      "source": [
        "cv = CountVectorizer()"
      ],
      "id": "a74d4650"
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "4a6a3480"
      },
      "outputs": [],
      "source": [
        "feature = cv.fit_transform(phish_data.text_sent)"
      ],
      "id": "4a6a3480"
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "74fc2383",
        "outputId": "c00c3788-8fd0-4287-b8f4-9bec4471c514"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "array([[0, 0, 0, ..., 0, 0, 0],\n",
              "       [0, 0, 0, ..., 0, 0, 0],\n",
              "       [0, 0, 0, ..., 0, 0, 0],\n",
              "       [0, 0, 0, ..., 0, 0, 0],\n",
              "       [0, 0, 0, ..., 0, 0, 0]])"
            ]
          },
          "execution_count": 26,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "feature[:5].toarray()"
      ],
      "id": "74fc2383"
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "45a4c61a"
      },
      "outputs": [],
      "source": [
        "trainX, testX, trainY, testY = train_test_split(feature, phish_data.Label)"
      ],
      "id": "45a4c61a"
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "39c60765"
      },
      "outputs": [],
      "source": [
        "lr = LogisticRegression()"
      ],
      "id": "39c60765"
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "2794d553",
        "outputId": "c1d6a2e6-315f-4568-c081-e0dee40747f6"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "LogisticRegression()"
            ]
          },
          "execution_count": 29,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "lr.fit(trainX,trainY)"
      ],
      "id": "2794d553"
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "2bfcf012",
        "outputId": "1a126270-9274-4dc3-a51b-9d55b54106bb"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "0.963447577855931"
            ]
          },
          "execution_count": 30,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "lr.score(testX,testY)"
      ],
      "id": "2bfcf012"
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "2cae7b90"
      },
      "outputs": [],
      "source": [
        "Scores_ml = {}\n",
        "Scores_ml['Logistic Regression'] = np.round(lr.score(testX,testY),2)"
      ],
      "id": "2cae7b90"
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 560
        },
        "id": "96bdf3c4",
        "outputId": "ab1bef46-7f2a-4104-991d-303d0edc0bbe"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Training Accuracy : 0.9768815729753476\n",
            "Testing Accuracy : 0.963447577855931\n",
            "\n",
            "CLASSIFICATION REPORT\n",
            "\n",
            "              precision    recall  f1-score   support\n",
            "\n",
            "         Bad       0.90      0.97      0.93     36260\n",
            "        Good       0.99      0.96      0.97    101077\n",
            "\n",
            "    accuracy                           0.96    137337\n",
            "   macro avg       0.94      0.96      0.95    137337\n",
            "weighted avg       0.97      0.96      0.96    137337\n",
            "\n",
            "\n",
            "CONFUSION MATRIX\n"
          ]
        },
        {
          "data": {
            "text/plain": [
              "<matplotlib.axes._subplots.AxesSubplot at 0x7f126f04d090>"
            ]
          },
          "execution_count": 32,
          "metadata": {},
          "output_type": "execute_result"
        },
        {
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 2 Axes>"
            ]
          },
          "metadata": {},
          "output_type": "display_data"
        }
      ],
      "source": [
        "print('Training Accuracy :',lr.score(trainX,trainY))\n",
        "print('Testing Accuracy :',lr.score(testX,testY))\n",
        "con_mat = pd.DataFrame(confusion_matrix(lr.predict(testX), testY),\n",
        "            columns = ['Predicted:Bad', 'Predicted:Good'],\n",
        "            index = ['Actual:Bad', 'Actual:Good'])\n",
        "\n",
        "\n",
        "print('\\nCLASSIFICATION REPORT\\n')\n",
        "print(classification_report(lr.predict(testX), testY,\n",
        "                            target_names =['Bad','Good']))\n",
        "\n",
        "print('\\nCONFUSION MATRIX')\n",
        "plt.figure(figsize= (6,4))\n",
        "sns.heatmap(con_mat, annot = True,fmt='d',cmap=\"YlGnBu\")"
      ],
      "id": "96bdf3c4"
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "5ee1f977"
      },
      "outputs": [],
      "source": [
        "mnb = MultinomialNB()"
      ],
      "id": "5ee1f977"
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "678bc26e",
        "outputId": "0a456661-91a7-499e-c8a4-bb5237030952"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "MultinomialNB()"
            ]
          },
          "execution_count": 34,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "mnb.fit(trainX,trainY)"
      ],
      "id": "678bc26e"
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "8b498e24",
        "outputId": "7ec774fb-c0f6-4c2e-88e0-1618b269073f"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "0.9577462737645354"
            ]
          },
          "execution_count": 35,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "mnb.score(testX,testY)"
      ],
      "id": "8b498e24"
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "6c411166"
      },
      "outputs": [],
      "source": [
        "Scores_ml['MultinomialNB'] = np.round(mnb.score(testX,testY),2)"
      ],
      "id": "6c411166"
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 560
        },
        "id": "39ac62cc",
        "outputId": "8dee1141-f773-48f9-a7d0-5a8b6e20765b"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Training Accuracy : 0.9741583314927587\n",
            "Testing Accuracy : 0.9577462737645354\n",
            "\n",
            "CLASSIFICATION REPORT\n",
            "\n",
            "              precision    recall  f1-score   support\n",
            "\n",
            "         Bad       0.91      0.93      0.92     38091\n",
            "        Good       0.97      0.97      0.97     99246\n",
            "\n",
            "    accuracy                           0.96    137337\n",
            "   macro avg       0.94      0.95      0.95    137337\n",
            "weighted avg       0.96      0.96      0.96    137337\n",
            "\n",
            "\n",
            "CONFUSION MATRIX\n"
          ]
        },
        {
          "data": {
            "text/plain": [
              "<matplotlib.axes._subplots.AxesSubplot at 0x7f1268db0e90>"
            ]
          },
          "execution_count": 37,
          "metadata": {},
          "output_type": "execute_result"
        },
        {
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 2 Axes>"
            ]
          },
          "metadata": {},
          "output_type": "display_data"
        }
      ],
      "source": [
        "print('Training Accuracy :',mnb.score(trainX,trainY))\n",
        "print('Testing Accuracy :',mnb.score(testX,testY))\n",
        "con_mat = pd.DataFrame(confusion_matrix(mnb.predict(testX), testY),\n",
        "            columns = ['Predicted:Bad', 'Predicted:Good'],\n",
        "            index = ['Actual:Bad', 'Actual:Good'])\n",
        "\n",
        "\n",
        "print('\\nCLASSIFICATION REPORT\\n')\n",
        "print(classification_report(mnb.predict(testX), testY,\n",
        "                            target_names =['Bad','Good']))\n",
        "\n",
        "print('\\nCONFUSION MATRIX')\n",
        "plt.figure(figsize= (6,4))\n",
        "sns.heatmap(con_mat, annot = True,fmt='d',cmap=\"YlGnBu\")"
      ],
      "id": "39ac62cc"
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 285
        },
        "id": "3933f6a9",
        "outputId": "2c16d15c-4012-4aca-c1e0-f558a5672032"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "<matplotlib.axes._subplots.AxesSubplot at 0x7f1268da68d0>"
            ]
          },
          "execution_count": 38,
          "metadata": {},
          "output_type": "execute_result"
        },
        {
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {},
          "output_type": "display_data"
        }
      ],
      "source": [
        "acc = pd.DataFrame.from_dict(Scores_ml,orient = 'index',columns=['Accuracy'])\n",
        "sns.set_style('darkgrid')\n",
        "sns.barplot(acc.index,acc.Accuracy)"
      ],
      "id": "3933f6a9"
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "f3c96a42"
      },
      "outputs": [],
      "source": [
        "pipeline_ls = make_pipeline(CountVectorizer(tokenizer = RegexpTokenizer(r'[A-Za-z]+').tokenize,stop_words='english'), LogisticRegression())"
      ],
      "id": "f3c96a42"
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "d1d5a1fe"
      },
      "outputs": [],
      "source": [
        "trainX, testX, trainY, testY = train_test_split(phish_data.URL, phish_data.Label)"
      ],
      "id": "d1d5a1fe"
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "f26e886f",
        "outputId": "06d73d7e-2715-463f-8fcf-d0c06df9f5b7"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "Pipeline(steps=[('countvectorizer',\n",
              "                 CountVectorizer(stop_words='english',\n",
              "                                 tokenizer=<bound method RegexpTokenizer.tokenize of RegexpTokenizer(pattern='[A-Za-z]+', gaps=False, discard_empty=True, flags=<RegexFlag.UNICODE|DOTALL|MULTILINE: 56>)>)),\n",
              "                ('logisticregression', LogisticRegression())])"
            ]
          },
          "execution_count": 41,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "pipeline_ls.fit(trainX,trainY)"
      ],
      "id": "f26e886f"
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "fc65e539",
        "outputId": "f2530bcb-01df-470f-e82f-103eaf7238e2"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "0.9667096266847245"
            ]
          },
          "execution_count": 42,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "pipeline_ls.score(testX,testY) "
      ],
      "id": "fc65e539"
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 560
        },
        "id": "6b11ed3d",
        "outputId": "a1700d32-b8f2-43d9-a26b-285e7b4867e1"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Training Accuracy : 0.9798184020251984\n",
            "Testing Accuracy : 0.9667096266847245\n",
            "\n",
            "CLASSIFICATION REPORT\n",
            "\n",
            "              precision    recall  f1-score   support\n",
            "\n",
            "         Bad       0.91      0.97      0.94     37056\n",
            "        Good       0.99      0.97      0.98    100281\n",
            "\n",
            "    accuracy                           0.97    137337\n",
            "   macro avg       0.95      0.97      0.96    137337\n",
            "weighted avg       0.97      0.97      0.97    137337\n",
            "\n",
            "\n",
            "CONFUSION MATRIX\n"
          ]
        },
        {
          "data": {
            "text/plain": [
              "<matplotlib.axes._subplots.AxesSubplot at 0x7f12995e3090>"
            ]
          },
          "execution_count": 43,
          "metadata": {},
          "output_type": "execute_result"
        },
        {
          "data": {
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAW0AAAD4CAYAAAAn3bdmAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4yLjIsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+WH4yJAAAgAElEQVR4nO3deVxVdf7H8dcFXFBkMwG3oXHNFUqtTCIlARUJN342pRPOr2kzzUonTcsSl5mJ0katXJpScxS1cCNzwRQtNTNNM6cZS3JJIAXBhUUu5/cHP+/EJN6LAnIu7+fjcR4P7uHc7/mc6318/PI53/P9WgzDMBAREVNwudkBiIiI45S0RURMRElbRMRElLRFRExESVtExETcKvsEf/56c2WfQkxofFDgzQ5BqqU2N9yC+29+5/CxeceX3fD5qpp62iIiJlLpPW0RkapksTh3X1RJW0SciovFudOac1+diNQ46mmLiJiIxWK52SFUKiVtEXEy6mmLiJiGyiMiIiaipC0iYiIaPSIiYiLqaYuImIiStoiIiVjQkD8REdNQT1tExERcXJw7rTn31YlIDaSetoiIaag8IiJiIkraIiImYlF5RETEPNTTFhExERcX15sdQqVS0hYRp6LyiIiIiag8IiJiIkraIiImovKIiIiJWPQYu4iIeWhhXxERE1F5RETERHQjUkTETFQeERExEefuaJedtA8fPnzNN3bo0KHCgxERuWEuzp21y0zaf/7znwEoLCzkm2++oW3btgB89913dOzYkcTExKqJUESkPJw7Z5edtJcsWQLA008/zUcffWRL2v/617+YM2dO1UQnIlJORk2vaR87dsyWsAHatGnD999/X6lBiYhcN+fO2faTdtu2bZk4cSIPPPAAAOvWrSuVxEVEqhUX587adqs/M2bMoHXr1ixevJjFixfTqlUrZsyYURWxiYiUn8Xi+GbH+++/T1RUFP379+e5556joKCAEydOEBsbS3h4OGPGjKGwsBAouf83ZswYwsPDiY2N5eTJk7Z25s2bR3h4OJGRkezYscO2PzU1lcjISMLDw5k/f75Dl2c3adepU4e4uDjmzp3L3LlziYuLo06dOg41LiJS5Vwtjm/XkJGRweLFi/nwww9Zv349VquV5ORkEhISiIuLY/PmzXh6erJq1SoAVq5ciaenJ5s3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GefPnzd69+5dKlapXmpETzs/P5+YmBigpHc1ZMgQ9u/fT6dOnWjevDkAn332Gd999x0bN24E4Pz58/z444/s3buXqKgoXF1d8ff35+677/5V+wcOHKBr1662try9va8ax+eff16q7nnhwgUuXrzI3r17mTNnDgA9e/bEy8vLdsyCBQtKtZGQkECnTp3IysriwQcf5N5776Vp06Zs2LCBFStWUFRUxM8//8z333+PYRg0a9aMW2+9FYAHHniAFStWXM9H6DSc4buQnZ1dqq0PP/yQxYsXc+7cOZYvX86+ffvo3bs39erVAyA8PJwvv/wSwzCuur+4uJjevXvj7u4OlNTRpfqqEUn7Sh3zv1358gIYhsGkSZO49957Sx2zffv2CoujuLiYFStW2P6kvRG+vr60b9+er7/+muLiYv7+97+zatUqvLy8GD9+PAUFBRUQsfNxhu9CYGAgp0+f5sKFC3h4eDB48GAGDx5M//79sVqtFRajVE814kakI0JCQli2bBmXL18G4NixY1y6dIlu3bqxYcMGrFYrmZmZ7Nmz51fvDQ4O5ssvv+TEiRMAnDt3DoD69etz8eLFUudYsmSJ7fWRI0cA6NatG+vWrQNKEkNOTo7dePPy8jhy5Ai/+c1vuHjxIu7u7jRo0IAzZ86QmpoKQIsWLTh16hTHjx8HIDk5udyfS01U3b8L7u7uDB48mPj4eNt/zlar1RZv165d2bJlC3l5eVy6dIktW7bQtWvXMvd369aNLVu2kJ+fz4ULF/j0009v+DOUylMjetqOiI2N5dSpUwwaNAjDMPDx8eGtt94iPDyc3bt3069fP5o0aUJwcPCv3uvr68uUKVMYNWoUxcXFNGzYkPfee49evXoxevRoUlJSeOmll5g4cSJTpkwhOjoaq9VK165dmTJlCiNHjuT5558nKiqK22+/nSZNmtja/uMf/8jUqVPx9/cHYOzYsdStW5fCwkIGDhxIx44dAWjfvj19+/YlICCAO+64A4A6deowZcoUHnvsMduNyF8mDrk6M3wXnn32Wd5880369+9P/fr1qVu3LgMGDMDPz49mzZoxaNAgYmNjgZIbju3btwcoc3+/fv2IiYnB19eXTp06VfZHLDdA82mLiJiIyiMiIiaipC0iYiJK2iIiJqKkLSJiIkraIiImoqQtImIiStoiIibyf9cd18k1tJ64AAAAAElFTkSuQmCC\n",
            "text/plain": [
              "<Figure size 432x288 with 2 Axes>"
            ]
          },
          "metadata": {},
          "output_type": "display_data"
        }
      ],
      "source": [
        "print('Training Accuracy :',pipeline_ls.score(trainX,trainY))\n",
        "print('Testing Accuracy :',pipeline_ls.score(testX,testY))\n",
        "con_mat = pd.DataFrame(confusion_matrix(pipeline_ls.predict(testX), testY),\n",
        "            columns = ['Predicted:Bad', 'Predicted:Good'],\n",
        "            index = ['Actual:Bad', 'Actual:Good'])\n",
        "\n",
        "\n",
        "print('\\nCLASSIFICATION REPORT\\n')\n",
        "print(classification_report(pipeline_ls.predict(testX), testY,\n",
        "                            target_names =['Bad','Good']))\n",
        "\n",
        "print('\\nCONFUSION MATRIX')\n",
        "plt.figure(figsize= (6,4))\n",
        "sns.heatmap(con_mat, annot = True,fmt='d',cmap=\"YlGnBu\")"
      ],
      "id": "6b11ed3d"
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "47485d0f"
      },
      "outputs": [],
      "source": [
        "pickle.dump(pipeline_ls,open('phishing.pkl','wb'))"
      ],
      "id": "47485d0f"
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "a6294ba3",
        "outputId": "22c1d029-5b11-46b0-8b5b-40541ba7b631"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "0.9667096266847245\n"
          ]
        }
      ],
      "source": [
        "loaded_model = pickle.load(open('phishing.pkl', 'rb'))\n",
        "result = loaded_model.score(testX,testY)\n",
        "print(result)"
      ],
      "id": "a6294ba3"
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "0442e188",
        "outputId": "63e578e1-f8fd-447a-81d7-ce2ce527eb28"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "['bad' 'bad' 'bad' 'bad']\n",
            "******************************\n",
            "['good' 'good' 'good' 'good']\n"
          ]
        }
      ],
      "source": [
        "predict_bad = ['yeniik.com.tr/wp-admin/js/login.alibaba.com/login.jsp.php','fazan-pacir.rs/temp/libraries/ipad','tubemoviez.exe','svision-online.de/mgfi/administrator/components/com_babackup/classes/fx29id1.txt']\n",
        "predict_good = ['youtube.com/','youtube.com/watch?v=qI0TQJI3vdU','retailhellunderground.com/','restorevisioncenters.com/html/technology.html']\n",
        "loaded_model = pickle.load(open('phishing.pkl', 'rb'))\n",
        "\n",
        "result = loaded_model.predict(predict_bad)\n",
        "result2 = loaded_model.predict(predict_good)\n",
        "print(result)\n",
        "print(\"*\"*30)\n",
        "print(result2)"
      ],
      "id": "0442e188"
    }
  ],
  "metadata": {
    "colab": {
      "provenance": []
    },
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
      "version": "3.8.8"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 5
}