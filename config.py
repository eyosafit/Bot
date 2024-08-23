import yaml
import dotenv
from pathlib import Path

config_dir = Path(__file__).parent.parent.resolve() / "config"

# load yaml config
with open("config.yml", 'r') as f:
    config_yaml = yaml.safe_load(f)

# load .env config
config_env = dotenv.dotenv_values("config.env")

# config parameters
telegram_token = config_yaml["telegram_token"]
allowed_telegram_usernames = config_yaml["allowed_telegram_usernames"]
PROXY = config_yaml["PROXY"]
mongodb_uri = f"mongodb://mongo:{config_env['MONGODB_PORT']}"


with open("models.yml", 'r') as f:
    models = yaml.safe_load(f)