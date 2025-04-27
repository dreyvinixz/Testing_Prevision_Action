import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from visualize_data import Visualization 
from datetime import datetime
from sklearn.preprocessing import StandardScaler

class TradingStrategy:
    def __init__(self, symbol, start_date, end_date, period):
        self.symbol = symbol
        self.start_date = start_date
        self.end_date = end_date
        self.period = period
        self.data = None

    def download_data(self):
        try:
            self.data = yf.download(self.symbol, start=self.start_date, end=self.end_date)
            if self.data.empty:
                raise ValueError("Nenhum dado foi baixado. Verifique o símbolo ou o período.")
        except Exception as e:
            print(f"Erro ao baixar dados: {e}")
            raise
        
    def save_data_to_csv(self, filename):
        self.data.to_csv(filename, index=False)

    def calculate_returns(self):
        self.data['Daily_Return'] = self.data['Adj Close'].pct_change()

    def calculate_sma_ema(self):
        self.data['SMA'] = self.data['Adj Close'].rolling(window=self.period, min_periods=1).mean()
        self.data['EMA'] = self.data['Adj Close'].ewm(span=self.period, adjust=False).mean()

    def generate_signals(self):
        self.data['Signal_Buy'] = 0.0
        self.data['Signal_Sell'] = 0.0

        self.data.loc[self.data['SMA'] > self.data['EMA'], 'Signal_Buy'] = 1.0
        self.data.loc[self.data['SMA'] < self.data['EMA'], 'Signal_Sell'] = -1.0

    def calculate_strategy_returns(self):
        self.data['Strategy_Return'] = self.data['Daily_Return'] * (
                self.data['Signal_Buy'].shift(1) + self.data['Signal_Sell'].shift(1))

    def calculate_cumulative_returns(self):
        self.data['Cumulative_Strategy_Return'] = (1 + self.data['Strategy_Return']).cumprod()

    def display_statistics(self):
        # Exibir as primeiras linhas dos dados com os retornos diários
        print("\nPrimeiras linhas dos dados com os retornos diários:")
        print(self.data[['Adj Close', 'Daily_Return']].head())

        # Exibir o Desvio Padrão dos Retornos Diários
        daily_std = self.data['Daily_Return'].std()
        print("Desvio Padrão dos Retornos Diários:", daily_std)

        # Exibir Média dos Retornos Diários
        mean_return = self.data['Daily_Return'].mean()
        print("Média dos Retornos Diários:", mean_return)

    def optimize_parameters(self, symbol, start_date, end_date):
        best_return = -float('inf')
        best_period = 0

        for period in range(10, 50, 5 ):
            strategy = TradingStrategy(symbol, start_date, end_date, period)
            strategy.download_data()
            strategy.calculate_returns()
            strategy.calculate_sma_ema()
            strategy.generate_signals()
            strategy.calculate_strategy_returns()
            strategy.calculate_cumulative_returns()

            cumulative_return = strategy.data['Cumulative_Strategy_Return'].iloc[-1]
            if cumulative_return > best_return:
                best_return = cumulative_return
                best_period = period

        return best_period, best_return

    def normalize_standardize_data(self):
        scaler = StandardScaler()

        # Ensure SMA and EMA are calculated before copying
        self.calculate_sma_ema()

        # Crie cópias das colunas necessárias
        self.data['Adj Close Original'] = self.data['Adj Close'].copy()
        self.data['SMA Original'] = self.data['SMA'].copy()
        self.data['EMA Original'] = self.data['EMA'].copy()

        # Normalização e Padronização
        self.data['Adj Close'] = scaler.fit_transform(self.data['Adj Close'].values.reshape(-1, 1))
        self.data['SMA'] = scaler.transform(self.data['SMA'].values.reshape(-1, 1))
        self.data['EMA'] = scaler.transform(self.data['EMA'].values.reshape(-1, 1))

    def add_temporal_features(self):
        # Adiciona informações temporais
        self.data['Day'] = self.data.index.day
        self.data['Month'] = self.data.index.month
        self.data['Year'] = self.data.index.year
        self.data['DayOfWeek'] = self.data.index.dayofweek
        self.data['DayOfYear'] = self.data.index.dayofyear

        # Adiciona janelas deslizantes para capturar padrões ao longo do tempo
        windows = [5, 10, 20, 50]

        for window in windows:
            self.data[f'Rolling_Mean_{window}'] = self.data['Adj Close'].rolling(window=window).mean()
            self.data[f'Rolling_Std_{window}'] = self.data['Adj Close'].rolling(window=window).std()

    def handle_missing_data(self):
        # Lidar com dados ausentes usando interpolação linear
        self.data['Adj Close'].interpolate(method='linear', inplace=True)
        self.data['Adj Close'].fillna(self.data['Adj Close'].mean(), inplace=True)

    def feature_engineering(self):
        # Criar médias móveis de diferentes janelas de tempo
        windows = [5, 10, 20, 50]
        for window in windows:
            self.data[f'SMA_{window}'] = self.data['Adj Close'].rolling(window=window, min_periods=1).mean()
            self.data[f'EMA_{window}'] = self.data['Adj Close'].ewm(span=window, adjust=False).mean()

        # Calcular retornos acumulados
        self.data['Cumulative_Return'] = (1 + self.data['Daily_Return']).cumprod()

def main():
    symbol = "^BVSP"
    start_date = datetime(2022, 1, 1)
    end_date = datetime.today()

    # Criar uma instância de TradingStrategy
    strategy_instance = TradingStrategy(symbol, start_date, end_date, 20)
    # Otimiza o período da média móvel
    best_period, best_return = strategy_instance.optimize_parameters(symbol, start_date, end_date)
    print(f"Melhor período encontrado: {best_period} com Retorno Acumulado: {best_return}")

    # Usa os melhores parâmetros na sua estratégia
    strategy = TradingStrategy(symbol, start_date, end_date, best_period)
    strategy.download_data()

    # Certifique-se de calcular a SMA, EMA e gerar os sinais antes da engenharia de recursos
    strategy.calculate_sma_ema()
    strategy.generate_signals()
    strategy.calculate_returns()

    # Engenharia de recursos
    strategy.feature_engineering()

    # Adiciona o tratamento de dados ausentes antes da normalização e padronização
    strategy.handle_missing_data()

    # Normalização e padronização
    strategy.normalize_standardize_data()

    # Adiciona informações temporais
    strategy.add_temporal_features()

    strategy.calculate_strategy_returns()
    strategy.calculate_cumulative_returns()

    # Exibe estatísticas, visualiza dados e os recursos adicionais
    strategy.display_statistics()

    visualization = Visualization(strategy.data , strategy.start_date, strategy.end_date , strategy.period, strategy.symbol)
    visualization.visualize_data_Geral()
    #visualização de outros graficos:
"""     visualization.visualize_data_PFA()
    visualization.visualize_data_adition()
    visualization.visualize_data_medias()
    visualization.visualize_data_stg()
    visualization.visualize_data_buy_and_sell()
    visualization.visualize_data_additional_features() """

if __name__ == "__main__":
    main()
