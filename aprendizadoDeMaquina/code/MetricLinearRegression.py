from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

class MetricLinearRegression():
    
    def __init__(self, dataFrame):
        self.dataFrame = dataFrame

    def machineLearning(self, columnsBase: list, previewColum, seed: int):

        if seed > 4294967296:
            return "this seed excped the valida elements plase try a value lower than 4294967296"

        self.columnsBase = columnsBase
        self.previewColum = previewColum

        X_simple = self.dataFrame[[columnsBase]]
        columPreview = self.dataFrame[previewColum].values.ravel()

        # Dividir o dataset em 80% treino e 20% teste
        
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X_simple, columPreview, test_size=0.2, random_state=seed)

        model_regression = LinearRegression()
        model_regression.fit(self.X_train, self.y_train)

        self.y_pred = model_regression.predict(self.X_test)

        # Calcular MAE e MSE
        self.mae = mean_absolute_error(self.y_test, self.y_pred)
        self.mse = mean_squared_error(self.y_test, self.y_pred)

        # Calcular a porcentagem de erro para MAE e MSE
        self.mae_percentage = (self.mae / self.y_test.mean()) * 100
        self.mse_percentage = (self.mse / self.y_test.mean()) * 100

    def showStatics(self):
        print("Erro Médio Absoluto (MAE):", self.mae)
        print("Erro Quadrático Médio (MSE):", self.mse)
        print("Porcentagem de Erro MAE:", self.mae_percentage, "%")
        print(f"Porcentagem de Erro MSE: {self.mse_percentage:.2f}")

    def displayDispersoionGraph(self):
        plt.figure(figsize=(10, 6))
        plt.scatter(self.X_test, self.y_test, color='blue', label='Valor Real', alpha=0.5)
        plt.plot(self.X_test, self.y_pred, color='red', label='Valor Previsto', alpha=0.5)
        plt.xlabel(str(self.columnsBase))
        plt.ylabel(str(self.previewColum))
        plt.title('Regressão Linear com uma Feature ou Recurso')
        plt.legend()
        plt.show()



