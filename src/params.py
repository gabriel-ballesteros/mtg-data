from dotenv import load_dotenv
import os
from selenium.webdriver.chrome.options import Options
from pathlib import Path


class Params:
    """
    Parameters class.

    This file centralizes anything that can be
    parametrized in the code.

    If you want to use a parameter later in the code, you
    should instantiate params as:
    `params = Params()`,
    send the object `params` within functions and, inside the
    function, call the parameter as an attribute of the `params` object.

    For instance, if you have a parameter called `url` created here, you'd
    call it in a function called `func` as:

    ```
    def func(params):
            ...

            url = params.url

        ...
    ```
    """

    # pre-requeqs

    # magically load environment variables from any .env files
    env_path = Path('.') / '.env'
    load_dotenv(dotenv_path=env_path)

    # parameters
    sites_to_scrape = ['https://mtgmelee.com/Decklists/Standard']
    mtgmelee_orgs = ['star city games', 'channelfireball']

    top_d_cut = 32
    min_t_players = 32

    chrome_options = Options()
    chrome_options.headless = True
    chrome_path = os.getenv('CHROME_PATH')

    scryfall_collection_url = 'https://api.scryfall.com/cards/collection'

    raw_data = ('../data/raw/')
    external_data = ('../data/external/')
    processed_data = ('../data/processed/')
    intermediate_data = ('../data/intermediate/')

    log_name = os.path.abspath('../log/dump.log')

    # if this is set to True, then all the nodes will be automatically
    # considered not up-to-date and will be rerun.
    force_execution = True

    # Database connection params
    user = os.getenv('DB_USERNAME')
    password = os.getenv('DB_PASSWORD')
    host = 'localhost'
    database = os.getenv('MTG_DATABASE')
