import matplotlib.pyplot as plt

class Visualization():
    def __init__(self, data, start_date, end_date, period , symbol):
        self.symbol = symbol
        self.start_date = start_date
        self.end_date = end_date
        self.period = period
        self.data = data

    def visualize_data_PFA(self):
        plt.figure(figsize=(12, 8))
        plt.title('Preço de Fechamento Ajustado')
        plt.xlabel('Data')
        plt.ylabel('Preço de Fechamento Ajustado')

        plt.plot(self.data['Adj Close'], label='Preço de Fechamento Ajustado', color='blue')
        
        plt.legend()
        plt.grid(True)
        plt.show()

    def visualize_data_Geral(self):
        plt.figure(figsize=(12, 8))
        plt.title('Panorama Geral')
        plt.xlabel('Data')
        plt.ylabel('Valores')

        plt.plot(self.data['Adj Close Original'], label='Preço de Fechamento Ajustado', color='blue')
        plt.plot(self.data['SMA Original'], label=f'Média Móvel Simples ({self.period} dias)', color='orange')
        plt.plot(self.data['EMA Original'], label=f'Média Móvel Exponencial ({self.period} dias)', color='green')

        plt.plot(self.data.loc[self.data['Signal_Buy'] == 1.0].index,
                 self.data['SMA Original'][self.data['Signal_Buy'] == 1.0],
                 '^', markersize=10, color='g', label='Sinal de Compra')

        plt.plot(self.data.loc[self.data['Signal_Sell'] == -1.0].index,
                 self.data['SMA Original'][self.data['Signal_Sell'] == -1.0],
                 'v', markersize=10, color='r', label='Sinal de Venda')
        
        plt.legend()
        plt.grid(True)
        plt.show()

    def visualize_data_adition(self):
        plt.figure(figsize=(12, 8))
        plt.title('Recursos Adicionais')
        plt.xlabel('Data')
        plt.ylabel('Valores')

        # Plot das características temporais
        plt.plot(self.data['Day'], label='Day', color='blue')
        plt.plot(self.data['Month'], label='Month', color='green')
        plt.plot(self.data['Year'], label='Year', color='red')
        plt.plot(self.data['DayOfWeek'], label='DayOfWeek', color='purple')
        plt.plot(self.data['DayOfYear'], label='DayOfYear', color='orange')

        # Plot das médias móveis para diferentes janelas de tempo
        windows = [5, 10, 20, 50]
        for window in windows:
            plt.plot(self.data[f'Rolling_Mean_{window}'], label=f'Rolling_Mean_{window}', linestyle='dashed')

        # Plot dos desvios padrão para diferentes janelas de tempo
        for window in windows:
            plt.plot(self.data[f'Rolling_Std_{window}'], label=f'Rolling_Std_{window}', linestyle='dashed')

        plt.legend()
        plt.grid(True)
        plt.show()

    def visualize_data_medias(self):
        plt.figure(figsize=(12, 8))
        plt.title('Vendas com Medias')
        plt.xlabel('Data')
        plt.ylabel('Sinal')

        plt.plot(self.data['SMA'], label=f'Média Móvel Simples ({self.period} dias)', color='orange')
        plt.plot(self.data['EMA'], label=f'Média Móvel Exponencial ({self.period} dias)', color='green')

        plt.legend()
        plt.grid(True)
        plt.show()

    def visualize_data_stg(self):
        plt.figure(figsize=(12, 8))
        plt.title('Retornos Acumulados da Estratégia de Negociação')
        plt.xlabel('Data')
        plt.ylabel('Retorno Acumulado')

        # Plota os retornos acumulados da estratégia
        plt.plot(self.data['Cumulative_Strategy_Return'], label='Estratégia de Negociação', color='purple')

        # Plota uma linha base (Buy and Hold)
        plt.plot((1 + self.data['Daily_Return']).cumprod(), label='Buy and Hold', color='gray', linestyle='--')

        plt.legend()
        plt.grid(True)
        plt.show()

    def visualize_data_buy_and_sell(self):
        plt.figure(figsize=(12, 8))
        plt.title('Sinais de Compra/Venda')
        plt.xlabel('Data')
        plt.ylabel('Sinal')

        plt.plot(self.data.loc[self.data['Signal_Buy'] == 1.0].index,
                self.data['SMA'][self.data['Signal_Buy'] == 1.0],
                '^', markersize=10, color='g', label='Sinal de Compra')

        plt.plot(self.data.loc[self.data['Signal_Sell'] == -1.0].index,
                self.data['SMA'][self.data['Signal_Sell'] == -1.0],
                'v', markersize=10, color='r', label='Sinal de Venda')

        plt.legend()
        plt.grid(True)
        plt.show()

    def visualize_data_additional_features(self):

            plt.figure(figsize=(12, 8))
            plt.title('Recursos Adicionais')
            plt.xlabel('Data')
            plt.ylabel('Valores')

            windows = [5, 10, 20, 50 ]

            for window in windows:
                plt.plot(self.data[f'SMA_{window}'], label=f'SMA_{window}', alpha=0.7)

            plt.plot(self.data['Cumulative_Return'], label='Retorno Acumulado', color='red', linewidth=2)

            plt.legend()
            plt.grid(True)
            plt.show()
