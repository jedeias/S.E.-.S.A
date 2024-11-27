from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

class KnnClassifier():
    
    def __init__(self, dataFrame):
        self.dataFrame = dataFrame

    def machineLearning(self, columnsBase, groups, previewColum, seed, k_pontos):

        # print(self.dataFrame[columnsBase[0]].values)

        self.groups = groups

        groups = pd.cut(self.dataFrame[columnsBase[0]].values, bins=len(groups), labels=groups)

        if seed > 4294967296:
            return "this seed excped the valida elements plase try a value lower than 4294967296"

        X_simple = self.dataFrame[[previewColum]]
        
        # Dividir o dataset em 80% treino e 20% teste
        
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X_simple, groups, test_size=0.2, random_state=seed)

        if k_pontos == 0 or k_pontos == None:
            k_pontos = 5 
        
        self.model_knn = KNeighborsClassifier(n_neighbors=k_pontos)
        self.model_knn.fit(self.X_train, self.y_train)

        self.y_pred = self.model_knn.predict(self.X_test)



    def showStatics(self):
        accuracy = accuracy_score(self.y_test, self.y_pred),
        precision = precision_score(self.y_test, self.y_pred, average='weighted')
        recall = recall_score(self.y_test, self.y_pred, average='weighted')
        f1 = f1_score(self.y_test, self.y_pred, average='weighted')
        print("Acurácia:", accuracy)
        print("Precisão:", precision)
        print("Recall:", recall)
        print("F1-score:", f1)

    def graph(self):
        # Configura o tamanho da figura
        plt.figure(figsize=(10, 6))

        # Plota os valores reais (y_test) com cor azul
        plt.scatter(range(len(self.y_test)), self.y_test, color='blue', label='Valor Real', alpha=0.5)

        # Plota os valores previstos (y_pred) com cor vermelha
        plt.scatter(range(len(self.y_pred)), self.y_pred, color='red', label='Valor Previsto', alpha=0.5)

        # Define os rótulos dos eixos e o título
        plt.xlabel("Índice das Amostras de Teste")
        plt.ylabel("Classificação (Page Views)")
        plt.title("Classificação com KNN - Page Views")

        # Adiciona a legenda
        plt.legend()

        # Exibe o gráfico
        plt.show()


    def matrizCofusion(self):
        cm = confusion_matrix(self.y_test, self.y_pred)
        sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", cbar=False)
        plt.xlabel(self.groups)
        plt.ylabel(self.groups)
        plt.title('Matriz de Confusão')
        plt.show()

    def matrizConfusionStatistics(self):

        cm = confusion_matrix(self.y_test, self.y_pred)
        num_classes = cm.shape[0]

        total_precisao = 0
        total_recall = 0
        total_especificidade = 0

        print("Estatísticas por Classe:")
        for i in range(num_classes):
            TP = cm[i, i]
            FP = cm[:, i].sum() - TP
            FN = cm[i, :].sum() - TP
            TN = cm.sum() - (TP + FP + FN)

            precisao = TP / (TP + FP) if (TP + FP) != 0 else 0
            recall = TP / (TP + FN) if (TP + FN) != 0 else 0
            especificidade = TN / (TN + FP) if (TN + FP) != 0 else 0

            total_precisao += precisao
            total_recall += recall
            total_especificidade += especificidade

        print(f"Classe {i}: Precisão: {round(precisao * 100, 2)}%, Recall: {round(recall * 100, 2)}%, Especificidade: {round(especificidade * 100, 2)}%")
        print("\nMédia Geral:")
        print(f"Precisão: {round((total_precisao / num_classes) * 100, 2)}%")
        print(f"Recall: {round((total_recall / num_classes) * 100, 2)}%")
        print(f"Especificidade: {round((total_especificidade / num_classes) * 100, 2)}%")
