# config.py

# === CAMINHOS DE ARQUIVOS ===
DATA_DIR = "C:/PythonProjects/estudocd1/data"
RAW_DATA_PATH = f"{DATA_DIR}dados_brutos.csv"
CLEAN_DATA_PATH = f"{DATA_DIR}dados_limpos.csv"
MODEL_OUTPUT_PATH = f"{DATA_DIR}modelo_treinado.pkl"

# === PARÂMETROS DE MODELO ===
TRAINING_RATIO = 0.8
RANDOM_STATE = 42
N_ESTIMATORS = 100
MAX_DEPTH = 10

# === CHAVES E TOKENS ===
API_KEY = "SUA_API_KEY_AQUI"  # Substitua por uma chave real se necessário

# === CONFIGURAÇÃO DE LOG ===
LOG_FILE = "logs/projeto.log"
DEBUG = True